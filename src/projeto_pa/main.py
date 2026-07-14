from modelo.desenho import Desenho
import modelo.desenho
print(modelo.desenho.__file__)
from visao.janela import Janela
from controlador.controlador import Controlador


desenho = Desenho()

janela = Janela()

Controlador(desenho, janela)

janela.root.mainloop()