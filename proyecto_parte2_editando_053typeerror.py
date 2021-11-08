import json


def carga_archivo(archivo=None):
    try:
        with open(archivo) as archivo1:
            datos = json.load(archivo1)
            return datos
    except FileNotFoundError:
        print("El archivo no fue encontrado")
        quit()


def buscar_paises(pais, diccionario):

    try:
        for key, values in diccionario[0].items():
            for i in values.get(pais):
                print("fecha: ", i.get("fecha"))
                print("tipo de vacuna: ", i.get("tipo vacuna"))
                print("vacunados a la fecha", i.get("vacunados a la fecha"))
                print("personas completamente vacunadas",i.get("personas completamente vacunadas"))
                print("\n\n")
        # print(values.get(pais))
    except TypeError:
        pass

    try:
        for key, values in diccionario[1].items():
            for i in values.get(pais):
                print("fecha: ", i.get("fecha"))
                print("tipo de vacuna: ", i.get("tipo vacuna"))
                print("vacunados a la fecha", i.get("vacunados a la fecha"))
                print("\n\n")
    except  TypeError:
        print("no esta la wea, hubo un error")            


def buscar_fecha(fecha, diccionario, pais):

    try:
        for key, values in diccionario[0].items():
            for i in values.get(pais):
                # print(i.get("fecha"))
                if i.get("fecha") == fecha:
                    print("fecha: ", i.get("fecha"))
                    print("tipo de vacuna: ", i.get("tipo vacuna"))
                    print("vacunados a la fecha", i.get("vacunados a la fecha"))
                    print("personas completamente vacunadas",i.get("personas completamente vacunadas"))
                    print("\n\n")
                else:
                    pass
    except  TypeError:
        print("no esta la wea, hubo un error")
        # print(values.get(pais))
    print("\n")
    try:
        for key, values in diccionario[1].items():
            for i in values.get(pais):
                if i.get("fecha") == fecha:
                    print("tipo de vacuna: ", i.get("tipo vacuna"))
                    print("vacunados a la fecha", i.get("vacunados a la fecha"))
                    print("\n\n")
                else:

                    pass
    except  TypeError:
        print("no esta la wea, hubo un error") 


def imprimir_todo_diccionario(diccionario):
    for key, values in diccionario[0].items():
        print(key, ":\n")
        for paises in values:
            print(paises)

    print("\n")
    for key, values in diccionario[1].items():
        print(key, ":\n")
        for paises in values:
            print(paises)

def variable_pais():

    paises = str(input("ingrese un pais: "))
    pais = paises.capitalize()
    return pais


def menu(archivo):

    eleccion = None

    print(" HOLA! A CONTINUACIÓN DEBE ELEGIR UNA DE LAS OPCIONES DADAS")
    print(" < 1 > muestra todos los datos de un país, ingresando el país")
    print(" < 2 > muestra todos los datos de un país ingresando el país y la fecha")

    eleccion = int(input("ingrese el numero de su eleccion: "))

    if eleccion == 1:
        pais = variable_pais()
        buscar_paises(pais, archivo)
    elif eleccion == 2:
        pais = variable_pais()
        print("FECHA: ")
        año = str(input("ingrese el año: "))
        año1 = año.strip()
        mes = str(input("ingrese el mes: "))
        mes1 = mes.strip()
        dia = str(input("ingrese el dia: "))
        dia1 = dia.strip()
        fecha = (año1 + "-" + mes1 + "-" + dia1)
        buscar_fecha(fecha, archivo, pais)
    else:
        print("opcion no valida")


def main():

    hola = "diccionario.json"
    archivo = carga_archivo(hola)
    menu(archivo)


if __name__ == "__main__":
    main()