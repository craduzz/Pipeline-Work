import subprocess
import os

'''
Instrucciones de uso:

abrir la consola (CMD) y abrir la ubicacion de este archivo en la consola

Escribir python esferaCMD.py en la consola

Liso, la escena ya esta creada.

'''

#MAYAPY_PATH = 'C:/Program Files/Autodesk/Maya2022/bin/mayapy.exe'

MAYAPY_PATH = os.path.dirname('C:/Program Files/Autodesk/Maya2022/bin/mayapy.exe')
FILE_TO_RUN = os.path.dirname('D:/Charly/Documents/GitHub/Pipeline-Work/proyectoDCC/ts1.py')

COMMAND = "import proyectoDCC.main as main \n" \
          "m = main.Main() \n" \
          "m.crear_esfera('Esfera') \n" \
          "m.guardar_escena('escenaCMD')"

listTest = [MAYAPY_PATH,FILE_TO_RUN]

p = subprocess.Popen(listTest)

