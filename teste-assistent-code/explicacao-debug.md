# Explicação do código `pedido_corrigido.py`

Este arquivo descreve linha a linha o código corrigido que calcula o total de um pedido com imposto e desconto.

```python
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

## Linha a linha

- `cliente = input("Qual é seu nome? ")`
  - Pede o nome do cliente e guarda o texto na variável `cliente`.

- `qtd1 = int(input("Quantidade do item 1: "))`
  - Lê a quantidade do primeiro item como texto e converte para inteiro.

- `item1 = float(input("Preço do item 1? "))`
  - Lê o preço do primeiro item como texto e converte para número decimal.

- `qtd2 = int(input("Quantidade do item 2: "))`
  - Lê a quantidade do segundo item e converte para inteiro.

- `item2 = float(input("Preço do item 2? "))`
  - Lê o preço do segundo item e converte para float.

- `qtd3 = int(input("Quantidade do item 3: "))`
  - Lê a quantidade do terceiro item e converte para inteiro.

- `item3 = float(input("Preço do item 3? "))`
  - Lê o preço do terceiro item e converte para float.

- `total_item1 = qtd1 * item1`
  - Calcula o valor total do primeiro item multiplicando quantidade por preço unitário.

- `total_item2 = qtd2 * item2`
  - Calcula o valor total do segundo item.

- `total_item3 = qtd3 * item3`
  - Calcula o valor total do terceiro item.

- `subtotal = total_item1 + total_item2 + total_item3`
  - Soma os totais dos três itens para obter o subtotal.

- `imposto = subtotal * 0.10`
  - Calcula 10% de imposto sobre o subtotal.

- `desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
  - Lê o percentual de desconto e converte para float, permitindo cálculo numérico.

- `desconto = subtotal * (desconto_cupom / 100)`
  - Converte o percentual em fração e calcula o valor do desconto.

- `total = subtotal + imposto - desconto`
  - Calcula o valor final do pedido aplicando imposto e subtraindo o desconto.

- `linha = "=" * 31`
  - Cria uma linha de separação de 31 caracteres iguais.

- `separador = "-" * 31`
  - Cria outra linha de separação com traços.

- `print(linha)`
  - Imprime a linha de igualdade no relatório.

- `print(f" Cliente: {cliente}")`
  - Mostra o nome do cliente formatado.

- `print(linha)`
  - Imprime a linha de igualdade novamente.

- `print(f" Item 1:        R$ {total_item1:.2f}")`
  - Exibe o total do primeiro item com duas casas decimais.

- `print(f" Item 2:        R$ {total_item2:.2f}")`
  - Exibe o total do segundo item.

- `print(f" Item 3:        R$ {total_item3:.2f}")`
  - Exibe o total do terceiro item.

- `print(separador)`
  - Imprime a linha de traços antes do subtotal.

- `print(f" Subtotal:      R$ {subtotal:.2f}")`
  - Exibe o subtotal.

- `print(f" Imposto (10%): R$ {imposto:.2f}")`
  - Exibe o valor do imposto calculado.

- `if desconto_cupom > 0:`
  - Verifica se houve desconto maior que zero.
  - Se sim, o desconto será exibido.

- `    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
  - Imprime o desconto aplicado, formatado como porcentagem inteira e valor positivo com sinal negativo.

- `print(linha)`
  - Imprime a linha de igualdade antes do total final.

- `print(f" TOTAL:         R$ {total:.2f}")`
  - Exibe o total final a pagar.

- `print(linha)`
  - Finaliza o relatório com uma linha de igualdade.

## Observações

- A conversão de `input()` para `int` e `float` é essencial para permitir cálculos.
- O uso de `f-strings` com `:.2f` garante que os valores monetários apareçam com duas casas decimais.
- A indentação correta é fundamental para o bloco do `if` funcionar.
