# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validar_numero_telefone(numero):
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    padrao = re.compile(r"^\(\d{2}\) 9\d{4}-\d{4}$")

    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(padrao, numero):  
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
        return "Número de telefone válido."
    # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
numero = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
resultado = validar_numero_telefone(numero)
# Imprime o resultado:
print(resultado)