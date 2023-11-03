"""
helper.py - Código auxiliar para o projeto 2 de POO com Python
"""
def formata_float_str_moeda(valor: float) -> str:
    """Formata um float para moeda formato string"""
    return f'R$ {valor:.2f}'.replace('.', ',')
