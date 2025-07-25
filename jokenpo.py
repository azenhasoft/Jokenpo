# Importa a biblioteca para fazer escolhas aleatórias
import random

# Lista com as escolhas possíveis
opcoes = ["pedra", "papel", "tesoura"]

# Loop infinito para continuar jogando
while True:
    # Pede a jogada do jogador. A mensagem agora inclui a opção sair
    jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para parar): ").lower()

    # Se o jogador digitar sair, o jogo para
    if jogador == 'sair':
        print("Obrigado por jogar!")
        break  # Interrompe o loop e encerra o programa

    # Se a jogada não for uma das opções válidas, avisa e volta ao início do loop
    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue  # Pula o resto do código e começa uma nova rodada

    # O computador escolhe uma opção aleatória da lista
    computador = random.choice(opcoes)

    # Mostra o que cada um escolheu
    print(f"\nVocê jogou: {jogador}")
    print(f"Computador jogou: {computador}\n")

    # Lógica para decidir o resultado

    # Se as escolhas forem iguais, é empate
    if jogador == computador:
        print("Deu empate!")

    # Condições em que o jogador ganha
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("Você ganhou!")

    # Se não empatou e não ganhou, então o jogador perdeu
    else:
        print("Você perdeu!")