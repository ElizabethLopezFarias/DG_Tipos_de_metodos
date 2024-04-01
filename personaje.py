class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    # Getter para obtener el estado del personaje
    @property
    def estado(self):
        return f"""
        NOMBRE: {self.nombre}     NIVEL: {self.nivel}     EXPERIENCIA: {self.experiencia}
        """

    # Setter para actualizar la experiencia del personaje
    @estado.setter
    def estado(self, exp_actual):
        calculo_exp = self.experiencia + exp_actual

        # Recalcula hasta que la experiencia sea menor a 100
        while calculo_exp >= 100:
            self.nivel += 1
            calculo_exp -= 100

        # Reasigna en caso de tener puntos en contra
        while calculo_exp < 0:
            if self.nivel > 1:
                calculo_exp = exp_actual + 100
                self.nivel -= 1
            else:
                calculo_exp = 0

        self.experiencia = calculo_exp

    # Método que retorna la probabilidad de ganar en un enfrentamiento
    def get_probabilidad_ganar(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    # Creamos el método para calcular y mostrar las probailidades
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        # Mostramos el diálogo y obtenemos la elección del usuario
        eleccion = int(input(
            f""" 
            Considerando tu nivel, tienes:
            {probabilidad_ganar*100}% de probabilidades de ganarle al Orco.
            Si ganas, ganarás 50 puntos de experiencia 
            y el orco perderá 30.
            Si pierdes, perderás 30 puntos de experiencia
            y el orco ganará 50.
            
            -------------------
            ¿Qué deseas hacer?
            1. Atacar
            2. Huir
            --------------------
            """
        ))

        # Visualización de la elección del usuario
        if eleccion == 1:
            print("Has elegido atacar al Orco.")
        elif eleccion == 2:
            print("Has elegido huir del enfrentamiento.")
        else:
            eleccion = int(input("Elección inválida. Por favor, selecciona 1 o 2."))

        return eleccion
    
    # Sobrecarga de operadores para comparar niveles entre personajes
    # sobrecarga del operador de menor que 
    def __lt__(self, other):
        return self.nivel < other.nivel
	#sobrecarga del operador de mayor que
    def __gt__(self, other):
        return self.nivel > other.nivel
	#sobrecarga del operador de igualdad
    def __eq__(self, other):
        return self.nivel == other.nivel


	



 