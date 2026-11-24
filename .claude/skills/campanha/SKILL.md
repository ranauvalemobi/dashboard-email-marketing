---
name: campanha
description: Cria uma campanha de marketing completa com o Time de Marketing IA (Minhas Economias, RocketTrader ou TradeMap) — brief, inteligência de produto e dados, mídia, copy, criativo e revisão de compliance, rodando os agentes em paralelo. Use quando o usuário pedir uma campanha, ação, lançamento, promoção, régua de e-mail, ativação ou "ideias de marketing" para um dos produtos.
---

# /campanha — pipeline completo do Time de Marketing IA

Entrada: o pedido do usuário em linguagem livre (ex.: "Black Friday do TradeMap com 30% off no
anual", "reativar inativos do Minhas Economias", "divulgar a liga de dezembro da Rocket").

Siga o fluxo do `CLAUDE.md` sem fazer perguntas ao usuário:

1. **Brief** — preencha `time-marketing/modelos/brief.md`. Lacunas viram premissas explícitas.
   Pasta: `time-marketing/entregas/AAAA-MM-DD-<slug>/00-brief.md`. Adicione a linha da campanha
   em `time-marketing/entregas/STATUS.md` com status "🔄 Em produção".
2. **Inteligência (paralelo, uma única mensagem)** — chame o especialista do produto,
   `analista-dados-crm` e `estrategista-midia-paga`. Em cada prompt informe: caminho do brief,
   caminho da pasta, arquivo de saída esperado, produto.
3. **Criação (paralelo, uma única mensagem)** — `copywriter` e `designer`, apontando os
   arquivos gerados no passo 2.
4. **Compliance** — `compliance`. Se ❌ ou houver apontamento de severidade alta, aplique as
   correções sugeridas no `04-copy.md`/`05-criativo.md` (ou devolva ao agente) e rode o compliance
   de novo (máx. 2 rodadas).
5. **Consolidação** — `README.md` da entrega:
   - Resumo executivo (objetivo, público, ângulo vencedor, canais, meta, verba).
   - Índice dos arquivos.
   - **Pendências `[VALIDAR]`** (o que só o usuário/time sabe).
   - **Checklist de OK** (o que será publicado/disparado quando o usuário aprovar).
   Atualize `STATUS.md` para "⏳ Aguardando OK".
6. **Commit + push** na branch de trabalho.
7. Responda ao usuário em no máximo ~15 linhas: o ângulo escolhido, as peças entregues, o link da
   pasta, as pendências e a pergunta única: "Posso considerar aprovado?".

Se o pedido envolver liga da RocketTrader com premiação, inclua também a geração do briefing
(skill `briefing-ligas`) e lembre do registro SPA/MF (skill `registro-ligas`).
