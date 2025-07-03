from xhtml2pdf import pisa

import pdfkit
pdfkitconfig = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

def gerarHTML(input="template.html", output="template.pdf", substitutions:dict[str, str]=dict()):

    with open(input, "r") as file:
        htmlContent = str(file.read()).strip()

    for target in substitutions:
        htmlContent = htmlContent.replace(target, substitutions[target])

    # HTML(string=htmlContent).write_pdf(output)

    saveHTMLTOpdf(htmlContent, output)

def saveHTMLTOpdf(htmlcontent, output):
    pdfkit.from_string(htmlcontent, output, configuration=pdfkitconfig)

def save_html_to_pdf(html_str: str, output_filename: str) -> bool:
    """
    Converts HTML string to PDF and saves it as a file.
    
    Args:
        html_str (str): The HTML content to convert.
        output_filename (str): The name of the output PDF file.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(output_filename, "wb") as file:
            result = pisa.CreatePDF(src=html_str, dest=file)
        return not result.err
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    gerarHTML()
    # test weasyprint