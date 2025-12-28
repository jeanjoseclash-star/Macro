# Macro – Automação de Teclado e Mouse com Interface Gráfica

Aplicação desktop desenvolvida em **Python** com **Tkinter**, voltada para automação de tarefas repetitivas envolvendo **mouse**, **teclado** e **espera inteligente por carregamento de tela**.  
O sistema permite criar, salvar e executar scripts personalizados de macro, com múltiplos clientes, logs detalhados e destaque visual da linha em execução.

---

## 📌 Principais Funcionalidades

- Interface gráfica simples e funcional (Tkinter)
- Execução de macros com:
  - Cliques de mouse
  - Escrita automática de texto
  - Pressionamento de teclas
  - Espera inteligente por estabilização de pixel (`wait`)
- Sistema de **WAIT inteligente** (ideal para páginas, vídeos e carregamentos)
- Destaque visual da linha em execução no editor
- Execução repetida do script (loop configurável)
- Salvamento de scripts por cliente
- Logs detalhados de execução
- Interrupção global por tecla **ESC**
- Captura rápida de coordenadas por tecla **F8**
- Compatível com versão empacotada `.exe` (PyInstaller)

---

## 🖥️ Interface

A interface é composta por:
- Editor de script
- Barra de progresso
- Status em tempo real
- Botões de controle (Play, Stop, CDS, Wait, Salvar, Novo cliente)

Cada linha executada é destacada visualmente durante a execução do macro.

---

## 🧠 Conceito do WAIT Inteligente

O comando `wait(x, y)` **não depende de cor fixa**.

Ele funciona da seguinte forma:
- Monitora o pixel na posição informada
- Aguarda até que a cor **estabilize por vários ciclos consecutivos**
- Só libera a execução quando o pixel parar de variar

Esse comportamento é ideal para:
- Carregamento de páginas
- Vídeos (ex: YouTube)
- Telas de loading
- Elementos dinâmicos

---

## ✍️ Linguagem de Script

O editor aceita comandos simples, linha por linha.

### Comandos disponíveis

```text
click(x, y)
write("texto")
press("enter")
sleep(segundos)
wait(x, y)
Também disponíveis em português:

text
Copiar código
clique(x, y)
escreva("texto")
aperte("enter")
espere(segundos)
aguarde(x, y)
Exemplo de Script
python
Copiar código
click(500, 300)
sleep(1)
write("youtube.com")
press("enter")
wait(134, 100)
click(800, 120)
🎯 Captura Rápida de Ações
Capturar clique (CDS)
Clique no botão CDS

Posicione o mouse

Pressione F8

A linha click(x, y) será inserida automaticamente

Capturar WAIT
Clique no botão Wait

Posicione o mouse sobre o ponto desejado

Pressione F8

A linha wait(x, y) será inserida no editor

⌨️ Teclas Globais
Tecla	Função
F8	Confirmar CDS ou WAIT
ESC	Interromper execução do macro

📂 Estrutura do Projeto
text
Copiar código
Macro/
├── main.py
├── config.json
├── assets/
│   └── icon.png
├── dist/
│   └── Macro.exe
└── README.md
⚙️ Tecnologias Utilizadas
Python 3.8 (32-bit)

Tkinter

PyAutoGUI

Keyboard

PyInstaller

📦 Geração do Executável (.exe)
O projeto pode ser empacotado em um único executável usando PyInstaller.

Comando utilizado:
powershell
Copiar código
pyinstaller --onefile --noconsole --name Macro --icon assets/icon.png --add-data "assets;assets" main.py
O executável será gerado em:

text
Copiar código
dist/Macro.exe
⚠️ Observações Importantes
O macro interage diretamente com mouse e teclado do sistema

Utilize com cuidado durante a execução

Recomenda-se testar scripts antes de uso prolongado

Alguns antivírus podem gerar falso positivo em automações

👤 Autor
Jean Developer
Projeto desenvolvido para automação de tarefas repetitivas com foco em confiabilidade, controle visual e estabilidade.

© 2025 – Todos os direitos reservados
