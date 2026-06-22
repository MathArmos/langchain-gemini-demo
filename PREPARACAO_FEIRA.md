# Preparação para a Feira de Trabalho — 23/06

> Plano de treino até a feira. Formato do evento: **online, um meet por empresa,
> Q&A aberto em grupo** (vários candidatos, perguntas aleatórias) — não é entrevista 1:1.

---

## 🎯 As vagas (3 empresas, 4 vagas)

| Empresa | Vaga | Prioridade |
|---------|------|-----------|
| **IPNET by Vivo** | Analista de IA Jr | ⭐ Alvo nº1 (melhor fit) |
| **Be Solution** | IA + Dados + GCP | ✅ Feira |
| **CALRIZ Sistemas** | SRE Jr GCP | ✅ Feira (exclusiva) |
| **IPNET by Vivo** | Dev FullStack Jr/Pleno | ⚪ Plano B (não é da feira) |

---

## 💪 Meu maior trunfo

Tenho um **agente conversacional LLM em produção na GCP**:
- Gemini 2.5 Flash via **Vertex AI** (keyless/ADC)
- **function calling** + **structured outputs**
- defesa contra **prompt injection**
- atende no **WhatsApp** para uma empresa de portaria remota

Quase nenhum júnior chega na feira com isso. **É a carta na manga.**

---

## 📚 O que treinar (esforço × impacto)

### 🥇 Vocabulário Vertex AI (~30 min) — só ensaiar, não hands-on
Saber o que é cada produto e onde meu trabalho se encaixa:

| Termo | O que é (1 linha) | Minha conexão |
|-------|-------------------|---------------|
| **Vertex AI** | Plataforma de ML/IA gerenciada da GCP | Já uso pra servir o Gemini |
| **Model Garden** | Catálogo de modelos (Gemini, Llama, Claude...) | "Escolhi Gemini 2.5 Flash por custo/latência em pt-BR" |
| **Agent Builder** (ex-"Search and Conversation") | Construtor gerenciado de agentes/RAG, low-code | "Fiz custom pra ter controle; conheço o caminho gerenciado" |
| **Grounding / RAG no Vertex** | RAG vetorial gerenciado | "No meu caso uso injeção estática no prompt, não RAG vetorial" |
| **Function Calling / Structured Output** | LLM chama funções / saída JSON forçada | **Uso os dois em produção** (ponto mais forte) |
| **ADC / keyless** | Autenticação sem chave | Meu backend usa — segurança real |

### 🥈 LangChain — ✅ FEITO
Demo rodando neste repo. Cobre o gap "LangChain" da vaga IPNET-IA.
Saber explicar em 30s as 4 peças (ver seção "O demo" abaixo).

### 🥉 Python brushup leve (~1h)
Já programo (JS/TS). O `agent.py` já é prática. Só destravar sintaxe.

### 🏅 Ensaiar SRE/observability (~1h) — NÃO estudar mais, só falar em voz alta
Já estudei a fundo (SLI/SLO/SLA, error budget, alerting). Decorar a frase:
> "Error budget = 100% − SLO, e o alerta dispara no SLO, não no SLA, pra ter
> tempo de reagir antes de violar o contrato."

### ✂️ Cortar (baixo ROI até o dia 23)
Áudio/mídia no agente, evaluator, agente juiz, ML preditivo, BigQuery profundo, PHP.
→ Viram **roadmap falado**, não estudo. (LLMOps citado vale mais que construído.)

---

## 🤖 O demo (saber explicar em 30s)

Micro-agente de portaria que faz **automaticamente** o loop de tool-calling que
escrevi à mão no `ConversationService` do backend. As 4 peças:

1. **Tools** (`@tool`) — funções que o LLM pode chamar (= `ToolDefinitions` + `ToolExecutorService`)
2. **LLM** (`ChatGoogleGenerativeAI`) — `gemini-2.5-flash` (= `GeminiService`)
3. **Prompt** (`ChatPromptTemplate`) — system prompt + placeholders (= `SystemPromptBuilder`)
4. **AgentExecutor** (`max_iterations=5`) — o loop (= meu `while (stopReason === 'tool_use')` com `MAX_TOOL_ROUNDS`)

**Repo público (portfólio):** github.com/MathArmos/langchain-gemini-demo

### Como rodar / testar
```powershell
cd c:\Users\mathx\OneDrive\Desktop\Nodejs\langchain-gemini-demo
.\.venv\Scripts\python.exe agent.py
```
Testes: `qual o apartamento do Matheus?` (chama tool) · `bom dia` (não chama tool) ·
`e o da Ana?` (usa memória) · `qual o apartamento do Pedro?` (lida com "não encontrado").

---

## 🎤 Estratégia na feira (Q&A online em grupo)

### Meta
Não dá pra fazer pitch — dá pra fazer **uma pergunta**. Objetivos:
1. Ser **lembrado** pelo recrutador.
2. **Coletar info** pra decidir onde aplicar.
3. Garantir o **próximo passo** (contato/como se candidatar).

### A técnica: pergunta que também é pitch
**[credencial curta] + [pergunta técnica específica]**
> "Tenho um agente LLM **em produção na GCP** com Gemini via Vertex AI, function
> calling e structured outputs. Vocês usam orquestração custom ou **Agent Builder**?
> E como fazem **avaliação/observabilidade dos modelos** em produção?"

### Antes do meet
- [ ] Nome completo visível ("Matheus Ramos — Dev")
- [ ] Câmera ligada, fundo neutro, áudio testado, entrar 5 min antes
- [ ] Links prontos pra colar no chat: GitHub do demo + LinkedIn
- [ ] 2 perguntas por empresa num bloco de notas

### Durante
- Ouvir 2-3 min antes de perguntar (calibrar), mas não deixar pro fim
- Falar: nome + credencial curta + pergunta. Direto, sem monólogo.
- Usar o **chat** como 2º canal: "Complementando — meu agente está aqui: [link]"
- Se não falar no mic, fazer a pergunta no chat (mesma estrutura)

### Perguntas-matadoras por empresa
- **IPNET (IA):** "Orquestração custom ou Agent Builder? Como avaliam modelos em produção?" / "LangChain/LangGraph ou próprio? Prompt engineering vs fine-tuning?"
- **Be Solution:** "Separam IA aplicada de MLOps/ML preditivo em squads? Como tratam governança/LGPD em GenAI?"
- **CALRIZ (SRE):** "Estou tirando a ACE e estudei SLI/SLO/SLA e error budget. IaC é Terraform puro ou Config Connector? Como é o ciclo de error budget no dia a dia?"
- **IPNET (FullStack):** "Como o time usa IA no dev e garante qualidade/revisão?"

### Fechamento (não esquecer)
> "Qual o melhor caminho pra eu me candidatar? Posso conectar no LinkedIn e mandar meu GitHub?"

Depois: conectar no LinkedIn citando a pergunta que fiz ("fui eu que perguntei sobre avaliação de modelos").

### ❌ Não fazer
- Perguntas genéricas ("quais as vagas?", "tem home office?", "qual o salário?")
- Monólogo sem pergunta
- Ler a credencial de forma robótica (decorar o *fluxo*, não as palavras)

---

## ✅ Checklist final (dias até 23/06)

- [ ] Ensaiar as 4 perguntas-pitch em voz alta (natural, não decorado)
- [ ] 30 min de vocabulário Vertex AI (tabela acima)
- [ ] Explicar o `agent.py` em 30s (as 4 peças + paralelo com o backend)
- [ ] Frase do error budget na ponta da língua (CALRIZ)
- [ ] Links (GitHub + LinkedIn) salvos pra colar no chat
- [ ] Setup do meet testado (câmera/áudio/fundo/nome)
