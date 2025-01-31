# Aprimoramento do Exercício - Curso em Vídeo

Este projeto é um aprimoramento de um exercício do Curso em Vídeo, onde foram criadas as funções `leiaInt()` e `leiaFloat()`. Essas funções melhoram a validação de entrada de dados, garantindo que o usuário informe valores numéricos corretamente.

## Funcionalidades
- `leiaInt(msg)`: Lê um número inteiro, tratando erros de digitação e interrupção do usuário.
- `leiaFloat(msg)`: Lê um número real com as mesmas validações.

## Como usar
Basta chamar as funções passando uma mensagem como argumento:

```python
from utils import leiaint, leiafloat

i = leiaint("Digite um número inteiro: ")
r = leiafloat("Digite um número real: ")

print(f"O valor inteiro digitado foi {i} e o real foi {r}.")
