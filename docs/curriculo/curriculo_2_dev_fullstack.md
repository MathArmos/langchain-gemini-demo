# MATHEUS RAMOS

### Desenvolvedor Full Stack
**Foco em desenvolvimento assistido por IA**

---

**Contato**
📱 (44) 99871-8587 · ✉️ mathx1celular19@gmail.com
🔗 linkedin.com/in/matheus-ramos-322644212 · 💻 github.com/MathArmos

---

## Perfil

Desenvolvedor full stack com pouco mais de 1 ano de experiência e **mentalidade de dono** — me importo com o produto como se fosse meu. Construí e mantenho um sistema completo (backend + painel web) de um **agente conversacional inteligente**, do banco de dados à integração com APIs externas — atualmente **implantado na Google Cloud, em fase de treinamento supervisionado com o setor de qualidade**. Uso **IA no fluxo de desenvolvimento todos os dias** de forma responsável, com revisão e qualidade nas entregas.

---

## Linguagens e Habilidades

- **TypeScript** · **JavaScript**
- **Node.js** (APIs e sistemas) · **Express**
- **React** (painel web)
- **PostgreSQL** + **Prisma** · Yup · APIs REST
- **Redis** + BullMQ · Arquitetura modular **CSMR**
- **Context Engineering, Skills, Agents e MCPs** (Claude Code — dev assistido por IA e code review)
- Git / GitHub · Google Cloud (deploy) · Vertex AI (Gemini)

---

## Experiência

### Guardian — Sistema de Porteiro Virtual Inteligente
**Projeto autoral fullstack · Implantado na Google Cloud (em treinamento supervisionado)**

Sistema completo que atua como **porteiro virtual via WhatsApp** para uma empresa de portaria remota, **projetado para atender múltiplos condomínios**. Desenvolvimento **fullstack ponta a ponta**: backend do agente, banco de dados, integrações externas e **painel web para operadores**.

> **Status:** implantado e rodando na **Google Cloud**, atualmente em **treinamento supervisionado com o setor de qualidade** — rollout gradual antes de entrar em operação nos condomínios.

**Backend & Arquitetura**
- **Node.js + TypeScript + Express** no padrão **CSMR** (Controller, Service, Models, Repositories) com factories por domínio
- **PostgreSQL + Prisma + Yup** · modelagem de dados multi-tenant (isolamento por `tenantId`)
- **APIs REST** consumidas pelo painel web
- **Redis + BullMQ**: filas assíncronas, workers dedicados e deduplicação de mensagens
- Integração com **Meta Cloud API** (WhatsApp) via webhook com validação **HMAC**

**Front-end**
- **Painel web em React** para operadores e equipe de qualidade — consome a API REST do backend (ocorrências, dispositivos, métricas)

**Inteligência (IA)**
- Agente baseado em **Gemini 2.5 Flash** (Google Vertex AI) com **function calling** e **structured outputs**
- Integração responsável de IA na lógica de negócio (consultas, pré-cadastros, abertura de solicitações)

**Confiabilidade & Segurança**
- **Circuit breakers**, **retry com backoff exponencial** e **rate limiting** (Redis) nas integrações externas
- Autenticação **JWT role-based**, bcrypt, auditorias de segurança **OWASP Top 10** e retenção de dados **LGPD**

**Qualidade**
- Suíte de testes **Jest** (sem dependências externas) cobrindo segurança, filas e isolamento de dados
- **Code review assistido por IA** (Claude Code: skills, agents e MCPs) no fluxo de desenvolvimento

**Stack:** Node.js · TypeScript · React · Express · PostgreSQL · Prisma · Redis · BullMQ · Meta Cloud API · Vertex AI · Google Cloud

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

- Dominar **UX/UI Design** · Aprimorar inglês
