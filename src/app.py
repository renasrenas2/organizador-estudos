import sqlite3
import requests
import streamlit as st


def buscar_conselho():
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        if response.status_code == 200:
            return response.json()['slip']['advice']
        return "Estude com foco e persistência!"
    except Exception:
        return "Conexão com API falhou, mas não pare de estudar!"


def criar_banco():
    conn = sqlite3.connect("estudos.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tarefas
                 (id INTEGER PRIMARY KEY, materia TEXT,
                 horas TEXT, status TEXT)""")
    conn.commit()
    return conn


# --- Início da Aplicação (2 linhas vazias acima deste comentário) ---
conn = criar_banco()

st.set_page_config(page_title="Gestor de Estudos Pro v2.0", layout="centered")

st.title("🎓 Gestor de Estudos Acadêmicos")
st.subheader("Sua dose diária de motivação:")

# Exibe o conselho da API
st.info(buscar_conselho())

# Formulário de Entrada
with st.form("nova_materia"):
    col1, col2 = st.columns([3, 1])
    materia = col1.text_input("Nome da Matéria")
    horas = col2.text_input("Horas")
    submit = st.form_submit_button("Adicionar à Rotina")

if submit and materia and horas:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (materia, horas, status) VALUES (?,?,?)",
        (materia, horas, "Pendente")
    )
    conn.commit()
    st.success(f"{materia} adicionada!")

# Exibição da Tabela
st.write("---")
cursor = conn.cursor()
cursor.execute("SELECT * FROM tarefas")
tarefas = cursor.fetchall()

for t in tarefas:
    col_id, col_mat, col_hr, col_st, col_btn = st.columns([1, 4, 2, 3, 2])
    col_id.write(f"#{t[0]}")
    col_mat.write(t[1])
    col_hr.write(f"{t[2]}h")
    col_st.write(t[3])
    if col_btn.button("Excluir", key=f"del_{t[0]}"):
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (t[0],))
        conn.commit()
        st.rerun()