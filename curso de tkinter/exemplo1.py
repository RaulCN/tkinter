#Página 8 do pdf https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf


from tkinter import * #n funciona com Tkinter import * como o exemplo do pdf 
class Janela:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()
raiz=Tk() #N sei pq Tk e não tk
Janela(raiz)
raiz.mainloop()
        
