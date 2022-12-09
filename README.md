# API de aprobación de créditos a clientes
API REST que permite aceptar o rechazar el otorgamiento de un crédito a un cliente. Fue desarrollada con el lenguaje Python bajo el Framework Flask en backend e integración de base de datos MySQL.

### Pre - requisitos
Python
```
https://www.python.org/downloads/
```
## Cargar base de datos
### Descargar servidor de base de datos XAMPP
```
https://www.apachefriends.org/download.html
```
### Cargar script 
```
1. Abrir el cliente phpMyAdmin desde el navegador: http://localhost/phpmyadmin/
2. Click en "Nueva"
3. Escribir el nombre de la base de datos: crediclub, clic en crear.
4. Clic en "Importar".
5. Buscar el archivo "crediclub.sql", en la carpeta "sql" del repositorio y cargarlo.
6. Clic en importar.
```

### Instalación de dependencias
```
git clone https://github.com/r00tsh4rk/crediclub_api/
```
```
cd crediclub_api
```
```
pip install -r requeriments.txt
```

### Ejecución de la API
```
cd crediclub_api/src
python app.py
```

### Acceso mediante cliente REST
####  Extensión Thunder Client para Visual Studio Code
```
https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
```
####  POSTMAN
```
https://www.postman.com/
```
####  ADVANCE REST CLIENT (EXTENSIÓN DE GOOGLE CHROME)
```
https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo/related?hl=es
```
### Probar la API 
```
Abrir alguno de los clientes REST sugeridos o de su preferencia y colocar la siguiente URL:
http://127.0.0.1:5000/listar
```


### Captura de pantalla de la tabla con datos ingresados
```
Consultar la carpeta img del presente repositorio.
```


### Problemas de conexión con MySQL en Linux
```
sudo apt-get install libmysqlclient-dev
```
