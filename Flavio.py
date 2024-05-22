matriculas={}
comando=0
vendedor=''
mv={}

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
            cf='Vendedor'
        else:
            cf='Admnistrativo'
        x.append(cf)
        nf=int(input("Digite o número de faltas: "))
        x.append(nf)
        if(cf=='Vendedor'):
            vv=float(input("Digite seu volume de vendas: "))

            sb=(1500+(0.09*vv))-50*nf
        else:
            sb=float(input("Digite o salário fixo do admnistrativo: "))
            while(not 2150<=sb<=6950):
                print(f"Salario não considerado")
                sb=float(input("Digite o salário fixo do admnistrativo: "))
            else:
                sb=sb-(nf*(sb/30))
        x.append(sb)
        matriculas[matr]=x
        print(f"{matriculas}")
    return(matriculas,matr)


def Remover(matriculas):
    dig=int(input("Digite a Matricula que ira excluir: "))
    if(dig in matriculas):
        print(f"{matriculas[dig]}")
        dig2=input("Digite 'y' para proseguir com a exclusão: ")
        if(dig2=='y'):
            del matriculas[dig]
            print(f"Funcionario excluido!")
            print(f"{matriculas}")
        else:
            print(f"Cancelando o Processo")
    else:
        print(f"Matricula não encontrada")
    return(matriculas)
def MV(nf,)






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
