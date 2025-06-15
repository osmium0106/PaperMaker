from fpdf import FPDF
import os

def create_answer_sheet_pdf(
    paper_name, questions_by_section, output_path,
    school_name=None, exam_name=None, class_name=None, subject=None, time=None, max_marks=None
):
    pdf = FPDF()
    pdf.add_page()
    font_path_math = os.path.join(os.path.dirname(__file__), "NotoSansMath-Regular.ttf")
    pdf.add_font('NotoSansMath', '', font_path_math, uni=True)
    pdf.set_font('NotoSansMath', '', 14)
    margin = 15
    page_width = pdf.w - 2 * margin
    # Header
    if school_name:
        pdf.set_xy(margin, 10)
        pdf.set_font('NotoSansMath', '', 16)
        pdf.cell(page_width, 10, txt=school_name, ln=True, align='C')
    if exam_name:
        pdf.set_font('NotoSansMath', '', 14)
        pdf.cell(page_width, 10, txt=exam_name + " - Answer Sheet", ln=True, align='C')
    if class_name or subject:
        class_subject = f"Class: {class_name if class_name else ''}    Subject: {subject if subject else ''}"
        pdf.cell(page_width, 10, txt=class_subject, ln=True, align='C')
    if time or max_marks:
        pdf.set_font('NotoSansMath', '', 12)
        y = pdf.get_y()
        pdf.set_xy(margin, y)
        pdf.cell(page_width/2-5, 10, txt=f"Time: {time if time else ''}", align='L')
        pdf.set_xy(margin+page_width/2+5, y)
        pdf.cell(page_width/2-5, 10, txt=f"M.M.: {max_marks if max_marks else ''}", align='R')
        pdf.ln(10)
    x1 = margin
    x2 = pdf.w - margin
    y = pdf.get_y()
    pdf.set_line_width(0.5)
    pdf.line(x1, y, x2, y)
    pdf.ln(5)
    # Sections and Answers
    for section in questions_by_section:
        section_name = section.get('section_name', '')
        questions = section.get('questions', [])
        pdf.set_font('NotoSansMath', '', 14)
        pdf.cell(page_width, 10, txt=section_name, ln=True, align='C')
        pdf.set_font('NotoSansMath', '', 12)
        for idx, q in enumerate(questions, 1):
            q_text = q.get('text', '')
            # Extract answer if present
            answer = ''
            for line in q_text.split('\n'):
                if line.strip().lower().startswith('answer:'):
                    answer = line.strip()
            if answer:
                pdf.multi_cell(page_width, 8, f"Q{idx}: {answer}", align='L')
            else:
                pdf.multi_cell(page_width, 8, f"Q{idx}: [No answer found]", align='L')
            pdf.ln(2)
        pdf.ln(6)
    pdf.output(output_path)
    return output_path
