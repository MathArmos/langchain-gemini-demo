"""
Guardian — Demo LangChain + Gemini
===================================

Objetivo de aprendizado: ver o LangChain fazer AUTOMATICAMENTE o mesmo loop de
tool-calling que você escreveu À MÃO no `ConversationService` do backend-portaria.

Mapa mental (o que cada parte equivale no SEU código):

  LangChain (aqui)                       Seu backend (backend-portaria)
  --------------------------------       ------------------------------------------
  @tool / lista `tools`                  AGENT_TOOLS + ToolExecutorService
  ChatGoogleGenerativeAI                 GeminiService (chamada ao Gemini)
  ChatPromptTemplate (system)            SystemPromptBuilder.build()
  create_tool_calling_agent              a lógica que decide "stopReason: tool_use"
  AgentExecutor (max_iterations=5)       seu loop `while (stopReason === 'tool_use')`
                                         com MAX_TOOL_ROUNDS = 5
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()

# ---------------------------------------------------------------------------
# 1. TOOLS — funções que o agente pode chamar.
#    O decorador @tool transforma a função numa "ferramenta" que o LangChain
#    expõe ao modelo. A DOCSTRING vira a descrição que o modelo lê para decidir
#    quando usar — exatamente como o `description` no seu ToolDefinitions.ts.
# ---------------------------------------------------------------------------

@tool
def consultar_morador(nome: str) -> str:
    """Consulta o cadastro de um morador pelo primeiro nome. Retorna apartamento e status."""
    base = {
        "matheus": "Apartamento 101, Bloco A — cadastro ativo",
        "ana": "Apartamento 202, Bloco A — cadastro ativo",
    }
    return base.get(nome.lower().strip(), "Morador não encontrado.")


@tool
def pre_cadastrar_visitante(morador: str, visitante: str) -> str:
    """Pré-cadastra um visitante para um morador. Retorna o protocolo gerado.

    NÃO libera entrada nem abre portão — apenas registra o cadastro prévio,
    igual à regra do Guardian real.
    """
    return f"Visitante '{visitante}' pré-cadastrado para {morador}. Protocolo VIS-2026-0042."


tools = [consultar_morador, pre_cadastrar_visitante]

# ---------------------------------------------------------------------------
# 2. LLM — mesmo modelo do seu backend (gemini-2.5-flash).
#    Diferença: aqui usamos a Gemini API (chave do AI Studio). No backend, o
#    mesmo modelo é acessado via Vertex AI keyless/ADC. Saber explicar essa
#    diferença na feira é um ponto a seu favor.
# ---------------------------------------------------------------------------

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# ---------------------------------------------------------------------------
# 3. PROMPT — o "system prompt" + os placeholders que o agente preenche.
#    - chat_history: memória da conversa
#    - agent_scratchpad: onde o agente "anota" as chamadas de tool e os
#      resultados durante o loop (obrigatório para tool-calling agents)
# ---------------------------------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é o Guardian, porteiro virtual de um condomínio, no WhatsApp. "
        "Responda em português, de forma curta e cordial. Use as ferramentas "
        "disponíveis para consultar moradores e pré-cadastrar visitantes. "
        "Nunca invente dados: se não souber, pergunte ou consulte a ferramenta.",
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# ---------------------------------------------------------------------------
# 4. AGENT + EXECUTOR — o coração.
#    create_tool_calling_agent monta a "cabeça" que decide qual tool chamar.
#    AgentExecutor roda o LOOP: chama o modelo -> executa a tool -> devolve o
#    resultado ao modelo -> repete até o modelo dar a resposta final.
#    `max_iterations=5` é o seu MAX_TOOL_ROUNDS. `verbose=True` imprime cada
#    passo do raciocínio/loop no terminal — ótimo para ENTENDER o que acontece.
# ---------------------------------------------------------------------------

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=5)


def main() -> None:
    print("Guardian (demo LangChain) — digite 'sair' para encerrar.\n")
    print("Experimente: 'qual o apartamento do Matheus?' ou")
    print("             'deixa a visita do João autorizada pra Ana'\n")

    chat_history: list = []

    while True:
        try:
            msg = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if msg.lower() in {"sair", "exit", "quit", ""}:
            break

        result = executor.invoke({"input": msg, "chat_history": chat_history})
        output = result["output"]
        print(f"\nGuardian: {output}\n")

        # Acumula memória da conversa (turno do usuário + turno do agente)
        from langchain_core.messages import HumanMessage, AIMessage
        chat_history.append(HumanMessage(content=msg))
        chat_history.append(AIMessage(content=output))


if __name__ == "__main__":
    main()
