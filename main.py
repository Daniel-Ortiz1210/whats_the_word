import random

words = ['cadena', 'capataz', 'piedra', 'cargador', 'pinza', 'arbol', 'auditorio', 'balon', 'mochila', 'trampa', 'lapiz', 'cadera', 'cabeza', 'audifonos', 'cubo', 'mueble', 'computadora', 'carro', 'camara', 'pantalla', 'hoja']

guesses_cap = 5

print('''

BIENVENIDO EL JUEGO "WHAT´S THE WORD?"

¿PUEDES ADIVINAR LA PALABRA ANTES QUE SE ACABEN TUS VIDAS?

|                                                             |
v Esta es la lista de palabras, ¿puedes adivinar la correcta? v

            cadena    | capataz     | piedra 
            cargador  | pinza       | arbol 
            auditorio | balon       | mochila 
            trampa    | lapiz       | cadera 
            cabeza    | audifonos   | cubo
            mueble    | computadora | carro 
            camara    | pantalla    | hoja

''')

def main(guesses_cap, words):
    random_word = words[random.randint(0, len(words))]
    while guesses_cap > 0:
        user = input('Adivina la palabra: ').lower()
        if user == random_word:
            print('¡ADIVINASTE LA PALABRA!')
        else:
            guesses_cap -= 1
            print('Ups! Esta palabra no es correcta.')
            if guesses_cap == 0:
                print('GameOver! :(')
            print('Te quedan {} vidas.'.format(guesses_cap))


if __name__ == '__main__':
    main(guesses_cap, words)