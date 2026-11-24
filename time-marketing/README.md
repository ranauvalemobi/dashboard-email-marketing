# 🏢 Time de Marketing IA — Valemobi

Um time de agentes de IA especialistas que cria campanhas completas para **Minhas Economias**,
**RocketTrader** e **TradeMap**. Você pede em uma frase, o time trabalha em paralelo e entrega um
pacote pronto. **Você só dá o OK.**

## Como usar

Abra uma sessão do Claude Code neste repositório e escreva, por exemplo:

```
/campanha Black Friday do TradeMap, foco em converter free para o plano anual
/campanha reativar usuários inativos do Minhas Economias em dezembro
/campanha divulgar a liga de dezembro da Rocket com a SmartProp
/resultado-campanha (anexe a planilha da Wake ou cole os números)
/conteudo calendário de dezembro dos três produtos
/video transformar a live da liga de ontem em 5 cortes verticais
```

Ou simplesmente peça em linguagem natural — o orquestrador entende e aciona o time.

## O prédio

```
┌──────────────────────────────────────────────────────────────┐
│ 5º ANDAR · DIRETORIA                                         │
│   Orquestrador (sessão principal) — brief, distribuição,     │
│   consolidação, pede o seu OK                                │
├──────────────────────────────────────────────────────────────┤
│ 4º ANDAR · CONTROLE                                          │
│   compliance — CVM, CONAR, LGPD, SPA/MF, marca               │
├──────────────────────────────────────────────────────────────┤
│ 3º ANDAR · ESTÚDIO DE CONTEÚDO             (contínuo)        │
│   estrategista-conteudo · editor-video-ia                    │
├──────────────────────────────────────────────────────────────┤
│ 2º ANDAR · CRIAÇÃO                         (em paralelo)     │
│   redator · diretor-criativo                                 │
├──────────────────────────────────────────────────────────────┤
│ 1º ANDAR · INTELIGÊNCIA                    (em paralelo)     │
│   especialista-minhas-economias · especialista-rocket-trader │
│   especialista-trademap · analista-dados-crm ·               │
│   estrategista-midia-paga                                    │
├──────────────────────────────────────────────────────────────┤
│ SUBSOLO · MEMÓRIA                                            │
│   conhecimento/ (produto, público, tom de voz, conteúdo,     │
│   padrões de vídeo, histórico)                               │
└──────────────────────────────────────────────────────────────┘
```

| Agente | Arquivo | Entrega |
|---|---|---|
| Especialista do produto | `.claude/agents/especialista-*.md` | `01-produto.md` |
| Analista de dados & CRM | `.claude/agents/analista-dados-crm.md` | `02-dados.md` |
| Estrategista de mídia | `.claude/agents/estrategista-midia-paga.md` | `03-midia.md` |
| Redator | `.claude/agents/redator.md` | `04-copy.md` |
| Diretor criativo | `.claude/agents/diretor-criativo.md` | `05-criativo.md` |
| Compliance | `.claude/agents/compliance.md` | `06-compliance.md` |
| Estrategista de conteúdo | `.claude/agents/estrategista-conteudo.md` | `01-calendario.md` (em `/conteudo`) |
| Editor de vídeo IA | `.claude/agents/editor-video-ia.md` | `08-video.md` + vídeos em `midia/` |

## Onde ficam as coisas

- `entregas/STATUS.md` — quadro de todas as campanhas e o status de cada uma.
- `entregas/AAAA-MM-DD-<campanha>/README.md` — resumo executivo + o que precisa do seu OK.
- `conhecimento/` — a memória do time. Quanto mais completa, melhores as campanhas.
- `modelos/brief.md` — modelo de brief usado pelo orquestrador.

## Como o time fica mais inteligente

1. Os arquivos de conhecimento têm marcas `[VALIDAR]` onde a informação pública era incerta.
   Sempre que você responder uma dúvida ou corrigir algo, o orquestrador atualiza o arquivo.
2. Depois de veicular, mande os resultados (`/resultado-campanha`). Eles entram no
   `historico.md` e os agentes passam a usar esses aprendizados.

## Ver os agentes trabalhando (visual de escritório)

**Planta do prédio:** `predio.html` (publicada em https://claude.ai/artifact/573iFHMJztbtugPZuSAc9T) — vista 3D diagonal ou de cima, com os agentes por andar e a reprodução da campanha de teste. Cores do Valemobi Design System.

O time roda como subagentes do Claude Code, então qualquer visualizador de agentes do Claude Code
funciona sem mudar nada aqui. Recomendado: **[Pixel Agents](https://github.com/pablodelucca/pixel-agents)**
— cada agente vira um personagem em pixel art num escritório.

- No computador, com o Claude Code instalado: instalar a extensão "Pixel Agents" no VS Code, ou
  rodar `npx pixel-agents` e abrir no navegador.
- Funciona com sessões locais do Claude Code (não com sessões na nuvem do claude.ai).

Alternativas: [pixtuoid](https://awesome.ecosyste.ms/projects/github.com%2FIvanWng97%2Fpixtuoid)
(andares automáticos), [Pixel Agent Desk](https://github.com/Mgpixelart/pixel-agent-desk).

## Regras que o time segue sozinho

- Não pergunta antes de começar: assume premissas e as registra.
- Não inventa preço, prêmio, número de base ou resultado — marca `[VALIDAR]`.
- Não publica, não dispara e não gasta verba sem o seu OK explícito.
- Não grava dados pessoais de clientes no repositório.
