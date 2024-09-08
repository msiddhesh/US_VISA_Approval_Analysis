import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gzip

# Load the model using gzip compression
with gzip.open('random_forest_model_compressed.pkl.gz', 'rb') as f:
    rf = pickle.load(f)
# Load the preprocessor and Random Forest model from pickle files
with open('PII_model.pickle', 'rb') as file:
    preprocessor = pickle.load(file)

# Streamlit application
st.title('Visa Approval Prediction')

# Define the input fields
prevailing_wage = st.text_input('Prevailing Wage', value='5000')
continent = st.selectbox('Continent', ["asia", "europe", "north_america", "others"])
Education_of_employee  = st.selectbox('Education Level ', ["high_school",'bachelors', "masters",'doctorate'])
region_of_employment =st.selectbox('Region of employment ',['Island', 'Midwest', 'Northeast', 'South', 'West'])
unit_of_wage = st.selectbox('Unit of Wage', ['hour', 'month',"week","year"])
has_job_experience = st.selectbox('Has Job Experience', ['Yes', 'No'])
full_time_position = st.selectbox('Full Time Position', ['Yes', 'No'])
no_of_employees = st.text_input('Number of Employees', value='100')
company_age = st.text_input('Company Age', value='25')

def make_yes_no(feature):
    if feature == 'Yes':
        return 1
    else:
        return 0
# Button to submit the form
if st.button('Check Visa'):
    # Combine all input into a list

    if continent == "asia":
        asia = 1
        europe = 0
        north_america = 0
        others = 0
    elif continent == "europe":
        asia = 0
        europe = 1
        north_america = 0
        others = 0
    elif continent == "north_america":
        asia = 0
        europe = 0
        north_america = 1
        others = 0
    else:
        asia = 0
        europe = 0
        north_america = 0
        others = 1

    if Education_of_employee == "bachelors":
         bachelors = 1
         doctorate = 0
         high_school = 0
         masters = 0
    elif Education_of_employee == "doctorate":
         bachelors = 0
         doctorate = 1
         high_school = 0
         masters = 0
    elif Education_of_employee == "high_school":
         bachelors = 0
         doctorate = 0
         high_school = 1
         masters = 0
    else :
         bachelors = 0
         doctorate = 0
         high_school = 0
         masters = 1


    if region_of_employment =="island":
        island= 1
        midwest= 0
        northeast =0
        south =0
        west=0
    elif region_of_employment =="midwest":
        island= 0
        midwest= 1
        northeast =0
        south =0
        west=0
    elif region_of_employment =="northeast":
        island= 0
        midwest= 0
        northeast =1
        south =0
        west=0
    elif region_of_employment =="south":
        island= 0
        midwest= 0
        northeast =0
        south =1
        west=0
    else:
        island= 0
        midwest= 0
        northeast =0
        south =0
        west=1

    if unit_of_wage == "hour":
        hour=1
        month=0
        week=0
        year=0
    elif unit_of_wage == "month":
        hour=0
        month=1
        week=0
        year=0
    elif unit_of_wage == "week":
        hour=0
        month=0
        week=1
        year=0
    else:
        hour=0
        month=0
        week=0
        year=1

    input_data = [prevailing_wage, asia, europe, north_america, others, bachelors, doctorate,
                    high_school, masters, island, midwest, northeast, south, west,
                    hour, month, week, year, make_yes_no(has_job_experience), make_yes_no(full_time_position),
                    no_of_employees, company_age]
    
    # Column names as defined
    num_features = ['prevailing_wage', 'Asia', 'Europe', 'North America', 'others', "Bachelor's", 
                    'Doctorate', 'High School', "Master's", 'Island', 'Midwest', 'Northeast', 
                    'South', 'West', 'Hour', 'Month', 'Week', 'Year']
    
    or_columns = ['has_job_experience', 'full_time_position']
    transform_columns = ['no_of_employees', 'company_age']


    # # Predict using the loaded model
    # prediction = model.predict(transformed_data_point)

    # Interpret the prediction (assuming binary classification: 0 = Denied, 1 = Approved)


    import pandas as pd

    # Define the column names used in your preprocessor (replace with actual names)
    column_names = ['has_job_experience', 'no_of_employees', 'prevailing_wage', 'full_time_position', "company_age", 'Europe', 'North America', 'Asia']

    # Create new data
    new_data = np.array([[1, no_of_employees, prevailing_wage,1,company_age, europe, north_america, asia]])

    # Convert the NumPy array to a pandas DataFrame with the correct column names
    new_data_df = pd.DataFrame(new_data, columns=column_names,dtype="float64")

    # Now pass the DataFrame to the preprocessor

    new_data_preprocessed = preprocessor.transform(new_data_df)

    # You can now make predictions using the preprocessed data
    new_prediction = rf.predict(new_data_preprocessed)

    if new_prediction[0] == "1":
        result = 'Visa Approved'
    else:
        result = 'Visa Denied'

    st.write(f'Result: {result}')
