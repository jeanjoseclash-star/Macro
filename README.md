Macro – Automação com Interface Gráfica (Tkinter)

Aplicação desktop em Python para criação, gerenciamento e execução de macros de automação de teclado e mouse, com interface gráfica simples, suporte a múltiplos clientes e persistência de scripts.


---

Visão Geral

O Macro é uma ferramenta voltada à automação de tarefas repetitivas em ambientes desktop. Utiliza Tkinter para a interface gráfica, PyAutoGUI para automação de mouse/teclado e keyboard para atalhos globais. Cada cliente possui seu próprio script, armazenado localmente em um arquivo JSON.

Principais características:

Editor integrado para scripts de automação

Execução controlada (Play / Stop)

Captura de coordenadas de tela (CDS)

Suporte a múltiplos clientes

Barra de progresso e status de execução

Interrupção global via tecla ESC



---

Requisitos

Sistema operacional Windows 7 ou superior


Bibliotecas Python

pyautogui

keyboard

As bibliotecas abaixo fazem parte da biblioteca padrão do Python:

tkinter

threading

json

os

sys

time



---

Estrutura de Arquivos

.
├── main.py            # Arquivo principal da aplicação
├── config.json        # Armazena clientes e scripts (gerado automaticamente)
└── README.md          # Documentação


---

Como Executar

Abri o Executavel Macro.exe

Ao iniciar:

1. Crie um novo cliente clicando em Novo


2. Selecione o cliente no combo box


3. Escreva ou cole o script no editor


4. Clique em Salvar


5. Execute com Play




---

Interface e Controles

Botões

▶ Play: Executa o script do cliente selecionado

■ Stop: Interrompe imediatamente a execução

Salvar: Salva o script atual no config.json

CDS: Ativa o modo de captura de coordenadas do mouse

Novo: Cria um novo cliente


Atalhos Globais

ESC → Interrompe a execução do script

F8 → Confirma a captura de coordenadas (CDS)



---

Modo CDS (Captura de Coordenadas)

O modo CDS facilita a obtenção de coordenadas da tela:

1. Clique em CDS


2. Posicione o mouse no local desejado


3. Pressione F8


4. A linha click(x, y) será inserida automaticamente no editor




---

Linguagem de Script (API Disponível)

Os scripts são escritos em Python e executados via exec, com acesso controlado às funções abaixo:

Funções

click(x, y)            # Clique do mouse na posição (x, y)
write(texto, interval=0.05)  # Digita um texto
press(tecla)           # Pressiona uma tecla
sleep(segundos)        # Aguarda respeitando o controle de parada
esperar_estavel(x, y, tentativas=5, intervalo=0.5)  # Clique repetido

Variável Especial

qtd = 5  # Quantidade de repetições do script

Se qtd não for definida, o script será executado apenas uma vez.


---

Exemplo de Script

qtd = 3

click(500, 300)
sleep(1)
write("Olá mundo")
press("enter")


---

Persistência de Dados

Os dados são armazenados em config.json no formato:

{
  "clientes": {
    "cliente_1": {
      "nome": "Cliente Exemplo",
      "script": "click(100, 200)"
    }
  }
}


---

Encerramento Seguro

A execução é monitorada por uma flag interna (executando)

Qualquer chamada respeita a função check()

Pressionar ESC encerra imediatamente a macro em execução



---

Observações Importantes

O pyautogui.FAILSAFE está desativado

Utilize com cautela, especialmente em ambientes produtivos

Não execute macros sem supervisão



---

Compilação para Executável (Opcional)

Recomendado o uso do PyInstaller:

pip install pyinstaller
pyinstaller --onefile --noconsole main.py

O executável será gerado na pasta dist/.


---

Autor

Jean
© 2025 – Macro
