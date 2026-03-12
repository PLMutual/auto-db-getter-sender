# Recolector de Data de Ordenes Médicas & Mailer

## Setup
1. Antes de empezar se recomienda crear un ambiente virtual de trabajo. 
    1. Run: `python -m venv auto-mail`
        - Puedes usar otro nombre en vez de `auto-mail` si lo profieres, da lo mismo
        - Para trabajar dentro del ambiente virtual hay que correr el script `activate` que está dentro de la carpeta autogenerada Scripts.
    2. Actualizar pip
        - Run: `python.exe -m pip install --upgrade pip`
    3. Copia o clona el codigo dentro del ambiente virutal

2. Instalar los modulos necesarios
    - Run `python -m pip install -r requirements.txt`
        - Esto instalará todos los modulos dentro del archivo de texto de requerimientos

## Run
0. Preparación:
    1. Asegurarse de estar conectado a la red comercial a travéz de cable, wifi o VPN.
        - En caso de no estar conectado, al intenter conectarse a la base de datos y fallar se termina la ejecución del programa. (Es algo nativo de la librería de SAP.)
    2. En caso de haber creado el ambiende virutal, correr: `Scripts\activate`
1. Correr: `python src\main.py`
    - Tambien se pueden correr cualquiera de los archivos dentro de la carpeta src, para testear las funcionalidades de los modulos. 

## To Do
- Pasar el mailer a Graph, para poder dejar de usar rutas absolutas para el archivo a mandar

