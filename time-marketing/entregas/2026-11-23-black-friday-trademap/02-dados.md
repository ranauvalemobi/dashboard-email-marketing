# 02 — Dados & CRM · Black Friday TradeMap 2026

> Autor: analista de Dados & CRM · 23/11/2026
> Brief: `00-brief.md` · `utm_campaign=bf2026-trademap`

## 0. Status dos dados (leia primeiro)

| Item | Situação |
|---|---|
| Planilhas da base (Wake, compras, assinaturas) | **Não recebidas.** Nenhum número deste documento é dado real da base. |
| Histórico de campanhas TradeMap (`historico.md`) | Vazio. Não há baseline interno registrado. |
| Tamanhos de segmento | Critérios definidos; tamanhos = `[VALIDAR]` (extrair no CRM/Wake). |
| Taxas de conversão | **Hipóteses** do time, sinalizadas como estimativa. |
| Benchmarks de mercado | Citados como **referência externa**, nunca como dado da base. |

Legenda: **[REAL]** = dado confirmado da base · **[ESTIMATIVA]** = hipótese do time ·
**[REF. MERCADO]** = benchmark externo · `[VALIDAR]` = precisa de confirmação interna.

---

## 1. Segmentação

Regras gerais para todos os segmentos de e-mail e push:
- Consentimento de marketing válido para o canal + e-mail válido (sem hard bounce nos últimos 90 dias).
- Fora de qualquer lista de supressão (descadastro, reclamação de spam, pedido de exclusão LGPD).
- **Exclui quem já tem plano anual ativo** e quem comprou o anual durante a campanha (ver §3.2).
- Prioridade quando a pessoa cai em mais de um segmento: S3 > S2 > S1 (vale o segmento com a
  oferta mais específica; ela recebe só uma versão de cada e-mail).

| # | Segmento | Critério objetivo | Tamanho estimado | Prioridade |
|---|---|---|---|---|
| S1a | **Free engajado (alta)** | Plano free, nunca pagou, ≥8 sessões nos últimos 30 dias **e** ≥1 sessão nos últimos 7 dias | `N_S1a` `[VALIDAR]` | 1 |
| S1b | **Free engajado (média)** | Plano free, nunca pagou, 3–7 sessões nos últimos 30 dias **e** ≥1 sessão nos últimos 14 dias | `N_S1b` `[VALIDAR]` | 1 |
| S2 | **Ex-assinante (win-back)** | Assinatura (mensal ou anual) cancelada/expirada há 30 dias a 18 meses; não pagante hoje; **excluir** quem cancelou com estorno/chargeback ou reclamação formal | `N_S2` `[VALIDAR]` | 2 |
| S3 | **Assinante mensal → anual (upsell)** | Assinatura mensal ativa, ≥2 renovações pagas (≥60 dias de casa), sem inadimplência | `N_S3` `[VALIDAR]` | 3 |
| S4 | **Aquisição Meta Ads** | Remarketing: visitantes do site/página de planos nos últimos 30 dias (pixel) + engajados do Instagram 60 dias. Lookalike 1–3%: semente = assinantes anuais ativos | definido pela mídia (`03-midia.md`) | 4 |
| — | **Fora da campanha (cadastrado inativo)** | Free sem sessão há >30 dias | `N_inativo` `[VALIDAR]` | Não entra na régua de BF (risco de spam/descadastro). Reativação fica para outra campanha. |

Observações:
- Os cortes de sessões (8 / 3) são **[ESTIMATIVA]**: o ideal é ajustar pela distribuição real
  (S1a ≈ quartil superior de frequência dos free ativos). `[VALIDAR com a base]`
- S3 só entra se a oferta valer para migração mensal → anual (com crédito pró-rata ou não).
  `[VALIDAR: regra de migração e cobrança]`
- S4 (públicos de Meta): subir lista de clientes (hash) para Custom Audience exige base legal
  confirmada. `[VALIDAR com DPO]`. Lista de **supressão** no Meta = assinantes anuais ativos +
  compradores da campanha (atualizada diariamente).
- **Grupo de controle (holdout)**: separar aleatoriamente **5% de S1a+S1b** que **não recebe**
  e-mail nem push da BF (pode ver a oferta no app/site). Serve para medir o efeito incremental
  real da régua. S2 e S3 sem holdout (bases menores, e o ganho de margem vale mais que a medição).
  Se `N_S1a + N_S1b < 20.000`, dispensar o holdout (leitura ficaria sem poder estatístico).

---

## 2. Meta da campanha

### 2.1 KPI principal
**Nº de novas assinaturas do plano anual entre 24/11 00:00 e 30/11 23:59** (todas as origens,
inclusive upgrades S3), líquido de estornos em até 7 dias.

### 2.2 Meta proposta (fórmula — preencher com a base)

**Meta top-down (recomendada como meta oficial):**

```
Baseline_7d   = média diária de novas assinaturas anuais de 26/10 a 22/11 (4 semanas) × 7
Meta_total    = Baseline_7d × 3
```
- Multiplicador 3× = **[ESTIMATIVA]** do time para semana de Black Friday com desconto relevante
  em produto digital por assinatura. Ajustar se houver histórico de BF 2024/2025 do TradeMap.
  `[VALIDAR: existe resultado de BF anterior?]`
- Faixas: conservador 2× · base 3× · otimista 4×.

**Meta bottom-up por segmento (para conferir se a top-down é factível):**

```
Novas_anuais = Σ ( N_segmento × (1 − holdout) × taxa_conversão_segmento ) + Novas_anuais_S4 + Orgânico
```

| Segmento | Taxa de conversão na semana (conservador / base / otimista) | Base da hipótese |
|---|---|---|
| S1a Free engajado alta | 1,5% / 3% / 5% | [ESTIMATIVA] |
| S1b Free engajado média | 0,5% / 1% / 2% | [ESTIMATIVA] |
| S2 Ex-assinante | 1% / 2,5% / 4% | [ESTIMATIVA] |
| S3 Mensal → anual | 4% / 8% / 12% | [ESTIMATIVA] |
| S4 Meta Ads | definido em `03-midia.md` (verba ÷ CPA) | — |
| Orgânico | = Baseline_7d (vendas que aconteceriam sem campanha) | fórmula |

Taxa = compradores do anual no período ÷ pessoas elegíveis do segmento (não ÷ aberturas).
Se Σ bottom-up ficar muito abaixo da meta top-down, a meta top-down está agressiva: ficar com
o menor dos dois e reportar a diferença.

### 2.3 KPIs de apoio

| KPI | Fórmula | Meta proposta | Fonte da meta |
|---|---|---|---|
| Taxa de entrega | entregues ÷ enviados | ≥ 98% | [REF. MERCADO] boas práticas de entregabilidade |
| Taxa de abertura | aberturas únicas ÷ entregues | Acompanhar, não usar como meta principal | [REF. MERCADO] ~20–27% em serviços financeiros (benchmarks públicos de ESPs, ex.: Mailchimp/Campaign Monitor) `[VALIDAR fonte/ano]`. Inflada pela proteção de privacidade do Apple Mail. |
| CTR (clique ÷ entregue) | cliques únicos ÷ entregues | ≥ 2% | [REF. MERCADO] ~2–3% em serviços financeiros `[VALIDAR fonte/ano]` |
| Conversão do e-mail (método do dashboard) | quem abriu **e** assinou anual ÷ quem abriu | ≥ 2% ("boa") · ≥ 3% ("excelente") | Faixas internas codificadas em `dashboard_final_v1.py` — não são benchmark de mercado |
| Descadastro por envio | descadastros ÷ entregues | ≤ 0,3% | [REF. MERCADO] |
| Reclamação de spam | reclamações ÷ entregues | ≤ 0,1% | [REF. MERCADO] limite usado por Gmail/Yahoo para remetentes em massa |
| Receita da campanha | Σ valor líquido das assinaturas anuais no período | `Meta_total × R$ [PREÇO]` | depende do preço `[VALIDAR]` |
| Uplift incremental (S1) | conv(S1 que recebeu) − conv(holdout S1) | > 0 com significância | holdout §1 |
| Mix anual × mensal | novas anuais ÷ (novas anuais + novas mensais) | acima do mix das 4 semanas anteriores | fórmula, baseline interno |

---

## 3. Régua de e-mails do período

### 3.1 Calendário

Horários sugeridos (BRT) `[ESTIMATIVA — ajustar ao melhor horário histórico da Wake]`.

| ID | Data | Hora | Momento | Quem recebe | Objetivo |
|---|---|---|---|---|---|
| E01 | ter 24/11 | 10h | Esquenta 1 — "vem aí" | S1a, S1b, S2, S3 | Gerar expectativa; **teste A/B de assunto** (§5) |
| E02 | qui 26/11 | 18h | Esquenta 2 — "é amanhã" | S1a, S1b, S2, S3 | Lembrar a data; vencedor do A/B no assunto |
| E03 | sex 27/11 | 08h | **Abertura Black Friday** | S1a, S1b, S2, S3 | Oferta no ar, CTA direto para checkout do anual |
| E04 | sex 27/11 | 19h | Lembrete BF (só quentes) | Quem **clicou** em E01–E03 e não comprou | Recuperar intenção do dia |
| E05 | sáb 28/11 | 10h | Fim de semana | S1a, S2, S3 + quem abriu/clicou qualquer e-mail (S1b) | Reforço com benefício diferente (ex.: carteira consolidada) |
| E06 | seg 30/11 | 09h | **Cyber Monday — último dia** | S1a, S1b, S2, S3 | Urgência real: "termina hoje às 23h59" |
| E07 | seg 30/11 | 19h | Última chance (só quentes) | Quem **clicou** em qualquer e-mail da campanha e não comprou | Fechamento; prazo final |

- Domingo 29/11 sem e-mail (só push/in-app e Meta Ads), para controlar frequência.
- Teto de frequência: S1b recebe no máximo 4 e-mails (E01, E02, E03, E06) se não abrir/clicar
  em nenhum. Ninguém recebe mais de 2 e-mails no mesmo dia.
- Push/in-app seguem as mesmas datas e a mesma regra de exclusão (detalhe com o redator/mídia).
- E04 e E07 dependem de a Wake permitir segmentar por clique em envios anteriores
  `[VALIDAR com a operação da Wake]`; se não der, enviar E07 para S1a + S2 + S3.

### 3.2 Regra de exclusão de quem já comprou (obrigatória)

**Antes de cada envio** (e-mail e push), aplicar a lista de supressão:

```
Supressão = assinantes anuais ativos (antes de 24/11)
          ∪ quem assinou o anual entre 24/11 00:00 e o momento do envio
          ∪ (para S3) quem migrou de mensal → anual no período
          ∪ holdout S1 (5%)
          ∪ descadastros, hard bounces, reclamações de spam, pedidos LGPD
```

Operação:
1. Exportar compradores do anual (sistema de pagamentos/assinaturas) **até 2h antes de cada
   envio** e subir na Wake como lista de supressão `bf2026-compradores`. Idealmente via
   integração automática; se for manual, definir responsável para **sex 27/11 18h, sáb 28/11
   9h e seg 30/11 8h e 18h**. `[VALIDAR: dono da tarefa e se existe integração]`
2. Mesma lista vira audiência de exclusão no Meta Ads (atualização diária).
3. Comprador sai **de toda a régua**; após a compra, entra só no e-mail transacional/onboarding
   do plano anual (fora desta campanha).
4. A lista de supressão é operacional: **não salvar no repositório** (LGPD). Registrar apenas a
   contagem (ex.: "312 suprimidos em 28/11").

---

## 4. Plano de mensuração

### 4.1 Padrão de UTMs

| Parâmetro | Regra | Valores |
|---|---|---|
| `utm_source` | origem | `wake` · `push` · `inapp` · `meta` · `instagram` |
| `utm_medium` | tipo de canal | `email` · `push` · `inapp` · `paid_social` · `organic_social` |
| `utm_campaign` | fixo | **`bf2026-trademap`** |
| `utm_content` | peça + variante | `e01-esquenta-a`, `e01-esquenta-b`, `e03-abertura`, `p01-bf`, `ad-remkt-v1` … |
| `utm_term` | segmento | `s1a`, `s1b`, `s2`, `s3`, `remkt`, `lal` |

Tudo em minúsculas, sem acento, hífen como separador. Exemplos:

```
https://trademap.com.br/<pagina-oferta>?utm_source=wake&utm_medium=email&utm_campaign=bf2026-trademap&utm_content=e01-esquenta-a&utm_term=s1a
https://trademap.com.br/<pagina-oferta>?utm_source=push&utm_medium=push&utm_campaign=bf2026-trademap&utm_content=p03-abertura&utm_term=s2
https://trademap.com.br/<pagina-oferta>?utm_source=meta&utm_medium=paid_social&utm_campaign=bf2026-trademap&utm_content=ad-remkt-v1&utm_term=remkt
```

`[VALIDAR: URL da página da oferta; se links abrem o app via deep link, confirmar que a UTM é
preservada até o checkout — depende da ferramenta de atribuição mobile]`

Tabela de links por e-mail:

| E-mail | `utm_content` | `utm_term` |
|---|---|---|
| E01 | `e01-esquenta-a` / `e01-esquenta-b` | segmento do destinatário |
| E02 | `e02-esquenta-amanha` | idem |
| E03 | `e03-abertura` | idem |
| E04 | `e04-lembrete-bf` | idem |
| E05 | `e05-fim-de-semana` | idem |
| E06 | `e06-cyber-monday` | idem |
| E07 | `e07-ultima-chance` | idem |

### 4.2 Eventos a acompanhar

| Etapa | Evento | Onde |
|---|---|---|
| E-mail | enviado, entregue, aberto, clicado, descadastro, spam, bounce | Wake |
| Site/app | `view_offer_bf` (página da oferta) | analytics web/app |
| Site/app | `begin_checkout` (plano, periodicidade) | analytics web/app |
| Compra | `purchase` / `subscription_start` com plano, periodicidade (anual), valor, cupom, UTM | sistema de assinaturas + analytics |
| Pós-compra | estorno/cancelamento em até 7 dias | sistema de assinaturas |

`[VALIDAR: nomes reais dos eventos e se o evento de compra carrega a UTM]`

### 4.3 Janela de atribuição
- **Oficial (KPI principal):** toda nova assinatura anual de 24/11 00:00 a 30/11 23:59.
- **Por canal:** último clique com UTM `bf2026-trademap` até 7 dias antes da compra.
- **E-mail (método do dashboard):** pessoa que **abriu** algum e-mail da campanha e assinou o
  anual no período (24/11–30/11). É atribuição por abertura — mais generosa que último clique.
- **Incremental:** diferença entre quem recebeu e o holdout (§1).
- Fechamento definitivo em **07/12** (D+7), descontando estornos.

---

## 5. Teste A/B recomendado

| Item | Definição |
|---|---|
| Hipótese | Um assunto com **prazo concreto** ("Black Friday TradeMap: [X]% off no anual, de 27 a 30/11") gera mais cliques do que um assunto de **benefício** ("Sua carteira inteira num lugar só — e mais barato na Black Friday") porque, na semana de BF, a caixa de entrada está saturada e data clara ajuda a decidir. |
| Variável única | Linha de assunto (pré-header, corpo, oferta e horário iguais). |
| Onde | E01 (esquenta, 24/11), S1a + S1b, divisão aleatória 50/50 (fora do holdout). |
| Métrica de decisão | **CTR (clique único ÷ entregue)** — não abertura, por causa da inflação do Apple Mail. |
| Amostra mínima | Para detectar 2% → 3% de CTR (α = 5%, poder = 80%): **~3.800 por variante (~7.700 no total)**. Para detectar 2% → 2,5%: ~13.800 por variante. |
| Leitura | qua 25/11, 10h (24h após o envio). Vencedor vai para os assuntos de E02 e E03. |
| Se não houver amostra | Se S1a+S1b < 7.700 entregáveis, rodar o teste mesmo assim e tratar como **direcional**; sem diferença clara, usar a versão com prazo (mais alinhada à urgência do período). |

---

## 6. Régua de leitura

| Quando | O que olhar | Se ficar abaixo, fazer |
|---|---|---|
| **D+1 de cada envio** (manhã seguinte) | Entrega, CTR, descadastro, spam por segmento | CTR < 1% → trocar assunto/hero do próximo envio · descadastro > 0,5% ou spam > 0,1% no segmento → cortar o próximo envio para quem não abriu nada · entrega < 95% → checar domínio/listas com a Wake |
| **qua 25/11, 10h** | Resultado do A/B (E01) | Aplicar vencedor em E02/E03 |
| **sáb 28/11, 9h** (D+1 da BF) | Novas anuais acumuladas × meta | Ritmo < 50% da meta → antecipar push extra no domingo, reforçar remarketing no Meta, incluir S1b no E05 · Ritmo > 100% → manter, não aumentar frequência |
| **ter 01/12** (D+1 do fim) | Resultado do período por segmento e canal (UTM) | Rodar o dashboard (§7) com os dados do período |
| **seg 07/12** (D+7) | Fechamento: estornos, holdout, receita líquida | Registrar em `conhecimento/trademap/historico.md` (só agregados) |

---

## 7. Como ler a conversão do e-mail com `dashboard_final_v1.py`

O dashboard (Streamlit) cruza **quem abriu o e-mail na Wake** com **quem comprou**, pelo e-mail
(normalizado em minúsculas e sem espaços), e mostra: abriram, converteram, taxa de conversão
(convertidos ÷ abriram), receita, "abriram e não compraram" e "compraram sem abrir".

### 7.1 Preparar os arquivos (fora do repositório)
1. **Arquivo Wake:** exportar quem **abriu** qualquer e-mail com `utm_campaign=bf2026-trademap`
   (E01–E07) em uma planilha `.xlsx`/`.csv`, com uma coluna cujo nome contenha `email` ou `mail`.
   Duplicatas são removidas pelo próprio script.
2. **Arquivo de compras:** exportar assinaturas **apenas do TradeMap, plano anual, aprovadas,
   entre 24/11 00:00 e 30/11 23:59**, sem estornos. Precisa de coluna com `email`/`mail` e, para
   receita, uma coluna com `valor`, `value`, `amount` ou `price` no nome.
   - **Importante:** o script **não filtra por data, produto nem plano**. Esse filtro tem que vir
     pronto na exportação; senão, a conversão fica inflada.
3. Salvar os dois arquivos numa pasta local fora do repositório (ex.: `~/Downloads/bf2026/`).
   **Nunca** commitar exportações nem os CSVs baixados no dashboard (contêm e-mails — LGPD).

### 7.2 Rodar
```bash
cd /home/user/dashboard-email-marketing
pip install -r requirements.txt
streamlit run dashboard_final_v1.py
```
No navegador: nome da campanha = "BF 2026 TradeMap"; upload do arquivo Wake em "Quem ABRIU" e do
arquivo de compras em "Quem COMPROU".

### 7.3 Leituras recomendadas
| Leitura | Como rodar | O que significa |
|---|---|---|
| Conversão geral do e-mail | Wake = abriu E01–E07 | Taxa = KPI "conversão do e-mail" (meta ≥ 2%) |
| Por segmento | Uma exportação Wake por segmento (S1a, S1b, S2, S3), mesmo arquivo de compras | Mostra onde a régua funcionou |
| Por e-mail | Wake = abriu só E03 (ou só E06) | Peso de cada disparo (com sobreposição entre e-mails) |
| **Incrementalidade (S1)** | Rodar 2× trocando o "arquivo Wake": (a) **entregues** de S1 · (b) lista do **holdout** S1 | Taxa(a) − Taxa(b) = efeito real do e-mail. Usar "entregues" (não "abriu") nas duas para comparar igual com igual |
| Follow-up | Aba "Não Compraram" | Base para push/in-app pós-campanha — **não** baixar o CSV para o repositório |

### 7.4 Limitações a considerar na leitura
- O título/rodapé do dashboard diz "Minhas Economias", mas a lógica é genérica e serve para o
  TradeMap.
- **Correlação, não causa:** quem abriu já era mais propenso a comprar. A medida causal é o
  holdout.
- Aberturas infladas pelo Apple Mail (privacidade) aumentam o denominador e **reduzem** a taxa;
  a conversão do dashboard tende a ser conservadora.
- Faixas "boa" (≥2%) e "excelente" (≥3%) são regras fixas no código, não benchmark do setor.
- "Compraram sem abrir" = vendas vindas de outros canais (push, in-app, Meta, orgânico) — cruzar
  com UTM para atribuir.
- Registrar no `historico.md` apenas os agregados (abriram, converteram, taxa, receita).

---

## 8. Premissas e pendências `[VALIDAR]`
- Tamanhos de S1a, S1b, S2, S3 e da base inativa.
- Baseline de novas assinaturas anuais (26/10–22/11) e resultado de BF anteriores, se houver.
- % de desconto, preço final e regra de migração mensal → anual.
- Integração (ou responsável) para atualizar a supressão de compradores antes de cada envio.
- Wake: segmentação por clique em envio anterior (E04, E07) e suporte a A/B de assunto.
- URL da oferta, deep link e preservação de UTM no app; nomes dos eventos de compra.
- Base legal para Custom Audience com lista de clientes no Meta (DPO).
