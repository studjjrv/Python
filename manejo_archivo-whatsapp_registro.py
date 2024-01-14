import pyautogui, webbrowser
import time
import threading
import os
import re
from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
import pywhatkit as kit

print("----Bienvenidos al proyecto--")
input("Presiese enter para continuar")
os.system("cls")
print('¿Qué desea hacer?')
print('Ingrese el número correspondiente a la opción deseada, y presionde enter...')
print('1. Registrarse\n2. Ver registros\n3. Actualizar registros')
accion = int(input())
if accion <= 0 | accion >3:
    print("Debe elegir entre las tres opciones")
    print("Por favor, ingrese un dato válido...")
    input("Presiona enter para regresar...")
    os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")

else:
    if accion == 1:##Registrarse
        os.system("cls")
        print('Bienvenido al módulo de registro\n\n\n')
        nombre = input("Ingresa tu nombre: ")
        os.system("cls")
        apellido = input("Ingresa tu apellido: ")
        os.system("cls")
        while True:
            try:
                print("Formato de fecha de nacimiento => (dd/mm/aaaa)")
                fecha = input("Ingresa tu fecha de nacimiento: ")
                datetime.strptime(fecha, '%d/%m/%Y')
                break
            except ValueError as error:
                error = "Fecha inválida"
                print(error)
        os.system("cls")
        pais = input("Ingresa tu país de nacimiento: ")
        os.system("cls")
        while True:
            correo = input("Ingresa tu correo electrónico: ")
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',correo.lower()):
                break
            else: 
                print('El correo no es correcto...')
        os.system("cls")
        while True:
            telefono = input("Ingresa un número telefónico (+XXXXXXXXX): ")
            regex = r"^((\+[\d]{1,4})+([^0]{1,11}))$"
            result = re.match(regex, telefono)
            if result is None:
                print("Telefono inválido")
                print("El formato correcto es: +XXXXXXXXX (sin espacios ni parentesis)")
            else:
                try:
                    f= open(f'{correo}.txt','a')
                    f.write(f'Nombre:{nombre}\nApellido: {apellido}\nFecha Nacimiento: {fecha}\nPaís: {pais}\nCorreo electrónico: {correo}\nTeléfono: {telefono}\nHora de registro: {datetime.now()}\n\n\n')
                    f.close()
                    f.close()
                    def envio_email(email_recibir,nombre,apellido):
                        email_sender = 'jjoaquin.romero@gmail.com'
                        email_password = 'vmynldhaprfzbaug'
                        email_receiver = correo
                        subjet = "Sistema de registro"
                        body = f'Hola {nombre} {apellido}, gracias por tu registro, ha sido exitoso. '
                        em = EmailMessage()
                        em['From'] = email_sender
                        em['To'] = email_receiver
                        em['Subjetc'] = subjet
                        em.set_content(body)
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                            smtp.login(email_sender,email_password)
                            smtp.sendmail(email_sender,email_receiver,em.as_string())
                    envio_email(correo,nombre,apellido)
                    print("Usted se ha registrado correctamente en nuestro archivo.")
                    print("Se le enviará un mensaje al whatsApp.")
                    print("Se le enviará un mensaje al correo eléctrónico suministrado.")
                    mensaje = f'Hola {nombre} {apellido}, gracias por tu registro. ¡Ha sido exitoso!'
                    horaActual = datetime.now()
                    time.sleep(2)            
                    kit.sendwhatmsg(telefono,mensaje,horaActual.hour,horaActual.minute+3,wait_time=40)
                    os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")
                except ValueError as error:
                    error = "Ha ocurrido un error, vuelva  iniciar su registro"
                    print(error)
    elif accion == 2:##Ver registros
        nombre_buscar = input("Coloqué el correo del usuario regisrtado que desea revisar: ")
        try:
            f= open(f'{nombre_buscar}.txt','r')
            print(f.read())
            f.close()
            os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")
        except FileNotFoundError as error:
            error = "Archivo no encontrado\nPor favor, vuelva al menú principal y selecciona otra opción."
            print(error)
            time.sleep(5)
            os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")
    elif accion == 3: ## Editar registros
        nombre_buscar = input("Coloqué el correo del usuario regisrtado que desea editar: ")
        try:
            f= open(f'{nombre_buscar}.txt','r')
            print(f.read())
            search_text = input("Coloca el valor que quieres reemplazar: ")
            replace_text = input("Coloca el nuevao valor a agregar: ")
            with open(rf'{nombre_buscar}.txt','r') as file:  
                data = file.read() 
                data = data.replace(search_text, replace_text) 
            with open(rf'{nombre_buscar}.txt','w') as file: 
                file.write(data) 
            f.close()
            time.sleep(2)
            f= open(f'{nombre_buscar}.txt','r')
            print(f.read())
            f.close()
            os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")
        except FileNotFoundError as error:
            error = "Archivo no encontrado\nPor favor, vuelva al menú principal y selecciona otra opción."
            print(error)
            time.sleep(5)
            os.system("C:/Users/Indatech/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Indatech/Documents/11CPW/Python/Proyecto/proyecto.py")