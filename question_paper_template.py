from fpdf import FPDF
import os

def create_question_paper_pdf(
    paper_name, questions_by_section, total_marks, output_path,
    school_name=None, exam_name=None, class_name=None, subject=None, time=None, notes=None, max_marks=None
):
    pdf = FPDF()
    pdf.add_page()
    # Use a Unicode font (NotoSansMath) for full math symbol support
    font_path_math = os.path.join(os.path.dirname(__file__), "NotoSansMath-Regular.ttf")
    pdf.add_font('NotoSansMath', '', font_path_math, uni=True)
    pdf.set_font('NotoSansMath', '', 14)

    margin = 15
    page_width = pdf.w - 2 * margin

    # School Name
    if school_name:
        pdf.set_xy(margin, 10)
        pdf.set_font('NotoSansMath', '', 16)
        pdf.cell(page_width, 10, txt=school_name, ln=True, align='C')
    # Exam Name
    if exam_name:
        pdf.set_font('NotoSansMath', '', 14)
        pdf.cell(page_width, 10, txt=exam_name, ln=True, align='C')
    # Class and Subject
    if class_name or subject:
        class_subject = f"Class: {class_name if class_name else ''}    Subject: {subject if subject else ''}"
        pdf.cell(page_width, 10, txt=class_subject, ln=True, align='C')
    # Time and Max Marks
    if time or max_marks:
        pdf.set_font('NotoSansMath', '', 12)
        y = pdf.get_y()
        pdf.set_xy(margin, y)
        pdf.cell(page_width/2-5, 10, txt=f"Time: {time if time else ''}", align='L')
        pdf.set_xy(margin+page_width/2+5, y)
        pdf.cell(page_width/2-5, 10, txt=f"M.M.: {max_marks if max_marks else ''}", align='R')
        pdf.ln(10)
    # Horizontal line
    x1 = margin
    x2 = pdf.w - margin
    y = pdf.get_y()
    pdf.set_line_width(0.5)
    pdf.line(x1, y, x2, y)
    pdf.ln(5)
    # Notes
    if notes:
        pdf.set_font('NotoSansMath', '', 12)
        pdf.cell(page_width, 8, txt="Notes:", ln=True, align='L')
        for note in notes:
            pdf.cell(page_width, 8, txt=f"• {note}", ln=True, align='L')
        pdf.ln(2)
    # Sections and Questions
    for section in questions_by_section:
        section_name = section.get('section_name', '')
        section_marks = section.get('section_marks', '')
        questions = section.get('questions', [])
        pdf.set_font('NotoSansMath', '', 14)
        pdf.cell(page_width, 10, txt=section_name, ln=True, align='C')
        pdf.set_font('NotoSansMath', '', 12)
        for q in questions:
            q_text = q.get('text', '')
            q_marks = q.get('marks', '')
            # Remove answer lines and [MCQ]/[Short]/[Long] from question text
            q_text_no_answer = '\n'.join([
                line.replace('[MCQ]', '').replace('[Short]', '').replace('[Long]', '').rstrip()
                for line in q_text.split('\n') if not line.strip().lower().startswith('answer:')
            ])
            lines = q_text_no_answer.split('\n')
            y = pdf.get_y()
            pdf.set_xy(margin, y)
            start_y = pdf.get_y()
            if lines:
                # Print first line with marks on the right
                pdf.set_xy(margin, start_y)
                pdf.multi_cell(page_width-40, 8, lines[0], align='L')
                # Calculate y after first line
                after_first_line_y = pdf.get_y()
                pdf.set_xy(pdf.w-margin-40, start_y)
                pdf.cell(40, 8, txt=f"[{q_marks} marks]", align='R')
                pdf.set_y(after_first_line_y)
                # Print remaining lines (if any)
                for line in lines[1:]:
                    pdf.set_xy(margin, pdf.get_y())
                    pdf.multi_cell(page_width-40, 8, line, align='L')
            pdf.ln(2)
        pdf.ln(6)
    pdf.output(output_path)
    return output_path
