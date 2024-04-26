# Para los desarrolladores

Este archivo contiene comandos para configurar el entorno virtual de Python y no haya errores de compatibilidad

# Configuration del entorno
Para empezar necesitamos tener Python en su ultima versión instalado y la herramienta PIP, instalada tambien. 
Para la  herramienta pip dejo el link para que lo instalen dependiendo desde donde estén programando: `https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/`

 - Para instalar el entorno virtual usamos `pip install virtualenv`

Una vez hecho esto no notaremos ningún cambio hasta que ejecutemos el siguiente comando para instalar los archivos del entorno virtual en nuestra carpeta. `virtualenv venv`

Una vez que estemos ya programando necesitamos tener activado el entono virtual para ello ejecutamos el siguiente comando:
`.\venv\Scripts\activate`
Podremos comprobar que si lo activamos correctamente ya que no tendremos errores y el prompt de nuestra terminal lucirá asi.
`(venv) C:/projecto>.....` 

Ya una vez hecho esto tenemos todo listo para empezar a programar, solamente tenemos que seleccionar el interprete de Python ubicado en la carpeta `\venv` desde nuestro editor de código en turno.


