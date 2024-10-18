import tkinter as tk
from calculadora_logic import calcular  # Importa a função calcular do outro arquivo

# Função para atualizar o display da calculadora
def click(event):
    current_text = display_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        result = calcular(current_text)  # Usa a função do arquivo calculadora_logic.py
        display_var.set(result)
    elif button_text == "C":
        display_var.set("")  # Limpa o display
    elif button_text == "←":  # Botão de backspace
        display_var.set(current_text[:-1])  # Remove o último caractere
    else:
        # Permite a adição de um ponto (.) se ainda não houver um na expressão
        if button_text == "." and "." in current_text.split()[-1]:
            return  # Não permite adicionar mais de um ponto em um número
        display_var.set(current_text + button_text)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")
root.resizable(False, False)  # Impede o redimensionamento da janela

# Definir cores
bg_color = "#2c3e50"  # Cor de fundo da janela
button_color = "#34495e"  # Cor dos botões numéricos
text_color = "#ecf0f1"  # Cor do texto dos botões numéricos
operation_color = "#e67e22"  # Cor dos botões de operações (+, -, *, /)
special_button_color = "#e74c3c"  # Cor do botão "C"
equal_button_color = "#1abc9c"  # Cor do botão "="
display_bg = "#1abc9c"  # Cor de fundo do display
display_fg = "#ffffff"  # Cor do texto do display

# Configuração da janela principal
root.configure(bg=bg_color)

# Variável para o display
display_var = tk.StringVar()

# Display da calculadora (com fundo personalizado)
display = tk.Entry(
    root,
    textvariable=display_var,
    font="Arial 24",
    justify="right",
    bd=10,
    relief=tk.SUNKEN,
    bg=display_bg,
    fg=display_fg,
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões da calculadora com suas respectivas cores
buttons = [
    ("7", button_color),
    ("8", button_color),
    ("9", button_color),
    ("←", special_button_color),
    ("4", button_color),
    ("5", button_color),
    ("6", button_color),
    ("/", operation_color),
    ("1", button_color),
    ("2", button_color),
    ("3", button_color),
    ("*", operation_color),
    ("C", special_button_color),
    ("0", button_color),
    ("+", operation_color),  # Mover o botão + para a posição do .
    ("-", operation_color),
    (".", button_color),  # Mover o botão . para a posição do +
    ("=", equal_button_color),
]

# Adiciona os botões na interface com estilização
row = 1
col = 0
for button_text, color in buttons:
    button = tk.Button(
        root,
        text=button_text,
        font="Arial 20 bold",
        padx=20,
        pady=20,
        bg=color,
        fg=text_color,
        activebackground="#16a085",
        activeforeground="#ffffff",
    )

    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", click)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Ajustar o layout da grade para permitir redimensionamento
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Inicia o loop da interface gráfica
root.mainloop()
