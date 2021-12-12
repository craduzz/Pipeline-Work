import subprocess

MAYAPY_PATH = 'C:/Program Files/Autodesk/Maya2022/bin/mayapy.exe'

FILE_TO_RUN = 'D:/Charly/Documents/GitHub/Pipeline-Work/proyectoDCC/ts1.py'

COMMAND = "import proyectoDCC.main as main \n" \
          "m = main.Main() \n" \
          "m.crear_esfera('Esfera') \n" \
          "m.guardar_escena('escenaCMD')"

p = subprocess.Popen(f'{MAYAPY_PATH}  {FILE_TO_RUN}')

