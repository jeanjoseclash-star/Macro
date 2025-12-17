# Macro

## 1. Visão Geral

O **Macro** é uma aplicação desktop desenvolvida em Python, com interface gráfica baseada em **Tkinter**, destinada à automação de tarefas repetitivas por meio da simulação de ações humanas (mouse e teclado).

O software foi projetado como **ferramenta de apoio operacional**, sem integração direta com sistemas corporativos, banco de dados ou APIs internas, garantindo baixo risco técnico e fácil auditoria.

---

## 2. Objetivo do Sistema

* Automatizar tarefas manuais repetitivas
* Reduzir tempo operacional
* Minimizar erros humanos
* Padronizar execuções por cliente/processo
* Permitir controle total da execução

---

## 3. Público-Alvo

* Usuários operacionais
* Supervisores de processo
* Equipe de Tecnologia da Informação (TI)

---

## 4. Funcionalidades Principais

* Interface gráfica simples e intuitiva
* Cadastro e seleção de múltiplos clientes
* Scripts independentes por cliente
* Execução controlada por quantidade de ciclos (`qtd`)
* Barra de progresso visual
* Salvamento automático de scripts
* Interrupção manual por botão
* Interrupção global imediata via tecla **ESC**
* Persistência de dados em arquivo JSON
* Distribuição via executável e instalador

---

## 5. Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter** – Interface gráfica
* **PyAutoGUI** – Automação de mouse e teclado
* **Keyboard** – Captura global de teclas
* **JSON** – Persistência de configuração
* **PyInstaller** – Geração de executável
* **Inno Setup** – Criação do instalador

---

## 6. Arquitetura do Sistema

### 6.1 Arquitetura Geral

O sistema opera inteiramente em **modo local**, seguindo o fluxo:

1. Inicialização da interface gráfica
2. Leitura do arquivo `config.json`
3. Seleção do cliente
4. Execução do script no contexto controlado
5. Monitoramento e interrupção sob demanda

Não há comunicação externa, rede ou persistência fora do diretório local.

---

## 7. Estrutura de Diretórios

```
/Macro
 ├─ main.py              # Código-fonte principal
 ├─ config.json          # Configuração e scripts dos clientes
 ├─ assets/
 │   └─ icone.ico        # Ícone da aplicação
 ├─ dist/
 │   └─ Macro.exe        # Executável final
 └─ installer/
     └─ Setup.exe        # Instalador
```

---

## 8. Arquivo de Configuração (`config.json`)

### 8.1 Finalidade

Armazenar, de forma persistente:

* Lista de clientes
* Scripts associados a cada cliente

### 8.2 Estrutura

```json
{
  "clientes": {
    "cliente_1": {
      "nome": "Cliente Exemplo",
      "script": "qtd = 3\nclick(100, 200)\nsleep(1)"
    }
  }
}
```

### 8.3 Observações Técnicas

* Formato JSON legível
* Pode ser auditado e versionado
* Não contém credenciais
* Não executa código automaticamente sem ação do usuário

---

## 9. Linguagem de Script Interna

Os scripts são escritos em Python simplificado, executados em **contexto controlado**.

### 9.1 Funções Disponíveis

| Função            | Descrição                      |
| ----------------- | ------------------------------ |
| `click(x, y)`     | Clique do mouse na posição X/Y |
| `write(texto)`    | Digitação de texto             |
| `press(tecla)`    | Pressionar tecla               |
| `sleep(segundos)` | Pausa controlada               |
| `qtd = N`         | Número de execuções            |

### 9.2 Exemplo

```python
qtd = 3

click(590, 423)
sleep(1)

press("enter")
write("Funcionando perfeitamente")
```

---

## 10. Controle de Execução

* Execução ocorre em **thread separada**, evitando travamento da interface
* Botão **Stop** interrompe a execução
* Tecla **ESC** encerra imediatamente qualquer automação
* Sistema utiliza verificação contínua (`check()`) para parada segura

---

## 11. Segurança e Conformidade

### 11.1 O que o sistema NÃO faz

* Não acessa banco de dados
* Não coleta dados pessoais
* Não se conecta à internet
* Não injeta código em aplicações
* Não modifica arquivos do sistema

### 11.2 O que o sistema faz

* Opera apenas sob comando
* Pode ser interrompido a qualquer momento

---

## 12. Distribuição

* Executável gerado via **PyInstaller**
* Instalador criado com **Inno Setup**
* Ícone e arquivos incluídos no pacote
* Instalação padrão sem privilégios administrativos elevados

---

## 13. Manutenção e Suporte

### 13.1 Atualizações

* Atualizações podem ser feitas substituindo o executável
* Scripts permanecem preservados no `config.json`

### 13.2 Auditoria

* Código-fonte disponível
* Scripts legíveis
* Comportamento previsível

---

## 14. Possíveis Evoluções Futuras

* Atualizações automáticas

---

## 15. Autor

**Jean Filho**

Projeto desenvolvido para automação operacional e apresentação interna.

---

## 16. Observação Final

Este sistema é uma **ferramenta de apoio** e deve ser utilizado conforme as políticas internas de TI.
