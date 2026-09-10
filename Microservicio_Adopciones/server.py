from spyne import Application  
from spyne.protocol.soap import Soap11  
from spyne.server.wsgi import WsgiApplication  

from service import AdoptionService  # Importa las funciones del servicio de adopciones


# Configuración principal del servicio SOAP
application = Application(
    [AdoptionService],
    tns="huellitas.adopciones",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)


wsgi_application = WsgiApplication(application)  # Prepara la aplicación para el servidor


if __name__ == "__main__":

    from wsgiref.simple_server import make_server  # Crea un servidor web sencillo

    host = "0.0.0.0"
    port = 8001

    # Muestra información del servicio al iniciarlo
    print("--------------------------------------------")
    print("MICROSERVICIO DE ADOPCIONES")
    print("--------------------------------------------")
    print(f"Servidor iniciado en http://localhost:{port}")
    print(f"WSDL: http://localhost:{port}/?wsdl")
    print("--------------------------------------------")

    # Inicia el servidor en el puerto configurado
    server = make_server(
        host,
        port,
        wsgi_application
    )

    server.serve_forever()  
