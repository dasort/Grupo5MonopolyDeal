#tiene toda la config de las cartas - nota: faltan los comodines en carta.py y modiComodinettings

#propiedades 28 cartas  2 marron,2 azul, 3 celestes

from os.path import dirname, join

__cartas_path = join(dirname(dirname(__file__)), 'multimedia\\cartas')
__ui_path = join(dirname(dirname(__file__)), 'multimedia\\ui')

LISTA_PROPIEDADES= [
    {"id": 1, "nombre": "Propiedad Marron", "tipo": "propiedad", "valor": 1, "color": "marron", "path_a_imagen": f'{__cartas_path}\\propiedadMarron.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 2, "nombre": "Propiedad Marron", "tipo": "propiedad", "valor": 1, "color": "marron", "path_a_imagen": f'{__cartas_path}\\propiedadMarron.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 3, "nombre": "Propiedad Celeste", "tipo": "propiedad", "valor": 1, "color": "celeste", "path_a_imagen": f'{__cartas_path}\\propiedadCeleste.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 4, "nombre": "Propiedad Celeste", "tipo": "propiedad", "valor": 1, "color": "celeste", "path_a_imagen": f'{__cartas_path}\\propiedadCeleste.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 5, "nombre": "Propiedad Celeste", "tipo": "propiedad", "valor": 1, "color": "celeste", "path_a_imagen": f'{__cartas_path}\\propiedadCeleste.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 6, "nombre": "Propiedad Rosa", "tipo": "propiedad", "valor": 2, "color": "rosa", "path_a_imagen": f'{__cartas_path}\\propiedadRosa.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 7, "nombre": "Propiedad Rosa", "tipo": "propiedad", "valor": 2, "color": "rosa", "path_a_imagen": f'{__cartas_path}\\propiedadRosa.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 8, "nombre": "Propiedad Rosa", "tipo": "propiedad", "valor": 2, "color": "rosa", "path_a_imagen": f'{__cartas_path}\\propiedadRosa.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 9, "nombre": "Propiedad Naranja", "tipo": "propiedad", "valor": 2, "color": "naranja", "path_a_imagen": f'{__cartas_path}\\propiedadNaranja.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 10, "nombre": "Propiedad Naranja", "tipo": "propiedad", "valor": 2, "color": "naranja", "path_a_imagen": f'{__cartas_path}\\propiedadNaranja.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 11, "nombre": "Propiedad Naranja", "tipo": "propiedad", "valor": 2, "color": "naranja", "path_a_imagen": f'{__cartas_path}\\propiedadNaranja.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 12, "nombre": "Propiedad Rojo", "tipo": "propiedad", "valor": 3, "color": "rojo", "path_a_imagen": f'{__cartas_path}\\propiedadRojo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 13, "nombre": "Propiedad Rojo", "tipo": "propiedad", "valor": 3, "color": "rojo", "path_a_imagen": f'{__cartas_path}\\propiedadRojo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 14, "nombre": "Propiedad Rojo", "tipo": "propiedad", "valor": 3, "color": "rojo", "path_a_imagen": f'{__cartas_path}\\propiedadRojo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 15, "nombre": "Propiedad Amarillo", "tipo": "propiedad", "valor": 3, "color": "amarillo", "path_a_imagen": f'{__cartas_path}\\propiedadAmarillo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 16, "nombre": "Propiedad Amarillo", "tipo": "propiedad", "valor": 3, "color": "amarillo", "path_a_imagen": f'{__cartas_path}\\propiedadAmarillo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 17, "nombre": "Propiedad Amarillo", "tipo": "propiedad", "valor": 3, "color": "amarillo", "path_a_imagen": f'{__cartas_path}\\propiedadAmarillo.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 18, "nombre": "Propiedad Verde", "tipo": "propiedad", "valor": 4, "color": "verde", "path_a_imagen": f'{__cartas_path}\\propiedadVerde.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 19, "nombre": "Propiedad Verde", "tipo": "propiedad", "valor": 4, "color": "verde", "path_a_imagen": f'{__cartas_path}\\propiedadVerde.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 20, "nombre": "Propiedad Verde", "tipo": "propiedad", "valor": 4, "color": "verde", "path_a_imagen": f'{__cartas_path}\\propiedadVerde.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 21, "nombre": "Propiedad Azul", "tipo": "propiedad", "valor": 4, "color": "azul", "path_a_imagen": f'{__cartas_path}\\propiedadAzul.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 22, "nombre": "Propiedad Azul", "tipo": "propiedad", "valor": 4, "color": "azul", "path_a_imagen": f'{__cartas_path}\\propiedadAzul.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 23, "nombre": "Propiedad Servicio", "tipo": "propiedad", "valor": 2, "color": "servicio", "path_a_imagen": f'{__cartas_path}\\propiedadServicio1.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 24, "nombre": "Propiedad Servicio", "tipo": "propiedad", "valor": 2, "color": "servicio", "path_a_imagen": f'{__cartas_path}\\propiedadServicio2.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 25, "nombre": "Propiedad Ferrocarril", "tipo": "propiedad", "valor": 1, "color": "ferrocarril", "path_a_imagen": f'{__cartas_path}\\propiedadFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 26, "nombre": "Propiedad Ferrocarril", "tipo": "propiedad", "valor": 1, "color": "ferrocarril", "path_a_imagen": f'{__cartas_path}\\propiedadFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 27, "nombre": "Propiedad Ferrocarril", "tipo": "propiedad", "valor": 1, "color": "ferrocarril", "path_a_imagen": f'{__cartas_path}\\propiedadFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'},
    {"id": 28, "nombre": "Propiedad Ferrocarril", "tipo": "propiedad", "valor": 1, "color": "ferrocarril", "path_a_imagen": f'{__cartas_path}\\propiedadFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHacePropiedades.png'}
]

LISTA_PROPIEDADES_COMODIN = [
    {"id": 29, "nombre": "Comodin Multicolor", "tipo": "propiedad_comodin", "valor": 0, "color": ["marron", "celeste", "rosa", "naranja", "rojo", "amarillo", "verde", "azul", "sevicio", "ferrocarril"], "path_a_imagen": f'{__cartas_path}\\comodinMulticolor.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 30, "nombre": "Comodin Multicolor", "tipo": "propiedad_comodin", "valor": 0, "color": ["marron", "celeste", "rosa", "naranja", "rojo", "amarillo", "verde", "azul", "sevicio", "ferrocarril"], "path_a_imagen": f'{__cartas_path}\\comodinMulticolor.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 31, "nombre": "Comodin Naranja/Rosa", "tipo": "propiedad_comodin", "valor": 2, "color": ["naranja", "rosa"], "path_a_imagen": f'{__cartas_path}\\comodinNaranjaRosa.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 32, "nombre": "Comodin Naranja/Rosa", "tipo": "propiedad_comodin", "valor": 2, "color": ["naranja", "rosa"], "path_a_imagen": f'{__cartas_path}\\comodinNaranjaRosa.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 33, "nombre": "Comodin Amarillo/Rojo", "tipo": "propiedad_comodin", "valor": 3, "color": ["amarillo", "rojo"], "path_a_imagen": f'{__cartas_path}\\comodinAmarilloRojo.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 34, "nombre": "Comodin Amarillo/Rojo", "tipo": "propiedad_comodin", "valor": 3, "color": ["amarillo", "rojo"], "path_a_imagen": f'{__cartas_path}\\comodinAmarilloRojo.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 35, "nombre": "Comodin Celeste/Marron", "tipo": "propiedad_comodin", "valor": 1, "color": ["celeste", "marron"], "path_a_imagen": f'{__cartas_path}\\comodinCelesteMarron.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 36, "nombre": "Comodin Azul/Verde", "tipo": "propiedad_comodin", "valor": 4, "color": ["azul", "verde"], "path_a_imagen": f'{__cartas_path}\\comodinAzulVerde.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 37, "nombre": "Comodin Celeste/Ferrocarril", "tipo": "propiedad_comodin", "valor": 4, "color": ["celeste", "ferrocarril"], "path_a_imagen": f'{__cartas_path}\\comodinCelesteFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 38, "nombre": "Comodin Servicio/Ferrocarril", "tipo": "propiedad_comodin", "valor": 2, "color": ["servicio", "ferrocarril"], "path_a_imagen": f'{__cartas_path}\\comodinServicioFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'},
    {"id": 39, "nombre": "Comodin Verde/Ferrocarril", "tipo": "propiedad_comodin", "valor": 4, "color": ["verde", "ferrocarril"], "path_a_imagen": f'{__cartas_path}\\comodinVerdeFerrocarril.png', "path_a_queHace": f'{__ui_path}\\queHaceComodin.png'}
]

LISTA_DINERO = [
    {"id": 40, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 41, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 42, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 43, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 44, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 45, "nombre": "Dinero de 1", "tipo": "dinero", "valor": 1, "path_a_imagen": f'{__cartas_path}\\dinero1.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 46, "nombre": "Dinero de 2", "tipo": "dinero", "valor": 2, "path_a_imagen": f'{__cartas_path}\\dinero2.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 47, "nombre": "Dinero de 2", "tipo": "dinero", "valor": 2, "path_a_imagen": f'{__cartas_path}\\dinero2.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 48, "nombre": "Dinero de 2", "tipo": "dinero", "valor": 2, "path_a_imagen": f'{__cartas_path}\\dinero2.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 49, "nombre": "Dinero de 2", "tipo": "dinero", "valor": 2, "path_a_imagen": f'{__cartas_path}\\dinero2.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 50, "nombre": "Dinero de 2", "tipo": "dinero", "valor": 2, "path_a_imagen": f'{__cartas_path}\\dinero2.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 51, "nombre": "Dinero de 3", "tipo": "dinero", "valor": 3, "path_a_imagen": f'{__cartas_path}\\dinero3.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 52, "nombre": "Dinero de 3", "tipo": "dinero", "valor": 3, "path_a_imagen": f'{__cartas_path}\\dinero3.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 53, "nombre": "Dinero de 3", "tipo": "dinero", "valor": 3, "path_a_imagen": f'{__cartas_path}\\dinero3.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 54, "nombre": "Dinero de 4", "tipo": "dinero", "valor": 4, "path_a_imagen": f'{__cartas_path}\\dinero4.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 55, "nombre": "Dinero de 4", "tipo": "dinero", "valor": 4, "path_a_imagen": f'{__cartas_path}\\dinero4.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 56, "nombre": "Dinero de 4", "tipo": "dinero", "valor": 4, "path_a_imagen": f'{__cartas_path}\\dinero4.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 57, "nombre": "Dinero de 5", "tipo": "dinero", "valor": 5, "path_a_imagen": f'{__cartas_path}\\dinero5.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 58, "nombre": "Dinero de 5", "tipo": "dinero", "valor": 5, "path_a_imagen": f'{__cartas_path}\\dinero5.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'},
    {"id": 59, "nombre": "Dinero de 10", "tipo": "dinero", "valor": 10, "path_a_imagen": f'{__cartas_path}\\dinero10.png', "path_a_queHace": f'{__ui_path}\\queHaceDinero.png'}
]

# Datos de las cartas de acción de Monopoly Deal
LISTA_ACCIONES= [
    {"id": 60, "nombre": "Es Mi Cumpleaños", "tipo": "accion", "valor": 5, "path_a_imagen": f'{__cartas_path}\\esMiCumpleanos.png', "path_a_queHace": f'{__ui_path}\\queHaceEsMiCumpleanos.png'},
    {"id": 61, "nombre": "Es Mi Cumpleaños", "tipo": "accion", "valor": 5, "path_a_imagen": f'{__cartas_path}\\esMiCumpleanos.png', "path_a_queHace": f'{__ui_path}\\queHaceEsMiCumpleanos.png'},
    {"id": 62, "nombre": "Es Mi Cumpleaños", "tipo": "accion", "valor": 5, "path_a_imagen": f'{__cartas_path}\\esMiCumpleanos.png', "path_a_queHace": f'{__ui_path}\\queHaceEsMiCumpleanos.png'},
    {"id": 63, "nombre": "Negocio Furtivo", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\negocioFurtivo.png', "path_a_queHace": f'{__ui_path}\\queHaceNegocioFurtivo.png'},
    {"id": 64, "nombre": "Negocio Furtivo", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\negocioFurtivo.png', "path_a_queHace": f'{__ui_path}\\queHaceNegocioFurtivo.png'},
    {"id": 65, "nombre": "Negocio Furtivo", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\negocioFurtivo.png', "path_a_queHace": f'{__ui_path}\\queHaceNegocioFurtivo.png'},
    {"id": 66, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 67, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 68, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 69, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 70, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 71, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 72, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 73, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 74, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 75, "nombre": "Pasa Por La Salida", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\pasaPorLaSalida.png', "path_a_queHace": f'{__ui_path}\\queHacePasaPorLaSalida.png'},
    {"id": 76, "nombre": "Roba Negocios", "tipo": "accion", "valor": 5, "path_a_imagen": f'{__cartas_path}\\robaNegocios.png', "path_a_queHace": f'{__ui_path}\\queHaceRobaNegocios.png'},
    {"id": 77, "nombre": "Roba Negocios", "tipo": "accion", "valor": 5, "path_a_imagen": f'{__cartas_path}\\robaNegocios.png', "path_a_queHace": f'{__ui_path}\\queHaceRobaNegocios.png'},
    {"id": 78, "nombre": "Trato Forzoso", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\tratoForzoso.png', "path_a_queHace": f'{__ui_path}\\queHaceTratoForzoso.png'},
    {"id": 79, "nombre": "Trato Forzoso", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\tratoForzoso.png', "path_a_queHace": f'{__ui_path}\\queHaceTratoForzoso.png'},
    {"id": 80, "nombre": "Trato Forzoso", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\tratoForzoso.png', "path_a_queHace": f'{__ui_path}\\queHaceTratoForzoso.png'},
    {"id": 81, "nombre": "Alquiler Doble", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerDoble.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquilerDoble.png'},
    {"id": 82, "nombre": "Alquiler Doble", "tipo": "accion", "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerDoble.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquilerDoble.png'},
    {"id": 83, "nombre": "Cobrador De Deudas", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\cobradorDeDeudas.png', "path_a_queHace": f'{__ui_path}\\queHaceCobradorDeDeudas.png'},
    {"id": 84, "nombre": "Cobrador De Deudas", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\cobradorDeDeudas.png', "path_a_queHace": f'{__ui_path}\\queHaceCobradorDeDeudas.png'},
    {"id": 85, "nombre": "Cobrador De Deudas", "tipo": "accion", "valor": 3, "path_a_imagen": f'{__cartas_path}\\cobradorDeDeudas.png', "path_a_queHace": f'{__ui_path}\\queHaceCobradorDeDeudas.png'}
]

LISTA_RENTA_DOBLE = [
    {"id": 89, "nombre": "Alquiler Marron/Celeste", "tipo": "accion", "color": ["marron", "celeste"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerMarronCeleste.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 90, "nombre": "Alquiler Marron/Celeste", "tipo": "accion", "color": ["marron", "celeste"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerMarronCeleste.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 91, "nombre": "Alquiler Rojo/Amarillo", "tipo": "accion", "color": ["rojo", "amarillo"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerRojoAmarillo.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 92, "nombre": "Alquiler Rojo/Amarillo", "tipo": "accion", "color": ["rojo", "amarillo"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerRojoAmarillo.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 93, "nombre": "Alquiler Rosa/Naranja", "tipo": "accion", "color": ["rosa", "naranja"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerRosaNaranja.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 94, "nombre": "Alquiler Rosa/Naranja", "tipo": "accion", "color": ["rosa", "naranja"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerRosaNaranja.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 95, "nombre": "Alquiler Verde/Azul", "tipo": "accion", "color": ["verde", "azul"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerVerdeAzul.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 96, "nombre": "Alquiler Verde/Azul", "tipo": "accion", "color": ["verde", "azul"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerVerdeAzul.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 97, "nombre": "Alquiler Ferrocarril/Servicio", "tipo": "accion", "color": ["ferrocarril", "servicio"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerFerrocarrilServicio.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 98, "nombre": "Alquiler Ferrocarril/Servicio", "tipo": "accion", "color": ["ferrocarril", "servicio"], "valor": 1, "path_a_imagen": f'{__cartas_path}\\alquilerFerrocarrilServicio.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'}
]

LISTA_RENTA_MULTICOLOR = [
    {"id": 86, "nombre": "Alquiler Multicolor", "tipo": "accion", "color": ["ferrocarril", "servicio", "verde", "azul", "rosa", "naranja", "rojo", "amarillo", "marron", "celeste"], "valor": 3, "path_a_imagen": f'{__cartas_path}\\alquilerMulticolor.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 87, "nombre": "Alquiler Multicolor", "tipo": "accion", "color": ["ferrocarril", "servicio", "verde", "azul", "rosa", "naranja", "rojo", "amarillo", "marron", "celeste"], "valor": 3, "path_a_imagen": f'{__cartas_path}\\alquilerMulticolor.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'},
    {"id": 88, "nombre": "Alquiler Multicolor", "tipo": "accion", "color": ["ferrocarril", "servicio", "verde", "azul", "rosa", "naranja", "rojo", "amarillo", "marron", "celeste"], "valor": 3, "path_a_imagen": f'{__cartas_path}\\alquilerMulticolor.png', "path_a_queHace": f'{__ui_path}\\queHaceAlquiler.png'}
]