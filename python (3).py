import tkinter as tk
from tkinter import messagebox


def cadastrar_cliente():
  
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    email = entry_email.get()
    

    messagebox.showinfo("Cadastro de Cliente", "Cliente cadastrado com sucesso!")


root = tk.Tk()
root.title("PET SHOP")


frame_cliente = tk.Frame(root)
frame_cliente.pack()
frame_cliente.grid(row=0, column=0, padx=10, pady=10)

label_nome = tk.Label(frame_cliente, text="Cliente:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(frame_cliente)
entry_nome.grid(row=0, column=1)

label_telefone = tk.Label(frame_cliente, text="Telefone:")
label_telefone.grid(row=1, column=0)
entry_telefone = tk.Entry(frame_cliente)
entry_telefone.grid(row=1, column=1)

label_endereco = tk.Label(frame_cliente, text="Endereço:")
label_endereco.grid(row=2, column=0)
entry_endereco = tk.Entry(frame_cliente)
entry_endereco.grid(row=2, column=1)

label_email = tk.Label(frame_cliente, text="E-mail:")
label_email.grid(row=3, column=0)
entry_email = tk.Entry(frame_cliente)
entry_email.grid(row=3, column=1)


button_cadastrar_cliente = tk.Button(frame_cliente, text="Cadastrar Cliente", command=cadastrar_cliente)
button_cadastrar_cliente.grid(row=4, columnspan=2)

root.mainloop()