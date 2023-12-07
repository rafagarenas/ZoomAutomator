
# Zoom Automator
Este script automatiza la entrada y salida de sesiones de Zoom en base a un horario predefinido. El programa utiliza la biblioteca **pyautogui** para realizar acciones automatizadas en la interfaz gráfica de usuario.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas:


```http
pip install pandas pyautogui
```

## Uso

1. Ejecuta el script.

2. El programa verificará si Zoom está abierto. Si no lo está, se abrirá automáticamente.

3. El script buscará en el archivo CSV timings.csv las reuniones programadas en el momento actual.

4. Si encuentra una reunión programada, ingresará automáticamente a la sesión con el ID y la contraseña proporcionados.

5. Después de un tiempo predeterminado, el programa verificará si es hora de salir de la reunión y realizará la desconexión correspondiente.

## Archivos Necesarios

* timings.csv: Un archivo CSV que contiene las horas de inicio (timings), los IDs de las reuniones y sus contraseñas.

* Imágenes necesarias para la identificación de elementos en la interfaz gráfica de Zoom: **zoomgui.png, join_button.png, meeting_id_button.png, join_btn.png, sharescreen_btn.png, micoff_btn.png, exit_btn.png, exitconfirm_btn.png.**

## Notas
* Asegúrate de tener todas las imágenes necesarias en la misma carpeta que el script.

El programa generará un archivo de registro llamado logs.txt donde se registrarán eventos importantes, como la ejecución del programa, errores y acciones realizadas.

Ten en cuenta que el uso de automatización en aplicaciones como Zoom puede estar sujeto a las políticas y términos de servicio de Zoom. Utiliza este script con responsabilidad y respetando las normas de uso de la plataforma.
