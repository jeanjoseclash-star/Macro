import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog
import threading
import json
import os
import sys
import pyautogui as pa
import time
import keyboard

CONFIG_ARQUIVO = "config.json"

executando = False
cliente_atual_id = None

pa.FAILSAFE = False
pa.PAUSE = 0

cds = False

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
    editor.insert(tk.END, f"click({x}, {y})\n")
    editor.see(tk.END)

    cds = False
    status_var.set(f"Status: CDS Capturadas ({x}, {y})")

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

def esperar_estavel(x, y, tentativas=5, intervalo=0.5):
    for _ in range(tentativas):
        check()
        pa.click(x, y)
        time.sleep(intervalo)

def executar_tarefa():
    global executando

    if executando or not cliente_atual_id:
        return

    executando = True
    btn_play.config(text="▶ Executando", state="disabled")
    status_var.set("Status: Executando")

    codigo = editor.get("1.0", "end-1c")
    qtd = qtd_var.get()

    def run():
        global executando
        try:
            progress["maximum"] = qtd
            progress["value"] = 0

            for i in range(qtd):
                check()
                progress["value"] = i + 1
                status_var.set(f"Status: Executando ({i+1}/{qtd})")

                exec(codigo, {
                    "click": click,
                    "write": write,
                    "press": press,
                    "sleep": sleep,
                    "esperar_estavel": esperar_estavel,

                    "clique": click,
                    "escreva": write,
                    "aperte": press,
                    "espere": sleep
                })

            status_var.set("Status: Finalizado")

        except SystemExit:
            status_var.set("Status: Interrompido")

        except Exception as e:
            status_var.set("Status: Erro")
            print("Erro no script:", e)

        executando = False
        btn_play.config(text="Play", state="normal")

    threading.Thread(target=run, daemon=True).start()

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

def listar_clientes():
    return [d["nome"] for d in config["clientes"].values()]

def selecionar_cliente(event=None):
    global cliente_atual_id
    nome = cliente_var.get()
    for cid, dados in config["clientes"].items():
        if dados["nome"] == nome:
            cliente_atual_id = cid
            editor.delete("1.0", "end")
            editor.insert("1.0", dados["script"])
            break

def novo_cliente():
    nome = simpledialog.askstring("Novo cliente", "Nome do cliente:")
    if not nome:
        return
    cid = f"cliente_{len(config['clientes']) + 1}"
    config["clientes"][cid] = {"nome": nome, "script": ""}
    salvar_config()
    combo["values"] = listar_clientes()
    cliente_var.set(nome)
    selecionar_cliente()

def salvar_codigo():
    if cliente_atual_id:
        config["clientes"][cliente_atual_id]["script"] = editor.get("1.0", "end-1c")
        salvar_config()

def caminho_recurso(nome):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, nome)
    return os.path.join(os.path.abspath("."), nome)

janela = tk.Tk()
janela.title("Macro")
janela.geometry("360x520")

logo = tk.PhotoImage(file=caminho_recurso("assets/icon.png"))
janela.iconphoto(True, logo)

top = tk.Frame(janela)
top.pack(fill="x")

btn_play = tk.Button(top, text="Play", command=executar_tarefa)
btn_play.pack(side="left", padx=1.5)

tk.Button(top, text="Stop", command=stop_global).pack(side="left", padx=1.5)
tk.Button(top, text="Salvar", command=salvar_codigo).pack(side="left", padx=1.5)
tk.Button(top, text="CDS", command=ativar_cds).pack(side="left", padx=1.5)
tk.Button(top, text="Novo", command=novo_cliente).pack(side="left", padx=1.5)

qtd_var = tk.IntVar(value=1)
tk.Label(top, text="Qtd:").pack(side="left", padx=(8, 1.5))
tk.Spinbox(top, from_=1, to=999, width=5, textvariable=qtd_var).pack(side="left")

cliente_var = tk.StringVar()
combo = ttk.Combobox(top, textvariable=cliente_var, values=listar_clientes(), state="readonly", width=15)
combo.pack(side="left", padx=5)
combo.bind("<<ComboboxSelected>>", selecionar_cliente)

status_var = tk.StringVar(value="Status: Parado")
tk.Label(janela, textvariable=status_var).pack(fill="x", padx=5)

progress = ttk.Progressbar(janela, orient="horizontal", mode="determinate")
progress.pack(fill="x", padx=5, pady=5)

editor = scrolledtext.ScrolledText(janela)
editor.pack(expand=True, fill="both")

footer = tk.Frame(janela, bd=1, relief="sunken")
footer.pack(side="bottom", fill="x")

tk.Label(footer, text="© 2025 Macro by Jean", font=("Arial", 8), fg="gray").pack(pady=2)

janela.mainloop()
