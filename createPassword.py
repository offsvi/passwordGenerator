import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Exemplo de uso: gerar uma senha de 12 caracteres
senha = gerar_senha(10)
print("Senha gerada:", senha)
