# Basta_game
Game similar to basta, using python and  Kivy

game:
Un juego similar a "basta".

Como funcionara el juego:
1 - Primero dará una categoria al azar (de una lista de categorias) al apretar un boton "categoria".
2 - EL juego iniciara al apretar un boton "iniciar".
3 - Aparecera en la pantalla un boton que diga "Basta", debajo del boton una letra grande y una barra con un time que durará 5 segundos.
4 - El jugador en turno tendra que decir un palabra que iniciara con la letra que apareció y la categoria
5 - Ccuando diga la palabra, aparecera una nueva letra y será turno del siguiente jugador.
6  - Si el timer termina, en el centro aparecera EL mensaje "You lose!"
7 - Ese jugador ya perdió ahora el siguiente jugador tiene que apretar el boton iniciar y el juego continuará "Iniciar"
8 - Cuando solo quede un jugador, el juego termina y el jugador ganará un punto.
9 - Los jugadores apretan un boton "reset" para reiniciar las letras.

Notas: Las letras aparecerán al azar de la A ala Z sin que se repitan.
Por eso cuando apreten azar las letras se reiniciaran y ya podran aperecer todas otravez.

La pantaññapantalla debe tener:
1- Un boton que diga "categorias"
2 - un boton que diga "resetear"
3 - un boton que diga "iniciar"
4 - un timer con forma de barra de caraga que contara del 5 al 0.
5 - Si el timer llega a cero aparece la el mensaje "You lose!".
6 - Una letra en grande del abecedario que cambiara cuando apretes el boton iniciar.

