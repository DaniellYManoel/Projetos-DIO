
xp = 0
nome = input("Digite um nome para o Herói: ")

if xp < 1000:
    nivel = 'Ferro' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 1000 and xp < 2000:
    nivel = 'Bronze' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 2000 and xp < 5000:
    nivel = 'Prata' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 6000 and xp < 7000:
   nivel = 'Ouro' 
   print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 7000 and xp < 8000:
    nivel = 'Platina' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 8000 and xp < 9000:
    nivel = 'Ascendente' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 9000 and xp < 10000:
    nivel = 'Imortal' 
    print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

elif xp > 10000:
   nivel = 'Radiante' 
   print("O nome do Herói "+ nome + " está no nível" + nivel + '!') 

