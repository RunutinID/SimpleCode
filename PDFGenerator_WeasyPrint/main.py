from weasyprint import HTML

def create_pdf(title, content):
    html_content = f"<h1>{title}</h1><p>{content}</p>"
    pdf_filename = f"{title}.pdf"
    HTML(string=html_content).write_pdf(pdf_filename)
    print(f'PDF created: {pdf_filename}')

if __name__ == '__main__':
    input_title = input('Enter title: ')
    input_content = input('Enter content: ')
    create_pdf(input_title, input_content)