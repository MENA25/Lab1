from random import randint
import sys

categoriaDeportes = [
    
     {
        "pregunta": "¿En qué año ganó Colombia la Copa América?",
        "opciones": "a. 2005 b. 2000 c. 2001 d. 2002",
        "rCorrecta": "a"  
    },
    {
        "pregunta": "¿Qué selección ganó el Mundial de Sudáfrica?",
        "opciones": "a. España b. Alemania c. Países Bajos d. Uruguay",
        "rCorrecta": "a"  
    },
    {
        "pregunta": "¿En qué año Óscar Figueroa obtuvo medalla de oro en unos Juegos Olímpicos?",
        "opciones": "a. 2012 b. 2015 c. 2016 d. 2020",
        "rCorrecta": "c"
    },
    {
        "pregunta": "¿Quién tiene el récord olímpico de 100 metros en atletismo?",
        "opciones": "a. Asafa Powell b. Yohan Blake c. Tyson Gay d. Usain Bolt",
        "rCorrecta": "d"
    },
    {
        "pregunta": "¿Qué deporte no hace parte de los Juegos Olímpicos?",
        "opciones": "a. Balonmano b. Atletismo c. Patinaje d. Tiro con arco",
        "rCorrecta": "c"
    },
    {
        "pregunta": "¿Quién fue la primera mujer en ganar una medalla olímpica?",
        "opciones": "a. Trudy Ederle b. Charlotte Cooper c. Alice Milliat d. Megan Rapinoe",
        "rCorrecta": "b"
    },
    {
        "pregunta": "¿Cuál es el deporte más popular en India?",
        "opciones": "a. Criquet b. Badminton c. Fútbol d. Mallakhamb",
        "rCorrecta": "a"
    },
    {
        "pregunta": "¿Cuál es el deporte más difícil del mundo?",
        "opciones": "a. Lucha libre b. Gimnasia c. Fútbol americano d. Boxeo",
        "rCorrecta": "d"
    },
    {
        "pregunta": "¿Cuántos colombianos asistieron a los Juegos Olímpicos?",
        "opciones": "a. 87 b. 85 c. 90 d. 93",
        "rCorrecta": "a"  
    },
    {
        "pregunta": "¿Cada cuántos años se celebra el Mundial de fútbol?",
        "opciones": "a. 5 b. 3 c. 4 d. 2",
        "rCorrecta": "c"
    }
]

categoriaCiencia = [
   
    {
        "pregunta":"¿En el MRU que magnitud varia constantemente?",
        "opciones":"A. Velocidad B. Aceleracion C. Pocicion D. Distancia",
        "rCorrecta":"c"
    },
    {
        "pregunta":"Qué órgano del cuerpo humano afecta el licor",
        "opciones":"a. Próstata B. Hígado C. Riñones D. Colón",
        "rCorrecta":"b"
    },
    {
        "pregunta":"Cual es la fórmula correcta para hallar energía cinética",
        "opciones":"A. Ec=(1/2)m^2*V B. Ec=(1/2)m*V^2 C. Ec=(1/2)*V^2 D. Ec=(1/2)m*V ",
        "rCorrecta":"b"
    },
    {
        "pregunta":"Cual es la derivada correcta de la función Ln(Sec(x))",
        "opciones":"A. 1/secx B. cscx*secx C. secx/tanx D. tanx",
        "rCorrecta":"d"
    },
    {
        "pregunta":"Cual de las siguientes afirmaciones es correcta",
        "opciones":"a. La primera derivada de la distancia es la aceleración b. La derivada de la aceleración es la posición c. La integral de la velocidad es distancia d. la integral de la aceleración es distancia",
        "rCorrecta":"c"
    },
    {
        "pregunta":"¿Cuantos huesos tiene el cuerpo humano?",
        "opciones":"a. 206 b. 305 c. 20 d. 300",
        "rCorrecta":"a"
    },
    {
        "pregunta":"¿Cual es el órgano que se encarga de producir insulina?",
        "opciones":"a. estómago b. riñones c. hígado d. páncreas",
        "rCorrecta":"d"
    },
    {
        "pregunta":"¿Quien fue el encargado de desarrollar la teoría del big bang?",
        "opciones":"a. Stephen Hawking b. Charles Darwin c. Georges Lemaître d. Albert einstein",
        "rCorrecta":"c"
    },
    {
        "pregunta":"¿Cual de los siguientes físicos descubrió la gravedad?",
        "opciones":"a. Albert einstein b. Isaac newton c. Stephen Hawking d. Charles Darwin",
        "rCorrecta":"b"
    },
    {
        "pregunta":"¿Quien fue la primera mujer en recibir un premio nobel?",
        "opciones":"a. lise meitner b. Marie Curie c. caroline herschel d. rosalind franklin",
        "rCorrecta":"b"
    }
    
]

def puntuacion(n):
    puntuacion = (n*100)/10
    print(f"Tu puntuacion es: {puntuacion}")

def eleccionCategoria(categoria):
     while True:
            
            numeroAl = randint(0,n)
            print(categoria[numeroAl]["pregunta"])
            print(categoria[numeroAl]["opciones"])
            eleccionC = input().lower()
            if eleccionC == (categoria[numeroAl]["rCorrecta"]):
                print("Correcto")
                nRespuestasCorrectas += 1
            else :
                print("Incorrecto")
                print(f"La respuesta correcta es: {categoria[numeroAl]["rCorrecta"]}")
                nRespuestasMalas += 1
            categoria.pop(numeroAl)
            if nRespuestasMalas == 3:
                puntuacion(nRespuestasCorrectas)
                print("Numero maximo de errores alcanzado \n¡Fin del juego!")
                sys.exit(0)
            if len(categoria) == 0:
                puntuacion(nRespuestasCorrectas)
                print("Haz contestado todas las preguntas de la categoria")
                break
            n-=1
    
    
print("\n          ################################################################################## \n")
print("                               Bienvenido al juego de preguntados                              \n")
usuario = str(input("Ingresa tu nombre: "))

while True:
    nRespuestasMalas = 0
    n = 9
    nRespuestasCorrectas = 0
    print(f"Hola {usuario} que categoria quieres jugar: \n1.Deportes \n2.Ciencia \n3.Salir")
    eleccion = int(input())

    
    if eleccion == 1: ##categoria Deportes
            
        while True:
            
            numeroAl = randint(0,n)
            print(categoriaDeportes[numeroAl]["pregunta"])
            print(categoriaDeportes[numeroAl]["opciones"])
            eleccionC = input().lower()
            if eleccionC == (categoriaDeportes[numeroAl]["rCorrecta"]):
                print("Correcto")
                nRespuestasCorrectas += 1
            else :
                print("Incorrecto")
                print(f"La respuesta correcta es: {categoriaDeportes[numeroAl]["rCorrecta"]}")
                nRespuestasMalas += 1
            categoriaDeportes.pop(numeroAl)
            if nRespuestasMalas == 3:
                puntuacion(nRespuestasCorrectas)
                print("Numero maximo de errores alcanzado \n¡Fin del juego!")
                sys.exit(0)
            if len(categoriaDeportes) == 0:
                puntuacion(nRespuestasCorrectas)
                print("Haz contestado todas las preguntas de la categoria")
                break
            n-=1
            
        
    elif eleccion == 2: ## Categoria Ciencia
            ##print("\n")
        while True:
            
            numeroAl = randint(0,n)
            print(categoriaCiencia[numeroAl]["pregunta"])
            print(categoriaCiencia[numeroAl]["opciones"])
            eleccionC = input().lower()
            if eleccionC == (categoriaCiencia[numeroAl]["rCorrecta"]):
                print("Correcto")
                nRespuestasCorrectas += 1
            else :
                print("Incorrecto")
                print(f"La respuesta correcta es: {categoriaCiencia[numeroAl]["rCorrecta"]}")
                nRespuestasMalas += 1
            categoriaCiencia.pop(numeroAl)
            if nRespuestasMalas == 3:
                puntuacion(nRespuestasCorrectas)
                print("Numero maximo de errores alcanzado \n¡Fin del juego!")
                sys.exit(0)
            if len(categoriaCiencia) == 0:
                puntuacion(nRespuestasCorrectas)
                print("Haz contestado todas las preguntas de la categoria")
                break
            n-=1
            
    elif eleccion == 3:
        print("¡Vuelve pronto!")
        sys.exit(0)
    
    else:
        print("Opcion invalida, selecciona una opcion correcta")
        
    
                
            
        