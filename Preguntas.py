import os

matriz1 = [['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎']]

correcto = '😋'
incorrecto = '💀'

list_pregunta = [
    '¿Qué es Python?\n1. Juego\n2. Lenguaje de programación\n3. Marca de auto\n4. Ninguna de las anteriores',
    '¿Qué es HTML?\n1. Marca de Computadores\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente',
    '¿Cuál es el resultado de 2 + 2?\n1. 3\n2. 4\n3. 5\n4. 6',
    '¿Cuál es el nombre del planeta más grande del sistema solar?\n1. Tierra\n2. Marte\n3. Júpiter\n4. Venus',
    '¿Cuál es el metal más denso?\n1. Hierro\n2. Oro\n3. Plomo\n4. Platino',
    '¿Cuál es el río más largo del mundo?\n1. Nilo\n2. Amazonas\n3. Yangtsé\n4. Misisipi',
    '¿Cuál es el océano más grande del mundo?\n1. Pacífico\n2. Atlántico\n3. Índico\n4. Antártico',
    '¿Quién pintó la Mona Lisa?\n1. Pablo Picasso\n2. Leonardo da Vinci\n3. Vincent van Gogh\n4. Claude Monet',
    '¿Cuál es el animal más grande del mundo?\n1. Elefante\n2. Ballena Azul\n3. Jirafa\n4. Rinoceronte',
    '¿En qué año comenzó la Segunda Guerra Mundial?\n1. 1939\n2. 1941\n3. 1945\n4. 1950',
    '¿Quién escribió "Romeo y Julieta"?\n1. William Shakespeare\n2. Charles Dickens\n3. Jane Austen\n4. Mark Twain',
    '¿Cuál es el metal más caro del mundo?\n1. Oro\n2. Platino\n3. Rodio\n4. Paladio',
    '¿Cuál es la capital de Francia?\n1. Berlín\n2. Madrid\n3. París\n4. Roma',
    '¿Quién fue el primer presidente de Estados Unidos?\n1. Thomas Jefferson\n2. Abraham Lincoln\n3. George Washington\n4. John F. Kennedy',
    '¿Cuál es el hueso más largo del cuerpo humano?\n1. Fémur\n2. Tibia\n3. Radio\n4. Húmero',
    '¿Cuál es el órgano más grande del cuerpo humano?\n1. Hígado\n2. Piel\n3. Pulmones\n4. Intestino',
    '¿Cuál es la montaña más alta del mundo?\n1. Kilimanjaro\n2. Everest\n3. Aconcagua\n4. K2',
    '¿Cuál es el país más poblado del mundo?\n1. India\n2. China\n3. Estados Unidos\n4. Brasil',
    '¿Cuál es el idioma más hablado del mundo?\n1. Inglés\n2. Español\n3. Mandarín\n4. Hindi',
    '¿Cuál es el metal más abundante en la corteza terrestre?\n1. Hierro\n2. Aluminio\n3. Cobre\n4. Plomo',
    '¿Cuál es la capital de Australia?\n1. Sídney\n2. Melbourne\n3. Canberra\n4. Brisbane',
    '¿Quién fue el primer hombre en pisar la luna?\n1. Neil Armstrong\n2. Buzz Aldrin\n3. Yuri Gagarin\n4. Alan Shepard',
    '¿En qué año se fundó Google?\n1. 1995\n2. 1998\n3. 2001\n4. 2005',
    '¿Quién escribió "Don Quijote de la Mancha"?\n1. Miguel de Cervantes\n2. Federico García Lorca\n3. Gabriel García Márquez\n4. Mario Vargas Llosa',
    '¿Cuál es el océano más pequeño del mundo?\n1. Atlántico\n2. Pacífico\n3. Índico\n4. Ártico',
]

list_respuesta = ['2', '3', '2', '3', '3', '1', '1', '2', '2', '1', '1', '3', '3', '3', '1', '2', '2', '2', '1', '2', '3', '2', '2', '1', '1', '4']

def fnt_pintarmatriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='    ')
        print()

os.system('cls' if os.name == 'nt' else 'clear')
fnt_pintarmatriz()

contador = 0

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print()
        print(list_pregunta[contador])
        print()
        respuesta = input('->')
        if respuesta == list_respuesta[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        fnt_pintarmatriz()
