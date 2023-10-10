from tkinter import messagebox
from tela_clientes import*
from tela animais import*

tela = tk ()
tela.configure(background="#fffffff")
def chamar_tela_clientes():
    desenha_clientes(tela)
def chamar_tela_animais():
    desenha_animais(tela)
def sair_sistema():
 tela.destroy()

botao_clientes = Button(tela,text="CLIENTES",width=30,height=4,font=("Helvetica",16),command=chamar_tela_clintes).place(x=420,y=20)
botao_animais = Button(tela,text="PETS",width=30,height=4,font=("Helvetica",16),command=chamar_tela_animais).place(x=420,y=170)
botao_servicos_cad = Button(tela,text="SERVIÇOS",width=30,height=4,font=("Helvetica",16)).place(x=420,y=320)
botao_servicos= Button(tela,text="REALIZAR",width=30,height=4,font=("Helvetica",16)).place(x=420,y=470)
botao_sair = Button(tela,text="SAIR",width=30,height=4,font=("Helvetica",16),command=lambda:fechartela(tela)).place(x=420,y=620)

tela.geometry('800x600')
tela.title("pet shop -zooblue")
tela.state('zoomed')

tela.main.loop