# Calculadora de partidas Rankeados 
# . Variaveis
# . operadores 
# . estruturas de decisões
# . Funções

# Objetivo: 
# Crie uma função que recebe como parâmentro a quantidade de vitórias
# e derrotas de um jogador, depois disso retorne o resultado para uma 
# variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias- derrotas).

vitorias = int(input("Digite o seu número de vitórias: "))
derrotas = int(input("Digite o seu número de derrotas: "))

pontuacao = vitorias - derrotas

def nivel_do_heroi(pontuacao):
    
    if pontuacao <= 10:
        nivel = 'Ferro'
    elif pontuacao <= 20:
        nivel = 'Bronze'
    elif pontuacao <= 50:
        nivel = 'Prata'
    elif pontuacao <= 80:
        nivel = 'Ouro'
    elif pontuacao <= 90:
        nivel = 'Diamante'  # Corrigido o erro de digitação
    elif pontuacao <= 100:
        nivel = 'Imortal'
    else:
        nivel = 'Lendário'  # Opção para pontuações acima de 100
    
    return nivel

# Chamando a função e exibindo o nível do herói
print(f'O Herói com saldo de {pontuacao} está no nível {nivel_do_heroi(pontuacao)}')
