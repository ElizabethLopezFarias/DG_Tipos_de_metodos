# -*- coding: utf-8 -*-

from personaje import Personaje
import random

#Bienvenida al Juego
print("Bienvenido al Juego Gran Fantasía")
nombre = input("Ingresa el nombre de tú personaje: \n")
#Crea una la instancia nombre en la clase Personaje
personaje_actual = Personaje(nombre)
#Aviso de interacción
print (""" 
    --------------------------------
    ¡Cuidado!. Ha aparecido un Orco!
    -------------------------------- """)
# Creación de la instancia orco en la clase Personaje
personaje_orco = Personaje('Orco')
#llama al método get_probabilidad_ganar()
probabilidad_ganar = personaje_actual.get_probabilidad_ganar(personaje_orco)
# Llama al método mostrar_dialogo_opcion
opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
# Mientras 
while opcion_orco == 1:
    numero =random.uniform (0,1)
    resultado = 'G' if numero < probabilidad_ganar else 'P'

    if resultado =='G':
        print(f""" Felicidades, le has ganado al Orco!
              ¡¡ Recibirás 50 puntos de experiencia !!
            """)
        personaje_actual.estado = 50
        personaje_orco.estado = -30
    elif resultado == 'P':
        print(f""" Lo sentimos, el Orco te ha ganado!
              ¡¡ Perdiste 30 puntos de experiencia !!
            """)
        personaje_actual.estado = -30
        personaje_orco.estado = 50 

    print(personaje_actual.estado)
    print(personaje_orco.estado)       

    probabilidad_ganar = personaje_actual.get_probabilidad_ganar(personaje_orco)
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

print('Has huido! El orco ha quedado atrás')