
from flask import Flask, request, send_file, make_response
from flask import render_template

from utils import process_employee_info, process_daily_report, process_weekly_report, process_monthly_report, \
    process_feedback_form, process_leave_letter, process_project_report

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('form.html')

#Route to render the form HTML page
@app.route('/form-render')
def form_render():
    return render_template('tools/form.html')

# Route to process the form submission
@app.route('/form-process', methods=['POST'])
def form_process():
    print("Enter -- form_process")
    for key, value in request.form.items():
        print(f"{key}: {value}")

    selected_request = request.form['request_type']
    print("-- Collected req type --")
    if selected_request == "employee_info":
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        department = request.form['department']
        filename = process_employee_info(employee_id, employee_name, department)
        return send_attachment(filename)
    elif selected_request == "daily_report":
        report_date = request.form['report_date']
        hours_worked = request.form['hours_worked']
        tasks_completed = request.form['tasks_completed']
        filename = process_daily_report(report_date, hours_worked, tasks_completed)
        return send_attachment(filename)
    elif selected_request == "weekly_report":
        report_week = request.form['report_week']
        project_name = request.form['project_name']
        tasks_planned = request.form['tasks_planned']
        filename = process_weekly_report(report_week, project_name, tasks_planned)
        return send_attachment(filename)
    elif selected_request == "monthly_report":
        report_month = request.form['report_month']
        project_name = request.form['project_name']
        tasks_planned = request.form['tasks_planned']
        filename = process_monthly_report(report_month, project_name, tasks_planned)
        return send_attachment(filename)
    elif selected_request == "feedback_form":
        feedback_subject = request.form['feedback_subject']
        feedback_message = request.form['feedback_message']
        feedback_email = request.form['feedback_email']
        filename = process_feedback_form(feedback_subject, feedback_message, feedback_email)
        return send_attachment(filename)
    elif selected_request == "project_report":
        project_id = request.form['project_id']
        project_name = request.form['project_name']
        project_manager = request.form['project_manager']
        filename = process_project_report(project_id, project_name, project_manager)
        return send_attachment(filename)
    elif selected_request == "leave_letter":
        leave_start_date = request.form['leave_start_date']
        leave_end_date = request.form['leave_end_date']
        leave_reason = request.form['leave_reason']
        filename = process_leave_letter(leave_start_date, leave_end_date, leave_reason)
        return send_attachment(filename)

    return 'Form submitted successfully!'

def send_attachment(filename):
    response = make_response(open(filename, 'rb').read())
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == '__main__':
    app.run()
