import os
import inicio

usuario = os.path.expanduser("~")
videos = os.path.join(usuario, "Videos")
downloadtube = os.path.join(videos, "DownloadTube")

def inicializador(a=None):
    os.makedirs(downloadtube, exist_ok=True)
    inicio.comecar.comeca(downloadtube)
