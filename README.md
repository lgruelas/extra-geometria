# Extraordinario de Geometria Computacional.

Luis Germán Ruelas Luna.

## Notas de problemas
Al principio empecé a escribir los comentarios del código en ingles, pero después cambié a español, perdón :(
Los de python tienen unittests que iba escribiendo para ayudarme en el desarrollo.

### Problema 1
El código es casi en su totalidad de cuando curse la materia por primera vez, me limité a actualizar la medida de distancia.
- Código fuente: [first.cpp](https://github.com/lgruelas/extra-geometria/blob/master/first.cpp)

### Problema 2
__NO TERMINADO__ Para este me basé en el libro que me recomendaste la primera vez que tomé el curso: Computational Geometry - Algorithms and Applications, 3rd Ed.

El event queue lo implementé como una heap porque para el caso de intersección entre dos conjuntos de segmentos, ya no es tan malo meter dos veces el mismo punto (en el libro comenta que se implementa como arbol binario en lugar de como heap para buscar si ya hay un punto), porque algunos podrían ser del conjunto azul y otros del rojo, entonces se tiene que buscar por intersecciones en los dos, en los segmentos correspondientes al color contrario.

En este no se me ocurrió muy bien como resolverlo, pero la ídea es:
- Mantener una *structure* (los segmentos que toca la *sweep_line*) que solo contenga los segmentos rojos.
- Mantener otra *structure* que solo contenga los elementos azules.
- Cada vez que llegue a un *event point*, revisar si es azul o rojo, y buscar las intersecciones en el *structure* de otro color.
- Se sigue la misma idea que para buscar todas las intersecciones en un conjunto de segmentos, de buscar solo en los vecinos y cosas así.


- Código fuente: [second.py](https://github.com/lgruelas/extra-geometria/blob/master/second.py)

### Problema 3
Gran parte es actual, pero también saqué una parte de un código mío que escribí para una clase de Adriana.
Las suposiciones que hago para mi respuesta son:
- Si un punto *p* está dentro de la componente convexa de un conjunto de puntos, necesariamente puede estar contenido en un triangulo formado por 3 puntos del conjunto *x*.
- Si añado el punto *p* al conjunto original de puntos *x*, saco la componente convexa y *p* se encuentra en ella, puedo asumir que está fuera del área delimitada por el polígono que forma la componente convexa del conjunto original de puntos *x*, y por lo tanto, no se pueden tomar 3 puntos del conjunto *x* que contengan a *p*.

Archivos:
- Código fuente: [third.py](https://github.com/lgruelas/extra-geometria/blob/master/third.py)

## Tests
```bash
nosetests -v
```