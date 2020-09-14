from instabot import Bot #pip install instabot
import time
import os
import random

bot = Bot()

while True:
	user = input("Ingrese su nombre de usuario: ")
	psw = input("Ingrese su contraseña: ")
	try:
		bot.login(username=user,password=psw)
		break
	except:
		print("\n Usuario o contraseña incorrecta, intente nuevamente: \n")
	
print("\n Has iniciado sesión correctamente \n")

while True:
	imgs = input("Ingrese nombre de carpeta donde tiene las imágenes: ")
	path = os.getcwd()+"\\"+imgs
	try:
		imagenes = os.listdir(path)
		break
	except:
		print("\n Carpeta no encontrada")
		print("La carpeta debe estar en el directorio del archivo .py \n")
	
#descripcion de fotografias
pregunta = int(input("¿Desea un tiempo aleatorio(0) o determinista(1)?: "))

if pregunta == 1:
	minutos = int(input('Intervalo de publicación[minutos]: '))
else:
	t_max = int(input("Tiempo máximo de espera[minutos]: "))

d1 = "" #descripcion 1
d2 = "" #descripcion 2
d3 = "" #descripcion 3 ...
descripciones = [d1,d2,d3]

formatos = [".jpg",".png",".jpeg"]

while imagenes != []:
	for img in imagenes: 
		if img[-4:len(img)] in formatos:  #la imagen tiene el formato correcto
			try:
				print("\n Subiendo imagenes...\n")
				bot.upload_photo(path+"\\"+img, caption=descripciones[random.randint(1,len(descripciones)-1)]) #se sube la foto con una descripcion al azar
				os.remove(path+"\\"+img+".REMOVE_ME")
			except:
				print("\n Formato no compatible \n")
				pass
			imagenes.remove(img)
			if pregunta == 0:
				t = random.randint(0,t_max*60)
				print("\n Esperando {} minutos...\n".format(round(t/60,2)))
				time.sleep(t)
			else:
				print("\n Esperando {} minutos...\n".format(minutos))
				time.sleep(minutos*60)
		else:
			print("\n Error en formato de imagen \n")

print("\n Todas las imagenes han sido subidas \n")