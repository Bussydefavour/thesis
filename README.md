# Ensemble Modeling To Enhance Click-Through Rate Prediction For Nigerian Online Marketing Campaigns

## Introduction
This MSc Data Science project focuses on building an ensemble model for ad click prediction to create a valuable tool for Nigerian business owners. The model aims to help predict the success of advertisement campaigns before they are launched, guiding businesses to select the most effective channels for ad placement and maximizing their return on investment.

## Project Aim
The primary aim of this study is to design and implement computationally efficient machine learning models for ad click prediction that maintain high predictive accuracy. The research addresses the limitations of existing ensemble methodologies, which use datasets capped at 300,000 observations, by employing an expanded dataset. The ultimate goal is to enhance the performance of ad click prediction models, providing scalable and practical solutions for real-world online advertising applications and advancing the field of predictive analytics.

## How to Run the Code

1. **Set up Environment:**
   - The project is developed using Anaconda Jupyter Notebook. 
   - Open the Anaconda Command Prompt and create a new environment:
     ```bash
     conda create --name <env_name>
     ```
   - Activate the environment:
     ```bash
     conda activate <env_name>
     ```
   - Install all required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Clone Repository:**
   - Clone this repository to your local machine and navigate to the project directory:
     ```bash
     git clone <repository_url>
     cd <repository_folder>
     ```

3. **Download the Dataset**
    - Download the dataset from this this [link](ttps://www.kaggle.com/c/avazu-ctr-prediction/data)
    - You don't need to downnload the dataset to run this code as the direct link to the balanced train  dataset has been provided in the notebook. 
    - However, if you will like to work with the whole dataset, download in via the link above, unzip it and provide the path to the train dataset in the notebook. 
   

4. **Run the Jupyter Notebook:**
   - Open Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Inside Jupyter Notebook, open `ad_click_notebook.ipynb` and run all cells to execute the code.

## How to Run the Flask App

1. **Save the Models:**
   - The ensemble model is not included in the repository due to its size. To run the app, save the ensemble and scaler models from the notebook by executing the code in the "Save Models" section. The models will be saved in the `models` folder within the current working directory.

2. **Launch the Flask App:**
   - Using the same environment created earlier, navigate to the directory where the `app.py` file is located.
   - Run the Flask app:
     ```bash
     python app.py
     ```
   - Go to the "Home" tab on the app interface to upload the file for prediction. Ensure the file is in CSV format.
   - Click on "Predict" to get the prediction results, which will display the corresponding ad IDs.

3. **Additional Information:**
   - For details on the required features for the input data, check the "About the App" section on the app interface.

## Acknowledgments
I would like to express my sincere gratitude to my supervisor, **Dr. Momina Shaheen**, for her invaluable guidance and support throughout this project. 

A special thank you to my husband, **Mr. Akinwale**, for his constant encouragement and assistance during the course of this work.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

