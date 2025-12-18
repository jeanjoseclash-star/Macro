import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog
import threading
import json
import os
import sys
import pyautogui as pa
import time
import keyboard
# ---------------- VARIÁVEIS GLOBAIS ---------------- #

CONFIG_ARQUIVO = "config.json"

executando = False
cliente_atual_id = None

pa.FAILSAFE = False
pa.PAUSE = 0

cds = False

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

def ativar_cds():
    global cds
    cds = True
    status_var.set("CDS Ativo - Aperte (F8)")

def confirmar_cds():
    global cds

    if not cds:
        return

    x, y = pa.position()
    linha = f"click({x}, {y})\n"

    editor.insert(tk.END, linha)
    editor.see(tk.END)

    cds = False
    status_var.set(f"Status: CDS Capturadas ({x}, {y})")

# ---------------- CONTROLE ---------------- #

def check():
    if not executando:
        raise SystemExit

def sleep(segundos):
    inicio = time.time()
    while time.time() - inicio < segundos:
        check()
        time.sleep(0.01)

def click(x, y):
    check()
    pa.click(x, y)

def write(texto, interval=0.05):
    check()
    pa.write(texto, interval=interval)

def press(tecla):
    check()
    pa.press(tecla)

# ---------------- EXECUÇÃO ---------------- #

def executar_tarefa():
    global executando

    if executando or not cliente_atual_id:
        return

    executando = True
    btn_play.config(text="▶ Executando", state="disabled")
    status_var.set("Status: Executando")

    codigo = editor.get("1.0", "end-1c")

    def run():
        global executando

        contexto = {
            "click": click,
            "write": write,
            "press": press,
            "sleep": sleep,
            "esperar_estavel": esperar_estavel,
            "qtd": 1
        }

        try:
            exec(codigo, contexto)
            qtd = int(contexto.get("qtd", 1))

            progress["maximum"] = qtd
            progress["value"] = 0

            for i in range(qtd):
                check()
                progress["value"] = i + 1
                status_var.set(f"Status: Executando ({i+1}/{qtd})")
                exec(codigo, contexto)

            status_var.set("Status: Finalizado")

        except SystemExit:
            status_var.set("Status: Interrompido")

        except Exception as e:
            status_var.set("Status: Erro")
            print("Erro no script:", e)

        executando = False
        btn_play.config(text="▶ Play", state="normal")

    threading.Thread(target=run, daemon=True).start()
    
def esperar_estavel(x, y, tentativas=5, intervalo=0.5):
    for _ in range(tentativas):
        check()
        pa.click(x, y)
        time.sleep(intervalo)


# ---------------- STOP GLOBAL ---------------- #

def stop_global():
    global executando
    executando = False
    status_var.set("Status: Parado")

def listener_esc():
    keyboard.on_press_key("esc", lambda e: stop_global())
    keyboard.wait()

threading.Thread(target=listener_esc, daemon=True).start()

def listener_f8():
    keyboard.on_press_key("f8", lambda e: confirmar_cds())
    keyboard.wait()

threading.Thread(target=listener_f8, daemon=True).start()

# ---------------- CLIENTES ---------------- #

def listar_clientes():
    return [f"{d['nome']} ({cid})" for cid, d in config["clientes"].items()]

def selecionar_cliente(event=None):
    global cliente_atual_id
    valor = cliente_var.get()
    if not valor:
        return
    cliente_atual_id = valor.split("(")[-1].replace(")", "")
    editor.delete("1.0", "end")
    editor.insert("1.0", config["clientes"][cliente_atual_id]["script"])

def novo_cliente():
    nome = simpledialog.askstring("Novo cliente", "Nome do cliente:")
    if not nome:
        return
    cid = f"cliente_{len(config['clientes']) + 1}"
    config["clientes"][cid] = {"nome": nome, "script": ""}
    salvar_config()
    combo["values"] = listar_clientes()
    cliente_var.set(f"{nome} ({cid})")
    selecionar_cliente()

def salvar_codigo():
    if cliente_atual_id:
        config["clientes"][cliente_atual_id]["script"] = editor.get("1.0", "end-1c")
        salvar_config()

# ---------------- INTERFACE ---------------- #

def caminho_recurso(nome):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, nome)
    return os.path.join(os.path.abspath("."), nome)

janela = tk.Tk()
janela.title("Macro")
janela.geometry("360x500")

logo = tk.PhotoImage(file=caminho_recurso("assets/icon.png"))
janela.iconphoto(True, logo)


footer = tk.Frame(janela, bd=1, relief="sunken")
footer.pack(side="bottom", fill="x")

footer_label = tk.Label(
    footer,
    text="© 2025 Macro App by Jean",
    font=("Arial", 8),
    fg="gray"
)
footer_label.pack(pady=2)

top = tk.Frame(janela)
top.pack(fill="x")

btn_play = tk.Button(top, text="▶ Play", command=executar_tarefa)
btn_play.pack(side="left", padx=2)

tk.Button(top, text="■ Stop", command=stop_global).pack(side="left", padx=2)
tk.Button(top, text="💾 Salvar", command=salvar_codigo).pack(side="left", padx=2)
tk.Button(top, text="CDS", command=ativar_cds).pack(side="left", padx=2)
tk.Button(top, text="➕ Novo", command=novo_cliente).pack(side="left", padx=2)

cliente_var = tk.StringVar()
combo = ttk.Combobox(
    top,
    textvariable=cliente_var,
    values=listar_clientes(),
    state="readonly",
    width=30
)
combo.pack(side="left", padx=5)
combo.bind("<<ComboboxSelected>>", selecionar_cliente)

status_var = tk.StringVar(value="Status: Parado")
tk.Label(janela, textvariable=status_var).pack(fill="x", padx=5)

progress = ttk.Progressbar(janela, orient="horizontal", mode="determinate")
progress.pack(fill="x", padx=5, pady=5)

editor = scrolledtext.ScrolledText(janela)
editor.pack(expand=True, fill="both")

janela.mainloop()
