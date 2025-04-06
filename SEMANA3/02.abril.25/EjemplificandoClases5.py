class Perro: 
    def __init__(self, nombre, raza, edad, altura):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.altura = altura
    
    def comer(self):
        return "El perro esta comiendo..."
    
    def dormir(self):
        return "El perrro esta durmiendo..."
    
    def ladrar(self):
        return "El perro esta ladrando..."
    
kira = Perro(input("Ingresa el nombre de tu mascota: "), input("Ingresa la raza de tu mascota: "), int(input("Ingresa la edad de tu mascota: ")), float(input("Ingresa la aultura de tu mascota: ")))

print(kira.nombre, ", ", kira.raza,", ", kira.edad, ", ", kira.altura)