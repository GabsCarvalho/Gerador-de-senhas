import string
import random

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_caracteres_especiais=True):
    """Gera uma senha aleatória com base nas preferências do usuário."""
    if tamanho < 4:
        raise ValueError("O comprimento mínimo da senha é 4.")

    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas Aleatórias!")
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
        incluir_caracteres_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_caracteres_especiais)
        print(f"Sua senha gerada é: {senha}")

    except ValueError as erro:
        print(f"Erro: {erro}")

if __name__ == "__main__":
    main()