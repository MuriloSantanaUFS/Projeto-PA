from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
# =========================
# ALTERAÇÕES - MURILO
# Adição de retângulo, oval e círculo
# =========================
    tipo = tipo_figura_var.get()

    if tipo == 'Linha':
        figura_nova = (
            "linha",
            (event.x, event.y, event.x, event.y),
            cor_borda
        )

    elif tipo == 'Rabisco':
        figura_nova = (
            "rabisco",
            [(event.x, event.y)],
            cor_borda
        )

    elif tipo == 'Retangulo':
        figura_nova = (
            "retangulo",
            (event.x, event.y, event.x, event.y),
            cor_borda
        )

    elif tipo == 'Oval':
        figura_nova = (
            "oval",
            (event.x, event.y, event.x, event.y),
            cor_borda
        )

    elif tipo == 'Circulo':
        figura_nova = (
            "circulo",
            (event.x, event.y, event.x, event.y),
            cor_borda
        )

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))

    else:
        figura_nova = (
            figura_nova[0],
            (
                figura_nova[1][0],
                figura_nova[1][1],
                event.x,
                event.y
            ),
            figura_nova[2]
        )
        

    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()
    
def desenhar(figura, tracejado=False):

    fig, values, cor = figura

    opcoes = {}
    opcoes["outline"] = cor
    opcoes["fill"] = ""

    if tracejado:
        opcoes["dash"] = (4, 2)

    if fig == "linha":
        canvas.create_line(
            values[0],
            values[1],
            values[2],
            values[3],
            fill = cor,
            **({"dash": (4,2)} if tracejado else {})
        )

    elif fig == "rabisco":
        canvas.create_line(
            values,
            fill = cor,
            **({"dash": (4,2)} if tracejado else {})
        )

    elif fig == "retangulo":
        canvas.create_rectangle(
            values,
            **opcoes
        )

    elif fig == "oval":
        canvas.create_oval(
            values,
            **opcoes
        )

    elif fig == "circulo":

        x1, y1, x2, y2 = values

        lado = min(abs(x2-x1), abs(y2-y1))

        if x2 < x1:
            lado *= -1

        x2 = x1 + lado

        lado = min(abs(x2-x1), abs(y2-y1))

        if y2 < y1:
            lado *= -1

        y2 = y1 + lado

        canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            **opcoes
        )

def desenhar_figuras():

    canvas.delete("all")

    for figura in figuras:
        desenhar(figura)
        
def desenhar_figura_nova():

    desenhar(
        figura_nova,
        tracejado=True
    )

def incompleta(figura):
    fig, values, cor = figura

    if fig == "rabisco":
        return len(values) <= 1

    return (values[0], values[1]) == (values[2], values[3])

def escolher_cor_borda():
    global cor_borda

    cor = askcolor(title="Escolha a cor da borda")

    if cor[1] is not None:
        cor_borda = cor[1]




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
cor_borda = "black" #define a borda padrão para preta

root = Tk()
root.title('Exemplo de aplicação')
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Escolha se vai desenhar linha ou Rabisco:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')

botao_cor = ttk.Button( #botao para selecionar cor da borda
    frame,
    text="Cor da borda",
    command=escolher_cor_borda
)

botao_cor.grid(column=2, row=0, padx=5, pady=5)
# =========================
# - Atualização do OptionMenu com novos tipos de figura (feito por Murilo)
# =========================



option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
