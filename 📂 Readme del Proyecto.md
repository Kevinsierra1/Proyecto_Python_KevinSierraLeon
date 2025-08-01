1. 📘 Descripción General

   Este proyecto es una aplicación de consola desarrollada en Python para la gestión de colecciones personales. Permite a los usuarios organizar y mantener un registro de sus libros, películas y música de manera sencilla e intuitiva. Toda la información de la colección se guarda de forma persistente en un archivo JSON, lo que permite reanudar la sesión en cualquier momento.

   # 📂 Estructura del Proyecto

   El proyecto está organizado con la siguiente estructura de archivos y carpetas, que separa la lógica de los menús, las utilidades y los datos:

   

   ```
   (root)/
   │
   ├── data/
   │   └── db.json                 # Archivo JSON que almacena toda la información de la colección.
   │
   ├── menus/
   │   ├── aniadir_elemento.py     # Lógica para el submenú y registro de nuevos elementos.
   │   ├── buscar_elemento.py      # Lógica para la búsqueda de elementos en la colección.
   │   ├── editar_elemento.py      # Lógica para modificar la información de elementos existentes.
   │   ├── eliminar_elemento.py    # Lógica para borrar elementos de la colección.
   │   ├── guardar_collecion.py    # Lógica para guardar y cargar la colección desde/hacia el JSON.
   │   ├── ver_elemento.py         # Lógica para mostrar todos los elementos.
   │   └── ver_por_categoria.py    # Lógica para filtrar y mostrar elementos por su categoría.
   │
   ├── utils/
   │   ├── corefiles.py            # Funciones centrales para leer y escribir en el archivo db.json.
   │   ├── screenController.py     # Funciones para limpiar la pantalla y pausar la ejecución.
   │   └── validateData.py         # Funciones para validar los datos ingresados por el usuario.
   │
   ├── app.py                      # Punto de entrada de la aplicación. Contiene el menú principal.
   └── config.py                   # Archivo para configurar rutas o constantes del proyecto.
   ```

   # 🚀 Funcionalidades Principales

   El sistema se organiza en torno a un menú principal que da acceso a todas las funcionalidades clave de la aplicación:

   ### 1. Gestión de la Colección

   - 
   - **Añadir un Nuevo Elemento:** Permite registrar nuevos libros, películas o música. El sistema solicita los datos correspondientes a cada categoría.
   - **Ver Todos los Elementos:** Muestra una lista completa y detallada de todos los ítems registrados en la colección.
   - **Editar un Elemento:** Ofrece la posibilidad de modificar la información de un elemento existente, como su título, autor/director/artista, género o valoración.
   - **Eliminar un Elemento:** Permite borrar un elemento de la colección, ya sea buscándolo por su título o a través de un identificador único.

   ### 2. Búsqueda y Filtrado

   - 
   - **Búsqueda Específica:** Facilita la localización de un elemento concreto mediante una búsqueda por título, autor/director/artista o por género.
   - **Vista por Categoría:** Permite filtrar la colección para mostrar únicamente los libros, las películas o la música, según la elección del usuario.

   ### 3. Persistencia de Datos

   - 
   - **Guardar y Cargar Colección:** Da al usuario el control para guardar la colección actual en un archivo db.json en cualquier momento. Del mismo modo, puede cargar una colección previamente guardada para continuar gestionándola.

   # 🛠️ Tecnologías Utilizadas

   - 
   - **Lenguaje:** Python 3
   - **Manejo de Datos:** Módulo json para la serialización y deserialización de la colección.
   - **Sistema de Archivos:** Módulo os (usado en screenController.py) para interactuar con el sistema operativo y limpiar la consola.

   # ⚙️ Cómo se Ejecuta

   No se requiere la instalación de ninguna librería externa, solo tener Python 3 instalado en tu sistema.

   1. 

   2. Clona o descarga el repositorio en tu máquina local.

   3. Abre una terminal o línea de comandos.

   4. Navega hasta la carpeta raíz del proyecto.

   5. Ejecuta el punto de entrada de la aplicación con el siguiente comando:

      ```
      python app.py
      ```

   