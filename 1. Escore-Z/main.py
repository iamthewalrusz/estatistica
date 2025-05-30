from scipy import stats
# A biblioteca SciPy fornece algoritmos para otimização, 
# integração, interpolação, problemas de autovalor, 
# equações algébricas, equações diferenciais, estatísticas 
# e muitas outras classes de problemas.

import os # Biblioteca usada apenas para limpar o terminal


dados = []

def adicionar_dados():
    dado = float(input("Digite um número: "))
    dados.append(dado)

def deletar_dados():
    dados.clear()

def calcular_escore_z():
    """Usa a função zscore da biblioteca Scipy.
    Ela automaticamente calcula cada dado do array menos a média dividido pelo desvio padrão,
    assim calculando e retornando o escore-z para todos os dados do array."""
    return stats.zscore(dados)

def main():
    while True:
        print("Conjunto de dados atual:", dados, "\n")

        print("Opções:\n" \
        "1: Adicionar dados\n" \
        "2: Deletar dados\n" \
        "3: Calcular Escore-Z\n" \
        "4: Sair\n")
        opcao = int(input("Escolha uma opção: "))
        os.system('cls')

        match opcao:
            case 1:
                adicionar_dados()

            case 2:
                deletar_dados()

            case 3:
                print(calcular_escore_z())
            
            case 4:
                break

main()