---
name: conteudo
description: Planeja e produz conteúdo always-on (calendário editorial, pautas, roteiros, posts, cortes de vídeo) para Minhas Economias, RocketTrader e TradeMap com o Estúdio de Conteúdo. Use quando o usuário pedir calendário editorial, pautas, conteúdo da semana/mês, posts orgânicos, ideias para YouTube/Reels/TikTok, newsletter ou blog.
---

# /conteudo — Estúdio de Conteúdo

Entrada: período e produto(s) (ex.: "conteúdo de dezembro do TradeMap", "semana que vem, os três
produtos"). Sem pergunta ao usuário: na falta de info, assuma a próxima semana e os três produtos.

1. Crie `time-marketing/conteudo/AAAA-MM-<slug>/` e registre em `time-marketing/entregas/STATUS.md`.
2. **`estrategista-conteudo`** → `01-calendario.md` (calendário + pautas + roteiros + mapa de
   reaproveitamento).
3. **Em paralelo** (uma única mensagem):
   - `redator` → `02-textos.md` (legendas, carrosséis, newsletter, artigos) a partir das pautas;
   - `editor-video-ia` → `08-video.md` com decupagem e plano de edição dos vídeos previstos. Se
     houver vídeo bruto disponível, ele já renderiza os cortes locais (ffmpeg, sem custo); gerações
     pagas param no orçamento para o OK.
   - `diretor-criativo` só se houver peças visuais novas além do padrão.
4. **`compliance`** revisa tudo → `06-compliance.md` (correções de severidade alta aplicadas).
5. `README.md` da pasta: resumo do período, peças por produto/canal, custos estimados de IA,
   pendências e checklist de OK. Commit + push.
6. Responda em até 10 linhas e peça o OK (publicar e gastar créditos dependem dele).
