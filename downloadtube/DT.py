from colorama import Fore, init
init()
import random
import DTinicializador
import timer

print(Fore.LIGHTMAGENTA_EX + "carregando...")
dicas = random.choice(["não tente baixar lives em transmissão", "leia todas as mensagens que aparecer na tela", "mensagem começa com 'traceback:' desinstale a versão e instale uma versão anterior que funcione", "se aparecer 'traceback' entre em contato com sempreolucas41@gmail.com", "apenas videos do youtube podem ser baixados por essa ferramenta", "use de forma consciente", "vai baixar o que hoje?", "Você está lendo isso porque é humano ou é humano porque está lendo isso?", "sabe o site preferido do cavalo? é cavalhinho PONTO COM PONTO COM PONTO COM PONTO COM PONTO COM", "o que a galhina disse pro pato... CÓ CÓ"])
print(f"DICA:{dicas}")
timer.coutdown.go(5)
DTinicializador.inicializador()
