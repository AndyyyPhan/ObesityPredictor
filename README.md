# Obesity Prediction Tool

## Overview
This project is an obesity prediction tool that uses machine learning to assess the risk of obesity based on individual lifestyle and health data. The tool was developed to help individuals better understand their health and proactively manage obesity risks. A Django web application serves as the interface where users can input their data to receive a personalized risk assessment.

## Features
- **Machine Learning Models**: Implemented multiple algorithms, including Logistic Regression, Support Vector Machines, and Random Forests.
- **Accuracy**: The Random Forest model achieved an accuracy of 89% in predicting obesity.
- **Web Application**: Built with Django, allowing users to input their personal data and receive instant obesity risk predictions.
- **Accessibility**: Designed to make health information easily accessible and actionable.

## Technologies Used
- **Machine Learning**: Python, scikit-learn
- **Web Development**: Django, HTML/CSS
- **Data Handling**: Pandas, NumPy
- **Deployment**: N/A

## Getting Started
1. **Clone the repository**:
   ```
   git clone https://github.com/AndyyyPhan/ObesityPredictor.git
   ```
2. **Navigate to the project directory**:
   ```
   cd obesity_project
   ```
3. **Install the dependencies**:
   ```
   pip install -r requirements.txt
   ```
4. **Run the web application**:
   ```
   python manage.py runserver
   ```

## Usage
- Open the web application in your browser and fill in the required information in the form.
- Submit the form to receive an obesity risk prediction based on your input.

## Machine Learning Details
- **Data**: The model was trained on an obesity dataset containing information such as age, lifestyle, physical activity, and dietary habits.
- **Algorithms Compared**: Logistic Regression, Support Vector Machines (SVM), and Random Forests.
- **Best Performing Model**: The Random Forest model achieved the highest accuracy at 89%.

## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements for the project.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Kaggle for providing the obesity dataset.
- scikit-learn and Django communities for the tools and support.

