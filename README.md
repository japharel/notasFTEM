# Notas de Fundamentos de Teoría Electromagnética

Hola, bienvenidxs a este repositorio.

Aquí podrán encontrar Jupyter Notebooks con las notas del curso de *Fundamentos de Teoría Electromagnética*, impartido por el Dr. Andrés Tejero Andrade en la Facultad de Ingeniería de la UNAM.

Espero esto sea de utilidad para quien lo consulte y pueda darles una perspectiva diferente a este curso, de una manera interactiva y visual.

Versión a 22/02/23: **v1.0.0**

<ins>**v1.0.0 (22/02/23)**</ins> 

- Actualización del archivo **README.md**
    - Descripción de las versiones anteriores y versión actual
- Organización de directorios:
    - utils -> ftem
    - Eliminado directorio src
    - ftem_toolbox -> toolbox
    - Se elimina un notebook ajeno al proyecto
- Generación de código por medio de sympy:
    - Uso de las ecuaciones analítcas del campo gravitacional y conversión a aproximaciones numéricas por medio de la función ```lambdify```
    - Corrección de la gráfica del contorno y las líneas del campo:
        - Uso de las componentes esférica/polar para el contorno del campo
        - Uso de las componentes cartesiandas para las líneas del campo
- Opciones para personalizar las gráficas:
    - Opciones para graficar sólo líneas del campo, contorno del campo o ambos
    - Mapa de colores para el contorno del campo
    - Colores para las líneas del campo
    - Selección de aspecto de la gráfica
- Corrección del efecto infinito en r = 0 para la gráfica del campo gravitacional
    - Adición de un ruido experimental, cuya proporción permite una mejor visualización del campo (contorno y líneas) sin observar el efecto de tendencia al infinito en r = 0, así como una visualización completa del campo dentro del rango establecido.

*v0.2.1* (25/01/23)

- Organización de directorios:
    - eliminado directorio por notebook por conflictos para usar el módulo **ftem_toolbox**
- Ajustes menores al módulo **ftem_toolbox**:
    - Esqueleto inicial para implementación futura de gráficas 3D de campos
- Versión beta del notebook Tema02:
    - Sólo texto y desarrollos de ecuaciones, sin imágenes aún

*v0.2.0* (22/01/23)

- Organización de directorios:
    - Creación del directorio utils:
        - images
        - src
    - Creación del directorio Tema01
- Implementación del script **ftem_toolbox**:
    - Clases gravityField y magneticField
    - Gráfica de campos usando componentes cartesianas
        - Se añade un ruido experimental para evitar problemas en r = 0
    - Opciones para graficar líneas de campo o también el contorno

*v0.1.0* (27/05/22)

- Creación del proyecto:
    - Versión inicial del notebook Tema01
    - Directorio para imágenes