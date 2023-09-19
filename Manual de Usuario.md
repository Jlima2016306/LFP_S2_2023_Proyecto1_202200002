# Manual de Usuario

En este manual de usuario, se describe cómo utilizar la aplicación de editor de texto y el lenguaje de programación desarrollados en Python. El proyecto consta de varios componentes y archivos, y este manual te guiará a través de su uso.

## Aplicación de Editor de Texto

### Editor.py

La aplicación de editor de texto es una herramienta que te permite abrir, editar y guardar archivos de texto. También ofrece funciones adicionales para analizar operaciones matemáticas y generar gráficos. A continuación, se describen las principales características y funciones de la aplicación:

#### Características Principales

- **Abrir Archivos**: Puedes abrir archivos de texto existentes haciendo clic en "Archivo" > "Abrir" y seleccionando el archivo deseado desde tu sistema de archivos.

- **Editar Archivos**: La aplicación te permite editar el contenido del archivo de texto. Puedes realizar cambios en el texto según tus necesidades.

- **Guardar Archivos**: Después de realizar modificaciones en el archivo, puedes guardar los cambios haciendo clic en "Archivo" > "Guardar". También puedes usar "Guardar como" para guardar el archivo con un nombre diferente.

#### Funciones Adicionales

- **Análisis de Operaciones Matemáticas**: La aplicación tiene la capacidad de analizar operaciones matemáticas presentes en el archivo de texto. Para realizar un análisis, selecciona el texto con la operación y luego haz clic en "Análisis" > "Analizar Operación".

- **Generación de Gráficos**: Si tienes una operación matemática válida, puedes generar un gráfico haciendo clic en "Análisis" > "Generar Gráfico". Esto utilizará la biblioteca Graphviz para crear visualizaciones de las operaciones.

- **Detección de Errores Léxicos**: La aplicación puede detectar errores léxicos en el código fuente. Si se encuentran errores, se generará un archivo JSON de registro de errores que podrás consultar.

## Lenguaje de Programación

El lenguaje de programación es una parte integral de la aplicación de editor de texto. Aquí se describen las clases y archivos relacionados con el lenguaje de programación:

### Archivos de Instrucciones

- **Aritmetica.py**: Define la clase `Aritmetica`, que permite realizar operaciones aritméticas como suma, resta, multiplicación, división, potencia, raíz, y módulo.

- **T.py**: Define la clase `T`, que representa operaciones trigonométricas como seno, coseno, tangente e inverso.

- **Texto.py**: Define la clase `Texto`, que representa valores de texto (cadenas de caracteres) y sus tipos (texto, fondo, fuente y forma).

### Archivo de Errores

- **Errores.py**: Define la clase `Errores`, que se utiliza para almacenar información sobre errores léxicos, incluyendo el lexema, la fila y la columna donde ocurrió el error.

### Clases Abstractas

- **Abstract.py**: Contiene una clase abstracta llamada `Expression`, que sirve como base para las clases relacionadas con expresiones y elementos del lenguaje de programación.

### Clases de Utilidad

- **Lexema.py**: Define la clase `Lexema`, que representa un lexema en el lenguaje de programación y su ubicación en el código fuente.

- **Numero.py**: Define la clase `Numero`, que representa un número en el lenguaje de programación y su ubicación en el código fuente.

Este manual de usuario proporciona una descripción general de la aplicación de editor de texto y el lenguaje de programación asociado. Puedes utilizar la aplicación para editar y analizar archivos de texto, así como explorar las clases y funciones del lenguaje de programación para realizar operaciones matemáticas y detectar errores léxicos. ¡Disfruta utilizando esta herramienta versátil!
