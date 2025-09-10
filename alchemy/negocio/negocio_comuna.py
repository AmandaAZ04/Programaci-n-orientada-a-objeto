#Todos los metodos para comuna
from data.conexion import Session
from modelo.comuna import Comuna
from sqlalchemy import func

from prettytable import PrettyTable

sesion = Session()

# Instancia de clase
def crear_comuna():
    mensaje = ''
    nueva_comuna = Comuna()

    # nueva_comuna.id_comuna = 15
    nueva_comuna.cod_comuna = input('Ingrese código de comuna: ')
    nueva_comuna.nombre_comuna = input('Ingrese nombre de comuna: ')

    sesion.add(nueva_comuna)
    try:
        sesion.commit()
        mensaje = 'Su comuna se ha agregado con éxito!'
    except Exception as error:
        sesion.rollback()
        mensaje = f'Error al guardar su comuna: {error}'
    finally:
        sesion.close()
    return mensaje

def listado_comunas():
    listado_comunas = sesion.query(Comuna).order_by('cod_comuna').all()
    table = PrettyTable()
    table.field_names = ["Id", "Código Comuna", "Nombre Comuna"]
    for comuna in listado_comunas:
        table.add_row([comuna.id_comuna, comuna.cod_comuna, comuna.nombre_comuna])
    print(table)

def buscar_comuna(nombre_comuna):
    comuna = input('Ingrese comuna a buscar: ')
    comuna = sesion.query(Comuna).filter_by(nombre_comuna=nombre_comuna).first()
    if comuna:
        return comuna

def actualizar_comuna():
    mensaje = ''
    listado_comunas()
    comuna_busqueda = input('Ingrese nombre comuna: ')
    comuna_editar = Comuna()
    comuna_editar = buscar_comuna(comuna_busqueda)

    if comuna_editar:
        nuevo_codigo_comuna = input('Ingrese código comuna (ENTER para NO modificar): ')
        if nuevo_codigo_comuna != '':
            comuna_editar.cod_comuna = nuevo_codigo_comuna
            nuevo_nombre_comuna = input('Ingrese nombre comuna (ENTER para NO modificar): ')
        if nuevo_nombre_comuna != '':
            comuna_editar.nombre_comuna = nuevo_nombre_comuna
        
        try:
            sesion.commit()
            mensaje = f'{comuna_editar.nombre_comuna} ha sido modificada con éxito'
        except Exception as error:
            sesion.rollback()
            mensaje = f'{comuna_editar.nombre_comuna} no se ha podido actualizar. {error}'
        finally:
            sesion.close()
    return mensaje

    buscar_comuna()
