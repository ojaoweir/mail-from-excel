# Reads from files to create a template of for the mail
def fillTemplate():
    emailTemplateFile = open("templates/email_content.html", "w")
    emailHTMLFile = open("templates/template_start.html")
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()

    printText(emailTemplateFile)

    emailHTMLFile = open("templates/template_end.html")
    emailFooterFile = open("Files/footer_picture.txt")
    emailTemplateFile.write("<img src='" + emailFooterFile.read() + "'></img>" + emailHTMLFile.read())
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()
    emailFooterFile.close()

    emailTemplateFile.close()

def printText(emailTemplateFile):
    emailContentFile = open("Files/email_text.txt")
    text = emailContentFile.read()

    for c in text:
        if c == "\n":
            emailTemplateFile.write("<br>")
        else:
            emailTemplateFile.write(c)

    emailContentFile.close()
