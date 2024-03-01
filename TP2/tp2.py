#Exercicio 3

def AND(postList1,postList2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(postList1) and p2 < len(postList2):
        if postList1[p1] == postList2[p2]:
            result.append(postList1[p1])
            p1 += 1
            p2 += 1
        elif postList1[p1] > postList2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result 

print(f'Teste função AND: {AND([1,3,5,7,8],[2,4,5,6,7])}')

def NOT(postList1,dim):
    result = [x for x in range(1,dim+1) if x not in postList1]
    return result

print(f'Teste função NOT: {NOT([2,3,6,7],10)}')

def OR(postList1,postList2):
    result=[]
    p1 = 0
    p2 = 0
    while p1 < len(postList1) and p2 < len(postList2):
        if postList1[p1] == postList2[p2]:
            result.append(postList1[p1])
            p1 += 1
            p2 += 1
        elif postList1[p1] > postList2[p2]:
            result.append(postList2[p2])
            p2 += 1
        else: 
            result.append(postList1[p1])
            p1 += 1
    while p1 < len(postList1):
        result.append(postList1[p1])
        p1 += 1
    while p2 < len(postList2):
        result.append(postList2[p2])
        p2 += 1
    return result

print(f'Teste função OR: {OR([2,3,5,6,7,9],[2,3,4,8,10])}')

#Exercicio 5

def tokens(file):
    f = open(file,'r')
    text = f.read()
    for elem in text:
        if not elem.isalnum():
            text = text.replace(elem," ")
    text = text.lower()
    tokens = text.split()
    tokens = list(set(tokens))
    f.close()
    return tokens

def matrizIndiceInvertido(list_files):
    termos = ['medicina','medieval','europa','igreja','literatura','filosofia','livro','obra','cura']
    termos.sort()
    matriz = {}
    i=0
    for file in list_files:
        i+=1
        lista_tokens = tokens(file)
        for token in lista_tokens:
            if token in termos and token not in matriz.keys():
                matriz[token] = [i]
            if token in termos and token in matriz.keys():
                if i not in matriz[token]:
                    matriz[token].append(i)
    matriz = dict(sorted(matriz.items()))
    return matriz

#print(matrizIndiceInvertido(['hilda1.txt','hilda2.txt','hilda3.txt']))
