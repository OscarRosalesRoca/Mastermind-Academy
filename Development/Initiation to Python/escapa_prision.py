title ="La mazmorra del Enigma Eterno"
print("\n" + title + "\n" + "-" * len(title) + "\n")

#Inventario
botella_agua = False
cuchillo_oxidado = False
sandwitch = False
pocion = False


print("Despiertas en el suelo frío de una mazmorra oscura. Unas antorchas parpadean en la lejanía, revelando dos caminos frente a ti.\n"
      "Uno iluminado con las antorchas y otro en completa oscuridad. No recuerdas cómo llegaste aquí, pero sabes que debes salir.\n"
      "A tu alrededor, notas algunos objetos:\n"
      "una botella de agua y un cuchillo oxidado. ¿Qué decides llevar contigo? Solo puedes un objeto\n")


objetos_iniciales = int(input(  "1. Una botella de agua\n"
                                "2. Un cuchillo oxidado\n"
                                "Escribe el número de tu opción:"))
if objetos_iniciales == 1:
    botella_agua = True
elif objetos_iniciales == 2:
    cuchillo_oxidado = True


primera_desviacion = input("¿Seguirás el camino iluminado por las antorchas (A) o te aventurarás en la oscuridad total(O)?")
if primera_desviacion == "A":
    print("\nSigues la tenue luz de las antorchas y llegas a una gran puerta de piedra. Un guardián esquelético se \n"
          "encuentra allí, con un báculo de energía brillante.\n"
          "'Solo aquellos que resuelvan mis acertijos podrán seguir adelante', dice con una sonrisa macabra.\n")

    primer_acertijo = int(input("'Si tienes dos manzas y tomas dos más, ¿cuántas tienes?'"))
    if primer_acertijo == 4:
        print("\n'Muy bien muy bien... No creas que te saldrás tan facilmente con la tuya...' Dice riéndose y acariciando su báculo.")
        segundo_acertijo = input("'Si un reloj marca las 3:15 y el ángulo entre las manecillas es de 7.5 grados,\n"
                                 "¿qué hora será cuando el ángulo sea de 90 grados?'")
        if segundo_acertijo == "3:30":
            print("\n'¡CÓMO! ¡NO PENSÉ QUE PODRÍAS SOLUCIONARLO! Sigue tu camino aventurero, la suerte no siempre estará de tu lado'")
            opcion = input("\nCruzas la puerta y te encuentras en una sala con un cofre. Decides abrirlo y dentro encuentras:\n"
                            "Un sandwitch y una poción de salud.\n"
                            "¿Qué decides coger? (S)Sandwitch o (P)Poción de salud: ")
            if opcion == "S":
                sandwitch = True
            print("\nSigues avanzando y encuentras una enorme criatura peluda encadenada a la puerta de salida.\n"
                  "'¡TENGO HAMBRE! Dame algo de comer o serás tú mi cena', ruge la bestia.")
            if sandwitch:
                print("Recuerdas que en la sala anterior conseguiste un sandwitch, se lo das de comer y parece que le gusta.\n"
                      "'ÑAM ÑAM... Buena comida, te dejaré salir'\n"
                      "La bestia te abre la puerta y sales de la mazmorra ileso.")
            else:
                print("Con terror en los ojos recuerdas que no coguiste el sandwitch hace unos momentos. Intentas escapar pero\n"
                      "la bestia te coge con sus grandes manos y te devora al instante.")
        else:
            print("'¡RESPUESTA EQUIVOCADA!' El esqueleto agita su mano libre por encima del báculo y de golpe explotas en mil pedazos")
            exit()
    else:
        print("'¡RESPUESTA EQUIVOCADA!' El esqueleto agita su mano libre por encima del báculo y de golpe explotas en mil pedazos")
        exit()
elif primera_desviacion == "O":
    print("\nAvanzas a ciegas y tropiezas con un foso profundo. Al tantear el suelo encuentras una cuerda gastada que baja hacia las profundidades.\n"
          "Por un acto de valentía o inconsciencia decides bajar por la cuerda y te encuentras en una sala con un anciano en ella.\n"
          "\n'¿Quien eres tú?' Pregunta incrédulo y algo nervioso, no sabes por qué. 'No me importa... Acabé aquí hace unos días, no recuerdo cómo llegue a esta mazmorra\n"
          "pero al despertarme entre sus pasillos encontré una botella de agua y un cuchillo. Me llevé conmigo el agua pero me la terminé hace un día.\n"
          "¿No tendrás tú alguna botella de agua también no?'\n"
          "Te pregunta mientras se le iluminan los ojos. Un esalofrío te recorre la espalda")
    if botella_agua:
        print("\nLe contestas con algo de desconfianza que sí tienes contigo una botella de agua y se la puedes prestar\n"
              "'Bien bien... Veo que eres amable. No me gusta la gente que no es amable ¿sabes? Quizá habría hecho algúna locura...\n"
              "Te mentí muchacho, soy un guardian de una de las puertas que dan al exterior de la mazmorra, sígueme y te llevaré a ella'\n"
              "El anciano te conduce por un pasillo hasta una puerta, la cuál cruzas. Se cierra rápidamente una vez estás fuera")
    else:
        print("\nConfuso le dices que no, que no tienes ninguna botella de agua.\n"
              "'¡CÓMO QUE NO TIENES AGUA! ¡¿CÓMO VOY A SOBREVIVIR SINO?! ¡¿ME MIENTES VERDAD?! Sé que tienes una no me engañes...'\n"
              "Preso de la ira se avalanza hacia a tí, pero en el acto recuerdas que cogiste el cuchillo al despertarte.\n"
              "Empuñas temblando tu cuchillo y te libras del anciano, clavándoselo en la barriga cuando saltaba hacia tí.\n"
              "Con miedo a un nuevo obstáculo en tu camino, continuas caminando en la oscuridad y llegas a una puerta, pero está cerrada.\n"
              "Intentas abrirla y no puedes. Vuelves a la sala e intentas subir por la cuerda pero esta se rompe. Te has quedado atrapado.")