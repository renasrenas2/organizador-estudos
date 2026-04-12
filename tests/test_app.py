import pytest

# Função simples para validar a lógica que seu app usará
def validar_materia(nome):
    if not nome or nome.strip() == "" or nome == "Digite a matéria...":
        return False
    return True

# 1. Teste de Caminho Feliz (Sucesso)
def test_adicionar_materia_valida():
    assert validar_materia("Engenharia de Software") is True

# 2. Teste de Entrada Inválida (Vazio)
def test_adicionar_materia_vazia():
    assert validar_materia("") is False

# 3. Teste de Caso Limite (Espaços em branco)
def test_adicionar_materia_so_espacos():
    assert validar_materia("   ") is False