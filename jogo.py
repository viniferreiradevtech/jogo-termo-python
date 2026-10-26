secreta = "prato"
acertou = False

for vez in range(6):
    chute = input("Palpite: ").lower().strip()

    while len(chute) != 5:
        chute = input("Use exatamente 5 letras: ").lower().strip()

    dica = ""

    for i in range(5):
        if chute[i] == secreta[i]:
            dica += "🟩"
        elif chute[i] in secreta:
            dica += "🟨"
        else:
            dica += "⬛"

    print(dica)

    if chute == secreta:
        print("Acertou!")
        acertou = True
        break

if not acertou:
    print(f"Fim de jogo! A palavra era {secreta}.")
    
