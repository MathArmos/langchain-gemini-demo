# MATHEUS RAMOS

### Desenvolvedor — Foco em IA Generativa e Google Cloud
**Agente LLM conversacional rodando na Google Cloud**

---

**Contato**
📱 (44) 99871-8587 · ✉️ mathx1celular19@gmail.com
🔗 linkedin.com/in/matheus-ramos-322644212 · 💻 github.com/MathArmos

---

## Perfil

Desenvolvedor com pouco mais de 1 ano de experiência e **mentalidade de dono** — cuido do produto como se fosse meu. Construí e mantenho um **agente conversacional LLM implantado na Google Cloud** — atualmente em **treinamento supervisionado com o setor de qualidade** antes de atender os condomínios — usando Vertex AI (Gemini), function calling, structured outputs e padrões de confiabilidade (circuit breakers, retry, rate limiting). Foco em IA generativa aplicada, integrações em nuvem e desenvolvimento assistido por IA.

---

## Competências

**IA Generativa & LLMs**
- Google **Gemini 2.5 Flash** via **Vertex AI** (keyless/ADC, região `southamerica-east1`)
- **Function calling** e **Structured Outputs** (JSON com schema) em produção
- **Engenharia de prompt** e defesa contra **prompt injection**
- Orquestração de agentes (loop de tool-calling) · **LangChain** (demo público)
- Observabilidade de modelos (**LLM tracing** LGPD-safe)

**Google Cloud & Infraestrutura**
- GCP · Vertex AI · **IAM / Service Accounts** · autenticação **keyless (ADC)**
- Confiabilidade: **circuit breakers**, **retry com backoff**, **rate limiting** (Redis)
- Observabilidade e logging estruturado · fail-fast config
- Redis + **BullMQ** (filas assíncronas, workers, deduplicação)

**Desenvolvimento**
- **TypeScript**, **Node.js**, Express · PostgreSQL + **Prisma** · Yup
- APIs REST · arquitetura modular **CSMR** · multi-tenant
- **Context Engineering, Skills, Agents e MCPs** (desenvolvimento assistido por IA)

---

## Experiência

### Guardian — Porteiro Virtual Inteligente (Agente LLM)
**Projeto autoral · Implantado na Google Cloud (em treinamento supervisionado)**

Agente conversacional que atua como **porteiro virtual via WhatsApp** para uma empresa de portaria remota, **projetado para atender múltiplos condomínios** a partir de um único número central, com meta de **85% de resolução automática**.

> **Status:** implantado e rodando na **Google Cloud**, atualmente em **treinamento supervisionado com o setor de qualidade** — rollout gradual antes de entrar em produção plena nos condomínios.

**IA & Google Cloud**
- Gemini 2.5 Flash servido via **Vertex AI**, autenticação **keyless/ADC** (sem chave exposta), região `southamerica-east1`
- **Function calling** para pré-cadastro de visitantes, consulta de moradores/dispositivos e abertura de solicitações operacionais
- **Structured Outputs** para garantir respostas em JSON parseável no dispatcher de mensagens
- **Defesa contra prompt injection** (delimitação de contexto) validada em auditoria de segurança
- **LLM tracing** (LGPD-safe) para observabilidade do modelo em produção

**Confiabilidade / SRE**
- **Circuit breakers** para Vertex AI, Meta Cloud API e integrações externas — evita falha em cascata
- **Retry com backoff exponencial** (3 tentativas) nas chamadas externas
- **Rate limiting por telefone** (sliding window em Redis)
- Validação **fail-fast** de variáveis de ambiente no startup

**Arquitetura & Backend**
- Node.js + TypeScript + Express no padrão **CSMR** (Controller, Service, Models, Repositories) com factories por domínio
- PostgreSQL + **Prisma** + Yup · **multi-tenant** (isolamento por `tenantId` em todas as queries)
- **Redis + BullMQ**: fila assíncrona, deduplicação e workers dedicados
- Integração **Meta Cloud API** (WhatsApp) via webhook com validação **HMAC**
- **Signed URLs keyless** via `iam.signBlob`

**Segurança & LGPD**
- Autenticação **JWT role-based**, bcrypt, rate limiters
- Auditorias de segurança **OWASP Top 10** por módulo
- Retenção de dados **LGPD** com fila de expiração automática

**Testes:** suíte Jest cobrindo HMAC, circuit breaker, rate limit e isolamento de tenant — sem dependências externas.

**Stack:** Node.js · TypeScript · Express · Vertex AI (Gemini 2.5 Flash) · PostgreSQL · Prisma · Redis · BullMQ · Meta Cloud API · Google Cloud

---

## Formação

- **Engenharia de Software** — UniCesumar *(cursando)*
- Curso de **Node.js** — ONP
- Curso de **JavaScript** — ONP
- Workshop **Desenvolvimento assistido por IA avançado** — Tech Leads Club *(ministrado por Waldemar Neto)*
- **Análise e Design de Software** — ACCION Sistemas *(presencial)*
- Workshop **UX/UI Design** — Kacio Felipe
- **Inglês** *(técnico/básico)*

## Formações em andamento

- **Google Cloud Associate Cloud Engineer (ACE)** *(em estudo)*
- **Google ADK** — Agent Development Kit *(em estudo)*
- Leitura: *Arquitetura de Software: as Partes Difíceis* — Neal Ford, Mark Richards et al.
- Próxima leitura: *O Engenheiro de Software com Mentalidade de Produto*

## Interesses

- Aprimorar inglês
