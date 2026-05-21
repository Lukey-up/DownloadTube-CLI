from pytubefix import Search
import timer
import downloader
import menumain
from colorama import Fore

class sarch: 
    def pesquisa(a=None):
        filme = input(Fore.WHITE + "insira o titulo do video:")
        print(Fore.LIGHTBLUE_EX + "[!] copie a url do video desejado e cole-o na proxima entrada de texto.\napos a pesquisa você terá 2 minutos para achar o video.")
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
                print(Fore.RED + "[!] BOTDETECTADO: nosso bot foi detectado tente um novo prompt ou abra o navegador e va atras da url.")
                menumain.menu.MenuMain()

        timer.coutdown.go(5)
        downloader.download.download()

