from spyne import Application  
from spyne.protocol.soap import Soap11  
from spyne.server.wsgi import WsgiApplication  

from service import PetService  # Importa el servicio de mascotas


# Crea la aplicación principal del microservicio
application = Application(
    [PetService],
    tns="huellitas.mascotas",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)


wsgi_application = WsgiApplication(application)  # Prepara el servicio para ejecutarlo


if __name__ == "__main__":

    from wsgiref.simple_server import make_server  # Permite levantar el servidor

    host = "0.0.0.0"
    port = 8000

  
    print("--------------------------------------------")
    print("MICROSERVICIO DE MASCOTAS")
    print("--------------------------------------------")
    print(f"Servidor iniciado en http://localhost:{port}")
    print(f"WSDL: http://localhost:{port}/?wsdl")
    print("--------------------------------------------")

    # Crea el servidor usando el puerto indicado
    server = make_server(
        host,
        port,
        wsgi_application
    )

    server.serve_forever()  
