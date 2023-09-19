# Manual Técnico: Editor.py

El archivo `Editor.py` es un programa escrito en Python que implementa un editor de texto con funcionalidades adicionales. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

El programa `Editor.py` es una aplicación de editor de texto que utiliza la biblioteca `tkinter` para la interfaz de usuario. Permite al usuario abrir, editar y guardar archivos de texto en formato JSON. Además, ofrece las siguientes características:

- Barra de números de línea para facilitar la navegación en el texto.
- Opciones de menú para abrir, guardar y guardar como archivos.
- Funcionalidad de análisis de texto.
- Generación de gráficos utilizando Graphviz.
- Detección y manejo de errores léxicos en el texto.

## Componentes Principales

### `TextEditorApp` Clase

La clase `TextEditorApp` es la clase principal que define la aplicación de editor de texto. Sus principales atributos y métodos incluyen:

- `line_number_bar`: Barra de números de línea en el lado izquierdo del editor.
- `text_widget`: Área de edición de texto.
- `open_file()`: Método para abrir un archivo JSON.
- `save_file()`: Método para guardar un archivo JSON.
- `guardar_archivo()`: Método para guardar el archivo actual.
- `update_line_numbers()`: Método para actualizar los números de línea.
- `analizar()`: Método para analizar el texto y mostrar los resultados.
- `Errores()`: Método para detectar y mostrar errores léxicos.
- `gh()`: Método para generar gráficos utilizando Graphviz.

### Funciones y Métodos Auxiliares

El archivo también contiene varias funciones y métodos auxiliares que se utilizan para realizar tareas específicas, como el análisis de instrucciones y la generación de gráficos.

## Requisitos

Para ejecutar este programa, es necesario tener instalada una versión de Python que incluya las bibliotecas `tkinter` y `Graphviz`.

## Uso

1. Ejecute el programa `Editor.py`.
2. Utilice las opciones del menú "Archivo" para abrir, guardar y guardar como archivos.
3. Utilice la opción "Analizar" para analizar el texto y ver los resultados.
4. Utilice la opción "Graficar" para generar gráficos utilizando Graphviz.
5. Utilice la opción "Errores" para detectar y mostrar errores léxicos en el texto.

## Notas Adicionales

- El programa asume que se trabaja con archivos JSON.
- Los resultados del análisis y los gráficos generados se mostrarán en ventanas emergentes.

# Manual Técnico: Analizador.py

El archivo `Analizador.py` es un módulo Python que implementa un analizador léxico y una serie de funciones para procesar y operar con instrucciones en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

El módulo `Analizador.py` tiene dos funciones principales: la primera es analizar el código fuente en busca de tokens léxicos y la segunda es realizar operaciones basadas en instrucciones del lenguaje. Además, el módulo contiene clases y funciones auxiliares para gestionar errores y trabajar con lexemas y números.

## Componentes Principales

### Funciones Principales

1. `intruccion(cadena)`: Esta función toma una cadena de texto como entrada y realiza el análisis léxico para extraer lexemas y números. Los resultados se almacenan en listas y se devuelven como una lista de lexemas.

2. `operar()`: Esta función toma la lista de lexemas generada por `intruccion` y realiza operaciones basadas en las instrucciones presentes en el código. Las instrucciones se construyen a partir de los lexemas y se devuelven como una lista de instrucciones.

3. `operar_()`: Esta función llama a `operar` repetidamente hasta que no hay más instrucciones que procesar. Devuelve una lista de instrucciones resultantes.

4. `getErrores()`: Devuelve una lista de errores léxicos detectados durante el análisis.

### Clases

- `Lexema`: Clase que representa un lexema en el código fuente, almacena información como el valor del lexema, la línea y columna de inicio y fin.

- `Numero`: Clase que representa un número en el código fuente, almacena información similar a `Lexema`, pero para números.

### Variables y Listas Globales

- `reserved`: Un diccionario que contiene palabras clave reservadas del lenguaje junto con sus correspondientes tokens.

- `lexemas`: Una lista de tokens léxicos generados durante el análisis.

- `n_linea` y `n_columna`: Variables globales para rastrear la posición actual en el código fuente.

- `instrucciones`: Una lista que almacena las instrucciones resultantes después del análisis.

- `lista_errores`: Una lista que almacena errores léxicos detectados durante el análisis.

## Uso

1. Importa el módulo `Analizador.py` en tu código Python.

2. Llama a la función `intruccion(cadena)` con una cadena de texto que contenga el código fuente que deseas analizar. Esto generará una lista de lexemas.

3. Utiliza la función `operar_()` para realizar operaciones basadas en las instrucciones presentes en el código. Esto generará una lista de instrucciones resultantes.

4. Utiliza la función `getErrores()` para obtener una lista de errores léxicos detectados durante el análisis, si es necesario.

## Notas Adicionales

- El módulo está diseñado para trabajar con un lenguaje específico, y las palabras clave reservadas se definen en el diccionario `reserved`. Asegúrate de ajustar este diccionario según las necesidades de tu lenguaje.

# Manual Técnico: Aritmetica.py

El archivo `Aritmetica.py` es un módulo Python que implementa una clase llamada `Aritmetica`, que representa una expresión aritmética en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Aritmetica` es una subclase de `Expression` y se utiliza para representar operaciones aritméticas en el código fuente. Puede realizar operaciones de suma, resta, multiplicación, potencia, raíz, módulo y división, según el tipo de operación especificado.

## Componentes Principales

### Clase `Aritmetica`

- `__init__(self, left, right, tipo, fila, columna)`: Constructor de la clase `Aritmetica`. Recibe dos operandos (`left` y `right`), el tipo de operación (`tipo`), y las coordenadas de fila y columna en el código fuente donde se encuentra la expresión.

- `operar(self, arbol)`: Método que realiza la operación aritmética según el tipo especificado (`suma`, `resta`, `multiplicacion`, `potencia`, `raiz`, `mod`, `division`). Retorna el resultado de la operación.

- `getFila(self)`: Método que devuelve la fila donde se encuentra la expresión en el código fuente.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra la expresión en el código fuente.

## Uso

1. Importa la clase `Aritmetica` desde el archivo `Aritmetica.py` en tu código Python.

2. Crea una instancia de la clase `Aritmetica`, proporcionando los operandos, el tipo de operación y las coordenadas de fila y columna.

3. Llama al método `operar(arbol)` para realizar la operación aritmética y obtener el resultado.

4. Utiliza los métodos `getFila()` y `getColumna()` si necesitas obtener la ubicación de la expresión en el código fuente.

## Notas Adicionales

- La clase `Aritmetica` está diseñada para trabajar en conjunto con otros componentes de un analizador o intérprete de un lenguaje específico. Asegúrate de ajustar las operaciones y el comportamiento según las necesidades de tu lenguaje.

# Manual Técnico: T.py

El archivo `T.py` es un módulo Python que implementa una clase llamada `T`, que representa una expresión trigonométrica en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `T` es una subclase de `Expression` y se utiliza para representar expresiones trigonométricas en el código fuente. Puede realizar operaciones trigonométricas como el seno, coseno, tangente e inverso, según el tipo de operación especificado.

## Componentes Principales

### Clase `T`

- `__init__(self, left, right, tipo, fila, columna)`: Constructor de la clase `T`. Recibe un operando (`left`), el tipo de operación trigonométrica (`tipo`), y las coordenadas de fila y columna en el código fuente donde se encuentra la expresión.

- `operar(self, arbol)`: Método que realiza la operación trigonométrica según el tipo especificado (`seno`, `coseno`, `tangente`, `inverso`). Retorna el resultado de la operación.

- `getFila(self)`: Método que devuelve la fila donde se encuentra la expresión en el código fuente.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra la expresión en el código fuente.

## Uso

1. Importa la clase `T` desde el archivo `T.py` en tu código Python.

2. Crea una instancia de la clase `T`, proporcionando el operando, el tipo de operación trigonométrica y las coordenadas de fila y columna.

3. Llama al método `operar(arbol)` para realizar la operación trigonométrica y obtener el resultado.

4. Utiliza los métodos `getFila()` y `getColumna()` si necesitas obtener la ubicación de la expresión en el código fuente.

## Notas Adicionales

- La clase `T` está diseñada para trabajar en conjunto con otros componentes de un analizador o intérprete de un lenguaje específico. Asegúrate de ajustar las operaciones y el comportamiento según las necesidades de tu lenguaje.

# Manual Técnico: Texto.py

El archivo `Texto.py` es un módulo Python que implementa una clase llamada `Texto`, que representa una expresión de texto en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Texto` es una subclase de `Expression` y se utiliza para representar expresiones de texto en el código fuente. Esta clase se utiliza para manejar elementos relacionados con el texto, como texto normal, color de fondo, color de fuente y forma de nodo.

## Componentes Principales

### Clase `Texto`

- `__init__(self, texto, tipo, fila, columna)`: Constructor de la clase `Texto`. Recibe el texto a representar (`texto`), el tipo de expresión de texto (`tipo`), y las coordenadas de fila y columna en el código fuente donde se encuentra la expresión.

- `operar(self, arbol)`: Método que se deja sin implementar. Puede ser utilizado en futuras extensiones de la clase para realizar operaciones específicas con expresiones de texto.

- `ejecutarT(self)`: Método que devuelve el tipo de expresión de texto, como "texto", "fondo", "fuente" o "forma". Se utiliza para identificar el propósito de la expresión de texto.

- `getFila(self)`: Método que devuelve la fila donde se encuentra la expresión en el código fuente.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra la expresión en el código fuente.

## Uso

1. Importa la clase `Texto` desde el archivo `Texto.py` en tu código Python.

2. Crea una instancia de la clase `Texto`, proporcionando el texto, el tipo de expresión de texto y las coordenadas de fila y columna.

3. Utiliza el método `ejecutarT()` para obtener el tipo de expresión de texto y determinar su propósito.

4. Utiliza los métodos `getFila()` y `getColumna()` si necesitas obtener la ubicación de la expresión en el código fuente.

## Notas Adicionales

- La clase `Texto` se utiliza para manejar expresiones relacionadas con el formato y el estilo del texto, como colores, fuentes y formas de nodos. Su implementación y comportamiento específico pueden variar según las necesidades del lenguaje.

# Manual Técnico: Errores.py

El archivo `Errores.py` es un módulo Python que implementa una clase llamada `Errores`, que se utiliza para representar errores léxicos en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Errores` es una subclase de `Expression` y se utiliza para representar errores léxicos encontrados durante el análisis de un código fuente. Estos errores pueden estar relacionados con caracteres no reconocidos o problemas de sintaxis.

## Componentes Principales

### Clase `Errores`

- `__init__(self, lexema, fila, columna)`: Constructor de la clase `Errores`. Recibe el lexema que causó el error (`lexema`), así como las coordenadas de fila y columna en el código fuente donde se encuentra el error.

- `operar(self, no)`: Método que devuelve el lexema que causó el error. No se utiliza el parámetro `no`.

- `operarf(self, no)`: Método que devuelve la fila donde se encuentra el error en el código fuente. No se utiliza el parámetro `no`.

- `operarC(self, no)`: Método que devuelve la columna donde se encuentra el error en el código fuente. No se utiliza el parámetro `no`.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra el error en el código fuente.

- `getFila(self)`: Método que devuelve la fila donde se encuentra el error en el código fuente.

## Uso

1. Importa la clase `Errores` desde el archivo `Errores.py` en tu código Python.

2. Crea una instancia de la clase `Errores`, proporcionando el lexema que causó el error y las coordenadas de fila y columna.

3. Utiliza los métodos `operar()`, `operarf()`, y `operarC()` para obtener información sobre el error.

4. Utiliza los métodos `getFila()` y `getColumna()` si necesitas obtener la ubicación del error en el código fuente.

## Notas Adicionales

- La clase `Errores` se utiliza para registrar y manejar errores léxicos durante el análisis de un código fuente. Su implementación y comportamiento pueden variar según las necesidades del lenguaje.

# Manual Técnico: Abstract.py

El archivo `Abstract.py` es un módulo Python que contiene una clase abstracta llamada `Expression`. A través de esta clase abstracta, se establecen los métodos y atributos que deben ser implementados por las clases concretas que representan expresiones en un lenguaje específico. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Expression` es una clase abstracta que sirve como base para la representación de expresiones en un lenguaje de programación. Contiene métodos y atributos comunes que deben estar presentes en todas las expresiones concretas. Esta clase no se utiliza directamente en el análisis de código, pero establece una estructura común para las clases derivadas.

## Componentes Principales

### Clase Abstracta `Expression`

- `__init__(self, fila, columna)`: Constructor de la clase abstracta `Expression`. Recibe las coordenadas de fila y columna en el código fuente donde se encuentra la expresión.

- `@abstractmethod operar(self, arbol)`: Método abstracto que debe ser implementado por las clases derivadas. Representa la operación principal que realiza la expresión y devuelve un resultado.

- `@abstractmethod getFila(self)`: Método abstracto que debe ser implementado por las clases derivadas. Devuelve la fila donde se encuentra la expresión en el código fuente.

- `@abstractmethod getColumna(self)`: Método abstracto que debe ser implementado por las clases derivadas. Devuelve la columna donde se encuentra la expresión en el código fuente.

## Uso

1. Importa la clase `Expression` desde el archivo `Abstract.py` en tu código Python.

2. Crea una clase concreta que represente una expresión en tu lenguaje de programación.

3. Hereda de la clase abstracta `Expression` y asegúrate de implementar los métodos `operar()`, `getFila()` y `getColumna()` en tu clase concreta.

4. Utiliza la clase concreta para representar expresiones en tu código fuente y proporcionar la lógica de operación específica.

## Notas Adicionales

- La clase abstracta `Expression` se utiliza para establecer una estructura común para todas las expresiones en un lenguaje de programación. Las clases concretas que heredan de esta clase deben implementar la lógica de operación específica de cada tipo de expresión.

# Manual Técnico: Lexema.py

El archivo `Lexema.py` es un módulo Python que contiene una clase llamada `Lexema`. Esta clase representa un lexema en un lenguaje de programación y se utiliza para almacenar información sobre el lexema, como su valor y ubicación en el código fuente. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Lexema` se utiliza para representar un lexema en el análisis léxico de un lenguaje de programación. Un lexema es una unidad mínima de significado en un programa, como una palabra clave, un identificador, un número o un símbolo. Esta clase almacena el valor del lexema, así como su ubicación en el código fuente (fila y columna).

## Componentes Principales

### Clase `Lexema`

- `__init__(self, lexema, fila, columna)`: Constructor de la clase `Lexema`. Recibe el valor del lexema, así como las coordenadas de fila y columna en el código fuente donde se encuentra el lexema.

- `operar(self, arbol)`: Método que devuelve el valor del lexema.

- `operarT(self)`: Método que también devuelve el valor del lexema. Este método podría ser utilizado para obtener el valor del lexema en ciertas circunstancias.

- `getFila(self)`: Método que devuelve la fila donde se encuentra el lexema en el código fuente.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra el lexema en el código fuente.

## Uso

1. Importa la clase `Lexema` desde el archivo `Lexema.py` en tu código Python.

2. Crea instancias de la clase `Lexema` para representar lexemas en tu programa.

3. Utiliza el método `operar()` o `operarT()` para obtener el valor del lexema cuando sea necesario.

4. Utiliza los métodos `getFila()` y `getColumna()` para obtener la ubicación del lexema en el código fuente.

## Notas Adicionales

- La clase `Lexema` es útil en el análisis léxico de un lenguaje de programación, donde se identifican y clasifican los lexemas en el código fuente.

- Esta clase puede ser utilizada en conjunto con otras clases y componentes del analizador léxico para procesar y entender el código fuente.

# Manual Técnico: Numero.py

El archivo `Numero.py` es un módulo Python que contiene una clase llamada `Numero`. Esta clase representa un número en un lenguaje de programación y se utiliza para almacenar su valor y ubicación en el código fuente. A continuación, se proporciona una descripción técnica de su funcionamiento.

## Descripción General

La clase `Numero` se utiliza para representar un número en el análisis léxico y sintáctico de un lenguaje de programación. Almacena el valor del número, así como su ubicación en el código fuente (fila y columna).

## Componentes Principales

### Clase `Numero`

- `__init__(self, valor, fila, columna)`: Constructor de la clase `Numero`. Recibe el valor del número, así como las coordenadas de fila y columna en el código fuente donde se encuentra el número.

- `operar(self, arbol)`: Método que devuelve el valor del número.

- `getFila(self)`: Método que devuelve la fila donde se encuentra el número en el código fuente.

- `getColumna(self)`: Método que devuelve la columna donde se encuentra el número en el código fuente.

## Uso

1. Importa la clase `Numero` desde el archivo `Numero.py` en tu código Python.

2. Crea instancias de la clase `Numero` para representar números en tu programa.

3. Utiliza el método `operar()` para obtener el valor del número cuando sea necesario.

4. Utiliza los métodos `getFila()` y `getColumna()` para obtener la ubicación del número en el código fuente.

## Notas Adicionales

- La clase `Numero` es útil en el análisis léxico y sintáctico de un lenguaje de programación para representar constantes numéricas.


