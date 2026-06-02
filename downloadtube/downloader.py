from pytubefix import YouTube
from pytubefix.cli import on_progress
from time import sleep as EsperaAiUmPouco
import menumain
from colorama import Fore
import DTinicializador
import DTUX

class download:
    def download():
        try:
            urlvideo =  input(Fore.WHITE + "insira uma URL do YT:")
            yt = YouTube(urlvideo, on_progress_callback=on_progress)
            ytt = yt.title
            yd = yt.streams.get_highest_resolution()
            print (f"{ytt}")
            yd.download(output_path=DTinicializador.downloadtube)
        except Exception as err:
            print(Fore.RED + str(err))
            menumain.menu.MenuMain()    
        EsperaAiUmPouco(5)
        DTUX.clear()
        menumain.menu.MenuMain()
        