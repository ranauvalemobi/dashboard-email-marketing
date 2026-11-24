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
/resultado-campanha (anexe a exportação do backoffice ou cole os números)
/conteudo calendário de dezembro dos três produtos
/video transformar a live da liga de ontem em 5 cortes verticais
```

Ou simplesmente peça em linguagem natural — o Head de Marketing entende e aciona o time.

## O escritório

Um andar em plano aberto, dividido em setores (veja em 3D em `predio.html`):

| Setor | Funções | Agente | Entrega |
|---|---|---|---|
| Diretoria | Head de Marketing | sessão principal | `00-brief.md`, `README.md` |
| Inteligência | Especialistas de produto | `especialista-*` | `01-produto.md` |
| | Dados e CRM | `analista-dados-crm` | `02-dados.md` |
| | Mídia Paga | `estrategista-midia-paga` | `03-midia.md` |
| Criação | Copywriter | `copywriter` | `04-copy.md` |
| | Designer e Web | `designer` | `05-criativo.md` + `web/` (LP e e-mails HTML) |
| Estúdio de Conteúdo | Social media | `estrategista-conteudo` | `01-calendario.md` (em `/conteudo`) |
| | Editor de vídeo IA | `editor-video-ia` | `08-video.md` + vídeos em `midia/` |
| | Parcerias e Influenciadores | `parcerias-influenciadores` | `10-influencia.md` |
| Controle | Compliance | `compliance` | `06-compliance.md` |
| | QA de entrega | `qa-entrega` | `09-qa.md` |
| Memória | Base de conhecimento | `conhecimento/` | produto, público, tom de voz, conteúdo, influenciadores, histórico |

Cada agente tem um **padrão sênior** no próprio arquivo: o repertório que usa e a lista que confere
antes de entregar.

## Onde ficam as coisas

- `entregas/STATUS.md` — quadro de todas as campanhas e o status de cada uma.
- `entregas/AAAA-MM-DD-<campanha>/README.md` — resumo executivo + o que precisa do seu OK.
- `conhecimento/` — a memória do time. Quanto mais completa, melhores as campanhas.
- `modelos/brief.md` — modelo de brief usado pelo Head de Marketing.

## Como o time fica mais inteligente

1. Os arquivos de conhecimento têm marcas `[VALIDAR]` onde a informação pública era incerta.
   Sempre que você responder uma dúvida ou corrigir algo, o Head de Marketing atualiza o arquivo.
2. Depois de veicular, mande os resultados (`/resultado-campanha`). Eles entram no
   `historico.md` e os agentes passam a usar esses aprendizados.

## Ver os agentes trabalhando (visual de escritório)

**Escritório 3D:** `predio.html` (publicado em https://claude.ai/artifact/573iFHMJztbtugPZuSAc9T) — um andar em plano aberto com seis setores, personagens e decoração em 3D, vista diagonal ou de cima, e a reprodução da campanha de teste. Cores do Valemobi Design System.

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
