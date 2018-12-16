from code_files.read_excel import getReceivers, getLogin, getHeader




receivers = getReceivers()

for receiver in receivers:
    contentFile = open("alt_file.txt", "w")
    print(receiver[2])
    contentFile.write("hej ")
    contentFile.write(receiver[2])
    contentFile.write("\n\nDu har blivit nominerad till förtroendepost som ska tillsättas på Vintermötet. För att fortsatt vara med i nomineringsprocessen vill vi att di fyller i enkäten länkad ned senast söndag 30/12 där du berättar om dig själv samt ger tillgänglighet.\n\nDu har nominerats till följande poster:\n")
    contentFile.write(receiver[2])
    contentFile.write("Länk till enkäten:\nhttps://goo.gl/forms/XLwUv2sDWBhrX7Lx1\n\nOm du väljer att gå vidare till nästa steg och svarar på enkäten kommer vi så fprt som möjligt efter enkätperioden att återkomma via mail med tid och plats för intervju.")
    contentFile.close()
    input()
