from colorama import Fore, init
init()
import random
import DTinicializador
import timer
import DTUX

print(Fore.LIGHTMAGENTA_EX + "carregando...")
dicas = random.choice(["é sempre bom manter-se atualizado" , "não tente baixar lives em transmissão", "leia todas as mensagens que aparecer na tela", "mensagem começa com 'traceback:' desinstale a versão e instale uma versão anterior que funcione", "se aparecer 'traceback' entre em contato com sempreolucas41@gmail.com", "apenas videos do youtube podem ser baixados por essa ferramenta", "use de forma consciente", "vai baixar o que hoje?", "Você está lendo isso porque é humano ou é humano porque está lendo isso?", "sabe o site preferido do cavalo? é cavalhinho PONTO COM PONTO COM PONTO COM PONTO COM PONTO COM", "o que a galinha disse pro pato... CÓ CÓ", "mantenha seu DT atualizado para a redução de bugs", "não recomendamos usar versões inferiores a 0.0.4"])
print(f"DICA:{dicas}")
timer.coutdown.go(10)
DTUX.clear()
DTinicializador.inicializador()
