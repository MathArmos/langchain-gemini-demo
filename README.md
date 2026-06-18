# Guardian — Demo LangChain + Gemini

Micro-agente de portaria em LangChain para aprender orquestração de agentes.
Faz **automaticamente** o mesmo loop de tool-calling que está escrito à mão no
`ConversationService` do `backend-portaria`.

## Por que a chave da API (e não Vertex AI) neste demo

O backend usa Gemini via **Vertex AI keyless/ADC**. Para um demo de *aprendizado*
rodando hoje, a **Gemini API (AI Studio)** é o caminho mais rápido: chave grátis,
sem `gcloud`, sem ADC. O modelo é o mesmo (`gemini-2.5-flash`).

> Frase para a feira: *"O demo usa a Gemini API; na produção o mesmo modelo roda
> via Vertex AI com autenticação keyless/ADC."*

## Setup (Windows / PowerShell)

```powershell
# 1. Instalar Python 3.12 (se ainda não tiver) — via winget:
winget install -e --id Python.Python.3.12

#    Feche e reabra o terminal depois de instalar.

# 2. Nesta pasta, criar e ativar um ambiente virtual:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instalar as dependências:
pip install -r requirements.txt

# 4. Configurar a chave:
#    - Pegue uma chave grátis: https://aistudio.google.com/apikey
#    - Copie .env.example para .env e cole a chave
copy .env.example .env
#    (edite o .env e cole a chave)

# 5. Rodar:
python agent.py
```

## O que observar

Rode com `verbose=True` (já está ligado) e veja no terminal o agente:
1. receber sua mensagem,
2. decidir chamar uma tool (`consultar_morador` / `pre_cadastrar_visitante`),
3. executar a tool e ler o resultado,
4. e só então gerar a resposta final.

Esse é o loop que você escreveu na mão em `while (stopReason === 'tool_use')`.

## Mapa LangChain → seu backend

| LangChain (aqui)            | backend-portaria                          |
|-----------------------------|-------------------------------------------|
| `@tool`                     | `ToolDefinitions.ts` + `ToolExecutorService` |
| `ChatGoogleGenerativeAI`    | `GeminiService`                           |
| `ChatPromptTemplate`        | `SystemPromptBuilder.build()`             |
| `create_tool_calling_agent` | decisão de `stopReason: 'tool_use'`       |
| `AgentExecutor` (max_iterations) | loop `while` com `MAX_TOOL_ROUNDS=5` |
