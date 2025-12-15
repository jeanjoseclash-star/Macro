# Macro
Macro desenvolvido em python para auxiliar o adm da Luft 

# Macro by Luft

Aplicação desktop em **Python + Tkinter** para criação e execução de **macros multi‑cliente**, com suporte a captura de coordenadas, hotkeys globais e persistência em um único arquivo `config.json`.

O projeto foi desenhado para cenários onde múltiplos clientes/janelas exigem **macros diferentes**, mantendo tudo organizado e controlável por interface gráfica.

---

## 📌 Funcionalidades

* 📂 **Gerenciamento de múltiplos clientes**

  * Cada cliente possui seu próprio script de macro
  * Todos os dados são armazenados em **um único `config.json`**

* ▶️ **Execução de macros**

* ⏹️ **Stop global (F1)**

* ⏸️ **Pause / Resume (F2)**

* 📍 **Captura de coordenadas do mouse (F8)**

* 💾 Salvamento automático por cliente

* 🔄 Execução segura com controle de threads

---

## 🧠 Conceito de Funcionamento

* A interface permite selecionar um **cliente** via Combobox

* Cada cliente possui:

  * `id`
  * `nome`
  * `script` (macro em Python)

* O script é executado dinamicamente via `exec()`

* O controle de execução é feito por flags globais:

  * `executando`
  * `pausado`

---

## ⌨️ Hotkeys Globais

| Tecla  | Função                                         |
| ------ | ---------------------------------------------- |
| **F1** | Stop global (interrompe imediatamente o macro) |
| **F2** | Pause / Resume do macro                        |
| **F8** | Captura coordenadas do mouse                   |

> As hotkeys funcionam **mesmo fora da janela do programa**.

---

## 📁 Estrutura do Projeto

```
macro/
│
├── main.py            # Código principal
├── config.json        # Configuração e scripts dos clientes
└── README.md          # Documentação
```

---

## 🧾 Estrutura do config.json

```json
{
  "clientes": {
    "cliente_1": {
      "nome": "Cliente A",
      "script": "pa.click(500, 300)\nsleep_seguro(2)"
    },
    "cliente_2": {
      "nome": "Cliente B",
      "script": "pa.click(800, 450)"
    }
  }
}
```

---

## ▶️ Como Executar

1. Instale o Python 3.10+
2. Instale as dependências:

```bash
pip install pyautogui keyboard
```

3. Execute o programa:

```bash
python main.py
```

---

## ✍️ Como Criar um Macro

### ❌ NÃO use

```python
time.sleep(2)
```

### ✅ USE

```python
sleep_seguro(2)
```

### Exemplo completo

```python
pa.click(700, 400)
sleep_seguro(2)

esperar_se_pausado()
pa.click(750, 450)
sleep_seguro(1)
```

Isso garante:

* Resposta imediata ao **STOP (F1)**
* Funcionamento correto do **PAUSE (F2)**

---

## 📍 Captura de Coordenadas

1. Clique em **CDS**
2. Posicione o mouse no local desejado
3. Pressione **F8**
4. O código será inserido automaticamente no editor

```python
pa.click(x, y)
```

---

## ⚠️ Observações Importantes

* O programa executa código Python dinamicamente (`exec`)
* **Use apenas scripts confiáveis**
* Evite loops infinitos sem `sleep_seguro()`


---

## 👤 Autor

Desenvolvido por **Jean Filho**
Projeto focado em automação multi‑cliente com controle fino de execução.

---

## 📜 Licença

Uso livre para fins educacionais e pessoais.
