from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/check_visa', methods=['POST'])
def check_visa():
    case_id = request.form['case_id']
    continent = request.form['continent']
    education_of_employee = request.form['education_of_employee']
    has_job_experience = request.form['has_job_experience']
    requires_job_training = request.form['requires_job_training']
    no_of_employees = request.form['no_of_employees']
    yr_of_estab = request.form['yr_of_estab']
    region_of_employment = request.form['region_of_employment']
    prevailing_wage = request.form['prevailing_wage']
    unit_of_wage = request.form['unit_of_wage']
    full_time_position = request.form['full_time_position']
    
    # Simple logic for visa approval (This is just an example. Replace with actual logic)
    if education_of_employee.lower() == 'phd' and has_job_experience.lower() == 'yes':
        result = 'Visa Approved'
    else:
        result = 'Visa Denied'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
