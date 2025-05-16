Sistema AgroTech Coop

Descripción

Este proyecto es una práctica en Python que simula un sistema de gestión para una cooperativa agrícola, AgroTech Coop. El programa ofrece una interfaz de consola interactiva con un menú principal y submenús para gestionar parcelas, sensores, registrar mediciones y consultar datos. Está diseñado para practicar estructuras de control (bucles y condicionales), entrada/salida por consola y organización de menús en Python.

Características

Menú Principal: Permite seleccionar entre cinco opciones: Gestionar Parcela, Gestionar Sensores, Registrar Mediciones, Consultar Datos y Salir.

Submenús Interactivos:

Gestionar Parcela: Ver, agregar, modificar o eliminar parcelas (ejemplo: "Campo Norte - Soja").

Gestionar Sensores: Ver o agregar sensores (ejemplo: "Termómetro - Parcela 1").

Registrar Mediciones: Registrar datos de sensores (ejemplo: temperatura).

Consultar Datos: Ver todas las mediciones o filtrar por sensor.

Interfaz de Consola: Menús claros con formato ASCII para una experiencia de usuario amigable.

Salida Simulada: Muestra resultados predefinidos para cada acción, simulando la gestión de datos.

Tecnologías Utilizadas

Python 3: Para la lógica del programa, usando bucles (while), condicionales (if-elif), y entrada/salida por consola (input y print).

Instrucciones de Configuración

Para ejecutar este proyecto localmente, sigue estos pasos:

Clonar el Repositorio:

git clone https://github.com/tu-usuario/tu-nombre-repositorio.git

Navegar al Directorio del Proyecto:

cd tu-nombre-repositorio

Ejecutar el Programa:

Asegúrate de tener Python 3 instalado.

Ejecuta el archivo principal (por ejemplo, menu.py):

python menu.py

Estructura de Archivos (asumida):

tu-nombre-repositorio/
├── menu.py
└── README.md

Uso

Ejecución: Al correr el programa, se muestra un menú principal con cinco opciones. Ingresa un número del 1 al 5 para seleccionar una acción.

Navegación: Cada opción (excepto "Salir") lleva a un submenú con acciones específicas. Selecciona un número para realizar una acción o regresar al menú principal.

Acciones:

Gestionar Parcela: Muestra parcelas registradas, agrega una nueva, modifica una existente o elimina una.

Gestionar Sensores: Lista sensores o agrega uno nuevo.

Registrar Mediciones: Registra datos simulados de sensores.

Consultar Datos: Muestra todas las mediciones o las de un sensor específico.

Salida: Los resultados son mensajes predefinidos que simulan la gestión de datos, como:

_________Parcelas Registradas________
Parcela 1: Campo Norte - Soja (10 ha)
Parcela 2: Campo Sur - Maíz (7 ha)


Salir: Selecciona la opción 5 para cerrar el programa.

Mejoras Futuras

Implementar una base de datos (por ejemplo, con listas, diccionarios o SQLite) para almacenar parcelas, sensores y mediciones en lugar de usar datos simulados.

Agregar validación de entrada para manejar errores (por ejemplo, entradas no numéricas).

Incluir más funcionalidades, como filtrar parcelas por cultivo o generar reportes gráficos de mediciones.

Crear una interfaz gráfica (con Tkinter o PyQt) para reemplazar la consola.

Añadir autenticación de usuario para simular un sistema multiusuario.

Contribuciones

Este es un proyecto de práctica personal, pero las sugerencias son bienvenidas. Si deseas contribuir, haz un fork del repositorio, realiza tus cambios y envía un pull request.

Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

Agradecimientos

Desarrollado como ejercicio para practicar estructuras de control y menús interactivos en Python.

Inspirado en sistemas de gestión agrícola modernos.
