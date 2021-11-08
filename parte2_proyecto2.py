import json

# funcion carga el archivo json
def carga_archivo(archivo=None):# esta funcion  carga el archivo 
    try:# control de excepciones 
        with open(archivo) as archivo1:#abre el archivo json 
            datos = json.load(archivo1)
            return datos
    except FileNotFoundError:# control de excepciones 
        print("El archivo no fue encontrado")
        quit()


# funcion creada para buscar los paises dentro del archivo json y mostrar de forma ordenada
# su interior
def buscar_paises(pais, diccionario):

    try:# control de excepciones 
        for key, values in diccionario[0].items():# recorre el diccionario en la posicion "PAISES"0
            for i in values.get(pais):#ingresa al diccionario uno y luego a la diccionario pais
                print("fecha: ", i.get("fecha"))# imprime la fecha
                print("tipo de vacuna: ", i.get("tipo vacuna"))# imprime tipo de vacuna 
                print("vacunados a la fecha", i.get("vacunados a la fecha"))# imprime vacunados a la fecha
                print(
                    "personas completamente vacunadas",
                    i.get("personas completamente vacunadas"),
                )#imprime lo señado entre comillas ""
                print("personas vacunadas hoy", i.get("personas vacunadas hoy"))#vacunados hoy
                print("\n\n")# 2 salto de lineas 
    except TypeError:# control de excepciones 
        print("se a ingresado mal un dato")
        

    try:# control de excepciones 
        for key, values in diccionario[1].items():# recorre el el diccionario en la posicion "paises"1
            for i in values.get(pais):
                print("fecha: ", i.get("fecha"))# imprime la fecha
                print("tipo de vacuna: ", i.get("tipo vacuna"))# imprime tipo de vacuna
                print("vacunados a la fecha", i.get("vacunados a la fecha"))# imprime vacunado a la fecha
                print("\n\n")
    except TypeError:# control de excepciones 
        print("se a ingresado mal un dato")
        


def buscar_fecha(fecha, diccionario, pais):

    try:# control de excepciones 
        for key, values in diccionario[0].items():# recorre el diccionario en la posicion "PAISES"0
            for i in values.get(pais):
                # print(i.get("fecha"))
                if i.get("fecha") == fecha:
                    print(pais)
                    print("fecha: ", i.get("fecha"))# imprime la fecha
                    print("tipo de vacuna: ", i.get("tipo vacuna"))# imprime tipo de vacuna
                    print("vacunados a la fecha", i.get("vacunados a la fecha"))# imprime vacunados a la fecha
                    print(
                        "personas completamente vacunadas",
                        i.get("personas completamente vacunadas"),
                    print("personas vacunadas hoy", i.get("personas vacunadas hoy"))#vacunados hoy
                    )#imprime lo señado entre comillas "
                    print("\n\n")
                else:
                    pass
    except TypeError:# control de excepciones 
        print("se a ingresado mal un dato")

    try: # control de excepciones 
        for key, values in diccionario[1].items():# recorre el el diccionario en la posicion "paises"1
            for i in values.get(pais):#revisa dentro  del diccionario ingresando en paises del csv2 para su revicion correspondiente 
                if i.get("fecha") == fecha:#luego de haber encontrado el pais reviza la fecha 
                    print("tipo de vacuna: ", i.get("tipo vacuna"))#imprime tipo de vacuna
                    print("vacunados a la fecha", i.get("vacunados a la fecha"))#imprime vacunados a la fecha
                    print("\n\n")
                else:# si no entra al if imprime no hay registro
                    #print("no hay registros de esa fecha")
                    pass
    except TypeError:# control de excepciones 
        print("se a ingresado mal un dato")


def variable_pais():

    while True:
        try:# control de excepciones 
            #usuario debe elegir una de las opciones presentadas 
            print("\n por favor elija una opcion: ")
            print("< 1 > el nombre del pais contiene 1 palabra")
            print("< 2 > el nombre del pais contiene 2 o mas palabras")
            # usuario ingresa opcion 
            respuesta = int(input("ingrese la opcion escogida: "))
            if respuesta == 1:
                paises = str(input("ingrese un pais: ")) #se pide nombre de pais
                pais = paises.capitalize() #se usa capitalize para que primera letra sea mayuscula 
                False # false termina ciclo while
                return pais
            #nombre de pais esta compuesto por 2 o mas palabras    
            elif respuesta == 2:
                #se pregunta el numero de palabras que componen el nombre de pais 
                palabras = int(input("cuantas palabras contiene el nombre del pais?"))
                lista1 = [] # se cre una lista 
                #se crea un for en donde se añadiran los componentes del nombre 
                # de país a la lista creada anteriormente
                for i in range(0, palabras):
                    palabra = input("palabra:")
                    lista1.append(palabra.capitalize())
                pais = "".join(lista1) # se unen los componentes de la lista en una variable
                print(pais)
                False # false termina ciclo while
                return pais
            #usuario ingreso un numero invalido
            else:
                print("la respuesta es invalidad, ingrese una nueva opcion")
        #en el caso de que usuario escriba una palabra, se le mostrara el 
        # siguiente mensaje        
        except ValueError:# control de excepciones 
            print("la respuesta es invalidad, ingrese una nueva opcion")

#se ingresa la fecha
def ingresa_fecha():
        #se pregunta la fecha por separado 
        año = str(input("ingrese el año: "))
        año1 = año.strip()
        mes = str(input("ingrese el mes: "))
        mes1 = mes.strip()
        dia = str(input("ingrese el dia: "))
        dia1 = dia.strip()
        print("\n")
        # se unen las variables ingresadas
        fecha = (año1 + "-" + mes1 + "-" + dia1)
        return fecha 

#funcion encargada de 
def menu(archivo):

    eleccion = None
    terminar = 0
    #se crea un while, el cual funcionara hasta que usuario decida terminar programa
    while terminar != 1:
        try: # control de excepciones 
            #se presentan opciones a usuario
            print(" HOLA! A CONTINUACIÓN DEBE ELEGIR UNA DE LAS OPCIONES DADAS")
            print(" < 1 > ingresar nombre del país.")
            print(" < 2 > ingresar nombre del país y la fecha.")
            print(" < 3 > comparar dos paises ")
            print(" < 4 > terminar programa.")

            #usuario debe ingresar opcion 
            eleccion = int(input("ingrese el numero de su eleccion: "))

            #dependiendo de opcion escogida se entrara en un if 
            if eleccion == 1:
                pais = variable_pais() #se pregunta por el pais que se quiera visualizar
                buscar_paises(pais, archivo) #se busca y muestra el pais ingresado
            elif eleccion == 2:
                pais = variable_pais() #se pregunta por el nombre del pais
                fecha = ingresa_fecha() #se pregunta por la fecha deseada 
                buscar_fecha(fecha, archivo, pais) #se busca y muestra en pantalla 
            elif eleccion == 3:
                print("\nprimer pais\n")
                pais = variable_pais()
                print("\nsegundo pais\n")
                pais1 = variable_pais()
                fecha = ingresa_fecha()
                buscar_fecha(fecha, archivo, pais)
                buscar_fecha(fecha, archivo, pais1)
            elif eleccion == 4:
                terminar = 1 # terminar se iguala a 1 para terminar programa
            else:
                print("opcion no valida")
        except ValueError:# control de excepciones 
            print("\n")
            print("usted a ingresado una opcion no validad")
            print("recuerde que se debe ingresar un numero ")
            print("\n")

def main():

    archivojson = "diccionario.json" #se asigna archivo json a una variable 
    archivo = carga_archivo(archivojson) # se carga archivo
    menu(archivo) #se ingresa al menu


if __name__ == "__main__":
    main()
