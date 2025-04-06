class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"\nEstudiante: {self.nombre}")
        print(f"Nota: {self.nota}")
        
    def aprobado(self):
        from colorama import init, Fore
        init(autoreset=True)
        
        if self.nota >= 70:
            print(Fore.GREEN+"Aprobado")
        else: 
            print(Fore.RED+"Reprobado")