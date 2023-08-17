```sh

Autor: Edwin Vargas
Entrga: Proyecto Final
Nombre: WEB_AV

El programa desarrollado es para una WEB de una Agencia de Viajes. 

Navegacion:
Sistema: para correr el sistema:http://127.0.0.1:8000/packages
Seleccionar opsion de menu Login, luego tienes dos opsiones Login o Registrate

Login:
usuario: admin
clave: admin123

Al Loguearse, se despliega un menu con diferentes opsiones de navegacion:
_admin1: Cuatro opsiones relacionadas al CRUD: Category, Classification, Product, User
_admin2: Administrador de Django
_Yo: Un poco como se construyo este proyecto
_Search: Busqueda de producto filta por titulo del producto
_Destino: Despliga las categorias creadas y al seleccionar una de ellas realiza una consulta filtrando por el fk de Category.
_Tipo: Despliga los Tipos creados y al seleccionar uno de ellos realiza una consulta filtrando por el fk de Classification
Hola, 'usuario': permite editar el perfil del usuario
_Logoud: sale del menu principal


Codigo:
El proyecto principal se llama core
Cree una carpeta con el nombre de apps donde estan dos app: packages y users
Cada app tiene una carpeta de templates con los archivos html para su funcionamiento
Hay una carpeta principal de templates donde estan el archivo base, home y about.
Los archivos static estan en una sola carpeta principal, no estan en las apps.
El codigo creado esta en ingles y las acciones trato que sean bien descriptivas.

Gracias por leerme y que le pueda servir.
