def preprocess(data):
    """
    Preprocess the input data before making the visa approval decision.
    
    :param data: Dictionary containing input data
    :return: Preprocessed data
    """
    # Example preprocessing: Convert yes/no to True/False
    data['has_job_experience'] = True if data['has_job_experience'].lower() == 'yes' else False
    data['requires_job_training'] = True if data['requires_job_training'].lower() == 'yes' else False
    data['full_time_position'] = True if data['full_time_position'].lower() == 'yes' else False
    
    # Example preprocessing: Convert unit of wage to annual salary
    if data['unit_of_wage'].lower() == 'hourly':
        data['prevailing_wage'] *= 2080  # Assuming 2080 working hours in a year
    elif data['unit_of_wage'].lower() == 'monthly':
        data['prevailing_wage'] *= 12
    
    return data


df_1["continent"] = df_1["continent"].apply(make_others_continent)

from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
current_year= todays_date.year
df_2['company_age'] = current_year-df_2['yr_of_estab']




df_3["has_job_experience"] = df_3["has_job_experience"].apply(no_yes)
df_3["full_time_position"] = df_3["full_time_position"].apply(no_yes)


categorical_features = ['continent', 'education_of_employee', 'region_of_employment', 'unit_of_wage']

numeric_features = ['has_job_experience','no_of_employees','prevailing_wage','full_time_position','case_status','company_age']


def no_yes(x):
    if x=="Y" or x=="Certified" :
        return 1
    return 0
def make_others_continent(x):
    if x not in ["Asia","Europe","North America"]:
        return "others"
    return x