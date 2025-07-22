nome = input("Olá, qual é o seu nome? \n")

while True:
    try:
        peso = float(input("Digite seu peso (em kg): \n"))
        if peso <= 0:
                raise ValueError("O peso deve ser maior que zero.")

        altura_cm = float(input("Digite sua altura (em cm): \n"))
        if altura_cm <= 0:
                raise ValueError("A altura deve ser maior que zero.")

        altura = altura_cm / 100

        IMC = peso / (altura * altura);

        print(f"{nome}, seu imc é: {IMC:.2f}")

        if IMC <= 18.5:
            print("Seu peso está abaixo do ideal")
        elif IMC >= 25:
            print("Seu peso está acima do ideal")
        else:
            print("Seu peso está normal.")

        break

    except ValueError as e:
        print(f"Erro: {e}")
        print("Vamos tentar de novo...\n")
