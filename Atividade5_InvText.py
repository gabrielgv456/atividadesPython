def invertText(text):
    invertedText = ""
    for palavra in text.split(" "):
        invertedText += palavra[::-1]+" "
    return invertedText

Text = input('Escreva a frase que deseja inverter: ')
invertedText = invertText(Text)
print(invertedText)