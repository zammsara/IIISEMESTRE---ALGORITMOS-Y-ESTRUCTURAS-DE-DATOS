usuario = input("USUARIO: ")
usuario = usuario.upper ()

if usuario == "DOCENTE":
    print("BIENVENIDO: DOCENTE.")
    password = input("Contraseña: ".upper())
    if password.upper () == "ABC123.":
        print("Usted es un usuario valido")
    else:
        print("Contraseña inválida")
else:
    print("Usuario invalido")