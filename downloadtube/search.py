from pytubefix import Search
import time
import downloader
import menumain
from colorama import Fore

class sarch: 
    def pesquisa():
        filme = input(Fore.WHITE + "insira o titulo do video:")
        print(Fore.BLUE + "[!] copie a url do video desejado e cole-o na proxima entrada de texto.\napos a pesquisa você terá 2 minutos para achar o video.")
        results = Search(filme)
        for video in results.videos:
            try:

                print(Fore.WHITE + f'Titulo: {video.title}')
                print(Fore.YELLOW + f'[#] criador(a): {video.author}')            
                print(Fore.YELLOW + f'[$] URL: {video.watch_url}')
                print(Fore.YELLOW + f'Duração: {video.length} s')
                print(Fore.WHITE + '---')

            except Exception as err:
                print(Fore.RED + str(err))
                menumain.menu.MenuMain()

        time.sleep(120)
        downloader.download.download()

