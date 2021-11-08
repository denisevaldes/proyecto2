
import json
import csv

def cargar_archivo(archivo1,archivo2):# funcion carga de los archivo csv
    
    try:# control de excepcion
        recarga1 = open (archivo1,'r')# abrir archivo X
        data1 = csv.reader(recarga1,delimiter =',')# indetificar la separacion csv ya que es un archivo separado por comas
        next(data1,None)#salta el titulo
        recarga2 = open (archivo2,'r')
        data2 = csv.reader(recarga2,delimiter =',')# identificar la separacion por comas 
        next(data2,None)#salta el titulo
        return data1,data2
    except FileNotFoundError:# si no encuentra el archivo ingresa aqui 
        print("el archivo no fue encontrado")

def reordenamiento_excel1(data1):# funcion para procesar el primer csv ya que las columnas a procesar estan en un orden distinto

    
    diccionario = {}
    paises = {}
    fecha = {}
    
    
    

    for aux in data1:# for que procesa archivo 1
        if not aux[4]:# cambio de str a float ya que habian espacios vacios "" en el archivo
            aux[4] = 0.0
        if not aux[5]:# cambio de str a float ya que habian espacios vacios "" en el archivo
            aux[5] = 0.0
        if not aux[7]: # cambio de str a float ya que habian espacios vacios "" en el archivo
            aux[7]= 0.0
        if aux[0] not in paises:
            paises[aux[0]] = []# crea una lista para agregar elementos por medio del append
        if aux[2] not in fecha:
            paises[aux[0]].append({"fecha": aux[2], "tipo vacuna" : aux[12], "vacunados a la fecha" : float(aux[4]),"personas completamente vacunadas" : float(aux[5]),"personas vacunadas hoy" : float(aux[7])})
       
        
    diccionario = {"PAISES": paises}

        
    return diccionario

def reordenamiento_excel2(data2,diccionario):# funcion que procesa el csv 2 y agrega al diccionario 

    
    diccionario = {}
    paises = {}
    fecha = {}

    for aux in data2:# for que procesa el archico csv 2 
        if not aux[3]:# cambio de variable string a float si  encuentra un espacio vacio
            aux[3] = 0.0
        if aux[0] not in paises:#
            paises[aux[0]] = []#crea una lista para añadir informacion por medio del append
        if aux[1] not in fecha:
            paises[aux[0]].append({"fecha": aux[1], "tipo vacuna" : aux[2], "vacunados a la fecha" : float(aux[3])})
   
    diccionario = {"paises": paises}        
        

    return diccionario



def main():
    archivo1 = "country_vaccinations.csv"#abrir archivo 
    archivo2 = "country_vaccinations_by_manufacturer.csv"#abrir archivo2
    data1,data2 = cargar_archivo(archivo1,archivo2)#funcion carga  y retorna 2 variables
    diccionario1 = reordenamiento_excel1(data1)# diccionario tratamiento 1
    diccionario2 = reordenamiento_excel2(data2,diccionario1)#tratamiento diccionario 2 
    with open ("diccionario.json", "w") as file:# crear archivo json 
        ejemplo1 = json.dump((diccionario1,diccionario2),file,indent=4)#agrego al json diccionario 1     
        file.write(ejemplo1)#escribo el archivo 1 
        file.close()#se cierra el archivo 




if __name__ == "__main__":
    main()
