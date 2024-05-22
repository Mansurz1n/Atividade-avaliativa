matriculas={}
comando=0
vendedor=''
ms=0
mvn=0
def cadastro():
    matr=int(input("Digite a matrícula do funcionário: "))
    if matr in matriculas.keys():
        print("Matricula já inserida")
    else:
        matriculas.setdefault(matr)
        x=[]
        nome=input("Digite o nome do funcionário: ")
        x.append(nome)
        cf=int(input("Digite o código de função: "))
        while(cf!=101 and cf!=102):
            print(f"codigo invalido")
            cf=int(input("Digite o código de função: "))
        if(cf==101):
            cod=cf
            cf='Vendedor' 
        else:
            cod=cf
            cf='Admnistrativo'
        x.append(cod)
        nf=int(input("Digite o número de faltas: "))
        x.append(nf)
        if(cf=='Vendedor'):
            vv=float(input("Digite seu volume de vendas: "))
            sb=round((1500+(0.09*vv))-50*nf,2)
        else:
            sb=float(input("Digite o salário fixo do admnistrativo: "))
            while(not 2150<=sb<=6950):
                print(f"Salario não considerado")
                sb=float(input("Digite o salário fixo do admnistrativo: "))
            else:
                sb=round(sb-(nf*(sb/30)),2)
        if sb<=2259.20:
            sliq=sb
            pv=0
        elif sb<=2828.65:
            sliq=round((sb-(sb*0.075)),2)
            pv=7.5
        elif sb<=3751.05:
            sliq=round((sb-(sb*0.15)),2)
            pv=15
        elif sb<=4664.68:
            sliq=round((sb-(sb*0.225)),2)
            pv=22.5
        elif sb>4664.68:
            sliq=round((sb-(sb*0.275)),2)
            pv=27.5
        x.append(sliq)
        x.append(pv)
        x.append(sb)
        matriculas[matr]=x
    return(matriculas)


def Remover(matriculas):
    dig=int(input("Digite a Matricula que ira excluir: "))
    if(dig in matriculas):
        print(f"{matriculas[dig]}")
        dig2=input("Digite 'y' para proseguir com a exclusão:")
        if(dig2=='y'):
            del matriculas[dig]
            print(f"Funcionario excluido!")
            print(f"{matriculas}")
        else:
            print(f"Cancelando o Processo")
    else:
        print(f"Matricula não encontrada")
    return(matriculas)

def folha(matriculas):
    dig=int(input("Digite a matricula do funcionario:"))
    if(dig in matriculas):
        print(f'''
|NOME:{matriculas[dig][0]}
|FUNÇÃO:{matriculas[dig][1]}           
|NUMERO DE FALTAS:{matriculas[dig][2]}
|SALARIO BRUTO: {matriculas[dig][5]}
|SALARIO LIQUIDO:{matriculas[dig][3]}               
|PERCENTUAL DE IMPOSTO:{matriculas[dig][4]}%''')
    else:
        print("matricula não encontrada ou inexistente")    

def salario(matriculas):
    for x in matriculas.keys():
        print(f''''
Matrícula:{x}
Nome:{matriculas[x][0]}
Função:{matriculas[x][1]}  
Salário bruto:{matriculas[x][5]}
Salário líquido:{matriculas[x][3]}
''')

def MS(matriculas,ms):
    for x,sliq in matriculas.items():
        if sliq[3]>ms :
            ms=sliq[3]
            pms=x
    print(f'''
O Funcionario com o maior salario liquido é o {pms} {matriculas[pms][0]} {matriculas[pms][1]}
Com um salario bruto de {matriculas[pms][5]} 
Com um percentual de imposto de {matriculas[pms][4]}
Com um salario liquido de {ms}
''')
    return ms

def MV(matriculas,mvn):
    for x,nf in matriculas.items():
        if nf[2]>mvn :
            mvn=nf[2]
            mv=x
    if(matriculas[mv][1] == 101):
        desc=50*mvn
    else:
        desc=mvn*(matriculas[mv][3]/30)
    print(f''' 
O Funcionario que Tem mais faltas é {mv} {matriculas[mv][0]} {matriculas[mv][1]}.
Com {mvn} faltas.
Assim Seu Salario teve um desconto de {round((desc),2)}.''')
    return mvn   

print("Bem vindo ao sistema Flavial")
while comando!=7:
    comando = int(input('''
=====================================================
                    Bem-vindo(a)!
=====================================================
| [1] Cadastro de funcionarios                      |
| [2] Remover funcionarios                          |
| [3] Determinar folha de pagamento de funcionarios |
| [4] Relatorio                                     |
| [5] Consultar Funcionario com maior salario       |
| [6] Consultar Funcionario com mais faltas         |
| [7] Sair                                          |
=====================================================
Digite o que quer fazer: '''))
    if comando == 1:
        cadastro()
    elif comando==2:
        Remover(matriculas)
    elif comando== 3 :
        folha(matriculas)
    elif comando == 4:
        salario(matriculas)
    elif comando == 5:
        MS(matriculas,ms)
    elif comando == 6:
        MV(matriculas,mvn)