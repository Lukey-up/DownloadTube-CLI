import os
from colorama import Fore
import menumain
import DTUX
import DTinicializador
import timer

#print(Fore.LIGHTRED_EX + '[!] essa opição não esta disponivel.')

def dire():
    cd = DTinicializador.downloadtube
    cam = os.listdir((cd))
    for i, dir in enumerate(cam, start=1):
        print(Fore.CYAN + f'[{i}] {Fore.WHITE}{dir}')
    esco = int(input(Fore.LIGHTYELLOW_EX + 'selecione o numero do video que você deseja assistir:'))
    try:
        if esco <= 0 or esco > len(cam):
            print(Fore.RED + f'[-] a opição {esco} e invalida tente outra.')
            menumain.menu.MenuMain(
                DTUX.clear()
            )
        else:
            viesco = cam[esco - 1]
            revi = os.path.join(cd, viesco)
            print(Fore.GREEN + '[+] reproduzindo video... \n\nvamos voltar para o munu inicial apos 3 segundos')
            timer.coutdown.go(3)
            os.startfile(revi)
    except Exception as err:
        print(Fore.RED + str(err))
    timer.coutdown.go(6)
    DTUX.clear()
    menumain.menu.MenuMain()
