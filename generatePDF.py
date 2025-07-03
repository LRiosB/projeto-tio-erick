from weasyprint import HTML

def gerarHTML(input="template.html", output="template.pdf", substitutions:dict[str, str]=dict()):

    with open(input, "r") as file:
        htmlContent = str(file.read()).strip()

    for target in substitutions:
        htmlContent = htmlContent.replace(target, substitutions[target])

    HTML(string=htmlContent).write_pdf(output)


if __name__ == "__main__":
    gerarHTML()
    # test weasyprint