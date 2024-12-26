import tkinter as tk
import customtkinter as ctk

# Função para adicionar valor ao visor
def clicar(valor):
    atual = visor.get()  # Obtém o texto atual do visor
    visor.delete(0, tk.END)  # Limpa o visor
    visor.insert(tk.END, atual + str(valor))  # Insere o valor clicado no visor

# Função para calcular a expressão
def calcular():
    try:
        resultado = eval(visor.get())  # Avalia a expressão no visor
        visor.delete(0, tk.END)  # Limpa o visor
        visor.insert(tk.END, str(resultado))  # Exibe o resultado
    except Exception as e:
        visor.delete(0, tk.END)  # Limpa o visor em caso de erro
        visor.insert(tk.END, "Erro")  # Exibe "Erro" no visor

# Função para limpar o visor
def limpar():
    visor.delete(0, tk.END)  # Limpa o visor

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")  # Título da janela
janela.maxsize(width=320, height=360)  # Limita o tamanho máximo da janela
janela.minsize(width=320, height=360)  # Limita o tamanho mínimo da janela

# Criação do Frame
frame = tk.Frame(janela, bg="white", pady=10)
frame.pack(fill="both", expand=True)  # Posiciona o frame na janela

# Criando o visor
visor = ctk.CTkEntry(
    frame, 
    height=50, 
    font=("SansSerif", 30), 
    state="normal", 
    justify="right", 
    corner_radius=5, 
    border_width=0, # Remove a borda
    fg_color="white"
)
visor.grid(column=0, row=0, padx=5, pady=10, sticky="nsew", columnspan=4)


# Configuração da grid para o Frame
for i in range(6):  # Agora são 6 linhas (1 para o visor e 5 para os botões)
    frame.grid_rowconfigure(i, weight=1, uniform="equal")

for i in range(4):  # 4 colunas
    frame.grid_columnconfigure(i, weight=1, uniform="equal")

# Botões
botao_ce = ctk.CTkButton(frame, text="CE", height=50, command=limpar, corner_radius=5)
botao_ce.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

botao_c = ctk.CTkButton(frame, text="C", height=50, command=limpar, corner_radius=5)
botao_c.grid(column=1, row=1, padx=5, pady=5, sticky="nsew")

botao_del = ctk.CTkButton(frame, text="DEL", height=50, command=limpar, corner_radius=5)
botao_del.grid(column=2, row=1, padx=5, pady=5, sticky="nsew")

botao_div = ctk.CTkButton(frame, text="/", height=50, command=lambda: clicar("/"), corner_radius=5)
botao_div.grid(column=3, row=1, padx=5, pady=5, sticky="nsew")

# Linha 2
botao_7 = ctk.CTkButton(frame, text="7", height=50, command=lambda: clicar(7), corner_radius=5)
botao_7.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")

botao_8 = ctk.CTkButton(frame, text="8", height=50, command=lambda: clicar(8), corner_radius=5)
botao_8.grid(column=1, row=2, padx=5, pady=5, sticky="nsew")

botao_9 = ctk.CTkButton(frame, text="9", height=50, command=lambda: clicar(9), corner_radius=5)
botao_9.grid(column=2, row=2, padx=5, pady=5, sticky="nsew")

botao_multiplicacao = ctk.CTkButton(frame, text="x", height=50, command=lambda: clicar("*"), corner_radius=5)
botao_multiplicacao.grid(column=3, row=2, padx=5, pady=5, sticky="nsew")

# Linha 3
botao_1 = ctk.CTkButton(frame, text="1", height=50, command=lambda: clicar(1), corner_radius=5)
botao_1.grid(column=0, row=3, padx=5, pady=5, sticky="nsew")

botao_2 = ctk.CTkButton(frame, text="2", height=50, command=lambda: clicar(2), corner_radius=5)
botao_2.grid(column=1, row=3, padx=5, pady=5, sticky="nsew")

botao_3 = ctk.CTkButton(frame, text="3", height=50, command=lambda: clicar(3), corner_radius=5)
botao_3.grid(column=2, row=3, padx=5, pady=5, sticky="nsew")

botao_soma = ctk.CTkButton(frame, text="+", height=50, command=lambda: clicar("+"), corner_radius=5)
botao_soma.grid(column=3, row=3, padx=5, pady=5, sticky="nsew")

# Linha 4
botao_4 = ctk.CTkButton(frame, text="4", height=50, command=lambda: clicar(4), corner_radius=5)
botao_4.grid(column=0, row=4, padx=5, pady=5, sticky="nsew")

botao_5 = ctk.CTkButton(frame, text="5", height=50, command=lambda: clicar(5), corner_radius=5)
botao_5.grid(column=1, row=4, padx=5, pady=5, sticky="nsew")

botao_6 = ctk.CTkButton(frame, text="6", height=50, command=lambda: clicar(6), corner_radius=5)
botao_6.grid(column=2, row=4, padx=5, pady=5, sticky="nsew")

botao_subtracao = ctk.CTkButton(frame, text="-", height=50, command=lambda: clicar("-"), corner_radius=5)
botao_subtracao.grid(column=3, row=4, padx=5, pady=5, sticky="nsew")

# Linha 5
botao_plus_minus = ctk.CTkButton(frame, text="+/-", height=55, command=lambda: clicar("+/-"), corner_radius=5)
botao_plus_minus.grid(column=0, row=5, padx=5, pady=5, sticky="nsew")

botao_0 = ctk.CTkButton(frame, text="0", height=55, command=lambda: clicar(0), corner_radius=5)
botao_0.grid(column=1, row=5, padx=5, pady=5, sticky="nsew")

botao_virgula = ctk.CTkButton(frame, text=",", height=55, command=lambda: clicar(","), corner_radius=5)
botao_virgula.grid(column=2, row=5, padx=5, pady=5, sticky="nsew")

botao_igual = ctk.CTkButton(frame, text="=", height=55, command=calcular, corner_radius=5)
botao_igual.grid(column=3, row=5, padx=5, pady=5, sticky="nsew")

# Executa a aplicação
janela.mainloop()
