import time

placa_de_video = []
placa_de_video_preco = ()

processador = []
processador_preco = ()

placa_mãe = []
placa_mãe_preco = ()

ssd = []
ssd_preco = ()

fonte = []
fonte_preco = ()

fonte_de_resfriamento = []
fonte_de_resfriamento_preco = ()

memoria_ram = []
memoria_ram_preco = ()

gabinete = []
gabinete_preco = ()

#preco_total = (placa_de_video_preco + processador_preco + placa_mãe_preco + ssd_preco + fonte_preco + fonte_de_resfriamento_preco + memoria_ram_preco + gabinete_preco)

time.sleep(2)

#Usuário irá enviar os dados e esperar a saida.
resposta = bool("Sim")
while resposta:
    placa_de_video.append(input("Digite a placa de vídeo: "))
    placa_de_video_preco = (int(input("Digite o valor da sua placa de vídeo: ")))
    

    processador.append(input("Digite o processador: "))
    processador_preco = (int(input("Digite o valor do seu processador: ")))

    placa_mãe.append(input("Digite a sua placa mãe: "))
    placa_mãe_preco = int(input("Digite o valor da sua placa mãe: "))
    
    ssd.append(input("Digite seu ssd: "))
    ssd_preco = (int(input("Digite o valor do seu ssd: ")))

    fonte.append(input("Digite sua fonte:"))
    fonte_preco = (int(input("Digite o valor da sua fonte: ")))

    fonte_de_resfriamento.append(input("Digite sua fonte de resfriamento:"))
    fonte_de_resfriamento_preco = (int(input("Digite o valor da sua fonte de resfriamento: ")))

    memoria_ram.append(input("Digite sua memória ram: "))
    memoria_ram_preco = (int(input("Digite o valor da sua memória ram: ")))

    gabinete.append(input("Digite seu gabinete: "))
    gabinete_preco = (int(input("Digite o valor do seu gabinete: ")))
    


    for placa_de_video in placa_de_video: # => saída  
        print("A sua placa de vídeo escolhida foi: ",placa_de_video, "e seu preço é: R$",placa_de_video_preco)

    for processador in processador:
        print("O seu processador escolhido foi: ",processador, "e seu preço é: R$",processador_preco)

    for placa_mãe in placa_mãe:
        print("A sua placa mãe escolhida foi: ",placa_mãe, "e seu preço é: R$",placa_mãe_preco)

    for ssd in ssd:
        print("O seu SSD escolhido foi: ",ssd, "e seu preço é: R$",ssd_preco)

    for fonte in fonte:
        print("A sua fonte escolhida foi: ",fonte, "e seu preço é: R$",fonte_preco)

    for fonte_de_resfriamento in fonte_de_resfriamento:
        print("A sua fonte de resfrimento escolhida foi: ",fonte_de_resfriamento, "e seu preço é: R$",fonte_de_resfriamento_preco)

    for memoria_ram in memoria_ram:
        print("A sua memória ram escolhida foi: ",memoria_ram, "e seu preço é: R$",memoria_ram_preco,)

    for gabinete in gabinete:
        print("O seu gabinete escolhido foi: ",gabinete, "e seu preço é: R$",gabinete_preco)

    break

preco_total = (placa_de_video_preco + processador_preco + placa_mãe_preco + ssd_preco + fonte_preco + fonte_de_resfriamento_preco + memoria_ram_preco + gabinete_preco)
if preco_total == preco_total:
    print("A soma de todos os seus produtos é", placa_de_video_preco + processador_preco + placa_mãe_preco + ssd_preco + fonte_preco + fonte_de_resfriamento_preco + memoria_ram_preco + gabinete_preco)



    


    



