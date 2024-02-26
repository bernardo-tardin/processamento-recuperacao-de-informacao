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

def main(file1,file2,file3,query):
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
    dic_decimal={}
    for key in dicionario:
        binary_num = ''
        for bit in dicionario[key]:
            binary_num += str(bit)
        decimal_num = int(binary_num,2)
        dic_decimal[key] = decimal_num
    query = query.replace("AND","&")
    query = query.replace("OR","|")
    query = query.replace("NOT","~")
    termos = query.split()
    for i in range(len(termos)):
        if termos[i] not in ["&", "|", "~", "(", ")"]:
            termos[i] = str(dic_decimal[termos[i]])
    new_query = ' '.join(termos)
    n = eval(new_query)
    binary = str(bin(n))
    if len(binary) < 5:
        binary = binary.replace("b","")
    else:
        binary = binary.replace("0b","")
    docs = []
    for i in range(0,len(binary)):
        if binary[i] == '1':
            docs.append("hilda"+str(i+1)+".pdf")
    print(docs)

main("hilda1.pdf","hilda2.pdf","hilda3.pdf","filosofia AND ( livro OR obra ) AND europa")