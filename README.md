# 🎓 Gestor de Estudos Acadêmicos Pro

**Versão:** 2.0.0
**Autor:** Renato Moreira Santos Faria
**Repositório:** https://github.com/renasrenas2/organizador-estudos

## 🚀 Aplicação Online (Deploy)

> **Acesse a aplicação publicada aqui:**
> **[🔗 https://organizador-estudos-ykblpr2sylxzo4kmjpquin.streamlit.app](https://organizador-estudos-ykblpr2sylxzo4kmjpquin.streamlit.app)**

---

## 📝 Descrição do Problema Real

Muitos estudantes universitários enfrentam dificuldades em organizar sua rotina de estudos. A falta de um local centralizado para listar matérias e acompanhar o progresso leva à procrastinação e à sensação de sobrecarga, dificultando a gestão do tempo e o foco nas prioridades acadêmicas.

## 🎯 Proposta da Solução

Aplicação web que permite ao aluno cadastrar disciplinas e cargas horárias, marcar tarefas como concluídas e receber um conselho motivacional diário via API pública — tudo com dados salvos de forma persistente.

## 👥 Público-Alvo

- Estudantes de graduação e pós-graduação.
- Alunos em preparação para o ENEM e concursos.
- Qualquer pessoa que necessite organizar tarefas de aprendizado.

---

## 🚀 Funcionalidades Principais

- **Conselho Motivacional:** Integração com a API [Advice Slip](https://api.adviceslip.com/) que exibe uma frase motivacional a cada acesso.
- **Cadastro Dinâmico:** Registro de matérias com definição de horas de estudo.
- **Persistência Local:** Banco de dados SQLite para que os dados não sejam perdidos.
- **Gestão de Status:** Marcação visual de tarefas como "Pendente" ou "Concluído ✅".
- **Sistema de Exclusão:** Remoção de matérias de forma simples.

## 🌐 API Pública Integrada

| API | Endpoint | Finalidade |
|-----|----------|------------|
| Advice Slip API | `GET https://api.adviceslip.com/advice` | Exibir conselho motivacional na tela inicial |

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Interface Gráfica:** Streamlit (Web GUI)
- **Banco de Dados:** SQLite3
- **Testes:** Pytest + unittest.mock
- **Qualidade de Código:** Flake8
- **CI/CD:** GitHub Actions
- **Deploy:** Streamlit Community Cloud

---

## 📦 Instruções de Instalação e Execução

### 1. Clonar e Instalar

```bash
git clone https://github.com/renasrenas2/organizador-estudos.git
cd organizador-estudos
pip install -r requirements.txt
```

### 2. Executar a Aplicação

```bash
streamlit run src/app.py
```

### 3. Rodar os Testes

```bash
pytest tests/ -v
```

### 4. Rodar o Lint

```bash
flake8 src/app.py tests/test_integration.py --max-line-length=88
```

---

## 🔁 Fluxo de Desenvolvimento (Etapa 2)

1. Issue #1 criada descrevendo a integração com a API
2. Branch `entrega-intermediaria` criada a partir da `main`
3. Integração com a Advice Slip API implementada
4. Testes de integração criados com mock
5. Deploy publicado no Streamlit Community Cloud
6. Pull Request #2 aberto com `Closes #1`
7. Merge realizado na `main`