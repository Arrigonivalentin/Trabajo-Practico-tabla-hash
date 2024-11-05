# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 

# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda tabla la función hash deberá utilizar el ultimo
#  dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 

# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;

# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;

# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.

# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;

# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;

# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo



pokemons=[
    {"nombre": "Bulbasaur", "tipo": "Plantas/Veneno", "nivel": 5, "numero": 1},
    {"nombre": "Charmander", "tipo": "Fuego", "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": "Agua", "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": "Eléctrico", "nivel": 66, "numero": 25},
    {"nombre": "Jigglypuff", "tipo": "Normal/Hada", "nivel": 5, "numero": 39},
    {"nombre": "Meowth", "tipo": "Normal", "nivel": 1, "numero": 52},
    {"nombre": "Psyduck", "tipo": "Agua", "nivel": 25, "numero": 54},
    {"nombre": "Machop", "tipo": "Lucha", "nivel": 38, "numero": 66},
    {"nombre": "Tentacool", "tipo": "Agua/Veneno", "nivel": 55, "numero": 72},
    {"nombre": "Geodude", "tipo": "Roca/Tierra", "nivel": 10, "numero": 74},
    {"nombre": "Nidorino" , "tipo": "Veneno", "nivel": 32, "numero":33 },
    {"nombre": "Blastoise" , "tipo": "Agua", "nivel": 5, "numero":9},
    {"nombre": "Glaceon" , "tipo": "Hielo", "nivel": 5 , "numero":471},
    {"nombre": "Metagross" , "tipo": "Acero/Psíquico", "nivel": 55 , "numero":376}
]



def hash_tipo(pokemons):
    return pokemon["tipo"].split('/')[0]

def hash_numero(pokemons):
    return pokemon["numero"]%10

def hash_nivel(pokemons):
    return pokemon["nivel"]%10


tabla_tipo = {}

tabla_numero = {}

tabla_nivel = {}



for pokemon in pokemons:
    value = hash_numero(pokemon)
    if value not in tabla_numero:
        tabla_numero[value] = []
    tabla_numero[value].append(pokemon)

    value_2 = hash_tipo(pokemon)
    if value_2 not in tabla_tipo:
        tabla_tipo[value_2] = []
    tabla_tipo[value_2].append(pokemon)
    
    value_3 = hash_nivel(pokemon)
    if value_3 not in tabla_nivel:
        tabla_nivel[value_3] = []
    tabla_nivel[value_3].append(pokemon)


# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
def agregar_pokemon(numero, nombre, tipo, nivel):
    pokemon = {"numero": numero, "nombre": nombre, "tipo": tipo, "nivel": nivel}
    pokemons.append(pokemon)


numero = 33
nombre = "Nidorino" 
tipo = ["Veneno"]
nivel = 32 

agregar_pokemon(numero, nombre, tipo, nivel)


for pokemon in pokemons:
    print(pokemon)

print()

# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
print("estos son los pokemones que terminan en 3: ")
print(tabla_numero[3])
print()

print("estos son los pokemones que terminan en 7: ")
print(tabla_numero[7])
print()

print("estos son los pokemones que terminan en 9: ")
print(tabla_numero[9])
print()

# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
print("estos son los pokemones de nivel multiplo 2: ")
print(tabla_nivel[2])
print(tabla_nivel[4])
print(tabla_nivel[6])
print(tabla_nivel[8])
print(tabla_nivel[0])
print()

print("estos son los pokemones de nivel multiplo 5: ")
print(tabla_nivel[5])
print(tabla_nivel[0])
print()

print("estos son los pokemones de nivel multiplo 10")
print(tabla_nivel[0])
print()

# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

print("estos son los pokemones de tipo acero: ")
print(tabla_tipo['Acero'])
print()

print("estos son los pokemones de tipo fuego: ")
print(tabla_tipo['Fuego'])
print()

print("estos son los pokemones de tipo electrico: ")
print(tabla_tipo['Eléctrico'])
print()

print("estos son los pokemones de tipo hielo: ")
print(tabla_tipo['Hielo'])
print()