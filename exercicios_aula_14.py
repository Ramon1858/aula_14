#1:Verificando se o número é par ou ímpar
number = int(input('digite um numero para verificação:')) %2 == 0

    match number: 
        case True:
            print('este numero é par')
    
        case False:
             print('this number é impar')

n1 = int(input('digite um numero:')) >0
#2:Verificando se um número é positivo, negativo ou zero
match n1:
    case True:
        print('é positivo')
    case False:
        print('é negativo')

s = input('digite algo (ou não):') == ''
#3:Verificando se uma string é vazia ou não
match s:
     case True:
         print('ela tá vazia')

     case False:
         print('ela não está vazia')

#4: Verificando se um número é maior, menor ou igual a 10
v1 = int(input('digite um numero para verificar:'))
    if v1 == 10:
        print('é igual a 10')
    elif v1 < 10:
        print('é menor que 10')
    elif v1 > 10:
        print('é maior que 10')

#5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso
idade = int(input('digite sua idade para saber sua faixa etária'))

match idade:

    case idade if idade >=65:
        print('idoso')

    case idade if idade >=18 and idade <35:
        print('jovem')

    case idade if idade >35 and idade <=64:
        print('adulto')
            
    case idade if idade >=14 and idade <=17:
        print('jovem')

    case _:
        print('criança')