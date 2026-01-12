```markdown
# Macro Automática Inteligente – Python

Este projeto implementa uma macro avançada em Python com captura de pixel, detecção de mudança de cor, clique automatizado, teclado virtual, validação de janela ativa e execução de scripts personalizados linha a linha.  
Voltado para automação de processos internos, sistemas de trabalho e rotinas repetitivas.

---

## Funcionalidades Principais

- Captura de coordenadas de tela com tecla **F8**
- Captura da cor de um pixel
- Execução de script personalizado linha a linha
- Funções de automação integradas:
  - `click(x, y)`
  - `write("texto")`
  - `press("tecla")`
  - `sleep(segundos)`
  - `wait(x, y)` — aguarda pixel estabilizar
  - `wait_color(x, y)` — aguarda pixel mudar de cor
  - `checar(px, py, cx, cy)` — clica e valida mudança
- Controle de foco:
  - Automação pausa/para caso a janela ativa mude
- Editor com destaque da linha executada
- Multi-cliente com scripts salvos automaticamente
- Logs detalhados de execução
- Botão stop global (ESC)

---

## Estrutura do Projeto

```

main.py
config.json
macro.exe


## Criando um Script de Automação

Você pode escrever comandos diretamente no editor da interface.

### Funções disponíveis

| Função                   | Descrição                 |
| ------------------------ | ------------------------- |
| `click(x, y)`            | Clique exato na posição   |
| `write("texto")`         | Digitação simulada        |
| `press("enter")`         | Tecla única               |
| `sleep(2)`               | Pausa em segundos         |
| `wait(x, y)`             | Aguarda pixel estabilizar |
| `wait_color(x, y)`       | Aguarda pixel mudar       |
| `checar(px, py, cx, cy)` | Clica e verifica cor      |

---

## Exemplo de Script Completo

```python
wait_color(500, 320)
click(800, 450)
sleep(1)
write("Acesso Liberado")
press("enter")
checar(300, 200, 350, 240)
sleep(0.5)
click(900, 600)
```

---

## Capturando Coordenadas

Use os botões da interface para iniciar o modo de captura:

* **Captura Coordenada (CDS)**
* **Wait**
* **Checar**
* **Wait Color**

Depois pressione **F8** para confirmar o pixel.

---

## Segurança – Validação da Janela

O sistema:

* identifica o título da janela ativa
* compara com a janela alvo escolhida
* aborta a automação se a janela for trocada
* evita erros e automações fora de contexto

---

## Salvamento Automático

Todos os scripts e clientes são armazenados em:

```
config.json
```

Estrutura:

```json
{
  "clientes": {
    "cliente1": {
      "nome": "Exemplo",
      "script": "click(200,200)\nwait(300,300)"
    }
  }
}
```

---

## Interromper Execução

Pressione:

```
ESC
```

Isto cancela imediatamente qualquer automação em andamento, mesmo dentro de loops ou waits.

---

## Licença

Uso livre para estudos, automação interna e modificação pessoal.
Revenda proibida sem autorização.

---

## Autor

Desenvolvido por Jean – 2026
Automação inteligente com controle de janela e análise de pixel.

---

```
