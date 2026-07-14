# Projeto PA - Editor de Desenhos

## Equipe

**Integrantes:**

- Marcelo Menezes
- Murilo Santana

---

## Descrição do sistema

Este projeto consiste em um editor de desenhos desenvolvido na linguagem Python utilizando a biblioteca Tkinter e a arquitetura MVC (Model-View-Controller).

O sistema permite ao usuário desenhar diferentes figuras geométricas, incluindo linhas, retângulos, círculos, ovais e rabiscos livres. Também é possível escolher a cor da borda e do preenchimento das figuras.

Nesta etapa do projeto foi implementada a persistência dos desenhos, permitindo salvar e abrir arquivos utilizando serialização com o módulo `pickle`.

---

## Funcionalidades

- Desenho de linhas;
- Desenho de retângulos;
- Desenho de círculos;
- Desenho de ovais;
- Desenho livre (rabisco);
- Escolha da cor da borda;
- Escolha da cor de preenchimento;
- Salvamento de desenhos em arquivo;
- Abertura de desenhos salvos anteriormente.

---

## Classes documentadas

Foram documentadas **10 classes**:

- Figura
- Linha
- Rabisco
- Retangulo
- Oval
- Circulo
- Poligono
- Desenho
- Controlador
- Janela

---

## Métodos documentados

Foram documentados todos os métodos públicos das classes do sistema, incluindo construtores, métodos de desenho, atualização, persistência e controle da interface.

---

## Estrutura do projeto

```
Projeto-PA/
│
├── src/
│   └── projeto_pa/
│       ├── main.py
│       ├── controlador/
│       ├── modelo/
│       └── visao/
│
├── docs/
│   ├── controlador.controlador.html
│   ├── modelo.desenho.html
│   ├── modelo.figuras.html
│   └── visao.janela.html
│
└── README.md
```

---

## Como executar o sistema

Na raiz do projeto, execute:

```bash
python src/projeto_pa/main.py
```

---

## Como visualizar a documentação

A documentação foi gerada utilizando a ferramenta **Pydoc**.

Para visualizá-la, basta abrir qualquer um dos arquivos HTML presentes na pasta `docs` utilizando um navegador de internet.

---

## Tecnologias utilizadas

- Python 3
- Tkinter
- Pickle
- Pydoc

---

## Versão

Versão **1.0** – Etapa 4 (Persistência e Documentação).