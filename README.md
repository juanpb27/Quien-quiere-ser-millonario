# Quien-quiere-ser-millonario

_**"Quien quiere ser millonario"** es un entretenido concurso de preguntas y respuestas. Está compuesto por 5 rondas de diferente nivel y categoría.
En cada ronda se debe responder 1 pregunta de opción múltiple y única respuesta, extraída aleatoriamente de un banco. El jugador va
ganando premios por ronda, y puede retirarse con el valor acumulado antes de responder, pero **si se equivoca pierde TODO**_

## Comenzando 🛠️

_Para desplegar este proyecto en tu pc puedes iniciar descargando el repositorio y utilizar un editor de código como **Visual Studio Code.**_

### Pre-requisitos 📋

_Este proyecto fue desarrollado con **Python 3.9.7**_

### Configuración 🔧

_Todo el proyecto está configurado para que no tengas que cargar archivos adicionales o realizar ajustes. Sin embargo, si deseas realizar modificaciones,
a continuación están los aspectos más importantes:_

1. _ Debido a que cada ronda tiene preguntas de diferentes categorias, debes cargar 5 bancos diferentes:_

```
from banco import banco1, banco2, banco3, banco4, banco5
bancos = [banco1, banco2, banco3, banco4, banco5]
```

2. _Puedes cambiar el número de rondas, pero si las aumentas, recuerda agregar los bancos de pregunta que hagan falta.
También puedes cambiar el tipo de premio (puntos/dinero):_

```
´rds = 5´
tipo = "puntos"
```

## Puesta en marcha 🚀

_Puedes utilizar una terminal como cmd. Estando en ella, debes ubicarte en la carpeta del proyecto y correr el archivo main.py, de la siguiente forma:_

```
cd Tu-ruta\Quien-quiere-ser-millonario-master
python main.py
```

_El historial de resultados se guardará en el archivo "registro.csv"_

---
## Autor ✒️

**Juan Camilo Peña Bermúdez** - [juanpb27](https://github.com/juanpb27)


