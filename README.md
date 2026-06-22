# Guardian — Demo de Agente (LangChain + Gemini)

Micro-agente de portaria construído com LangChain e Gemini, que demonstra o
**loop de tool-calling** de forma enxuta e reproduzível.

Este projeto é a versão didática de um padrão que implementei em produção no
**backend-portaria** (Node.js + TypeScript): lá, o loop de orquestração de
ferramentas é escrito manualmente sobre a API do Gemini via Vertex AI; aqui, o
mesmo comportamento é expresso de forma compacta com o `AgentExecutor` do
LangChain. O objetivo é evidenciar o domínio do conceito — não apenas o uso de
um framework.

## Arquitetura do loop de tool-calling

O agente executa o ciclo clássico de function calling:

1. recebe a mensagem do usuário;
2. decide chamar uma ferramenta (`consultar_morador` / `pre_cadastrar_visitante`);
3. executa a ferramenta e lê o resultado;
4. gera a resposta final com base nesse resultado.

Com `verbose=True` (habilitado por padrão), cada uma dessas etapas é visível no
terminal. No backend-portaria, esse mesmo ciclo é controlado por um laço
explícito `while (stopReason === 'tool_use')` — aqui ele é encapsulado pelo
`AgentExecutor`.

## Mapeamento: este demo ↔ backend-portaria

| LangChain (este demo)            | backend-portaria (produção)                    |
|----------------------------------|------------------------------------------------|
| `@tool`                          | `ToolDefinitions.ts` + `ToolExecutorService`   |
| `ChatGoogleGenerativeAI`         | `GeminiService`                                |
| `ChatPromptTemplate`             | `SystemPromptBuilder.build()`                  |
| `create_tool_calling_agent`      | decisão sobre `stopReason: 'tool_use'`         |
| `AgentExecutor` (`max_iterations`) | laço `while` com `MAX_TOOL_ROUNDS=5`         |

## Autenticação: Gemini API vs. Vertex AI

Em produção, o backend acessa o Gemini via **Vertex AI** com autenticação
keyless (ADC). Neste demo, optei pela **Gemini API (AI Studio)** por ser o
caminho mais direto para execução local — chave gratuita, sem `gcloud` e sem
configuração de ADC. O modelo é o mesmo: `gemini-2.5-flash`.

## Setup (Windows / PowerShell)

```powershell
# 1. Instalar Python 3.12 (se necessário) via winget:
winget install -e --id Python.Python.3.12
#    Feche e reabra o terminal após instalar.

# 2. Criar e ativar um ambiente virtual:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instalar as dependências:
pip install -r requirements.txt

# 4. Configurar a chave da API:
#    - Gere uma chave gratuita em https://aistudio.google.com/apikey
#    - Copie .env.example para .env e cole a chave
copy .env.example .env

# 5. Executar:
python agent.py
```
