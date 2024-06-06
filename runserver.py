from waitress import serve
from ERPCloudsoftware.wsgi import application

if __name__ == "__main__":
    serve(application, host='192.168.0.138', port=8000)