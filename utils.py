from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer, TableStyle
from reportlab.pdfgen import canvas

def process_employee_info(employee_id, employee_name, department):
    # Define the PDF filename
    filename = "employee_info.pdf"

    # Create a canvas and set the font colors
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFillColor(colors.red)
    c.setStrokeColor(colors.black)

    # Draw the round company logo on the top left corner
    logo_path = "static/logo.png"  # Replace with the actual path to your logo image
    c.drawImage(logo_path, 30, 720, width=70, height=70)

    # Add the title "Employee Information" using a Paragraph style
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title", parent=styles["Heading1"], textColor=colors.black, fontSize=18, spaceAfter=20)
    title = Paragraph("Employee Information", title_style)
    title.wrapOn(c, 400, 40)
    title.drawOn(c, 120, 730)

    # Create a table to display the employee details
    table_data = [
        ["Employee ID:", employee_id],
        ["Employee Name:", employee_name],
        ["Department:", department],
    ]
    table = Table(table_data, colWidths=[120, 200])
    table.setStyle([
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 0), (-1, 0), colors.red),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])

    # Wrap the table and add it to the canvas
    table.wrapOn(c, 400, 200)
    table.drawOn(c, 80, 600)

    # Add a footer with the date and page number
    footer_text = "Generated on {date}".format(date=datetime.now().strftime("%Y-%m-%d"))
    c.setFont("Helvetica", 10)
    c.drawRightString(550, 30, footer_text)
    c.drawString(30, 30, "Page 1")

    # Save the canvas as a PDF file and close it
    c.showPage()
    c.save()

    return filename


def process_daily_report(report_date, hours_worked, tasks_completed):
    # Define the PDF filename
    filename = "daily_report.pdf"

    # Create a canvas and set the font colors
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFillColor(colors.red)
    c.setStrokeColor(colors.black)

    # Draw the round company logo on the top left corner
    logo_path = "static/logo.png"  # Replace with the actual path to your logo image
    c.drawImage(logo_path, 30, 720, width=70, height=70)

    # Add the title "Daily Report" using a Paragraph style
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title", parent=styles["Heading1"], textColor=colors.black, fontSize=18, spaceAfter=20)
    title = Paragraph("Daily Report", title_style)
    title.wrapOn(c, 400, 40)
    title.drawOn(c, 120, 730)

    # Add the report date, hours worked, and tasks completed
    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, 650, "Report Date:")
    c.drawString(200, 650, report_date)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, 620, "Hours Worked:")
    c.drawString(200, 620, hours_worked)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, 590, "Tasks Completed:")

    tasks = tasks_completed.split("\n")
    y = 560
    for task in tasks:
        c.setFont("Helvetica", 12)
        c.drawString(100, y, "•")
        c.drawString(120, y, task)
        y -= 20

    # Add a footer with the date and page number
    footer_text = "Generated on {date}".format(date=datetime.now().strftime("%Y-%m-%d"))
    c.setFont("Helvetica", 10)
    c.drawRightString(550, 30, footer_text)
    c.drawString(30, 30, "Page 1")

    # Save the canvas as a PDF file and close it
    c.showPage()
    c.save()

    return filename


def process_weekly_report(report_week, project_name, tasks_planned):
    doc = SimpleDocTemplate("weekly_report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Company logo and header
    logo = "static/logo.png"  # replace with your actual logo file
    header = Paragraph(f'<img src="{logo}" width="50" height="50"/> Weekly Report', styles['Heading1'])
    elements.append(header)

    # Report week and project name
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f'Report Week: {report_week}', styles['Normal']))
    elements.append(Paragraph(f'Project Name: {project_name}', styles['Normal']))
    elements.append(Spacer(1, 20))

    # Tasks planned table
    table_data = [('Task')]
    for task in tasks_planned:
        table_data.append((task))

    tasks_table = Table(table_data)
    tasks_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(tasks_table)

    # Footer
    elements.append(Spacer(1, 20))

    doc.build(elements)
    return "weekly_report.pdf"



def process_monthly_report(report_month, project_name, tasks_planned):
    # Define the PDF filename
    filename = f"{project_name} Monthly Report {report_month}.pdf"

    # Create a canvas and set the font colors
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFillColor(colors.red)
    c.setStrokeColor(colors.black)

    # Draw the company logo on the top left corner
    logo_path = "static/logo.png"  # Replace with the actual path to your logo image
    c.drawImage(logo_path, 30, 720, width=70, height=70)

    # Add the report title using a Paragraph style
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title", parent=styles["Heading1"], textColor=colors.black, fontSize=18, spaceAfter=20)
    title = Paragraph(f"{project_name} Monthly Report - {report_month}", title_style)
    title.wrapOn(c, 400, 40)
    title.drawOn(c, 120, 730)

    # Create a table to display the tasks planned
    table_data = [
        ["Task", "Description"],
        *[[f"Task {i}", task] for i, task in enumerate(tasks_planned, start=1)]
    ]
    table = Table(table_data, colWidths=[80, 240])
    table.setStyle([
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 0), (-1, 0), colors.red),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])

    # Wrap the table and add it to the canvas
    table.wrapOn(c, 400, 200)
    table.drawOn(c, 80, 600)

    # Add a footer with the date and page number
    footer_text = "Generated on {date}".format(date=datetime.now().strftime("%Y-%m-%d"))
    c.setFont("Helvetica", 10)
    c.drawRightString(550, 30, footer_text)
    c.drawString(30, 30, "Page 1")

    # Save the canvas as a PDF file and close it
    c.showPage()
    c.save()

    return filename

def process_feedback_form(feedback_subject, feedback_message, feedback_email):
    print(f"Feedback Subject: {feedback_subject}")
    print(f"Feedback Message: {feedback_message}")
    print(f"Feedback Email: {feedback_email}")

def process_project_report(project_id, project_name, project_manager):
    print(f"Project ID: {project_id}")
    print(f"Project Name: {project_name}")
    print(f"Project Manager: {project_manager}")

def process_leave_letter(leave_start_date, leave_end_date, leave_reason):
    print(f"Leave Start Date: {leave_start_date}")
    print(f"Leave End Date: {leave_end_date}")
    print(f"Leave Reason: {leave_reason}")
