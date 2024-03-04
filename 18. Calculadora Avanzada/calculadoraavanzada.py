from tkinter import *
from tkinter import ttk
import math

def TemaOscuro(*args):
    estilos.configure('ventana.TFrame', background="#000D30")

    estilos_texto1.configure('Etexto1.TLabel', background="#000D30", foreground = "white")
    estilos_texto2.configure('Etexto2.TLabel', background="#000D30", foreground = "white")

    estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width = 5, background="#0A0E50", relief="flat", foreground = "white")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#020A90')])

    estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width = 5, background="#000D30", relief="flat", foreground = "white")
    estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#002689')])

    estilos_botones_igual.configure('Botones_igual.TButton', font="arial 22", width = 5, background="#000D30", relief="flat", foreground = "white")
    estilos_botones_igual.map('Botones_igual.TButton', foreground=[('active', '#27E324')], background=[('active', '#002689')])

    estilos_botones_otros.configure('Botones_otros.TButton', font="arial 22", width = 5, background="#000D30", relief="flat", foreground = "white")
    estilos_botones_otros.map('Botones_otros.TButton', background=[('active', '#002689')])

def TemaClaro(*args):
    estilos.configure('ventana.TFrame', background="#DBDBDB")

    estilos_texto1.configure('Etexto1.TLabel', background="#DBDBDB", foreground = "black")
    estilos_texto2.configure('Etexto2.TLabel', background="#DBDBDB", foreground = "black")

    estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width = 5, background="#FFFFFF", relief="flat", foreground = "black")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

    estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat", foreground = "black")
    estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

    estilos_botones_igual.configure('Botones_igual.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat", foreground = "black")
    estilos_botones_igual.map('Botones_igual.TButton', foreground=[('active', '#27E324')], background=[('active', '#858585')])

    estilos_botones_otros.configure('Botones_otros.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat", foreground = "black")
    estilos_botones_otros.map('Botones_otros.TButton', background=[('active', '#858585')])

def valores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada_texto2.set(entrada_texto2.get() + tecla)

    if tecla == '*' or tecla == '+' or tecla == '/' or tecla == '-':
        if tecla == '*':
            entrada_texto1.set(entrada_texto2.get() + '*')
        elif tecla == '/':
            entrada_texto1.set(entrada_texto2.get() + '/')
        elif tecla == '+':
            entrada_texto1.set(entrada_texto2.get() + '+')
        elif tecla == '-':
            entrada_texto1.set(entrada_texto2.get() + '-')

        entrada_texto2.set('')

    if tecla == '=':
        entrada_texto1.set(entrada_texto1.get() + entrada_texto2.get())
        resultado = eval(entrada_texto1.get())
        entrada_texto2.set(resultado)

def valoresTeclado(event):
    tecla = event.char
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada_texto2.set(entrada_texto2.get() + tecla)

    if tecla == '*' or tecla == '+' or tecla == '/' or tecla == '-':
        if tecla == '*':
            entrada_texto1.set(entrada_texto2.get() + '*')
        elif tecla == '/':
            entrada_texto1.set(entrada_texto2.get() + '/')
        elif tecla == '+':
            entrada_texto1.set(entrada_texto2.get() + '+')
        elif tecla == '-':
            entrada_texto1.set(entrada_texto2.get() + '-')

        entrada_texto2.set('')

    if tecla == '=':
        entrada_texto1.set(entrada_texto1.get() + entrada_texto2.get())
        resultado = eval(entrada_texto1.get())
        entrada_texto2.set(resultado)

def RaizCuadrada():
    entrada_texto1.set('')
    resultado = math.sqrt(float(entrada_texto2.get()))
    entrada_texto2.set(resultado)

def ExponencialCuadrado():
    entrada_texto1.set('')
    resultado = math.pow(float(entrada_texto2.get()), 2)
    entrada_texto2.set(resultado)

def ExponencialCubo():
    entrada_texto1.set('')
    resultado = math.pow(float(entrada_texto2.get()), 3)
    entrada_texto2.set(resultado)
    
def borrar(*args):
    inicio = 0
    final = len(entrada_texto2.get())

    entrada_texto2.set(entrada_texto2.get()[inicio:final-1])

def borrarTodo(*args):
    entrada_texto1.set('')
    entrada_texto2.set('')


root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Estilo Ventana

estilos = ttk.Style()
estilos.configure('ventana.TFrame', background="#DBDBDB")
estilos.theme_use('clam')

# Ventana

ventana = ttk.Frame(root, style="ventana.TFrame")
ventana.grid(column=0, row=0, sticky=(W, N, E, S))

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)
ventana.rowconfigure(7, weight=1)


# Estilo Entrada de Texto

estilos_texto1 = ttk.Style()
estilos_texto1.configure('Etexto1.TLabel', font = "arial 15", anchor = "E")

estilos_texto2 = ttk.Style()
estilos_texto2.configure('Etexto2.TLabel', font = "arial 40", anchor = "e")


# Entrada de Texto

entrada_texto1 = StringVar()
e_texto1 = ttk.Label(ventana, textvariable= entrada_texto1, style="Etexto1.TLabel")
e_texto1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada_texto2 = StringVar()
e_texto2 = ttk.Label(ventana, textvariable= entrada_texto2, style="Etexto2.TLabel")
e_texto2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))


# Estilo Botones

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width = 5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botones_igual = ttk.Style()
estilos_botones_igual.configure('Botones_igual.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat")
estilos_botones_igual.map('Botones_igual.TButton', foreground=[('active', '#27E324')], background=[('active', '#858585')])

estilos_botones_otros = ttk.Style()
estilos_botones_otros.configure('Botones_otros.TButton', font="arial 22", width = 5, background="#CECECE", relief="flat")
estilos_botones_otros.map('Botones_otros.TButton', background=[('active', '#858585')])


# Botones
    # Botones Numeros

boton1 = ttk.Button(ventana, text = "1", style="Botones_numeros.TButton", command=lambda:valores('1'))
boton2 = ttk.Button(ventana, text = "2", style="Botones_numeros.TButton", command=lambda:valores('2'))
boton3 = ttk.Button(ventana, text = "3", style="Botones_numeros.TButton", command=lambda:valores('3'))
boton4 = ttk.Button(ventana, text = "4", style="Botones_numeros.TButton", command=lambda:valores('4'))
boton5 = ttk.Button(ventana, text = "5", style="Botones_numeros.TButton", command=lambda:valores('5'))
boton6 = ttk.Button(ventana, text = "6", style="Botones_numeros.TButton", command=lambda:valores('6'))
boton7 = ttk.Button(ventana, text = "7", style="Botones_numeros.TButton", command=lambda:valores('7'))
boton8 = ttk.Button(ventana, text = "8", style="Botones_numeros.TButton", command=lambda:valores('8'))
boton9 = ttk.Button(ventana, text = "9", style="Botones_numeros.TButton", command=lambda:valores('9'))
boton0 = ttk.Button(ventana, text = "0", style="Botones_numeros.TButton", command=lambda:valores('0'))

    # Botones Complementos

boton_borrar  = ttk.Button(ventana, text = chr(9003), style="Botones_borrar.TButton", command=lambda:borrar())
boton_borrar_todo  = ttk.Button(ventana, text = "C", style="Botones_borrar.TButton", command=lambda:borrarTodo())
boton_parentesis1  = ttk.Button(ventana, text = "(", style="Botones_otros.TButton", command=lambda:valores('('))
boton_parentesis2  = ttk.Button(ventana, text = ")", style="Botones_otros.TButton", command=lambda:valores(')'))
boton_punto  = ttk.Button(ventana, text = ".", style="Botones_otros.TButton", command=lambda:valores('.'))
boton_masmenos = ttk.Button(ventana, text = "±", style="Botones_otros.TButton", command=lambda:valores('-'))

    # Botones Operaciones

boton_division  = ttk.Button(ventana, text = chr(247), style="Botones_otros.TButton", command=lambda:valores('/'))
boton_multiplicacion  = ttk.Button(ventana, text = "x", style="Botones_otros.TButton", command=lambda:valores('*'))
boton_suma  = ttk.Button(ventana, text = "+", style="Botones_otros.TButton", command=lambda:valores('+'))
boton_resta  = ttk.Button(ventana, text = "-", style="Botones_otros.TButton", command=lambda:valores('-'))
boton_raiz = ttk.Button(ventana, text = "√", style="Botones_otros.TButton", command=lambda:RaizCuadrada())
boton_cuadrada = ttk.Button(ventana, text = "x²", style="Botones_otros.TButton", command=lambda:ExponencialCuadrado())
boton_cubo = ttk.Button(ventana, text = "x³", style="Botones_otros.TButton", command=lambda:ExponencialCubo())
boton_igual  = ttk.Button(ventana, text = "=", style="Botones_igual.TButton", command=lambda:valores('='))


# Interface

boton_borrar_todo.grid(row = 2 ,column = 0, sticky=(W, N, E, S))
boton_parentesis1.grid(row = 2 ,column = 1, sticky=(W, N, E, S))
boton_parentesis2.grid(row = 2 ,column = 2, sticky=(W, N, E, S))
boton_borrar.grid(row = 2 ,column = 3, sticky=(W, N, E, S))

boton_raiz.grid(row = 3 ,column = 0, sticky=(W, N, E, S))
boton_cuadrada.grid(row = 3 ,column = 1, sticky=(W, N, E, S))
boton_cubo.grid(row = 3 ,column = 2, sticky=(W, N, E, S))
boton_division.grid(row = 3 ,column = 3, sticky=(W, N, E, S))

boton7.grid(row = 4 ,column = 0, sticky=(W, N, E, S))
boton8.grid(row = 4 ,column = 1, sticky=(W, N, E, S))
boton9.grid(row = 4 ,column = 2, sticky=(W, N, E, S))
boton_multiplicacion.grid(row = 4 ,column = 3, sticky=(W, N, E, S))

boton4.grid(row = 5 ,column = 0, sticky=(W, N, E, S))
boton5.grid(row = 5 ,column = 1, sticky=(W, N, E, S))
boton6.grid(row = 5 ,column = 2, sticky=(W, N, E, S))
boton_resta.grid(row = 5 ,column = 3, sticky=(W, N, E, S))

boton1.grid(row = 6 ,column = 0, sticky=(W, N, E, S))
boton2.grid(row = 6 ,column = 1, sticky=(W, N, E, S))
boton3.grid(row = 6 ,column = 2, sticky=(W, N, E, S))
boton_suma.grid(row = 6 ,column = 3, sticky=(W, N, E, S))

boton_masmenos.grid(row = 7 ,column = 0, sticky=(W, N, E, S))
boton0.grid(row = 7 ,column = 1, sticky=(W, N, E, S))
boton_punto.grid(row = 7 ,column = 2, sticky=(W, N, E, S))
boton_igual.grid(row = 7 ,column = 3, sticky=(W, N, E, S))

for child in ventana.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


root.bind('<KeyPress-o>', TemaOscuro)

root.bind('<KeyPress-c>', TemaClaro)

root.bind('<Key>', valoresTeclado)

root.bind('<KeyPress-b>', borrar)

root.bind('<KeyPress-n>', borrarTodo)

root.mainloop()