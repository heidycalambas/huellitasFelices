from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from service import AdoptionService


application = Application(
    [AdoptionService],
    tns="huellitas.adopciones",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)


wsgi_application = WsgiApplication(application)


if __name__ == "__main__":

    from wsgiref.simple_server import make_server

    host = "0.0.0.0"
    port = 8001

    print("--------------------------------------------")
    print("MICROSERVICIO DE ADOPCIONES")
    print("--------------------------------------------")
    print(f"Servidor iniciado en http://localhost:{port}")
    print(f"WSDL: http://localhost:{port}/?wsdl")
    print("--------------------------------------------")

    server = make_server(
        host,
        port,
        wsgi_application
    )

    server.serve_forever()