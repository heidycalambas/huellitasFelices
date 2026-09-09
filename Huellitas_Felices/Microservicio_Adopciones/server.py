from wsgiref.simple_server import make_server

from spyne.server.wsgi import WsgiApplication

from service import application

from config import Config


def main():

    wsgi_app = WsgiApplication(application)

    server = make_server(
        Config.SERVER_HOST,
        Config.SERVER_PORT,
        wsgi_app
    )

    print("-----------------------------------------")
    print("   HUELLITAS_FELICES - MICROSERVICIO")
    print("              ADOPCIONES")
    print("-----------------------------------------")

    print(
        f"Servidor: http://{Config.SERVER_HOST}:{Config.SERVER_PORT}"
    )

    print(
        f"WSDL: http://{Config.SERVER_HOST}:{Config.SERVER_PORT}/?wsdl"
    )

    server.serve_forever()


if __name__ == "__main__":
    main()