import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog
import threading
import json
import os
import pyautogui as pa
import keyboard
import time

CONFIG_ARQUIVO = "config.json"

executando = False
pausado = False
cliente_atual_id = None

# ---------------- CONFIG ---------------- #

def carregar_config():
    if not os.path.exists(CONFIG_ARQUIVO):
        return {"clientes": {}}

    with open(CONFIG_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_config():
    with open(CONFIG_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


config = carregar_config()

# ---------------- CONTROLE ---------------- #

def sleep_seguro(segundos):
    inicio = time.time()
    while time.time() - inicio < segundos:
        if not executando:
            return

        while pausado:
            time.sleep(0.1)
            if not executando:
                return

        time.sleep(0.05)


def esperar_se_pausado():
    while pausado:
        time.sleep(0.1)
        if not executando:
            return

# ---------------- FUNÇÕES MACRO ---------------- #

def executar_tarefa():
    global executando, pausado

    if executando:
        print("Macro já está em execução.")
        return

    if not cliente_atual_id:
        print("Nenhum cliente selecionado.")
        return

    executando = True
    pausado = False

    codigo = editor.get("1.0", "end-1c")

    def run():
        global executando
        try:
            exec(codigo, globals())
        except Exception as e:
            print("Erro no script:", e)
        executando = False

    threading.Thread(target=run, daemon=True).start()


def parar_tarefa():
    global executando, pausado
    executando = False
    pausado = False
    print("Tarefa parada.")


def stop_global():
    global executando, pausado
    executando = False
    pausado = False
    print("STOP GLOBAL acionado (F1)")


def pause_resume():
    global pausado

    if not executando:
        return

    pausado = not pausado

    if pausado:
        print("MACRO PAUSADO (F2)")
    else:
        print("MACRO RETOMADO (F2)")


def salvar_codigo():
    if not cliente_atual_id:
        print("Nenhum cliente selecionado.")
        return

    script = editor.get("1.0", "end-1c")
    config["clientes"][cliente_atual_id]["script"] = script
    salvar_config()
    print("Macro salvo para o cliente selecionado.")

# ---------------- CLIENTES ---------------- #

def listar_clientes():
    return [
        f"{dados['nome']} ({cid})"
        for cid, dados in config["clientes"].items()
    ]


def selecionar_cliente(event=None):
    global cliente_atual_id

    valor = cliente_var.get()
    if not valor:
        return

    cliente_atual_id = valor.split("(")[-1].replace(")", "")
    script = config["clientes"][cliente_atual_id]["script"]

    editor.delete("1.0", "end")
    editor.insert("1.0", script)


def novo_cliente():
    nome = simpledialog.askstring("Novo cliente", "Nome do cliente:")
    if not nome:
        return

    novo_id = f"cliente_{len(config['clientes']) + 1}"

    config["clientes"][novo_id] = {
        "nome": nome,
        "script": ""
    }

    salvar_config()
    combo_clientes["values"] = listar_clientes()
    cliente_var.set(f"{nome} ({novo_id})")
    selecionar_cliente()

# ---------------- CAPTURA ---------------- #

def capturar_coordenadas():
    print("Posicione o mouse e pressione F8 para capturar...")

    def esperar_f8():
        keyboard.wait("F8")
        x, y = pa.position()

        linha = f"\n# Coordenada capturada\npa.click({x}, {y})\n"
        editor.insert(tk.END, linha)
        editor.see(tk.END)

        print(f"Coordenadas capturadas: {x}, {y}")

    threading.Thread(target=esperar_f8, daemon=True).start()

# ---------------- INTERFACE ---------------- #

janela = tk.Tk()
janela.title("Macro by Luft")
janela.geometry("350x500")

frame_botoes = tk.Frame(janela)
frame_botoes.pack(fill="x")

btn_play = tk.Button(frame_botoes, text="▶ Play", command=executar_tarefa)
btn_play.pack(side="left", padx=2, pady=2)

btn_stop = tk.Button(frame_botoes, text="■ Stop", command=parar_tarefa)
btn_stop.pack(side="left", padx=2)

btn_salvar = tk.Button(frame_botoes, text="💾 Salvar", command=salvar_codigo)
btn_salvar.pack(side="left", padx=2)

btn_capturar = tk.Button(frame_botoes, text="CDS", command=capturar_coordenadas)
btn_capturar.pack(side="left", padx=2)

btn_novo = tk.Button(frame_botoes, text="➕ Novo", command=novo_cliente)
btn_novo.pack(side="left", padx=2)

cliente_var = tk.StringVar()

combo_clientes = ttk.Combobox(
    frame_botoes,
    textvariable=cliente_var,
    values=listar_clientes(),
    state="readonly",
    width=30
)
combo_clientes.pack(side="left", padx=10)
combo_clientes.bind("<<ComboboxSelected>>", selecionar_cliente)

editor = scrolledtext.ScrolledText(janela, wrap=tk.NONE)
editor.pack(expand=True, fill="both")

# ---------------- HOTKEYS GLOBAIS ---------------- #

keyboard.add_hotkey("F1", stop_global)
keyboard.add_hotkey("F2", pause_resume)

# ---------------- LOOP ---------------- #

janela.mainloop()
