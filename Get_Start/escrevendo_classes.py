
class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def ataque(tipo):

        ataque == ''
        if tipo == 'Mago':
            ataque = 'usando magia'

        elif tipo == 'Guerreiro':
            ataque = 'usando de espada'

        elif tipo == 'Monge':
            ataque = 'usando artes marciais'

        elif tipo == 'Ninja':
            ataque = 'usando de shuriken'



personagem_nome = input('Digite um nome para o seu personagem:')
personagem_idade = input('Digite a idade: ')
personagem_tipo = input('Digite o tipo (ex.: Mango; Gurreiro; Monge; Ninja):')

# Criando o objeto da classe heroi
personagem = heroi(personagem_nome, personagem_idade, personagem_tipo)

print(f" {personagem_nome}, o {personagem_tipo}, atacou {personagem.ataque()}.")