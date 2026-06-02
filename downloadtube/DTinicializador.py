import os
import inicio

usuario = os.path.expanduser("~")
videos = os.path.join(usuario, "Videos")
downloadtube = os.path.join(videos, "DownloadTube")

def inicializador():
    os.makedirs(downloadtube, exist_ok=True)
    inicio.comecar.comeca(downloadtube)
