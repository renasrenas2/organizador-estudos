import requests
import streamlit as st

SUPABASE_URL = "https://kxjoanonjuedsrsxucqp.supabase.co"
SUPABASE_KEY = "sb_publishable_sdQNr6YsH3hqWL_7LHk5NQ_6NyH-Q8o"
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
}


def buscar_conselho():
    """Busca um conselho motivacional da API pública."""
    try:
        response = requests.get(
            "https://api.adviceslip.com/advice", timeout=5
        )
        if response.status_code == 200:
            return response.json()['slip']['advice']
        return "Estude com foco e persistencia!"
    except Exception:
        return "Conexao com API falhou, mas nao pare de estudar!"


def listar_tarefas():
    """Lista todas as tarefas do Supabase."""
    try:
        r = requests.get(
            f"{SUPABASE_URL}/rest/v1/tarefas?select=*&order=id.asc",
            headers=HEADERS,
            timeout=10,
        )
        if r.status_code == 200:
            return r.json()
        return []
    except Exception:
        return []


def adicionar_tarefa(materia, horas, status="Pendente"):
    """Insere uma nova tarefa no Supabase."""
    payload = {"materia": materia, "horas": horas, "status": status}
    requests.post(
        f"{SUPABASE_URL}/rest/v1/tarefas",
        headers={**HEADERS, "Prefer": "return=minimal"},
        json=payload,
        timeout=10,
    )


def excluir_tarefa(tarefa_id):
    """Remove uma tarefa pelo ID no Supabase."""
    requests.delete(
        f"{SUPABASE_URL}/rest/v1/tarefas?id=eq.{tarefa_id}",
        headers=HEADERS,
        timeout=10,
    )


def concluir_tarefa(tarefa_id):
    """Marca uma tarefa como concluida no Supabase."""
    requests.patch(
        f"{SUPABASE_URL}/rest/v1/tarefas?id=eq.{tarefa_id}",
        headers={**HEADERS, "Prefer": "return=minimal"},
        json={"status": "Concluido"},
        timeout=10,
    )


# --- Interface ---
st.set_page_config(page_title="Gestor de Estudos Pro v3.0", layout="centered")

st.title("Gestor de Estudos Academicos")
st.subheader("Sua dose diaria de motivacao:")
st.info(buscar_conselho())

with st.form("nova_materia"):
    col1, col2 = st.columns([3, 1])
    materia = col1.text_input("Nome da Materia")
    horas = col2.text_input("Horas")
    submit = st.form_submit_button("Adicionar a Rotina")

if submit and materia and horas:
    adicionar_tarefa(materia, horas)
    st.success(f"{materia} adicionada!")
    st.rerun()

st.write("---")
tarefas = listar_tarefas()

if not tarefas:
    st.info("Nenhuma materia cadastrada ainda.")

for t in tarefas:
    col_id, col_mat, col_hr, col_st, col_ok, col_del = st.columns(
        [1, 4, 2, 3, 2, 2]
    )
    col_id.write(f"#{t['id']}")
    col_mat.write(t['materia'])
    col_hr.write(f"{t['horas']}h")
    col_st.write(t['status'])
    if col_ok.button("Concluir", key=f"ok_{t['id']}"):
        concluir_tarefa(t['id'])
        st.rerun()
    if col_del.button("Excluir", key=f"del_{t['id']}"):
        excluir_tarefa(t['id'])
        st.rerun()