# Explicação da refatoração

Este arquivo explica linha a linha o código refatorado que calcula estatísticas básicas sobre uma lista de números.

```python
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
```

## Linha a linha

- `def calcular_estatisticas(valores):`
  - Define a função `calcular_estatisticas` que recebe um argumento chamado `valores`.
  - A função calcula e retorna estatísticas a partir desta lista.

- `total = sum(valores)`
  - Usa a função embutida `sum()` do Python para somar todos os itens da lista.
  - Armazena o resultado na variável `total`.

- `media = total / len(valores)`
  - Calcula a média dividindo a soma pelo comprimento da lista.
  - A função `len()` retorna quantos elementos existem em `valores`.

- `maior = max(valores)`
  - Usa a função embutida `max()` para encontrar o maior valor da lista.
  - O resultado é armazenado em `maior`.

- `menor = min(valores)`
  - Usa a função embutida `min()` para encontrar o menor valor da lista.
  - O resultado é armazenado em `menor`.

- `return total, media, maior, menor`
  - Retorna uma tupla com as quatro estatísticas calculadas.
  - Isso permite receber os valores em variáveis separadas ao chamar a função.

- `if __name__ == "__main__":`
  - Verifica se o arquivo está sendo executado diretamente, e não importado como módulo.
  - O bloco abaixo só roda quando o script é executado diretamente.

- `numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`
  - Define a lista de números que será usada como exemplo.

- `total, media, maior, menor = calcular_estatisticas(numeros)`
  - Chama a função `calcular_estatisticas` com a lista `numeros`.
  - Desempacota os valores retornados em variáveis nomeadas.

- `print("total:", total)`
  - Exibe o total dos números no console.

- `print("média:", media)`
  - Exibe a média dos números no console.

- `print("maior:", maior)`
  - Exibe o maior número da lista.

- `print("menor:", menor)`
  - Exibe o menor número da lista.

## Observações de boas práticas

- O nome `calcular_estatisticas` é mais descritivo do que `c`.
- `valores`, `total`, `media`, `maior` e `menor` são nomes claros e fáceis de entender.
- O uso de funções embutidas (`sum`, `max`, `min`, `len`) torna o código mais legível e expressivo.
- O bloco `if __name__ == "__main__":` separa a lógica de execução direta da definição da função.
