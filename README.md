# 🎓 Gestor de Estudos Acadêmicos Pro

**Versão:** 3.0.0
**Repositório:** https://github.com/renasrenas2/organizador-estudos

## 🚀 Aplicação Online (Deploy)

> **Acesse a aplicação publicada aqui:**
> **[🔗 https://organizador-estudos-ykblpr2sylxzo4kmjpquin.streamlit.app](https://organizador-estudos-ykblpr2sylxzo4kmjpquin.streamlit.app)**

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Renato Moreira Santos Faria | [@renasrenas2](https://github.com/renasrenas2) |
| Guilherme Carvalho Ribeiro | [@GlCarvalho07](https://github.com/GlCarvalho07)|

---

## 📝 Descrição do Problema Real

Muitos estudantes universitários enfrentam dificuldades em organizar sua rotina de estudos. A falta de um local centralizado para listar matérias e acompanhar o progresso leva à procrastinação e à sensação de sobrecarga, dificultando a gestão do tempo e o foco nas prioridades acadêmicas.

## 🎯 Proposta da Solução

Aplicação web que permite ao aluno cadastrar disciplinas e cargas horárias, marcar tarefas como concluídas e receber um conselho motivacional diário via API pública — com dados salvos em banco de dados na nuvem (Supabase).

## 👥 Público-Alvo

- Estudantes de graduação e pós-graduação.
- Alunos em preparação para o ENEM e concursos.
- Qualquer pessoa que necessite organizar tarefas de aprendizado.

---

## 🚀 Funcionalidades Principais

- **Conselho Motivacional:** Integração com a API [Advice Slip](https://api.adviceslip.com/) que exibe uma frase motivacional a cada acesso.
- **Cadastro Dinâmico:** Registro de matérias com definição de horas de estudo.
- **Persistência em Nuvem:** Banco de dados Supabase (PostgreSQL) para dados acessíveis de qualquer lugar.
- **Gestão de Status:** Marcação de tarefas como "Pendente" ou "Concluído".
- **Sistema de Exclusão:** Remoção de matérias de forma simples.

## 🌐 APIs e Banco de Dados

| Serviço | Uso |
|---------|-----|
| Advice Slip API | Conselho motivacional na tela inicial |
| Supabase (PostgreSQL) | Banco de dados em nuvem para persistência das tarefas |

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Interface:** Streamlit
- **Banco de Dados:** Supabase (PostgreSQL)
- **Testes:** Pytest + unittest.mock
- **Qualidade:** Flake8
- **CI/CD:** GitHub Actions
- **Deploy:** Streamlit Community Cloud

---

## 📦 Como Rodar Localmente

```bash
git clone https://github.com/renasrenas2/organizador-estudos.git
cd organizador-estudos
pip install -r requirements.txt
py -m streamlit run src/app.py
```

## 🧪 Rodar os Testes

```bash
pytest tests/ -v
```

## 🔍 Rodar o Lint

```bash
flake8 src/app.py tests/test_integration.py --max-line-length=88
```