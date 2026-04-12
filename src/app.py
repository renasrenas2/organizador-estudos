import tkinter as tk
from tkinter import messagebox


class OrganizadorEstudos:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Estudos v1.0.0")
        self.root.geometry("400x400")

        # Elementos da Interface
        self.label_titulo = tk.Label(
            root, text="Meu Cronograma de Foco",
            font=("Arial", 14, "bold")
        )
        self.label_titulo.pack(pady=10)

        self.entry_materia = tk.Entry(root, width=30)
        self.entry_materia.insert(0, "Digite a matéria...")
        self.entry_materia.pack(pady=5)

        self.btn_adicionar = tk.Button(
            root, text="Adicionar Tarefa",
            command=self.adicionar_tarefa
        )
        self.btn_adicionar.pack(pady=5)

        self.lista_tarefas = tk.Listbox(root, width=50, height=10)
        self.lista_tarefas.pack(pady=10)

    def adicionar_tarefa(self):
        materia = self.entry_materia.get()
        if materia and materia != "Digite a matéria...":
            self.lista_tarefas.insert(tk.END, f"📚 {materia}")
            self.entry_materia.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Atenção", "Por favor, digite o nome de uma matéria."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizadorEstudos(root)
    root.mainloop()
