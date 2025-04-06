# Superclase "Cliente"
class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto
        # se asigna directamente en el __init__ ya que este tiene un valor fijo y no recibirá nungún valor
        self.descuento = 0 # El cliente normal no tiene descuento

    def get_descuento(self):
        return self.descuento
    
    # __str__ devuelve en forma de cadena del objeto, facilitando su impresión
    def __str__(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre}, Contacto: {self.contacto}, Descuento: {self.descuento}"
 
# Subclase "ClienteRegular" que hereda los atributos de la superclase    
class ClienteRegular(Cliente): 
    def __init__(self, id_cliente, nombre, contacto):
        super().__init__(id_cliente, nombre, contacto) # invocamos al constructor de la superclase
        self.descuento = 10 # El cliente regular tiene un 10% de descuento
    
# Subclase "ClienteVIP" que hereda los atributos de la superclase        
class ClienteVIP(Cliente):
    def __init__(self, id_cliente, nombre, contacto):
         super().__init__(id_cliente, nombre, contacto) # invocamos al constructor de la superclase
         self.descuento = 15 # El cliente vip tiene un 15% de descuento