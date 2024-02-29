class PADRE:
    """primera clase"""

    def __init__(self, nombre, edad, personalidad, peso, color):
        self._nombre = nombre
        self._edad = edad
        self._personalidad = personalidad
        self._peso = peso
        self._color = color

    @property
    def nombre(self):
        """nombre de la persona """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """Jeison"""
        self._nombre = nombre

    @property
    def edad(self):
        """edad de la persona """
        return self._edad

    @edad.setter
    def edad(self, edad):
        """21"""
        self._edad = edad

    @property
    def personalidad(self):
        """personalidad de la persona """
        return self._personalidad

    @personalidad.setter
    def personalidad(self, personalidad):
        """sincero,humilde,bondadoso,inteligente,amable"""
        self._personalidad = personalidad

    @property
    def peso(self):
        """peso de la persona """
        return self._peso

    @peso.setter
    def peso(self, peso):
        """74,5"""
        self._peso = peso

    @property
    def color(self):
        """color de la persona """
        return self._color

    @color.setter
    def color(self, color):
        """trigeño"""
        self._color = color

    def __str__(self):
        return f"{self._nombre}, {self._edad} años, {self._personalidad}, {self._peso} kg, {self._color}"

# Ejemplo de uso
padre = PADRE("Jeison", 21, "sincero,humilde,bondadoso,inteligente,amable", 74.5, "trigeño")
print(padre)