from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

pd = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    set_text_color(r=100, g=100, b=100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1,)
    pdf.line(10, 20, 200, 20)
    
    #set the footer
    pdf.ln(265)    
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(r=180, g=180, b=180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align='R')
    
    for i in range(row["Pages"] - 1):
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        set_text_color(r=100, g=100, b=100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

pdf.ougput('pdf-template.pdf')