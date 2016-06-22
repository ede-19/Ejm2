# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
# - El juego comienza aquí.

label start:

    e "So finally i discover the murder"
    python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/dsapandora/adriandetective.pl')
        asesino = list(prolog.query('murderer(X)'))
        lista_contradicciones = list(prolog.query('contradictory(X,Y)'))
        menu_contradiccion = []
        for contradiccion in lista_contradicciones:
          menu_contradiccion.append((contradiccion['X']+" "+contradiccion['Y'] ,'one'))
        result = menu(menu_contradiccion)
        e("The murder is %s y se selecciono %s"%(asesino[0]['X'],result))
        new_prolog_code = open('/home/dsapandora/adriandetective.pl','a')
        new_facts = []
    menu:
        "Buy her an Iguana":
            python:
                new_facts.append('contradictory(knife,gun).\n')
                new_facts.append('contradictory(gun,knife).\n')
            $ gift = "iguana"
            e "I'll take an iguana, my good man!"
        "Buy her a Corn Snake":
            python:
                new_facts.append('murderer(jason).\n')
                new_facts.append('claims(carl,[[innocent,carl],[inTown,burt],[inTown,carl]]).\n')
            $ gift = "corn snake"
            e "I'll take a Corn Snake, my good man!"
    python:
        new_set_of_facts = list(set(new_facts))
        for x in new_set_of_facts:
            new_prolog_code.write(x)
        new_prolog_code.close()
        prolog2 = Prolog()
        prolog2.consult('/home/dsapandora/murder.pl')
        asesino = list(prolog2.query('murderer(X)'))
        e("The murder is %s"%asesino[0]['X'])

    return

label art:
  e "soy el asesino"
  return

