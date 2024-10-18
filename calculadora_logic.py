# calculadora_logic.py

def calcular(expressao):
    """
    Função que recebe uma string contendo a expressão matemática e retorna o resultado.
    """
    try:
        return str(eval(expressao))  # Avalia a expressão e retorna o resultado como string
    except Exception as e:
        return "Erro"  # Retorna "Erro" se algo der errado (como uma divisão por zero, etc.)
