import csv
import smtplib
from email.message import EmailMessage
import mimetypes

def generar_reporte(nombre_archivo):
    datos = [
        ['Nombre', 'Edad', 'Ciudad'],
        ['Juan', 28, 'Madrid'],
        ['María', 34, 'Barcelona'],
        ['Luis', 45, 'Valencia']
    ]
    
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)
    print(f'Reporte generado: {nombre_archivo}')

def enviar_correo(contrasena, nombre_archivo, destinatarios):
    remitente = 'silvestre.hdz.h@gmail.com'
    asunto = 'Reporte Automatizado'
    cuerpo = 'Adjunto encontrarás el reporte generado automáticamente.'

    # Crear el mensaje de correo
    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = ', '.join(destinatarios)
    mensaje.set_content(cuerpo)

    # Adjuntar el archivo
    with open(nombre_archivo, 'rb') as archivo:
        tipo_mime, _ = mimetypes.guess_type(nombre_archivo)
        tipo_mime_principal, tipo_mime_sub = tipo_mime.split('/')
        mensaje.add_attachment(archivo.read(),
                               maintype=tipo_mime_principal,
                               subtype=tipo_mime_sub,
                               filename=nombre_archivo)

    # Enviar el correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remitente, contrasena)
        servidor.send_message(mensaje)
    print('Correo enviado')

# Generar y enviar el reporte
nombre_reporte = 'reporte.csv'
generar_reporte(nombre_reporte)

# Configurar la contraseña y destinatarios
contrasena = ''
destinatarios = ['silvestrehdz422@gmail.com']
enviar_correo(contrasena, nombre_reporte, destinatarios)
