from tkinter import *
import tkinter

#Cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

# configuração inicial da janela
janela = Tk()
#vou deixar o titulo em branco
janela.title("")
#definindo as dimensões da janela
janela.geometry("300x180")
#escolhendo o tamanho da janela
janela.configure(bg=cor1)
#Bloqueando as dimensões da janela
janela.resizable(width=FALSE, height=FALSE)

#Começando o programa// DEFININDO AS VARIAVEIS

global tempo
global rodar
global contador
global limitador

limitador = 59
tempo = "00:00:00"
rodar = False
contador = -2

#função iniciar
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <=-1:
            inicio = "começando em " + str(contador)
            label_tempo["text"] = inicio
            label_tempo["font"] = 'Arial 10'
        #rodando o cronometro
        else:
            label_tempo["font"] = 'Times 50 bold'

            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s>=limitador):
                contador = 0
                m+=1

            s = str(0)+ str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo["text"] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1

#função para dar inicio //rodar= true
def start():
    global rodar
    rodar = True
    iniciar()

#função pausar
def pause():
    global rodar
    rodar = False

#função reiniciar
def reiniciar():
    global contador
    global tempo

    contador = 0
    tempo = "00:00:00"
    label_tempo["text"] = tempo


#criando o nome do aplicativo
label_app = Label(janela, text= "Cronômetro", font= 'TimesNewRoman 14 bold', bg= cor1, fg= cor2)
label_app.place(x= 20, y= 5)

#criando o tempo
label_tempo = Label(janela, text= tempo, font= 'Times 50 bold', bg= cor1, fg= cor6)
#bold = negrito bg = fundo e fg = letra
label_tempo.place(x= 25, y= 40)

#CRIANDO OS BOTÕES
Botao_iniciar = Button(janela,command = start, text= 'Iniciar', width=10, height=2, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Botao_iniciar.place(x=20, y=130)
#relief = estilo do botão overrelief muda o botão quando o mouse passa em cima

Botao_pausar = Button(janela, command = pause, text= 'Pausar', width=10, height=2, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Botao_pausar.place(x=105, y=130)

Botao_reiniciar = Button(janela, command = reiniciar, text= 'Reiniciar', width=10, height=2, bg=cor1, fg=cor5, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Botao_reiniciar.place(x=190, y=130)


janela.mainloop()
