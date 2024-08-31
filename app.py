from flask import Flask, request, render_template, redirect, url_for 
from werkzeug.utils import secure_filename
import pandas as pd
import os
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

def load_model(model_name):
    with open(f'models/{model_name}.pkl', 'rb') as file:
        loadmodel = pickle.load(file)
    return loadmodel

def preprocess_data(data):
    data['hour'] = data['hour'].astype(str)
    data['hour'] = data['hour'].apply(lambda x: '20'+x[:2]+'-'+x[2:4]+'-'+x[4:6]+'-'+x[6:])
    data['hour'] = pd.to_datetime(data['hour'])
    data = data.rename(columns={"hour": "date"})
    data['hour'] = data['date'].dt.hour
    data['day'] = data['date'].dt.day
    try: 
        data = data.drop(columns=['C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C1'])
    except Exception as e:
        data = data
    categorical_features = ['site_id', 'site_domain','site_category', 'app_id', 'app_domain', 
                            'app_category', 'banner_pos','device_id','device_ip', 'device_model', 
                            'device_type', 'device_conn_type']
    hashed_df = data[categorical_features].applymap(lambda x: hash(x))
    full_df = pd.concat([data.drop(columns=categorical_features), hashed_df], axis=1)
    X = full_df.drop(columns=['id', 'date'])
    return X

def scale_data(data):
    scaler = load_model('scaler')
    X_transform = scaler.transform(data)
    return X_transform

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return "No file part"
            
            file = request.files['file']
            
            if file.filename == '':
                return "No selected file"
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                try:
                    if not os.path.exists(app.config['UPLOAD_FOLDER']):
                        os.makedirs(app.config['UPLOAD_FOLDER'])

                    file.save(file_path)

                except Exception as save_error:                    
                    return "An error occurred while saving the file. Please try again later."

                uploaded_data = pd.read_csv(file_path)    
                clean_data = preprocess_data(uploaded_data)  
                X_scaled = scale_data(clean_data)          
                model = load_model('esm_model')
                predictions = model.predict(X_scaled) 
                uploaded_data['click'] = predictions
                predictions_df = uploaded_data[['id', 'click']]
                
                # Convert DataFrame to HTML
                predictions_html = predictions_df.to_html(classes='table table-striped', index=False)

                # Render result template with predictions table
                return render_template('result.html', prediction_table=predictions_html)
                
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template('index.html')

@app.route('/result')
def result():
    prediction_table = request.args.get('prediction_table')
    return render_template('result.html', prediction_table=prediction_table)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/motivation')
def motivation():
    return render_template('motivation.html')

if __name__ == '__main__':
    app.run(debug=True)
