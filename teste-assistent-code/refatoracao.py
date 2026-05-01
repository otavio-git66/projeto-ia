def calcular_estatisticas(valores):
    total = sum(valores)
    media = total / len(valores)
    maior = max(valores)
    menor = min(valores)
    return total, media, maior, menor


if __name__ == "__main__":
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numeros)

    print("total:", total)
    print("média:", media)
    print("maior:", maior)
    print("menor:", menor)
