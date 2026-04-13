# 🎓 Gestor de Estudos Acadêmicos Pro

**Versão:** 2.0.0  
**Autor:** Renato Moreira Santos Faria  
**Repositório Público:** [https://github.com/renasrenas2/organizador-estudos](https://github.com/renasrenas2/organizador-estudos)

---

## 📝 Descrição do Problema Real
Muitos estudantes universitários e de cursos preparatórios enfrentam dificuldades severas em organizar sua rotina de estudos. A falta de um local centralizado para listar matérias e acompanhar o progresso leva à procrastinação e à sensação de sobrecarga, dificultando a gestão do tempo e o foco nas prioridades acadêmicas.

## 🎯 Proposta da Solução
A solução proposta é uma aplicação desktop leve e intuitiva que permite ao aluno cadastrar suas disciplinas e cargas horárias estimadas. Ao oferecer a possibilidade de marcar tarefas como concluídas e manter esses dados salvos permanentemente, o software ajuda na visualização clara do progresso e na organização mental da rotina.

## 👥 Público-Alvo
- Estudantes de graduação e pós-graduação.
- Alunos em preparação para o ENEM e concursos.
- Qualquer pessoa que necessite organizar tarefas de aprendizado de forma simples.

---

## 🚀 Funcionalidades Principais
- **Cadastro Dinâmico:** Registro de matérias com definição de horas de estudo.
- **Persistência Local:** Uso de banco de dados SQLite para que os dados não sejam perdidos ao fechar o app.
- **Gestão de Status:** Marcação visual de tarefas como "Pendente" ou "Concluído ✅".
- **Sistema de Exclusão:** Remoção de matérias da grade de estudos de forma simples.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.14.4
- **Interface Gráfica:** Tkinter (GUI)
- **Banco de Dados:** SQLite3
- **Testes:** Pytest
- **Qualidade de Código:** Flake8 (Linting)
- **CI/CD:** GitHub Actions

---

## 📦 Instruções de Instalação e Execução

### 1. Instalação
Clone o repositório e instale as dependências necessárias listadas no `requirements.txt`:
```bash
git clone [https://github.com/renasrenas2/organizador-estudos.git](https://github.com/renasrenas2/organizador-estudos.git)
cd organizador-estudos
pip install -r requirements.txt
```
### 2. Execução da Aplicação
Para iniciar a interface gráfica do projeto:
```bash
python src/app.py
```
### Como rodar os Testes (Pytest)
Para validar se a lógica interna do sistema está funcionando corretamente:
```bash
pytest
```
### Como rodar o Lint (Flake8)
Para verificar se o código segue os padrões estéticos e de boas práticas da PEP8:
```bash
flake8 src/app.py
