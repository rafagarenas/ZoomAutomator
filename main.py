import subprocess
import pyautogui
import time
import pandas as pd
import datetime
import threading
from datetime import datetime

#Variable para dar la Hora en el Sistema
ahora = datetime.now()
print(ahora.strftime('Programa Iniciado, escuchando. %d/%m/%Y %H:%M:%S\n'))

archivo = open("logs.txt","a")
archivo.write(ahora.strftime('Programa Iniciado, escuchando. %d/%m/%Y %H:%M:%S\n\n'))
archivo.flush()

def sign_in(meetingid, pswd):
    zoomgui = pyautogui.locateCenterOnScreen('zoomgui.png')
    if not zoomgui:
        subprocess.Popen('C:\\Users\\SmileyCat\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        ahora = datetime.now()
        archivo.write(ahora.strftime('Zoom estaba cerrado y se ejecutó correctamente. %d/%m/%Y %H:%M:%S\n'))
        archivo.flush()
    else:
        ahora = datetime.now()
        archivo.write(ahora.strftime('Zoom ya estaba abierto y todo esta funcionando correctamente. %d/%m/%Y %H:%M:%S\n'))
        archivo.flush()
        print(ahora.strftime('Zoom ya estaba abierto y todo esta funcionando correctamente. %d/%m/%Y %H:%M:%S'))
    time.sleep(3)

    #Da Click en entrar a una nueva sesión
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #Ingresa el ID de la Sesión
    time.sleep(3)
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)

    #Ingresa a la sesión acordada.
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(5)

    #Ingresa la contraseña de la reunión.
    pyautogui.write(pswd)
    pyautogui.press('enter')
    time.sleep(5)

    # Revisar si ingresé a la sesión correctamente o hubo un error.
    sharescreen_btn = pyautogui.locateCenterOnScreen('sharescreen_btn.png')
    if not sharescreen_btn:
        ahora = datetime.now()
        print(ahora.strftime('Ha habido un ERROR y no has ingresado a la sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S'))
        archivo.write(ahora.strftime('Ha habido un ERROR y no has ingresado a la sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S\n'))
        archivo.flush()
    else:
        ahora = datetime.now()
        print(ahora.strftime('Se ha ingresado a la sesión ' + m_id + ' exitosamente. %d/%m/%Y %H:%M:%S'))
        archivo.write(ahora.strftime('Se ha ingresado a la reunión ' + m_id + ' exitosamente. %d/%m/%Y %H:%M:%S\n'))
        archivo.flush()

    #Si el Microfono esta activado, desactivarlo.
    micoff_btn = pyautogui.locateCenterOnScreen('micoff_btn.png')
    if not micoff_btn:
        ahora = datetime.now()
        print(ahora.strftime('El Micrófono estaba desactivado. Sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S'))
        archivo.write(ahora.strftime('El Micrófono estaba desactivado. Sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S\n'))
        archivo.flush()
    else:
        pyautogui.moveTo(micoff_btn)
        pyautogui.click()
        ahora = datetime.now()
        print(ahora.strftime('Se ha desactivado manualmente el micrófono en la sesión '+m_id+'. %d/%m/%Y %H:%M:%S'))
        archivo.write(ahora.strftime('Se ha desactivado manualmente el micrófono en la sesión '+m_id+'. %d/%m/%Y %H:%M:%S'))
        archivo.flush()

# Archivo de Horario
df = pd.read_csv('timings.csv')

while True:
    #Ciclo que revisa si la hora actual existe en el archivo CSV.
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)

    #Ciclo que revisa la hora de salida en el CSV.
    if now in str(df['exithour']):
        row = df.loc[df['exithour'] == now]

        # Comprobación de si identifica el botón de salir de la sesión.
        exit_btn = pyautogui.locateCenterOnScreen('exit_btn.png')
        if not exit_btn:
            ahora = datetime.now()
            print(ahora.strftime('ERROR FATAL: Ocurrió una desconexión en el transcurso de la sesión: '+m_id+'. %d/%m/%Y %H:%M:%S\n'))
            archivo.write(ahora.strftime('ERROR FATAL: Ocurrió una desconexión en el transcurso de la sesión: '+m_id+'. %d/%m/%Y %H:%M:%S\n'))
        else:
            pyautogui.moveTo(exit_btn)
            pyautogui.click()
            time.sleep(1)

        # Confirmación de Salida
            exitconfirm_btn = pyautogui.locateCenterOnScreen('exitconfirm_btn.png')
            pyautogui.moveTo(exitconfirm_btn)
            pyautogui.click()

        # Revisar si salí de la sesión o hubo un error.
        sharescreen_btn = pyautogui.locateCenterOnScreen('sharescreen_btn.png')
        if not sharescreen_btn:
            ahora = datetime.now()
            print(ahora.strftime('Se ha salido exitosamente de la sesión '+m_id+'. %d/%m/%Y %H:%M:%S\n'))
            archivo.write(ahora.strftime('Se ha salido exitosamente de la sesión '+m_id+'. %d/%m/%Y %H:%M:%S\n\n'))
            archivo.flush()
        else:
            ahora = datetime.now()
            print(ahora.strftime('Ha habido un ERROR y no has SALIDO de la sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S'))
            archivo.write(ahora.strftime('Ha habido un ERROR y no has SALIDO de la sesión: ' + m_id + '. %d/%m/%Y %H:%M:%S\n'))
            archivo.flush()
        time.sleep(60)