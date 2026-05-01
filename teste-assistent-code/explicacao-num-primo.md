# Explicação da função `is_prime`

Este arquivo descreve linha a linha a função Python que verifica se um número é primo.

```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
```

## Linha a linha

- `def is_prime(n: int) -> bool:`
  - Declara a função `is_prime` com um parâmetro `n` do tipo inteiro.
  - O `-> bool` indica que a função retorna `True` ou `False`.

- `if n <= 1:`
  - Verifica se `n` é menor ou igual a 1.
  - Números menores ou iguais a 1 não são primos.

- `return False`
  - Retorna `False` quando `n` não é primo.

- `if n <= 3:`
  - Verifica se `n` é 2 ou 3.
  - Esses valores são primos.

- `return True`
  - Retorna `True` para `n = 2` ou `n = 3`.

- `if n % 2 == 0 or n % 3 == 0:`
  - Verifica se `n` é divisível por 2 ou por 3.
  - Se for, o número não é primo, exceto 2 e 3 que já foram tratados.

- `return False`
  - Retorna `False` se `n` for múltiplo de 2 ou de 3.

- `i = 5`
  - Inicializa o contador `i` com 5.
  - A checagem agora usará divisores na forma 6k-1 e 6k+1.

- `while i * i <= n:`
  - Continua enquanto o quadrado de `i` for menor ou igual a `n`.
  - Não é preciso testar divisores maiores que a raiz quadrada de `n`.

- `if n % i == 0 or n % (i + 2) == 0:`
  - Verifica divisibilidade por `i` ou por `i + 2`.
  - Isso cobre candidatos como 5 e 7, 11 e 13, 17 e 19.

- `return False`
  - Retorna `False` se encontrar qualquer divisor.

- `i += 6`
  - Incrementa `i` em 6 para testar o próximo par de possíveis divisores primos.
  - Isso evita testar múltiplos de 2 e 3 novamente.

- `return True`
  - Se nenhum divisor foi encontrado até a raiz de `n`, então `n` é primo.

## Resumo

A função é eficiente porque:
- exclui rapidamente valores inválidos `<= 1`;
- reconhece diretamente `2` e `3` como primos;
- elimina múltiplos de `2` e `3`;
- testa apenas possíveis divisores relevantes até a raiz de `n`.
