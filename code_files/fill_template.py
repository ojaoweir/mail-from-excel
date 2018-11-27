# Reads from files to create a template of for the mail
def fillTemplate():
    emailTemplateFile = open("templates/email_content.html", "w")
    emailHTMLFile = open("templates/template_start.html")
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()

    emailContentFile = open("Files/email_text.txt")
    emailTemplateFile.write(emailContentFile.read())
    emailContentFile.close()

    emailHTMLFile = open("templates/template_end.html")
    emailTemplateFile.write(emailHTMLFile.read())
    emailHTMLFile.close()

    emailTemplateFile.close()
