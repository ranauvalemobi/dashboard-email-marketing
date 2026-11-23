# 05 — Criativo: Black Friday TradeMap 2026

> Autor: diretor criativo · 23/11/2026 · Status: **proposta, aguardando OK**
> Base: `00-brief.md`, `01-produto.md` (ângulos A/B/C), `03-midia.md` (seção 9, "Peças
> necessárias"), `conhecimento/trademap/tom-de-voz.md`, `conhecimento/compliance/regras.md`.
> O `04-copy.md` está sendo escrito em paralelo. **Todo texto final das peças vem de lá**; aqui
> aparecem só a função de cada bloco de texto e, nos roteiros, textos provisórios marcados como tal.
> Preço e desconto sempre como `[X]%` / `R$ [PREÇO]` e nome do plano como "plano anual do
> TradeMap" `[VALIDAR nome]` até confirmação.

---

## 1. Conceito criativo

### Nome: **"Ano inteiro, dado inteiro"**

**Ideia central (1 frase):** a Black Friday do TradeMap transforma o dado pela metade de hoje em
12 meses de dado completo, e a campanha mostra isso com um único elemento visual: **a Régua**,
uma barra de 12 segmentos (JAN–DEZ 2027) que se acende sobre um print real do app.

**Por que conecta com o público**
- **Free engajado (prioridade 1):** ele já abre o app todo dia e conhece a sensação de "ver só
  parte". O visual mostra a mesma tela que ele usa, só que inteira. Não é promessa de resultado,
  é promessa de informação (ângulo A do `01-produto.md`).
- **Ex-assinante (win-back):** a Régua começa vazia em JAN/2027, um recomeço natural na virada do
  ano, sem culpa e sem "volte que ganha".
- **Mensal → anual (upsell):** os 12 segmentos soltos (12 cobranças) se fundem numa barra só
  (1 plano anual). A economia vira imagem, sem precisar de euforia.
- **Aquisição (Meta):** "nível profissional, preço de pessoa física" (ângulo B) ganha prova
  visual com o print real em destaque, com cara de terminal.
- **Black Friday sem clichê:** o fundo preto já é a Black Friday. Nada de etiqueta vermelha,
  carrinho, fogos ou dinheiro. O "desconto" aparece como um dado, em tipografia mono, como se
  fosse uma cotação.

### A Régua: um sistema, três usos (urgência sempre real)
| Fase | O que a Régua mede | Exemplo visual |
|---|---|---|
| Esquenta (24–26/11) | **Dias até 27/11** | Segmentos acendendo um a um, "3", "2", "1" |
| Oferta (27–29/11) | **Os 12 meses de 2027** cobertos pelo plano anual | JAN…DEZ, todos acesos |
| Últimas horas (30/11) | **Horas até 23h59 de 30/11** | Só os últimos segmentos acesos, rótulo "encerra 23h59" |

Regra: a Régua nunca mostra um número inventado de "vagas" ou "estoque". Só conta tempo real
(CONAR, seção 5 de `regras.md`).

---

## 2. Direção de arte

### Paleta (provisória, `[VALIDAR com guia de marca TradeMap]`)
| Uso | Cor | Hex sugerido |
|---|---|---|
| Fundo principal ("black") | Preto azulado | `#0B0F14` |
| Superfícies / cards | Grafite | `#161C24` |
| Linhas de grade, textos secundários | Cinza frio | `#5B6573` |
| Texto principal | Branco suave | `#F2F4F7` |
| Acento único (Régua acesa, CTA, `[X]%`) | Ciano/azul-dado | `#3FB8FF` `[VALIDAR: trocar pela cor primária oficial]` |

- **Sem verde e vermelho como cor de destaque.** No contexto financeiro, verde/vermelho leem como
  "alta/queda" e sugerem ganho. Se o print real tiver verde/vermelho, tudo bem (é o produto), mas
  a moldura da peça não reforça.
- Proporção: 80% escuro, 15% cinzas, no máximo 5% de acento.

### Tipografia (provisória, `[VALIDAR]`)
- **Títulos e texto:** sans grotesca neutra (Inter ou IBM Plex Sans), peso semibold nos títulos.
  Nada de condensada gritada.
- **Números (`[X]%`, `R$ [PREÇO]`, datas, contagem, rótulos JAN–DEZ):** mono (IBM Plex Mono ou
  JetBrains Mono). O desconto aparece "como dado", não como etiqueta de varejo.
- Hierarquia por peça: 1 título + 1 linha de apoio + oferta + CTA. No máximo 4 blocos de texto.

### Estilo de imagem
- **Protagonista: print real do app** (`usar print real do produto`) em mockup de smartphone neutro
  (sem marca de fabricante visível) ou recortado em card com cantos arredondados e sombra suave.
- **Fundo:** preto com grade fina de dados (linhas de 1 px a 6–8% de opacidade) e um leve
  brilho ciano atrás da tela. Pode ser gerado por IA (prompts abaixo) ou feito em vetor.
- **Gente (opcional, só em O1 e hero de e-mail):** pessoa comum de 28–45 anos, roupa casual,
  mesa simples de casa ou cozinha, luz de começo de manhã. Mãos e celular, rosto parcial ou fora
  de foco. Sem escritório de luxo, sem terno, sem relógio caro, sem várias telas de trader.
- **Movimento (vídeos e motion):** cortes secos, a Régua acendendo segmento por segmento, zoom
  lento sobre o print real. Sem transições chamativas.

### Elementos obrigatórios em toda peça
1. Logo TradeMap `[VALIDAR: versão para fundo escuro]`, no canto superior esquerdo ou no rodapé.
2. Aviso legal: **"Conteúdo informativo. Não constitui recomendação de investimento."**, legível
   (mínimo 24 px em 1080 px de largura; 11 px no e-mail a 600 px).
3. Prazo: **"até 30/11, 23h59"** (horário de Brasília) + **"consulte condições"**. Nas peças de
   esquenta (sem oferta), só o aviso legal e "27/11".
4. Oferta somente como `[X]%` / `R$ [PREÇO]`, até confirmação.
5. Selo de print real: as telas são capturas do app atual, de conta demo, sem dado pessoal.

### Regras para os prints reais (vale para todas as peças)
- `usar print real do produto` sempre. **Nunca desenhar nem gerar tela por IA.** Onde houver tela
  nos prompts, a IA gera o celular com tela preta lisa, e o print real é aplicado por cima no
  Figma/Canva.
- Capturar de **conta demo**, sem nome, e-mail, CPF ou patrimônio real de cliente (LGPD).
- Preferir telas de **notícias, carteira consolidada (demo), fundamentos e visão geral de
  mercado**. Se aparecer ticker, ele é incidental: sem seta, círculo, destaque ou chamada de
  desempenho (nada de "veja X subir").
- Evitar capturar momento com variação grande em destaque. Compliance aprova cada print.
- Telas que precisamos receber do produto (`[VALIDAR]` quais existem no plano em oferta):
  - **T1** Home / visão de mercado
  - **T2** Notícias em tempo real
  - **T3** Carteira consolidada de várias corretoras (demo)
  - **T4** Fundamentos / dados de empresa
  - **T5** Fundos / renda fixa
  - **T6** Mercado internacional
  - **T7** Paywall/limite do plano free (o "dado pela metade"), se existir
  - **T8** Tela de planos/checkout com a condição de BF (só depois do preço confirmado)
  - **Gravações de tela (MP4, 9:16, 60 fps se possível):** navegação T1→T2→T4→T3, 20–30 s.

### O que evitar
- Dinheiro, moedas, cofrinho, notas voando, gráfico de seta subindo, foguete, carro, iate,
  relógio, "lifestyle de trader".
- Etiquetas de preço vermelhas, "MEGA", "IMPERDÍVEL", fogos, confete, contagem com "últimas vagas".
- Logos ou marcas de terceiros (corretoras, B3, Bloomberg, Google, fabricante do celular).
- Tickers em destaque, gráfico de ativo específico com recomendação implícita.
- Telas inventadas ou "melhoradas" por IA.
- Emojis nas artes (no máximo 1 em texto de stories, se o `04-copy.md` pedir).

---

## 3. Lista de peças (visuais)

Fonte: `03-midia.md`, seção 9. M7 (textos de anúncio), P1–P8 (push) e G (Google Search) são só
texto: ficam com o `04-copy.md` e não têm arte. O ícone do push é o padrão do app.

| ID | Peça | Formato / medida | Qtd | Ângulo | Fase | Prazo (03-midia) |
|---|---|---|---|---|---|---|
| M6-a | Meta esquenta Feed | 1080×1350 (4:5) | 1 | A, sem preço | 24–26/11 | 24/11 9h |
| M6-b | Meta esquenta Stories/Reels | 1080×1920 (9:16) | 1 | A, sem preço | 24–26/11 | 24/11 9h |
| M1-1 | Meta Feed: oferta | 1080×1350 | 1 | A | 27–30/11 | 25/11 15h |
| M1-2 | Meta Feed: produto | 1080×1350 | 1 | B | 27–30/11 | 25/11 15h |
| M1-3 | Meta Feed: win-back | 1080×1350 | 1 | C + A | 27–30/11 | 25/11 15h |
| M1-4 | Meta Feed: upsell mensal → anual | 1080×1350 | 1 | A econômico | 27–30/11 | 25/11 15h |
| M2-1 a M2-4 | Meta Stories/Reels: os 4 ângulos de M1 | 1080×1920, zona segura de 250 px em cima e embaixo | 4 | = M1 | 27–30/11 | 25/11 15h |
| M3 | Meta Carrossel "o que o plano anual libera" | 1080×1080, 5 cards | 1 (5 arquivos) | A/B | 27–30/11 | 25/11 15h |
| M4-1 | Vídeo "Dado inteiro" | 9:16, 15 s, sem locução | 1 | A | 27–30/11 | 25/11 15h |
| M4-2 | Vídeo "Tudo numa tela" | 9:16, 10 s, sem locução | 1 | C/B | 27–30/11 | 25/11 15h |
| M5-a | Meta últimas horas Feed | 1080×1350 | 1 | A + prazo | 30/11 | 26/11 18h |
| M5-b | Meta últimas horas Stories | 1080×1920 | 1 | A + prazo | 30/11 | 26/11 18h |
| E1–E7 | Hero de e-mail (Wake) | 1200×600 (exibido a 600×300) | 7 (+4 variações de ângulo em E3/E6) | régua | 24–30/11 | E1: 24/11 9h; demais: 26/11 12h |
| I1-a | In-app modal: abertura | ≈1080×1350 `[VALIDAR SDK]` | 1 | A | 27/11 | 26/11 12h |
| I1-b | In-app modal: último dia | ≈1080×1350 `[VALIDAR SDK]` | 1 | A + prazo | 30/11 | 26/11 12h |
| I2-a | In-app banner home: esquenta | proposta 1080×360 `[VALIDAR medida do app]` | 1 | sem preço | 24–26/11 | 24/11 9h |
| I2-b | In-app banner home: oferta | proposta 1080×360 `[VALIDAR]` | 1 | A | 27–30/11 | 26/11 12h |
| O1-1 | IG Feed/Reels: anúncio da BF | 1080×1350 (carrossel de 3) ou Reels 9:16 | 1 | sem preço | 24/11 | 24/11 9h |
| O1-2 | IG Reels: abertura | 1080×1920 (reaproveita M4-1) | 1 | A | 27/11 | 26/11 12h |
| O1-3 | IG Feed: Cyber Monday | 1080×1350 | 1 | A + prazo | 30/11 | 26/11 12h |
| O2-C | IG Stories contagem regressiva | 1080×1920, template | 5 | sem preço / prazo | 24–30/11 | 24/11 9h (template) |
| O2-R | IG Stories recursos do app | 1080×1920, template | 4 | A/C | 25/11 e 28/11 | 25/11 15h |
| O2-L | IG Stories lembrete com link | 1080×1920, template | 3 | A + prazo | 27, 29, 30/11 | 26/11 18h |
| L-d | Banner topo página de planos (desktop) | 1920×480 | 1 | A | 27–30/11 | 26/11 12h |
| L-m | Banner topo página de planos (mobile) | 750×750 | 1 | A | 27–30/11 | 26/11 12h |

**Total de arquivos de arte:** 15 Meta + 7 heros (+4 variações) + 4 in-app + 3 O1 + 12 O2 + 2 L
= **47 arquivos**, a partir de **1 key visual + 4 templates** (Feed, Stories, horizontal,
quadrado).

---

## 4. Direção por peça

> Em todas: texto final em `04-copy.md`. "Título/apoio/CTA" abaixo indica a função do bloco de
> texto. Layout em grade de 12 colunas, margem de 64 px (1080 px de largura).

### Key visual (base de tudo)
Fundo `#0B0F14` com grade fina de dados. No centro, smartphone com **print real T1** levemente
inclinado (8–10°). Abaixo do celular, **a Régua**: 12 segmentos arredondados com rótulos mono
JAN…DEZ e "2027" à direita, todos acesos em ciano. Título acima do celular, oferta `[X]%` em mono
grande ao lado da Régua, CTA em botão ciano, aviso legal e prazo no rodapé.

### Meta Ads

**M6-a / M6-b — Esquenta (sem preço).** Celular com **print real T7** (ou T1), com a metade
inferior da tela em desfoque/escurecida (efeito aplicado sobre o print real, não redesenhado).
Régua em modo contagem: segmentos acendendo até "27/11". Título: "vem aí" (ver `04-copy.md`).
Sem `[X]%`. No 9:16, Régua acima da zona segura de baixo.

**M1-1 / M2-1 — Oferta (ângulo A).** O key visual completo. `[X]%` é o maior elemento
tipográfico, em mono ciano. Apoio: "12 meses de dado completo". CTA: assinar o anual.

**M1-2 / M2-2 — Produto (ângulo B, aquisição).** Print real T4 (fundamentos) em close, ocupando
60% da peça, com 3 callouts finos (linha de 1 px + rótulo mono) apontando para **tipos de dado**
("fundamentos", "notícias em tempo real", "carteira consolidada"), nunca para um ativo. Régua
pequena no rodapé. Sem citar Bloomberg nem concorrente.

**M1-3 / M2-3 — Win-back (C + A).** Print real T3 (carteira consolidada, demo). A Régua começa
em JAN com o primeiro segmento aceso e os outros em contorno: "recomeçar 2027". Tom de convite,
sem culpa. Texto de apoio sobre "sua carteira continua aqui" só se o produto confirmar
`[VALIDAR]`.

**M1-4 / M2-4 — Upsell mensal → anual.** Visual em dois estados lado a lado (Feed) ou em cima e
embaixo (Stories): em cima, 12 segmentos separados com espaço entre eles, rotulados "mensal";
embaixo, uma barra única contínua rotulada "anual". Economia como `[X]%` ou `R$ [Y]`
`[VALIDAR cálculo real]`. Sem print ou com print pequeno T8.

**M3 — Carrossel "o que o plano anual libera" (5 cards, 1080×1080).** Cada card: 1 print real +
1 rótulo + a Régua no rodapé, com o segmento do card aceso (dá continuidade ao arrastar).
- Card 1: capa. Régua completa + título + `[X]%`.
- Card 2: print T2 (notícias em tempo real).
- Card 3: print T4 (fundamentos).
- Card 4: print T3 (carteira consolidada de várias corretoras).
- Card 5: print T5 ou T6 (fundos / internacional) + CTA + prazo + aviso.
Os recursos de cada card dependem da lista oficial "free × pago" `[VALIDAR]`.

**M5-a / M5-b — Últimas horas (30/11).** Fundo mais escuro, Régua em modo horas: só os últimos
segmentos acesos, o último pulsando (no estático, com brilho). Selo mono "encerra hoje, 23h59".
Nada de relógio de bomba nem vermelho.

**M4-1 e M4-2 — Vídeos:** ver seção 5.

### E-mail (Wake), hero 1200×600
Layout padrão: print real à direita (40%), título à esquerda, Régua cruzando a base do hero.
O hero não carrega CTA nem aviso legal como imagem (esses ficam em HTML, para leitura com
imagens bloqueadas). Texto alternativo (alt) obrigatório, a partir do `04-copy.md`.
| E | Data | Régua | Print | Nota |
|---|---|---|---|---|
| E1 esquenta | 24/11 | contagem, 3 dias | T7 ou T1 com desfoque | sem preço |
| E2 prévia | 26/11 | contagem, "amanhã" | T1 | sem preço se o preço não estiver confirmado |
| E3 abertura | 27/11 | 12 meses, toda acesa | 3 versões: free (T7 → T1), ex-assinante (T3), mensal (barra fundida, como M1-4) | |
| E4 lembrete | 27/11 noite | 12 meses | T2 | variação de cor de fundo mais quente (grafite) para diferenciar de E3 |
| E5 benefícios | 28/11 | 12 meses | mosaico T2/T4/T3 | ângulo C, "tudo num só lugar" |
| E6 última chance | 30/11 manhã | horas | 3 versões como E3 | prazo visível no HTML |
| E7 últimas horas | 30/11 noite | últimos segmentos | T1 | o mais minimalista da régua |

### In-app
**I1-a modal abertura / I1-b modal último dia.** Topo: Régua (12 meses em I1-a; horas em I1-b).
Meio: `[X]%` em mono grande + 1 linha. Base: CTA cheio + "agora não" em texto. Aviso e prazo em
corpo pequeno legível. **Sem print do app** (o usuário já está dentro dele): só a Régua e a
tipografia. Área de toque mínima de 48 px; botão de fechar sempre visível.

**I2-a banner esquenta / I2-b banner oferta.** Faixa horizontal: Régua à esquerda (contagem em
I2-a, meses em I2-b), texto curto ao centro, seta/CTA à direita. Sem foto, sem print.

### Instagram orgânico
**O1-1 anúncio da BF (24/11).** Carrossel de 3 (1080×1350): 1) Régua vazia + "27/11";
2) print T7 → "o dado completo está chegando"; 3) data, horário e "ative o lembrete". Sem preço.

**O1-2 abertura (27/11).** Reels = M4-1 com capa própria (1080×1920, recorte 4:5 seguro no grid).

**O1-3 Cyber Monday (30/11).** Igual a M5-a, com mais respiro para a legenda e sem CTA de botão
(o CTA vai na legenda/link da bio).

**O2 — Stories (templates editáveis no Canva/Figma, troca só o número/print):**
- **O2-C contagem (5):** Régua grande no centro com o número de dias/horas em mono gigante
  ("3", "2", "1", "hoje", "encerra 23h59") + sticker de lembrete/contagem nativo do IG.
- **O2-R recursos (4):** um print real por story (T2, T4, T3, T6), print ocupando 70% da altura,
  rótulo mono acima.
- **O2-L lembrete com link (3):** key visual compacto + espaço vazio de 400 px para o sticker de
  link (área central inferior, fora da zona segura).

### Landing / checkout
**L-d 1920×480.** Esquerda: título + `[X]%` + prazo. Centro-direita: celular com print T1.
Régua atravessando a faixa inteira na base. Margens laterais de 240 px (conteúdo dentro de
1440 px). **L-m 750×750:** pilha vertical, título, Régua e `[X]%`, print cortado na base.
"Consulte condições" e "até 30/11, 23h59" sempre visíveis, nunca só no rodapé da página.

---

## 5. Roteiros de vídeo (M4)

> Sem locução (o plano de mídia pede assim). Trilha instrumental eletrônica minimalista, 100–110
> BPM, de banco licenciado `[VALIDAR licença]`. Legendas não são necessárias (não há fala), mas
> todo texto na tela fica dentro da zona segura 9:16. **Textos na tela abaixo são provisórios**: o
> final vem do `04-copy.md`. Telas = `usar gravação de tela real do produto`.

### M4-1 — "Dado inteiro" (15 s, ângulo A)
| Tempo | Imagem | Texto na tela (provisório) | Som |
|---|---|---|---|
| 0–3 s **(gancho)** | Close do celular com **gravação real** de uma tela do app (T7/T1). A metade de baixo está escurecida/desfocada (efeito de pós sobre a gravação). Um dedo rola, e a tela "abre": o desfoque se desfaz de cima para baixo. | "Você já vê o mercado no TradeMap." | Pulso grave, um "clique" quando a tela abre |
| 3–7 s | Gravação real navegando T2 → T4 → T3, cortes secos a cada ~1,3 s, zoom lento de 100% para 108%. | "Agora, o dado completo." | Batida entra |
| 7–11 s | A câmera "recua" e o celular fica menor no topo. Embaixo, a Régua acende JAN → DEZ, um segmento a cada ~0,3 s, com "2027" no fim. | "12 meses de dados, notícias e carteira num só lugar." | Tique sutil a cada segmento |
| 11–15 s **(CTA)** | Cartela final: `[X]%` em mono grande, logo, botão "Assine o plano anual", "até 30/11, 23h59 · consulte condições", aviso legal. Segura 3 s parada. | ver `04-copy.md` | Batida resolve e para |

Variação de 6 s (bumper, opcional): corta 3–7 s e 7–11 s pela metade.

### M4-2 — "Tudo numa tela" (10 s, ângulo C/B)
| Tempo | Imagem | Texto na tela (provisório) | Som |
|---|---|---|---|
| 0–3 s **(gancho)** | Tela dividida em 4 retângulos cinza abstratos (genéricos, sem marca, representando "abas e apps"), que piscam alternadamente rápido. Em seguida, os 4 se fundem num só retângulo. | "Cotação num app. Notícia em outro. Carteira numa planilha." | Ritmo rápido e um pouco caótico |
| 3–7 s | O retângulo único vira o celular com **gravação real** da carteira consolidada (T3), descendo para notícias (T2). | "Tudo num só lugar." | Ritmo se organiza |
| 7–10 s **(CTA)** | Régua 12 meses acesa + `[X]%` + CTA + prazo + aviso legal. | ver `04-copy.md` | Fecha |

**Versão últimas horas (M5, opcional, 30/11):** reaproveitar os 3 s finais de M4-1, trocando a
Régua pelo modo horas e o selo "encerra hoje, 23h59".

**Checklist de vídeo:** sem ticker em destaque, sem número de rentabilidade visível na gravação,
conta demo, aviso legal visível por pelo menos 3 s, cartela final sem movimento por 2–3 s.

---

## 6. Prompts de geração (inglês)

> Como usar: a IA gera **fundo, ambiente, mockup e motion**. Textos, logo, Régua final e **prints
> reais** são aplicados no Figma/Canva por cima. Todos os prompts pedem tela vazia e "no text",
> para evitar tela inventada e texto quebrado. Parâmetros de proporção no formato Midjourney
> (`--ar`); no Higgsfield/Canva, escolher a proporção equivalente.
>
> **Bloco de estilo comum (já incluído em cada prompt):** *dark navy-black background #0B0F14,
> subtle thin data grid lines, single cyan accent #3FB8FF, sober, premium fintech, credible,
> minimal, no money, no coins, no upward arrows, no candlestick charts, no logos, no brand names,
> no text.*

### Key visual (base para M1, M2, E, L)
```
Key visual for a financial data app campaign: a modern smartphone with no visible brand, tilted 8 degrees, floating in the center, its screen a flat pure black rectangle reserved for a real screenshot overlay. Below the phone, a horizontal segmented bar made of 12 rounded glowing cyan segments, evenly spaced, like a calendar timeline. Dark navy-black background #0B0F14 with subtle thin data grid lines at low opacity, soft cyan glow behind the phone, gentle rim light on the phone edges, studio lighting, shallow depth of field, clean 3D product render, sober premium fintech aesthetic, generous negative space at top for headline. No money, no coins, no upward arrows, no candlestick charts, no logos, no brand names, no text. --ar 4:5
```

### M6-a — Esquenta Feed (4:5)
```
Dark minimalist teaser image for a financial information app: an unbranded smartphone standing upright on a matte black surface, screen as a flat black rectangle reserved for a real screenshot, the lower half of the frame softly fogged as if hidden. In front of it, a horizontal bar of 12 rounded segments where only the first 3 glow cyan #3FB8FF and the rest are dim gray outlines, suggesting a countdown. Background navy-black #0B0F14 with faint thin data grid lines, low-key lighting, single soft cyan backlight, calm anticipation mood, 3D render, premium fintech, empty space at top for headline. No money, no arrows, no charts, no logos, no text. --ar 4:5
```

### M6-b — Esquenta Stories (9:16)
```
Vertical teaser for a financial data app: unbranded smartphone centered in the middle third, screen a flat black rectangle for a real screenshot overlay, lower part of the phone dissolving into soft fog. A vertical stack of segmented glowing bars below the phone, only the first segments lit in cyan #3FB8FF, others dim outlines, like a countdown. Navy-black background #0B0F14 with faint data grid, soft cyan backlight, top 250px and bottom 250px kept empty and dark for platform UI, 3D render, sober premium fintech. No money, no arrows, no charts, no logos, no text. --ar 9:16
```

### M1-1 — Feed oferta (4:5)
```
Hero offer visual for a financial data app subscription: unbranded smartphone tilted slightly, screen a flat black rectangle reserved for a real app screenshot, fully lit by a soft cyan glow. Beneath it, a horizontal timeline bar of 12 rounded segments, all glowing cyan #3FB8FF, representing a full year. Large empty dark area on the right side reserved for a big monospaced percentage number. Navy-black background #0B0F14, thin data grid lines at 6 percent opacity, clean studio lighting, crisp reflections, minimal 3D render, confident and credible fintech tone. No money, no coins, no upward arrows, no candlesticks, no logos, no text. --ar 4:5
```

### M1-2 — Feed produto (4:5)
```
Close-up of an unbranded smartphone lying at a slight angle on a dark graphite desk surface, screen a flat black rectangle filling most of the frame, reserved for a real screenshot of a financial data screen. Three very thin luminous cyan lines extend from the screen edges to empty label areas on the side, like technical annotation callouts. Low-key professional lighting, soft cyan reflection on the desk, navy-black background #0B0F14 with subtle grid, terminal-like professional mood but accessible, macro product photography style, 50mm lens, f/2.8. No money, no arrows, no charts, no logos, no text. --ar 4:5
```

### M1-3 — Feed win-back (4:5)
```
Calm early-morning scene: a person's hands (adult, 30s, casual sweater) holding an unbranded smartphone over a simple wooden kitchen table with a cup of coffee, phone screen a flat black rectangle reserved for a real screenshot overlay. Soft natural window light from the left, cool dark tones overall with a subtle cyan glow from the screen. Above the hands, floating minimal UI-like element: a horizontal bar of 12 rounded segments with only the first one lit cyan #3FB8FF, the rest thin outlines, suggesting a fresh start of the year. Face out of frame, no jewelry, no luxury items, documentary photography style, 35mm lens, shallow depth of field. No money, no logos, no text. --ar 4:5
```

### M1-4 — Feed upsell mensal → anual (4:5)
```
Minimal abstract data visual on a navy-black background #0B0F14: in the upper half, 12 small separate rounded cyan bars with visible gaps between them, slightly dim; in the lower half, the same 12 bars merged into one single continuous solid glowing cyan #3FB8FF bar, brighter and calmer. Smooth visual transition between the two states, thin data grid lines in the background, clean vector-like 3D render, soft glow, lots of negative space for labels on the left. Sober fintech aesthetic. No money, no coins, no arrows, no charts, no logos, no text. --ar 4:5
```

### M2-1 — Stories oferta (9:16)
```
Vertical hero offer visual: unbranded smartphone in the middle third with screen as a flat black rectangle for a real screenshot, soft cyan glow behind it. Below the phone, a horizontal 12-segment timeline bar fully lit in cyan #3FB8FF. Empty dark space above the phone for a large monospaced percentage number. Navy-black background #0B0F14 with faint data grid, top 250px and bottom 250px empty for platform UI, 3D studio render, sober premium fintech. No money, no arrows, no candlesticks, no logos, no text. --ar 9:16
```

### M2-2 — Stories produto (9:16)
```
Vertical close-up of an unbranded smartphone held upright, screen a flat black rectangle filling 65 percent of the frame for a real screenshot overlay, three thin cyan annotation lines extending from the screen to empty label areas. Dark graphite environment, navy-black background #0B0F14, low-key lighting with cyan rim light, macro product photography, professional and accessible mood, safe empty margins of 250px at top and bottom. No money, no arrows, no charts, no logos, no text. --ar 9:16
```

### M2-3 — Stories win-back (9:16)
```
Vertical early-morning scene: adult hands in a casual sweater holding an unbranded smartphone above a simple kitchen table with a coffee mug, screen a flat black rectangle for a real screenshot. Soft natural window light, cool dark palette, subtle cyan screen glow. Floating above, a 12-segment horizontal bar with only the first segment lit cyan #3FB8FF. Face not visible, no luxury items, documentary photo style, 35mm, shallow depth of field, empty 250px safe zones at top and bottom. No money, no logos, no text. --ar 9:16
```

### M2-4 — Stories upsell (9:16)
```
Vertical abstract data visual on navy-black #0B0F14: top section shows 12 small separate dim cyan rounded bars stacked with gaps, bottom section shows them merged into one continuous bright solid cyan #3FB8FF bar, smooth transition between them, faint data grid, soft glow, clean minimal 3D render, large empty areas for labels, 250px empty safe zones at top and bottom. No money, no arrows, no charts, no logos, no text. --ar 9:16
```

### M3 — Carrossel (1:1, um prompt por card)
```
Card 1 (cover): Square minimal composition, unbranded smartphone centered with flat black screen for a real screenshot overlay, a 12-segment cyan #3FB8FF timeline bar fully lit along the bottom edge, navy-black background #0B0F14 with faint data grid, soft cyan backlight, 3D render, sober fintech, empty space at top for headline. No money, no arrows, no logos, no text. --ar 1:1
```
```
Cards 2 to 5 (template, generate once and reuse): Square minimal layout, an unbranded smartphone seen straight-on occupying the right 55 percent, flat black screen reserved for a real screenshot, left side empty dark space for a short label, along the bottom edge a 12-segment bar with segments dim gray except one segment lit cyan #3FB8FF (vary which segment per card: 2, 3, 4, 5), navy-black background #0B0F14, faint grid, even soft lighting, consistent camera angle across cards, 3D render. No money, no arrows, no logos, no text. --ar 1:1
```

### M4-1 — Vídeo "Dado inteiro" (9:16, motion para compor com a gravação de tela real)
```
Vertical 15-second motion background for a fintech app ad. Shot 1 (0-3s): slow push-in on an unbranded smartphone floating in darkness, its screen a flat black rectangle (to be replaced by a real screen recording), a soft fog covering the lower half of the phone dissolves upward. Shot 2 (3-7s): phone holds center, gentle 8 percent zoom, cyan rim light pulses subtly on each beat. Shot 3 (7-11s): camera pulls back, phone moves to upper third, below it a horizontal bar of 12 rounded segments lights up one by one in cyan #3FB8FF from left to right. Shot 4 (11-15s): static end frame, all 12 segments lit, large empty dark area for text. Navy-black background #0B0F14 with faint data grid, smooth cinematic camera, no camera shake, sober premium fintech. No money, no arrows, no charts, no logos, no text, no people. 9:16, 24fps.
```

### M4-2 — Vídeo "Tudo numa tela" (9:16)
```
Vertical 10-second motion graphic. Shot 1 (0-3s): four plain gray rounded rectangles arranged in a 2x2 grid on a navy-black background #0B0F14, blinking alternately at a fast irregular rhythm like competing app windows, then sliding together and merging into one single rounded rectangle. Shot 2 (3-7s): the merged rectangle smoothly morphs into an unbranded smartphone with a flat black screen (to be replaced by a real screen recording), calm cyan #3FB8FF glow. Shot 3 (7-10s): phone shrinks to the top, a 12-segment cyan bar fully lit appears below, static end frame with empty space for text. Clean flat-to-3D motion design, faint data grid, smooth easing, sober fintech. No money, no arrows, no charts, no logos, no brand names, no text. 9:16, 24fps.
```

### M5-a — Últimas horas Feed (4:5)
```
Dark, focused final-hours visual for a financial data app: a horizontal bar of 12 rounded segments across the lower third, all dim graphite except the last two on the right glowing cyan #3FB8FF, the very last one brighter with a soft pulse glow. Above, an unbranded smartphone with a flat black screen reserved for a real screenshot, lit only by the cyan glow. Very dark navy-black background #0B0F14, faint data grid, calm urgency without alarm, no red, minimal 3D render. No money, no clocks, no arrows, no logos, no text. --ar 4:5
```

### M5-b — Últimas horas Stories (9:16)
```
Vertical final-hours visual: unbranded smartphone in the middle third with a flat black screen for a real screenshot, below it a 12-segment bar where only the last segment glows bright cyan #3FB8FF and the rest are dim graphite, very dark navy-black background #0B0F14, faint data grid, single soft cyan light source, calm urgency without alarm, no red, 250px empty safe zones top and bottom, minimal 3D render. No money, no clocks, no arrows, no logos, no text. --ar 9:16
```

### E1 a E7 — Heros de e-mail (1200×600, 2:1)
Base comum: unbranded smartphone on the right 40 percent with a flat black screen reserved for
a real screenshot, empty dark space on the left 60 percent for a headline, a horizontal
12-segment bar crossing the bottom edge, navy-black background #0B0F14, faint grid, soft cyan
glow, minimal 3D render, no money, no arrows, no logos, no text, `--ar 2:1`. O que muda por
e-mail:
```
E1 (teaser): [base] + only the first 3 segments lit cyan #3FB8FF, others dim outlines, lower half of the phone softly fogged, quiet anticipation mood. --ar 2:1
```
```
E2 (preview): [base] + segments lit up to the last but one, phone screen softly glowing as if about to switch on, "eve of the event" mood, slightly warmer graphite tones. --ar 2:1
```
```
E3 (opening, 3 versions): [base] + all 12 segments lit cyan #3FB8FF, crisp bright reflections, confident mood. Version "monthly subscriber": replace the phone with the 12 separate bars merging into one continuous bar. --ar 2:1
```
```
E4 (reminder): [base] + all 12 segments lit, background shifted to deep graphite #161C24, evening mood, softer and dimmer light. --ar 2:1
```
```
E5 (benefits): [base] but instead of one phone, three unbranded smartphones overlapping in a fan arrangement, each with a flat black screen for different real screenshots, all 12 segments lit. --ar 2:1
```
```
E6 (last day, 3 versions): [base] + only the last 3 segments lit cyan, the final one brighter, calm urgency, no red. --ar 2:1
```
```
E7 (final hours): Ultra-minimal: navy-black #0B0F14 background, no phone, a single horizontal 12-segment bar centered, all dim graphite except the very last segment glowing bright cyan #3FB8FF with a soft halo, large empty space above for text, no red, no clocks, no logos, no text. --ar 2:1
```

### I1-a — Modal abertura (≈4:5)
```
Flat minimal UI background for an in-app promotional modal: navy-black #0B0F14 rounded-corner card, a horizontal 12-segment bar near the top fully lit in cyan #3FB8FF with soft glow, large empty center area for a monospaced percentage number, empty bottom area for a button, faint data grid texture at very low opacity, clean vector style, no phone, no people. No money, no arrows, no logos, no text. --ar 4:5
```

### I1-b — Modal último dia (≈4:5)
```
Flat minimal UI background for an in-app modal: navy-black #0B0F14 rounded card, a 12-segment bar near the top with all segments dim graphite except the last one glowing bright cyan #3FB8FF with a halo, large empty center area for text, empty bottom area for a button, faint grid texture, clean vector style, calm urgency, no red. No phone, no money, no clocks, no logos, no text. --ar 4:5
```

### I2-a — Banner home esquenta (3:1)
```
Thin horizontal banner background, navy-black #0B0F14, on the left a compact 12-segment bar with the first 3 segments lit cyan #3FB8FF and the rest dim outlines, center and right empty for text and arrow, faint data grid, flat vector style, subtle glow. No phone, no money, no logos, no text. --ar 3:1
```

### I2-b — Banner home oferta (3:1)
```
Thin horizontal banner background, navy-black #0B0F14, on the left a compact 12-segment bar fully lit in cyan #3FB8FF, center and right empty for text and a call-to-action, faint data grid, flat vector style, crisp soft glow. No phone, no money, no logos, no text. --ar 3:1
```

### O1-1 — IG anúncio da BF (carrossel 4:5, 3 cards)
```
Series of 3 consistent dark minimal frames for a financial app teaser, same camera and lighting across all. Frame 1: a 12-segment horizontal bar centered on navy-black #0B0F14, all segments as thin dim outlines, empty space for a date. Frame 2: unbranded smartphone centered with a flat black screen for a real screenshot overlay, lower half veiled in soft fog. Frame 3: the same bar with the first segments lit cyan #3FB8FF, empty space for text. Faint data grid, soft cyan glow, 3D render, sober fintech. No money, no arrows, no logos, no text. --ar 4:5
```

### O1-2 — IG Reels abertura (9:16)
Reaproveitar o vídeo M4-1. Prompt só para a **capa**:
```
Vertical cover frame: unbranded smartphone centered with a flat black screen for a real screenshot, a fully lit 12-segment cyan #3FB8FF bar below, navy-black background #0B0F14, faint grid, soft cyan glow, central 1080x1350 area holding all key elements so it crops cleanly to 4:5 on the profile grid, minimal 3D render. No money, no arrows, no logos, no text. --ar 9:16
```

### O1-3 — IG Cyber Monday (4:5)
```
Dark final-day visual: navy-black #0B0F14 background, a 12-segment horizontal bar across the center with only the last segment glowing bright cyan #3FB8FF with a halo, an unbranded smartphone above it with a flat black screen for a real screenshot, generous empty space on the top and bottom for a caption-friendly layout, faint data grid, calm and focused mood, no red, minimal 3D render. No money, no clocks, no arrows, no logos, no text. --ar 4:5
```

### O2-C — Stories contagem regressiva (template 9:16)
```
Vertical countdown story template background: navy-black #0B0F14, a large vertical stack of 12 rounded horizontal segments in the center, a configurable number of them lit cyan #3FB8FF and the rest dim graphite, huge empty area in the middle-upper third for a giant monospaced number, empty area in the lower third for an Instagram countdown sticker, faint data grid, flat vector style, soft glow, 250px empty safe zones top and bottom. No money, no clocks, no logos, no text. --ar 9:16
```

### O2-R — Stories recursos (template 9:16)
```
Vertical story template: unbranded smartphone seen straight-on occupying 70 percent of the height, flat black screen reserved for a real app screenshot, small empty label area above the phone, a thin 12-segment cyan bar at the bottom above the safe zone, navy-black background #0B0F14, faint grid, even soft lighting, consistent framing for reuse across 4 stories, 3D render. No money, no arrows, no logos, no text. --ar 9:16
```

### O2-L — Stories lembrete com link (template 9:16)
```
Vertical story template: compact composition in the upper half with an unbranded smartphone (flat black screen for a real screenshot) and a fully lit 12-segment cyan #3FB8FF bar beneath it, lower-middle area left completely empty and dark (about 400px tall) for an Instagram link sticker, navy-black background #0B0F14, faint grid, soft cyan glow, 250px safe zones top and bottom, minimal 3D render. No money, no arrows, no logos, no text. --ar 9:16
```

### L-d — Banner landing desktop (1920×480, 4:1)
```
Ultra-wide website hero banner: navy-black #0B0F14 background with faint thin data grid, an unbranded smartphone tilted slightly at center-right with a flat black screen reserved for a real screenshot, soft cyan #3FB8FF backlight, a long horizontal 12-segment bar fully lit in cyan running across the entire bottom edge, left 45 percent empty for headline and offer, 240px empty margins on both sides, clean 3D render, sober premium fintech. No money, no arrows, no charts, no logos, no text. --ar 4:1
```

### L-m — Banner landing mobile (750×750, 1:1)
```
Square mobile hero banner: navy-black #0B0F14 background, upper half empty for headline and a monospaced percentage number, a fully lit 12-segment cyan #3FB8FF bar across the middle, an unbranded smartphone cropped at the bottom edge showing only its upper half with a flat black screen for a real screenshot, faint data grid, soft glow, minimal 3D render. No money, no arrows, no logos, no text. --ar 1:1
```

---

## 7. Pendências e dependências

| # | Pendência | Bloqueia | Dono |
|---|---|---|---|
| 1 | Guia de marca TradeMap (cores, tipografia, logo para fundo escuro) | Finalização de todas as peças (o conceito se adapta trocando o acento) | Marca/produto |
| 2 | Prints T1–T8 + gravação de tela, de conta demo | Todas as peças com celular; vídeos M4 | Produto |
| 3 | Lista oficial "free × pago" | M3 (cards 2–5), O2-R, E5 | Produto |
| 4 | `[X]%`, `R$ [PREÇO]`, nome do plano, cálculo mensal → anual | M1/M2/M3/M5, E3–E7, I1, I2-b, L | Produto/finanças |
| 5 | Medidas do modal e do banner in-app (SDK) | I1, I2 | Produto/CRM |
| 6 | Licença da trilha dos vídeos | M4 | Mídia |
| 7 | Textos finais | Todas | Redator (`04-copy.md`) |
| 8 | Revisão de compliance de cada print e peça antes de subir na Meta (até 25/11 18h) | Publicação | Compliance (`06-compliance.md`) |

**Ordem de produção sugerida (segue o `03-midia.md`):** key visual + templates hoje à noite →
M6, I2-a, E1, O1-1, O2-C até 24/11 9h → M1–M4 até 25/11 15h → E2–E7, I1, I2-b, L, O1-2/O1-3
até 26/11 12h → M5, O2-L até 26/11 18h.
