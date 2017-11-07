import re

regex=r"[o]i, |[e]u |[s]ou |[oa] |(\w+)|. Gostaria de | e queria |(\w+)| sobre |o |(\w+)"

arq=open('frases.txt','r')
test_str=arq.read()
arq.close()

matches=re.finditer(regex, test_str, re.M | re.I)

lista1, lista2, contador=[], [], 0

for matchNum, match in enumerate(matches):
    matchNum+=1
    for groupNum in range(0, len(match.groups())):
        if groupNum==1 and match.group(groupNum)!=None:
            lista1.append(match.group(groupNum))
            contador+=1
            if contador==3:
                lista2.append(lista1)
                lista1=[]
                contador=0

########### VERIFICA AÇÕES ############
produtos=[]
for i in lista2:
    produtos.append(i[2])
    
modelos=list(set(produtos))
quantidade, acumulador=[], 0
for m in modelos:
    for p in produtos:
        if m==p:
            acumulador+=1
    quantidade.append(acumulador)
    acumulador=0

print("\n ***** PRODUTOS *****\n")
print("Os modelos pesquisados foram:",modelos,'\n')
print("A quantidade total de mencões de produtos foi:",len(produtos),'\n')
for i in range(len(modelos)):
    print("O produto",modelos[i],"foi mencionado",quantidade[i],"vezes.")

###########VERIFICA E COMPARA AÇÕES############
            
cont_verbo = 0            
verbos=[]
verb=""
for l in lista2:
    verbos.append(l[1])

'''RECEBE A BASE DE VERBOS/AÇÕES'''
lista_verbos=[]
arq =open('verbos.txt','r')
v = arq.read()
lista_verbos = v.split('\n')
arq.close()

lista_final_verbos=[]
for verbo in lista_verbos:
    for verbo_frase in verbos:
        if verbo_frase == verbo:
            verb = verbo_frase
            cont_verbo+=1
    if cont_verbo>=1:
        lista_antes_da_final=[]
        lista_antes_da_final.append(verb)
        lista_antes_da_final.append(cont_verbo)
        lista_final_verbos.append(lista_antes_da_final)
    cont_verbo=0

print("\n ***** AÇÕES *****\n")
print("As ações presentes nas frases são:",verbos,'\n')
print("A quantidade total de ações presente nas frases foi:",len(verbos),"\n")
for z in lista_final_verbos:
    print("O verbo",z[0],"foi utilizado",z[1],"vezes.")
        

########### TOTAL VENDIDO ############

lista_produtos=[]
arq =open('produtos.txt','r')
v = arq.read()
lista_produtos = v.split('\n')
arq.close()

lista_prod_preco = []
for produto_preco in lista_produtos:
    lista_prod_preco.append(produto_preco.split(','))

cont = 0
valor = 0
for i in lista_prod_preco:
    for prod in produtos:
        if i[0] == prod:
            for verbo in verbos:
                if verbo == 'comprar' or verbo == 'adquirir' or verbo == 'obter':
                    valor += int(i[1])
                    break;

print("\n ***** TOTAL DE VENDAS *****\n")
print("O total de carros vendido foi R$",valor)
           
            
            
