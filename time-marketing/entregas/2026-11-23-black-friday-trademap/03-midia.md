# 03 — Plano de mídia e canais · Black Friday TradeMap 2026

> Autor: estrategista de mídia paga · Data: 23/11/2026 · Status: **proposta, aguardando OK**
> Este documento **só planeja**. Nada foi criado, publicado ou alterado em contas de anúncio.
> Subir campanhas e gastar verba dependem do OK explícito do usuário.

## 0. Resumo em 30 segundos

- **Janela**: 24/11 (esquenta) → 30/11 23h59 (Cyber Monday). São 7 dias de veiculação, e o
  plano precisa estar no ar entre **24 e 48h a partir de hoje (23/11)**.
- **Base de tudo: canais próprios** (e-mail Wake, push, in-app). Custo de mídia zero, sobem
  rápido e falam com os públicos prioritários do brief (free engajado, ex-assinantes,
  mensal → anual).
- **Meta Ads como reforço**: 70% em **remarketing** (visitantes, base, app) e 30% em
  **prospecção** (lookalike/amplo). Com 4 dias até a BF não dá para passar pela fase de
  aprendizado de campanhas frias grandes, então remarketing é a aposta mais segura.
- **Instagram orgânico** amplifica a contagem regressiva e serve de prova social do produto
  (prints reais do app).
- **Cenário recomendado: R$ 30.000 de mídia paga `[VALIDAR]`**, com 80% concentrado entre
  27/11 e 30/11.
- **Fora deste plano** (sem tempo hábil): YouTube (exige vídeo produzido), influenciadores
  (contrato, briefing e #publi não cabem em 48h). Google Search só para proteger a marca, e só a
  partir do cenário recomendado.

---

## 1. Premissas e dependências

| # | Premissa | Status |
|---|---|---|
| P1 | % de desconto, preço anual e nome do plano | `[VALIDAR]`: peças usam `[X]%`, `R$ [PREÇO]` e "plano anual do TradeMap" |
| P2 | Pixel Meta + API de Conversões (CAPI) disparando `Purchase` no checkout web | `[VALIDAR]` |
| P3 | Eventos do app (SDK Meta ou MMP, como AppsFlyer/Adjust) com evento de assinatura | `[VALIDAR]` |
| P4 | Volume de `Purchase` na conta Meta (precisa de ~50/semana para otimizar por compra) | `[VALIDAR]`; ver alternativa na seção 4.4 |
| P5 | Listas da base (free engajado, ex-assinantes, mensais) exportáveis para Público Personalizado, com base legal | `[VALIDAR com DPO]`; ver seção 4.5 |
| P6 | Landing page / checkout de BF com preço promocional e prazo explícito (encerra 30/11 23h59) | `[VALIDAR]`: quem publica e quando |
| P7 | Conta de anúncios com método de pagamento e limite de gasto compatível com o cenário escolhido | `[VALIDAR]` |
| P8 | Histórico de campanhas do TradeMap | Inexistente em `historico.md`. Benchmarks abaixo são estimativas de mercado `[VALIDAR]` |

**Sinal de alerta de prazo:** a revisão de anúncios da Meta costuma demorar mais na semana da BF.
Os anúncios precisam ser **enviados até 25/11 às 18h** para garantir a veiculação no dia 27.

---

## 2. Mix de canais e papel no funil

| Canal | Tipo | Público principal | Papel no funil | Prioridade |
|---|---|---|---|---|
| **E-mail (Wake)** | Próprio | Free engajado, ex-assinantes, mensais | Conversão. Carrega a régua completa (esquenta → última chance) | 1 |
| **Push** | Próprio | Usuários do app com opt-in | Conversão e urgência nos picos (abertura, viradas de dia, últimas horas) | 1 |
| **In-app** (modal + banner) | Próprio | Free ativo no app (o mais quente) | Conversão no momento de uso, com clique direto para o checkout | 1 |
| **Meta Ads: remarketing** | Pago | Visitantes do site e do checkout, base (listas), usuários do app | Conversão de quem já conhece o produto e não abre e-mail/push | 2 |
| **Meta Ads: prospecção** | Pago | Lookalike de assinantes e público amplo com sinal | Aquisição incremental (público 4 do brief) | 3 |
| **Instagram orgânico** | Próprio | Seguidores | Consideração e prova de produto: contagem regressiva, prints do app, stories com link | 2 |
| **Google Search (marca)** | Pago | Quem busca "TradeMap" | Proteger a marca de concorrentes que compram o termo na BF. Opcional | 4 |
| YouTube / influenciadores | Pago | n/a | **Não recomendado** neste prazo | n/a |

**Lógica de orquestração:** o canal próprio chega primeiro em cada pico. O Meta remarketing
pega quem foi impactado e não converteu, e a prospecção roda em paralelo com verba limitada.
Compradores saem de toda comunicação em até 24h (ver seção 7).

---

## 3. Verba: 3 cenários `[VALIDAR]`

Os valores cobrem só mídia paga, de 24/11 a 30/11. Canais próprios não têm custo de mídia
(custo de disparo da Wake `[VALIDAR]`).

| | **Enxuto** | **Recomendado** | **Agressivo** |
|---|---|---|---|
| **Total mídia** | **R$ 12.000** `[VALIDAR]` | **R$ 30.000** `[VALIDAR]` | **R$ 60.000** `[VALIDAR]` |
| Meta: remarketing | 75% · R$ 9.000 | 60% · R$ 18.000 | 45% · R$ 27.000 |
| Meta: prospecção (LAL/amplo) | 25% · R$ 3.000 | 30% · R$ 9.000 | 40% · R$ 24.000 |
| Meta: impulsionamento de posts orgânicos | — | 5% · R$ 1.500 | 5% · R$ 3.000 |
| Google Search (marca) | — | 5% · R$ 1.500 | 7% · R$ 4.200 |
| Reserva para escalar vencedores (liberada a partir de 28/11) | — | — | 3% · R$ 1.800 |
| **Quando faz sentido** | Pixel/CAPI sem histórico, oferta tímida, foco total na base | Tracking ok e desconto relevante (≥ 30%) | Tracking ok, CPA validado no esquenta e meta agressiva de assinaturas |

### Distribuição diária (cenário recomendado, R$ 30.000)

| Dia | Fase | % | Valor |
|---|---|---|---|
| 24/11 (ter) | Esquenta | 6% | R$ 1.800 |
| 25/11 (qua) | Esquenta | 7% | R$ 2.100 |
| 26/11 (qui) | Esquenta / véspera | 7% | R$ 2.100 |
| **27/11 (sex)** | **Black Friday** | **25%** | **R$ 7.500** |
| 28/11 (sáb) | Fim de semana | 14% | R$ 4.200 |
| 29/11 (dom) | Fim de semana | 14% | R$ 4.200 |
| **30/11 (seg)** | **Cyber Monday / última chance** | **27%** | **R$ 8.100** |

O enxuto e o agressivo seguem a mesma curva, proporcionalmente.

### Referências de custo (estimativas, sem histórico próprio) `[VALIDAR]`

| Métrica | Remarketing | Prospecção |
|---|---|---|
| CPM na semana da BF (leilão inflacionado) | R$ 35–60 | R$ 25–45 |
| CTR (link) | 1,2–2,5% | 0,6–1,2% |
| CPA de assinatura anual | R$ 60–150 | R$ 180–400 |

**CPA-meta:** defina pelo preço anual promocional. Sugestão: **CPA-meta ≤ 30% do `R$ [PREÇO]`
anual** `[VALIDAR]` com finanças. Exemplo: com plano anual de R$ 400, a meta é CPA ≤ R$ 120.
Com o recomendado e um CPA médio de R$ 120 a R$ 200, a projeção é de **150 a 250 assinaturas
anuais vindas de mídia paga** `[VALIDAR]`, somadas às conversões dos canais próprios.

---

## 4. Estrutura Meta Ads

### 4.1 Categoria especial: serviços financeiros

- Um app de informação de mercado e investimentos **pode ser enquadrado** na categoria especial
  de anúncio de *Produtos e serviços financeiros*. Nela, a Meta restringe a segmentação por
  idade, gênero e localização detalhada e **limita ou bloqueia lookalikes** `[VALIDAR com a
  política vigente no Brasil e com compliance]`.
- **Decisão de plano:** a estrutura abaixo funciona nos dois casos. Se a categoria for
  obrigatória, troque os conjuntos de lookalike por **público amplo Advantage+** com o público
  da base como sinal (sugestão de público). Os públicos personalizados de remarketing continuam
  permitidos.
- Toda peça leva o aviso "Conteúdo informativo. Não constitui recomendação de investimento.",
  além do prazo da oferta ("até 30/11, 23h59") e "consulte condições".
- Possível exigência de verificação de anunciante financeiro `[VALIDAR]`. Se faltar, isso
  bloqueia o lançamento, então é preciso checar **hoje**.

### 4.2 Campanhas → conjuntos → anúncios (cenário recomendado)

Nomenclatura: `TM_BF26_[CAMPANHA]_[CONJUNTO]_[CRIATIVO]`. UTMs:
`utm_source=meta&utm_medium=paid_social&utm_campaign=bf2026-trademap&utm_content=[criativo]`.

**C1 — `TM_BF26_REMKT` · Objetivo: Vendas · Evento: `Purchase` (assinatura anual) · CBO
(orçamento na campanha) · 60% da verba**

| Conjunto | Público | Janela | Exclusões | Anúncios |
|---|---|---|---|---|
| R1 · Checkout abandonado | Visitantes da página de planos ou do checkout sem compra | 14 dias | Assinantes ativos | 3 (urgência/prazo, oferta, carrossel do "o que libera") |
| R2 · Visitantes site + engajados IG/FB | Visitantes do site, engajamento IG/FB, visualizações de vídeo ≥ 50% | 30 dias | Assinantes, R1 | 3 |
| R3 · Base: free engajado + ex-assinantes | Lista da base (hash via CAPI/Público Personalizado) + usuários ativos do app (SDK) | n/a | Assinantes anuais ativos | 4 (2 para free: "dados completos"; 2 para win-back: "volte com [X]%") |
| R4 · Upsell mensal → anual | Lista de assinantes mensais | n/a | Assinantes anuais | 2 ("troque para o anual e pague menos por mês"; calculadora de economia) |

**C2 — `TM_BF26_PROSP` · Objetivo: Vendas · Evento: `Purchase` · CBO · 30% da verba**

| Conjunto | Público | Exclusões | Anúncios |
|---|---|---|---|
| P1 · Lookalike 1–3% de assinantes pagantes | LAL Brasil, a partir da lista de assinantes (mín. 1.000 registros `[VALIDAR]`) | Base inteira + visitantes de 30 dias | 4 |
| P2 · Amplo Advantage+ com sinal | Brasil, 22–55 anos (se a categoria especial permitir), sugestão de público = assinantes. Interesses de apoio: investimentos, bolsa de valores, ações, mercado financeiro, B3 | Base inteira + visitantes de 30 dias | 4 (os mesmos de P1, para consolidar aprendizado) |

> Se a categoria especial for exigida: P1 sai, e P2 fica com 100% da prospecção.

**C3 — `TM_BF26_BOOST` · Objetivo: Engajamento/Tráfego · 5% da verba (recomendado/agressivo)**
- Impulsionar os 2 posts orgânicos de melhor desempenho (abertura da BF e Cyber Monday) para
  seguidores e públicos semelhantes. Gera o público de engajamento que alimenta o R2.

**Total de anúncios únicos:** cerca de 10 criativos, reaproveitados entre os conjuntos
(detalhe na seção 9).

### 4.3 Posicionamentos
- Advantage+ placements, com prioridade para **Stories/Reels 9:16** e **Feed 4:5**.
- Audience Network fora em remarketing (qualidade de clique baixa).

### 4.4 Plano B de otimização (se não houver `Purchase` suficiente)
- Se a conta não tiver histórico de ~50 compras/semana, otimize por **`InitiateCheckout`** em
  C2 e mantenha **`Purchase`** em C1, onde o público é quente.
- Se o pixel/CAPI não estiver confirmado até **24/11 às 12h**, o plano cai para o **enxuto**,
  só com remarketing otimizado por cliques no link e leitura de conversão pelas UTMs e pelo
  checkout.

### 4.5 LGPD para listas
- Subir listas da base na Meta só com base legal de marketing válida, sempre com hash (o padrão
  da plataforma). Nenhuma lista vai para o Git `[VALIDAR com DPO]`.

---

## 5. Canais próprios: régua de contatos

Horários em BRT. Frequência máxima por pessoa: **1 e-mail e 1 push por dia**, com exceção de
27/11 e 30/11 (até 2 de cada). O in-app aparece uma vez por sessão.

| Data | E-mail (Wake) | Push | In-app | Instagram orgânico |
|---|---|---|---|---|
| **24/11 ter** | E1 · Esquenta "vem aí", com lista VIP/aviso, 10h | — | Banner "BF chegando" | Feed: anúncio da BF + 3 stories de contagem |
| **25/11 qua** | — (descanso) | P1 · Esquenta, 19h | Banner | Stories: "o que o anual libera" (prints do app) |
| **26/11 qui** | E2 · Esquenta 2: "é amanhã" (acesso antecipado removido pelo compliance, C-01), 18h | P2 · "Amanhã", 20h | Banner | Stories: contagem regressiva com sticker de lembrete |
| **27/11 sex** | E3 · Abertura, 07h · E4 · Lembrete para não abridores, 19h | P3 · 08h · P4 · 20h | **Modal de oferta** + banner | Feed/Reels: abertura + stories com link (manhã e noite) |
| **28/11 sáb** | E5 · Benefícios (o que libera), 10h | P5 · 11h | Banner | Stories |
| **29/11 dom** | — (descanso) | P6 · 18h | Banner | Stories: "último dia amanhã" |
| **30/11 seg** | E6 · Última chance, 09h · E7 · "Últimas horas", 19h, só para quem não abriu/clicou | P7 · 12h · P8 · 21h ("encerra às 23h59") | **Modal "último dia"** + banner | Feed/Reels: Cyber Monday + stories a cada ~3h |

**Segmentação da régua (vem do analista de dados, em `02-dados.md`):** variar o ângulo do
e-mail por segmento. Free engajado recebe "dados completos". Ex-assinante recebe "volte com
[X]%". Mensal recebe "troque para o anual". A mesma estrutura de envio vale para os três.

---

## 6. Cronograma de execução (24–48h)

| Quando | O quê | Dono |
|---|---|---|
| **23/11 (hoje) até 18h** | OK no cenário de verba; confirmar desconto, preço e nome do plano; checar pixel/CAPI, eventos do app e categoria especial/verificação na Meta | Usuário + orquestrador |
| 23/11 noite | Copy (`04-copy.md`) e direção de arte (`05-criativo.md`) a partir da lista de peças (seção 9) | Redator + diretor criativo |
| **24/11 até 10h** | E1 + banner in-app + post IG no ar (peças de esquenta não dependem do preço) | CRM / social |
| 24/11 até 12h | Públicos criados na Meta (listas, remarketing, LAL); checkpoint do tracking, que decide entre o recomendado e o enxuto | Mídia |
| 24/11 até 18h | Campanhas C1/C2 do esquenta no ar (criativos de "vem aí" + produto) | Mídia (após OK) |
| **25/11 até 18h** | **Criativos com oferta enviados para revisão da Meta**, agendados para 27/11 00h01. Compliance revisa antes (`06-compliance.md`) | Mídia + compliance |
| 26/11 | Programar E3/E4, P3/P4 e o modal in-app. Teste de link/UTM/checkout em web e app | CRM + produto |
| 27/11 00h01 | Troca automática para os criativos de oferta + aumento de orçamento | Mídia |
| 27–30/11 | Leitura de resultado 3×/dia (10h, 15h, 21h) com as regras da seção 7 | Mídia |
| **30/11 23h59** | Pausar tudo. Remover banner/modal. Checkout volta ao preço cheio | Mídia + produto |
| 02/12 | Relatório de resultado → `historico.md` (via `/resultado-campanha`) | Orquestrador |

---

## 7. Regras de otimização

Leituras às 10h, 15h e 21h, de 27/11 a 30/11. No esquenta, uma leitura diária às 18h.

| Situação | Ação |
|---|---|
| Anúncio com **CPA > 1,5× a meta** após **5 conversões** OU gasto **≥ 2× o CPA-meta sem conversão** | Pausar o anúncio |
| Conjunto com CPA > 1,5× a meta após 10 conversões | Cortar o orçamento do conjunto em 30%, ou pausar se houver alternativa |
| Anúncio/conjunto com **CPA ≤ 0,8× a meta** e ≥ 5 conversões | **Escalar +20–30% por leitura** (no máximo 1 aumento a cada ~8h, para não reiniciar o aprendizado) |
| **CTR (link) < 0,7%** após 3.000 impressões | Trocar o criativo pela variação reserva |
| **Frequência > 4** (remarketing) ou **> 2,5** (prospecção) em 3 dias | Rodar criativo novo nesse conjunto |
| CPM 50% acima da referência e CPA estável | Manter. CPM alto é esperado na BF |
| Prospecção com CPA > 2× a meta em 27/11 até as 15h | Mover 50% da verba de C2 para C1 (remarketing) |
| Taxa de abertura de e-mail < 15% `[VALIDAR benchmark Wake]` | Reenvio para não abridores com outro assunto (só em E3/E6) |
| Comprador detectado | Excluir de e-mail, push, in-app e Meta em até 24h (público de exclusão via CAPI/lista atualizada diariamente) |
| 30/11 após 18h | Sem novos testes. Só escala nos vencedores e troca para os criativos de "últimas horas" |

**Leitura do KPI:** novas assinaturas anuais por canal (UTM + origem no checkout + código
promocional por canal, se disponível `[VALIDAR]`). Atribuição da Meta: 7 dias clique / 1 dia
visualização. Para decidir verba, vale o CPA por clique.

---

## 8. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Preço/desconto não confirmados a tempo | Peças de esquenta saem sem preço. As de oferta usam `[X]%` e só sobem após confirmação |
| Reprovação ou atraso na revisão da Meta | Enviar até 25/11 às 18h. Duplicar anúncios aprovados em vez de editar (edição reabre a revisão) |
| Categoria especial obrigatória | Estrutura alternativa já prevista (amplo + sinal, sem LAL) |
| Tracking quebrado | Plano cai para o enxuto. Decisão às 12h de 24/11 |
| Saturação da base (muitos toques) | Limite de frequência da seção 5 e exclusão diária de compradores |
| Urgência artificial (CONAR) | Só usar prazo real (30/11 23h59). Nada de "últimas vagas" |

---

## 9. Peças necessárias (para o redator e o diretor criativo)

> Todas com: aviso "Conteúdo informativo. Não constitui recomendação de investimento.", prazo
> "até 30/11, 23h59", "consulte condições", e preço/desconto como `[X]%` / `R$ [PREÇO]` até
> confirmação. Visual escuro/sóbrio com **print real do app** (tom de voz TradeMap).

### Meta Ads (pago)

| # | Formato | Medida | Qtd | Uso / ângulo |
|---|---|---|---|---|
| M1 | Estático Feed | 1080×1350 (4:5) | 4 | Oferta (%), produto (dados em tempo real), win-back ("volte"), upsell mensal → anual |
| M2 | Estático Stories/Reels | 1080×1920 (9:16) | 4 | Os mesmos 4 ângulos de M1, adaptados (zona segura: 250px em cima e embaixo) |
| M3 | Carrossel | 1080×1080 (1:1), 4–5 cards | 1 | "O que o plano anual libera": um recurso por card |
| M4 | Vídeo curto / motion | 9:16, 6–15s | 2 | Tela do app em uso + oferta (screen recording animado, sem locução) |
| M5 | Variação "últimas horas" | 4:5 e 9:16 | 2 | Cyber Monday, encerra 23h59 (só no dia 30/11) |
| M6 | Esquenta (sem preço) | 4:5 e 9:16 | 2 | "Black Friday TradeMap vem aí" (sobe 24/11) |
| M7 | Textos de anúncio | Texto principal (≤125 caracteres visíveis), título (≤40), descrição | 3 variações por ângulo | Para os 4 ângulos + "últimas horas" |
| | **Subtotal Meta** | | **15 arquivos + textos** | |

### Canais próprios

| # | Canal | Formato | Qtd | Observação |
|---|---|---|---|---|
| E | E-mail (Wake) | HTML (600px) + assunto + pré-header (2 variações de assunto cada) | **7** (E1–E7) | E3 e E6 com 3 versões de ângulo (free / ex-assinante / mensal). Hero 1200×600 por e-mail |
| P | Push | Título (≤40 caracteres) + texto (≤120 caracteres) + deep link | **8** (P1–P8) | Duas variações para P3 e P7 (teste A/B) |
| I1 | In-app | Modal / pop-up (≈1080×1350 ou conforme o SDK `[VALIDAR]`) | **2** | Abertura da BF (27/11) e último dia (30/11) |
| I2 | In-app | Banner na home (medida conforme o app `[VALIDAR]`) | **2** | Esquenta (24–26/11) e oferta (27–30/11) |
| O1 | Instagram orgânico | Post Feed/Reels 4:5 ou 9:16 | **3** | Anúncio da BF (24/11), abertura (27/11), Cyber Monday (30/11). Os de 27 e 30 também viram impulsionamento (C3) |
| O2 | Instagram orgânico | Stories 1080×1920 | **~12** | Contagem regressiva (5), recursos do app (4), lembrete com link (3). Podem ser templates com o número trocado |
| L | Landing / checkout | Banner topo da página de planos (desktop 1920×480, mobile 750×750) | **2** | Mesmo key visual. Prazo e "consulte condições" visíveis |

### Opcional (cenário recomendado/agressivo)

| # | Canal | Formato | Qtd |
|---|---|---|---|
| G | Google Search (marca) | Anúncio responsivo: 15 títulos (≤30 caracteres) + 4 descrições (≤90 caracteres) | 1 grupo |

**Ordem de produção (prazo):** 1) M6 + E1 + I2 esquenta + O1 do dia 24 (até 24/11 9h);
2) M1–M4 + M7 (até 25/11 15h, para dar tempo de compliance e revisão da Meta);
3) E2–E7, P1–P8, I1, L (até 26/11 12h); 4) M5 + variações de stories (até 26/11 18h).
