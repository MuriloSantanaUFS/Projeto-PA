from modelo.desenho import Desenho
from visao.janela import Janela
from controlador.controlador import Controlador


desenho = Desenho()

janela = Janela()

Controlador(desenho, janela)

janela.root.mainloop()