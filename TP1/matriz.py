import PyPDF2

def tokens(file):
    text=''
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    for page in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        text_page = pageObj.extract_text()
        text = text + " " + text_page
    text = text.lower()
    for elem in text:
        if not elem.isalnum():
            text = text.replace(elem, " ")
    tokens = text.split()
    tokens = list(set(tokens))
    return tokens

def main(file1,file2,file3):
    dicionario = {"medicina":[0,0,0],"medieval":[0,0,0],"europa":[0,0,0],"igreja":[0,0,0],"literatura":[0,0,0],"filosofia":[0,0,0],
                  "livro":[0,0,0],"obra":[0,0,0],"cura":[0,0,0]}
    tokens1 = tokens(file1)
    tokens2 = tokens(file2)
    tokens3 = tokens(file3)
    for key in dicionario.keys():
        for elem in tokens1:
            if elem == key:
                dicionario[key][0] = 1
        for elem in tokens2:
            if elem == key:
                dicionario[key][1] = 1
        for elem in tokens3:
            if elem == key:
                dicionario[key][2] = 1
    print(f"                  {file1}    {file2}    {file3}")
    for key in dicionario:
        termo = key
        if len(key) < 10:
            for i in range(len(key),10):
                termo += " "
        print(f"  {termo}         {dicionario[key][0]}               {dicionario[key][1]}            {dicionario[key][2]}")
    return dicionario

main("hilda1.pdf","hilda2.pdf","hilda3.pdf")