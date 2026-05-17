from pytubefix import YouTube
from pytubefix.cli import on_progress
from time import sleep as EsperaAiUmPouco
import menumain
from colorama import Fore


class download:
    def download():
        try:
            urlvideo =  input(Fore.WHITE + "insira uma URL do YT:")
            yt = YouTube(Fore.GREEN + urlvideo, on_progress_callback=on_progress)
            ytt = yt.title
            yd = yt.streams.get_highest_resolution()
            print (f"{ytt}")
            yd.download(output_path="C:/Users/usuario/Videos/downloadtube")
        except Exception as err:
            print(Fore.RED + err)
            menumain.menu.MenuMain()    
        EsperaAiUmPouco(60)
        menumain.menu.MenuMain()
        