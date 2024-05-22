matriculas={}
comando=0
vendedor=''
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
        x.append(sb)
        if()
        if (nf>=mvn):
            matr=mv
            mvn=nf
        matriculas[matr]=x
        print(f"{matriculas}")
    return(matriculas,matr,mvn,mv,pv)


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


def salario(matriculas):
    for x in range (len(matriculas)):
        print(f"Matrícula:
                Nome:
                Função:
                Salário bruto:
                Salário líquido:")

def MV(mvn,mv,matriculas):
    if(matriculas[mv][1]==101):
        desc=50*mvn
    else:
        desc=mvn*(matriculas[mv][3]/30)
    print(f''' 
            O Funcionario que Tem mais faltas é {mv} {matriculas[mv][0]} {matriculas[mv][1]}
            Com {mvn} faltas.
            Assim Seu Salario teve um desconto de {desc}
    ''')    

def ms(matriculas,):


print("Bem vindo ao sistema Flavial")
while comando!=7:
    comando = int(input('''
=====================================================
                    Bem-vindo(a)!
=====================================================
| [1] Cadastro de funcionarios                      |
| [2] Remover funcionarios                          |
| [3] Determinar folha de pagamento de funcionarios |
| [4] relatorio com SB                              |
| [5] consultar maior salario                       |
| [6] consultar maior vagabundo                     |
| [7] Sair                                          |
=====================================================
 Digite o que quer fazer: '''))
    if comando == 1:
        cadastro()
    elif comando==2:
        Remover(matriculas)
    elif comando == 4:
        salario(matriculas)
        
    
    
        

