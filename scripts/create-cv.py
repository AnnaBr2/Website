"""Create an offline CV; no PDF is copied into the public website."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/anna-brabec-lebenslauf.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
GREEN = colors.HexColor('#486b48')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=30, leading=36, textColor=GREEN, spaceAfter=6),
    'tagline': ParagraphStyle('tagline', fontName='Helvetica', fontSize=12, leading=17, spaceAfter=10),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.2, leading=14.4, spaceAfter=6),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=14, spaceAfter=14),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=11.5, leading=16, textColor=GREEN, spaceBefore=13, spaceAfter=7),
    'item': ParagraphStyle('item', fontName='Helvetica-Bold', fontSize=10.2, leading=14.4, spaceAfter=2),
    'detail': ParagraphStyle('detail', fontName='Helvetica', fontSize=9.5, leading=13.3, spaceAfter=7),
}
story = []
def p(text, style='body'):
    return Paragraph(text, styles[style])
def section(title):
    story.append(p(title, 'section'))
def item(title, details):
    story.append(KeepTogether([p(title, 'item'), p(details, 'detail')]))

story += [p('Anna Brabec', 'name'), p('Master of Arts in Business<br/>Digital Marketing und Kommunikation', 'tagline')]
story += [p('<link href="mailto:contact@annabrabec.com">contact@annabrabec.com</link>  |  <link href="https://annabrabec.com/">annabrabec.com</link><br/><link href="https://www.linkedin.com/in/anna-maria-brabec-752b92246/">LinkedIn: Anna Maria Brabec</link>', 'contact'), HRFlowable(width='100%', thickness=1, color=GREEN), Spacer(1,10)]
story.append(p('Digital Marketing und Eventmanagement sind meine beruflichen Zielbereiche. Bei Cotton Classics arbeite ich als Marketing Allrounderin und im Projektmanagement und übernehme die Planung, Organisation und Durchführung der Roadshow. Mein Portfolio ergänzt diese Praxis um Studienprojekte in Markenentwicklung und Marketingforschung.'))
section('BERUFLICHE ERFAHRUNG')
item('Marketing Allrounderin & Projektmanagement | Cotton Classics Handels GmbH', 'Seit 08/2024 · Teilzeit · Schwadorf, Niederösterreich<br/>- Projektmanagement und Eventorganisation; Planung, Organisation und Durchführung der Roadshow<br/>- Mailings, Newsletter und Websitebetreuung<br/>- Content- und Giveaway-Management<br/>- KPI-Monitoring und Optimierung')
item('Social Media Management & PR-Assistenz | Unique Public Relations GmbH', '02/2024 - 05/2024<br/>- Sample- und Community-Management<br/>- PR- und Social-Media-Tätigkeiten für Kund*innen')
item('Chefredaktion des Magazins „Im Dialog“', '03/2023 - 10/2023<br/>- Management und Organisation<br/>- Kontakt mit Interviewpartner*innen<br/>- Verfassen und Freigeben von Artikeln')
item('Marketing-Assistenz | Erste Bank AG', '07/2022<br/>- Content-Erstellung, Arbeit mit Datenbanken und Designerstellung')
section('AUSBILDUNG')
item('Master of Arts in Business | Digital Marketing & Kommunikation', '09/2024 - 10/2026 · USTP - University of Applied Sciences St. Pölten')
item('Auslandssemester | International Tourism Management', '02/2026 - 06/2026 · Lucerne University of Applied Sciences and Arts')
item('Bachelor of Arts in Business | Marketing und Kommunikation', '09/2021 - 09/2024 · FH St. Pölten / USTP')
item('Interior- and Surface-Design', '09/2016 - 06/2021 · HTL Spengergasse, Wien')
section('AUSGEWÄHLTE AKADEMISCHE PROJEKTE')
item('<link href="https://annabrabec.com/projekte/masterarbeit-markenimage/">Masterarbeit: Psychische Gesundheit in der Werbung | 2026</link>', 'Experimentelle Online-Befragung mit 213 Personen zu narrativer und faktenbasierter Werbung sowie Markenimage. Forschungsdesign, Erhebung und statistische Auswertung mit Unipark und SPSS.')
item('<link href="https://annabrabec.com/projekte/anima/">Anima: Corporate Design | WS 2025</link>', 'Markenkonzept für einen Tee-Shop: Umfeldrecherche, Positionierung, visuelle Identität und Anwendungs-Mockups für Print, Verpackung und Website. Projektpräsentation mit Canva.')
section('KENNTNISSE & ZERTIFIKAT')
story.append(p('Organisation & Management · Adobe Suite · Office 365 · Meta Ads · Google Ads · Künstliche Intelligenz · Redaktionelles Arbeiten · Events & Digital Marketing · Design & Ästhetik'))
story.append(p('Cambridge Advanced Digital · Cambridge University Press & Assessment<br/>09/2025 · Englisch C1', 'detail'))
story.append(p('Google Search Certificate · Google<br/>2025', 'detail'))

def page_footer(canvas, doc):
    canvas.setTitle('Anna Brabec - Lebenslauf')
    canvas.setAuthor('Anna Brabec')
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.black)
    canvas.drawString(42, 26, 'Stand: November 2026')
    canvas.drawRightString(A4[0]-42, 26, str(doc.page))

SimpleDocTemplate(str(OUT), pagesize=A4, topMargin=36, bottomMargin=40, leftMargin=42, rightMargin=42).build(story, onFirstPage=page_footer, onLaterPages=page_footer)
print(f'Created {OUT}')
