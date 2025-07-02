from weasyprint import HTML

with open("./template.html", "r") as file:
    content = str(file.read()).strip()

HTML(string=content).write_pdf("./template.pdf")