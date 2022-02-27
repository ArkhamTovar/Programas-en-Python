# Se importa el modulo para creacion de tupla nominada
from collections import namedtuple
# Importacion de modulo fecha para validaciones
import datetime
#Creacion de tupla nominada para registros
Registros= namedtuple('Registro', 'folio fecha nombre_cliente descripcion_del_servicio descripcion_del_equipo montoCobrado')
#Diccionario donde se almacenaran los registros
registros={}
#funcion para creacion de registros
def RegistrarUnServicio():
    # Se crean listas para multiples servicios,equipos y sus respectivos montos sin iva
    listaServicios=[]
    listaDeEquipos=[]
    montosCobrados=[]
    
    global registros
    print('REGISTRAR SERVICIO')
    folio=int(input("Ingrese su folio: "))
    nombre_cliente=input('Nombre del cliente: ')
    #Ciclo para permitir solo formato de fecha valido
    while True:
        try:
            fecha_str = input("Fecha de la venta en formato (dd/mm/aaaa): ")
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            print("El valor de la fecha que fue proporcionado no puede ser procesado")
            continue
        except Exception:
            print("Se ha presentado una excepción")
            break
        else:
            # al validarse la fecha se pasa a otro ciclo el cual servira para añadir diferentes servicios, equipos
            # y sus montos que el cliente haya realizado
            while True:
                servicio=input('Servicio realizado: ')
                #Se agreagan valores a la lista de servicios realizados al cliente
                listaServicios.append(servicio)
                descripcion_del_equipo=input('Descripcion del equipo: ')
                listaDeEquipos.append(descripcion_del_equipo)
                #ciclo para validar solo valores numericos
                while True:
                    try:
                        montoCobrado=float(input('Monto cobrado: '))
                        montosCobrados.append(montoCobrado)
                        break
                    except:
                        print('El monto debe ser numerico')
                        continue
                #Opcion para agregar mas servicios,equipos y montos
                print('[n] no  [presionar ENTER] si')
                opcion=input('Desea agreagar otro servicio?: ')
                if opcion=='n':
                    break
                
        # Se agregan valores a la tupla nominada junto a otras listas
        registro=Registros(folio,fecha,nombre_cliente,listaServicios,listaDeEquipos,montosCobrados)

        registros[folio]=registro
        montoMasIva=sum(montosCobrados)*.16
        montosCobrados=sum(montosCobrados)+montoMasIva
        print()
        print(f'El cliente {nombre_cliente} debe pagar un monto total con IVA incluido ${montosCobrados}')
        print()
        break
    
    
    
    #funcion Utilizada para mostrar todos lso registros de servicios que hay actualmente
def DesplegarTodosLosDatos():
    print('\nFolio\tFecha\tCliente\tServicios\tEquipos\tMontos cobrado')
    print('-'*50)
    for elemento in registros.items():
        print(f'{elemento[0]}\t{elemento[1][1]}\t{elemento[1][2]}\t{elemento[1][3]}\t{elemento[1][4]}\t{elemento[1][5]}')
        print('-'*50)
        print()

#Funcion para consultar servicios realizados mediante folios de cliente
def BuscarFolio():
    global registros
    while True:
        try:
            folio_buscar = (int(input("Ingrese el numero de folio a buscar: ")))
            if folio_buscar not in registros.keys():
                break
            else:
                # Aqui se utiliza el diccionario para buscar por medio de una llave el folio (utilizacion de diccionario)
                for elemento in registros.items():
                    if elemento[0] == folio_buscar:
                        print('\nFolio\tFecha\tCliente\tServicios\tEquipos\tMontos cobrado')
                        print(f'{elemento[0]}\t{elemento[1][1]}\t{elemento[1][2]}\t{elemento[1][3]}\t{elemento[1][4]}\t{elemento[1][5]}')
                break
        except:
            print('debe ser un valor numerico')
            print()
            break

#Funcion para consultar servicios realizados mediante fechas
def ConsultarPorFechas():
    global registros
    while True:
        try:
            buscarFecha= input("Fecha de la venta en formato (dd/mm/aaaa): ")
            fecha = datetime.datetime.strptime(buscarFecha, "%d/%m/%Y").date()
        except ValueError:
            print("El valor de la fecha que fue proporcionado no puede ser procesado")
            continue
        except Exception:
            print("Se ha presentado una excepción")
            break
        else:
            for elemento in registros.items():
                    if elemento[1][1] == fecha:
                        print('\nFolio\tFecha\tCliente\tServicios\tEquipos\tMontos cobrado')
                        print(f'{elemento[0]}\t{elemento[1][1]}\t{elemento[1][2]}\t{elemento[1][3]}\t{elemento[1][4]}\t{elemento[1][5]}')
                        break

# Funcion para crear un menu principal por el cual se entrara a las demas funciones
def Menu():
    while True:
        print('*****SERVICIO DE SOPORTE TECNICO******')
        print('[1] Regitrar Servicio ')
        print('[2] Mostrar todos los servicios ')
        print('[3] Buscar servicio por folio ')
        print("[4] Salir")
        print('[5] Consultar por fecha')
        opcion=input('Seleccione una opcion: ')
        if opcion=='1':
            RegistrarUnServicio()
        if opcion=='2':
            DesplegarTodosLosDatos()
        if opcion=="3":
            BuscarFolio()
        if opcion=="4":
            break
        if opcion=='5':
            ConsultarPorFechas()
# Funcion activa para entrar directamente al menu al empezar a ejecutar el programa
Menu()