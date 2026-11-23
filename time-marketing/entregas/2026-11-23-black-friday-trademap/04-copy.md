# 04 — Copy · Black Friday TradeMap 2026

> Autor: redator(a) · 23/11/2026 · Status: **rascunho para revisão de compliance (`06-compliance.md`)**
> Base: `00-brief.md`, `01-produto.md`, `02-dados.md`, `03-midia.md`, `conhecimento/trademap/tom-de-voz.md`,
> `conhecimento/compliance/regras.md`.

## 0. Como usar este documento

- **Conceito de copy: "Decida com dados o ano inteiro."** A Black Friday é o momento de fechar o
  ano e planejar 2027. O plano anual vira "12 meses de dado completo", e a oferta entra como o
  empurrão para tomar uma decisão que a pessoa já está perto de tomar. Assinatura de campanha:
  **"Black Friday TradeMap. Decida com dados o ano inteiro."**
- Ângulo principal **A** (um ano de decisões com dados) em todos os canais próprios; **C** (tudo
  num lugar só) no fim de semana e no win-back; **B** (informação de nível profissional, preço de
  pessoa física) nos anúncios de prospecção.
- **Placeholders:** `[X]%` = desconto · `R$ [PREÇO]` = preço final do anual · `R$ [Y]` =
  equivalente mensal (só se o produto confirmar a conta e a forma de cobrança) ·
  `[VALIDAR: nome do plano]` = nome comercial do plano em oferta · `[NOME]` = merge tag da Wake
  (fallback: "Olá," sem nome) · `[link]` = URL da oferta com UTM (padrão em `02-dados.md` §4.1).
- **Contagem de caracteres** (entre crases, `atual/limite`) inclui espaços e pontuação e foi feita
  **com os placeholders** (`[X]%` = 4 caracteres, `R$ [PREÇO]` = 10). Com os valores reais
  (ex.: "40%", "R$ 299,90") o texto fica igual ou menor. Se o nome real do plano entrar num
  item com limite, recontar.
- **Nenhuma peça com preço sobe antes da confirmação** de `[X]%`, `R$ [PREÇO]` e nome do plano.
  As peças de esquenta (E01, E02, P1, P2, I2-A, M6, O1-1, stories de contagem) **não dependem de
  preço** e podem sair em 24/11.
- Sem emojis nas peças (tom TradeMap: analítico, sem euforia). Sem citar ativos, sem "ganhe",
  "lucre", "garantido", "sem risco", "menor preço do ano/da história", "última vez".
- **Calendário seguido:** a régua de e-mail segue `02-dados.md` §3.1 (E01–E07, horários e
  públicos). Push, in-app, Meta e Instagram seguem `03-midia.md` §5 e §9. Divergências entre os
  dois documentos estão no fim (§9 Pendências).

### Avisos legais (blocos padrão, usar exatamente como abaixo)

**AL-1 · Aviso de informação de mercado (todas as peças):**
> Conteúdo informativo. Não constitui recomendação de investimento.

**AL-2 · Oferta com prazo (todas as peças com oferta):**
> Oferta válida para novas assinaturas do plano anual [VALIDAR: nome do plano] feitas de
> 27/11/2026, 00h00, a 30/11/2026, 23h59 (horário de Brasília). Consulte as condições em [link].

**AL-2 curto (peças com pouco espaço: arte de anúncio, stories, banner):**
> Até 30/11, 23h59. Consulte condições.

**AL-3 · Rodapé de e-mail (todos os e-mails):**
> Você recebe este e-mail porque tem uma conta no TradeMap e autorizou o envio de comunicações.
> Não quer mais receber? [Descadastre-se aqui]. · Conteúdo informativo. Não constitui
> recomendação de investimento. · [Endereço e CNPJ da Valemobi `VALIDAR`]

> Em e-mails de **esquenta** (E01, E02), o AL-2 entra na versão sem preço: "A condição da Black
> Friday TradeMap vale de 27/11/2026, 00h00, a 30/11/2026, 23h59 (horário de Brasília). Detalhes
> e condições serão divulgados na abertura."

---

## 1. E-mails (Wake) — régua E01 a E07

Formato de cada e-mail: 3 opções de assunto (≤ 45 caracteres), 1 pré-header, corpo, CTA. Link de
todos os CTAs: `[link]` com `utm_source=wake&utm_medium=email&utm_campaign=bf2026-trademap&utm_content=<id>&utm_term=<segmento>`.

### E01 · ter 24/11, 10h · Esquenta 1 "vem aí" · S1a, S1b, S2, S3 · **teste A/B de assunto**

**Teste A/B (S1a + S1b, 50/50, decisão por CTR em 25/11 10h — `02-dados.md` §5).** Só o assunto
muda; pré-header, corpo e horário iguais.

| Variante | Hipótese | Assunto | `utm_content` |
|---|---|---|---|
| **A · prazo** | Data clara ajuda a decidir na caixa saturada | Black Friday TradeMap: de 27 a 30/11 `36/45` | `e01-esquenta-a` |
| **A' · prazo + %** (só se o desconto for confirmado até 24/11, 9h) | Idem, com o número | Black Friday TradeMap: [X]% off no anual `40/45` | `e01-esquenta-a` |
| **B · benefício** | Benefício concreto chama quem já usa | Tudo num só lugar, por menos, na Black Friday `45/45` | `e01-esquenta-b` |

> Variante B adaptada da hipótese de `02-dados.md` §5 ("Sua carteira inteira num lugar só — e
> mais barato na Black Friday", 65 caracteres, acima do limite). Para S2 e S3 (fora do teste), usar a variante A.

**Opções extras de assunto** (reserva, caso o teste precise ser refeito):
1. Vem aí: Black Friday TradeMap `29/45`
2. Sexta começa a Black Friday TradeMap `36/45`

**Pré-header:** Uma condição especial no plano anual começa na sexta. Fique de olho no seu e-mail. `82/90`

**Corpo:**

> Olá, [NOME].
>
> Na sexta-feira, 27/11, começa a **Black Friday TradeMap**.
>
> Durante quatro dias, até segunda-feira, 30/11, às 23h59, o plano anual do TradeMap
> [VALIDAR: nome do plano] terá uma condição especial. Os detalhes chegam aqui, no seu e-mail,
> na abertura.
>
> **Por que olhar o plano anual agora?** Porque 2027 tem 12 meses de mercado, e você pode
> acompanhar cada um deles com o dado completo:
>
> - Cotações e notícias do mercado em tempo real
> - Fundamentos das empresas para comparar com clareza
> - Sua carteira de várias corretoras consolidada numa tela só
>
> `[VALIDAR: lista oficial de recursos do plano em oferta × plano gratuito]`
>
> **[Linha por segmento, opcional]**
> - S1a/S1b: "Você já acompanha o mercado com o TradeMap. Em 2027, dá para fazer isso sem os limites do plano gratuito."
> - S2: "Você já foi assinante e sabe como é decidir com o dado completo. Vale ficar de olho na sexta."
> - S3: "Você já é assinante mensal. Na sexta, vale comparar com calma: o anual pode sair mais em conta. `[VALIDAR: regra de migração]`"
>
> Até sexta.
> Equipe TradeMap

**CTA (botão):** Ver o que o plano anual libera `30/30` → página de planos

**Rodapé:** AL-2 versão esquenta + AL-3.

---

### E02 · qui 26/11, 18h · Esquenta 2 "é amanhã" · S1a, S1b, S2, S3

Assunto: aplicar o **estilo vencedor do A/B** de E01.

| Estilo | Opções |
|---|---|
| Se vencer **prazo** | 1. É amanhã: Black Friday TradeMap `31/45` · 2. Amanhã, 00h: começa a Black Friday TradeMap `43/45` |
| Se vencer **benefício** | 3. Amanhã: 2027 inteiro com o dado completo `40/45` |

**Pré-header:** A partir da 0h de sexta, o plano anual entra em condição especial. Vale até 30/11. `82/90`

**Corpo:**

> Olá, [NOME].
>
> Amanhã, sexta-feira, 27/11, à 0h, começa a **Black Friday TradeMap**.
>
> A condição especial no plano anual do TradeMap [VALIDAR: nome do plano] fica no ar até
> segunda-feira, 30/11, às 23h59 (horário de Brasília). Nem um minuto a mais.
>
> Se você usa o TradeMap para acompanhar o mercado, a pergunta é simples: como você quer decidir
> em 2027? Com parte dos dados ou com o dado completo, num só lugar?
>
> Amanhã cedo você recebe a oferta completa aqui.
>
> Equipe TradeMap

**Bloco opcional "acesso antecipado"** (só se o produto aprovar liberar a oferta antes para a
base, conforme `03-midia.md` §5) `[VALIDAR]`:
> "Como você já usa o TradeMap, liberamos a sua condição algumas horas antes: ela já está
> disponível a partir de [HORA] de hoje. [Ver minha condição]"

**CTA (botão):** Conhecer o plano anual `22/30`

**Rodapé:** AL-2 versão esquenta + AL-3.

---

### E03 · sex 27/11, 08h · **Abertura Black Friday** · 3 versões por segmento

Assunto: estilo vencedor do A/B (mesmas opções para os três segmentos, com a opção 3 específica).

| Segmento | Assunto 1 (prazo) | Assunto 2 (benefício) | Assunto 3 (segmento) |
|---|---|---|---|
| S1 · Free engajado | Começou: [X]% off no plano anual `32/45` | Decida com dados o ano inteiro. [X]% off `40/45` | O dado completo, 12 meses, [X]% off `35/45` |
| S2 · Ex-assinante | Começou: [X]% off no plano anual `32/45` | Decida com dados o ano inteiro. [X]% off `40/45` | Volte ao TradeMap com [X]% off no anual `39/45` |
| S3 · Mensal → anual | Começou: [X]% off no plano anual `32/45` | Decida com dados o ano inteiro. [X]% off `40/45` | Troque para o anual com [X]% off `32/45` |

**Pré-header (os três):** Black Friday TradeMap no ar. Plano anual por R$ [PREÇO] até 30/11, 23h59. `73/90`

#### E03-S1 · Free engajado (ângulo A)

> Olá, [NOME].
>
> A **Black Friday TradeMap** começou.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
> `[VALIDAR: exibir "equivale a R$ [Y] por mês" só se o produto confirmar a conta e a cobrança]`
>
> Você já abre o TradeMap para acompanhar o mercado. Com o plano anual, faz isso o ano inteiro
> com o dado completo, sem esbarrar nos limites do plano gratuito:
>
> - **Mercado em tempo real:** cotações e notícias no momento em que acontecem
> - **Fundamentos:** dados das empresas para comparar e entender o contexto
> - **Carteira consolidada:** suas posições de várias corretoras numa tela só
>
> `[VALIDAR: lista free × pago e recursos exclusivos do plano]`
>
> O TradeMap não recomenda ativos nem promete resultado. Ele entrega informação para você
> decidir com clareza.
>
> A condição vale até segunda-feira, 30/11, às 23h59.

**CTA:** Assinar o plano anual `21/30` · `utm_content=e03-abertura`

#### E03-S2 · Ex-assinante (ângulo C + A)

> Olá, [NOME].
>
> A **Black Friday TradeMap** começou, e esta é a hora de voltar.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Você já conhece o TradeMap por dentro: cotações, notícias, fundamentos e a sua carteira de
> várias corretoras consolidada, tudo numa tela só. Menos abas abertas, mais clareza para decidir.
>
> `[VALIDAR: incluir "Sua conta continua aqui" só se o histórico/carteira for preservado após o cancelamento]`
>
> Com o anual, são 12 meses de dado completo para atravessar 2027, com uma assinatura só.
>
> A condição vale até segunda-feira, 30/11, às 23h59.
> `[VALIDAR: a oferta vale para ex-assinantes?]`

**CTA:** Voltar com [X]% off `19/30` · `utm_content=e03-abertura`

#### E03-S3 · Assinante mensal → anual (ângulo A, econômico)

> Olá, [NOME].
>
> Você já decide com o TradeMap todo mês. Na **Black Friday TradeMap**, dá para fazer isso pagando
> menos.
>
> **Troque para o plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Na comparação com 12 meses no plano mensal, a diferença é de R$ [ECONOMIA].
> `[VALIDAR: cálculo real da economia e regra de migração — crédito proporcional do mês atual?]`
>
> Os mesmos dados, a mesma conta, a mesma carteira. Só muda a forma de pagar, e você tira 2027
> inteiro da lista de renovações.
>
> A condição vale até segunda-feira, 30/11, às 23h59.

**CTA:** Trocar para o anual `19/30` · `utm_content=e03-abertura`

**Rodapé (os três):** AL-1 + AL-2 + AL-3.

---

### E04 · sex 27/11, 19h · Lembrete BF · quem **clicou** em E01–E03 e não comprou

**Assuntos:**
1. Ficou para depois? O anual segue com [X]% off `45/45`
2. Sua condição de Black Friday segue no ar `40/45`
3. [X]% off no anual: válido até segunda `37/45`

**Pré-header:** A condição da Black Friday continua no ar até segunda, 30/11, às 23h59. `71/90`

**Corpo:**

> Olá, [NOME].
>
> Hoje você deu uma olhada no plano anual do TradeMap. Se ficou para depois, tudo bem: a
> condição da Black Friday continua no ar.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Três perguntas que costumam aparecer:
>
> - **"Já tenho o app da corretora."** O app da corretora mostra o que está nela. O TradeMap
>   consolida suas posições de várias corretoras e traz dados e notícias independentes.
>   `[VALIDAR: lista de corretoras integradas]`
> - **"Vou usar o ano todo?"** Se você abre o app toda semana, são 12 meses de dado completo por
>   uma assinatura só. `[VALIDAR: política de cancelamento do anual, se houver, citar aqui]`
> - **"O TradeMap diz o que comprar?"** Não. O TradeMap não recomenda ativos nem promete
>   resultado. Ele entrega informação para você decidir com clareza.
>
> A condição vale até segunda-feira, 30/11, às 23h59.

**CTA:** Ver minha condição `18/30` · `utm_content=e04-lembrete-bf`

**Rodapé:** AL-1 + AL-2 + AL-3.

---

### E05 · sáb 28/11, 10h · Fim de semana (ângulo C) · S1a, S2, S3 + S1b que abriu/clicou

**Assuntos:**
1. Menos abas, mais clareza `24/45`
2. Várias corretoras, uma tela só `30/45`
3. Tudo num só lugar, com [X]% off no anual `40/45`

**Pré-header:** Cotações, notícias, fundamentos e carteira juntos. Plano anual com [X]% off até 30/11. `86/90`

**Corpo:**

> Olá, [NOME].
>
> Quantas abas você abre para acompanhar seus investimentos? O app de cada corretora, uma
> planilha, um site de notícias, outro de cotação.
>
> No TradeMap, fica tudo numa tela só:
>
> - **Carteira consolidada** de várias corretoras `[VALIDAR: free ou pago / corretoras integradas]`
> - **Mercado em tempo real**, no Brasil e lá fora
> - **Notícias e fundamentos** ao lado da cotação, para entender o contexto antes de decidir
>
> Menos tempo alternando entre apps. Mais clareza para decidir.
>
> Até segunda-feira, 30/11, às 23h59, o plano anual [VALIDAR: nome do plano] está com [X]% off:
> **R$ [PREÇO] por 12 meses.**
>
> **[Linha por segmento, opcional]**
> - S2: "Seu jeito de acompanhar o mercado, de volta num lugar só."
> - S3: "Você já tem tudo isso. No anual, paga menos por mês. `[VALIDAR cálculo]`"

**CTA:** Assinar o plano anual `21/30` · `utm_content=e05-fim-de-semana`

**Rodapé:** AL-1 + AL-2 + AL-3.

---

### E06 · seg 30/11, 09h · **Cyber Monday — último dia** · 3 versões por segmento

| Segmento | Assunto 1 (prazo) | Assunto 2 (benefício) | Assunto 3 (segmento) |
|---|---|---|---|
| S1 · Free engajado | Último dia: [X]% off no plano anual `35/45` | Termina hoje, 23h59: 2027 com dados `35/45` | Último dia do dado completo por menos `37/45` |
| S2 · Ex-assinante | Último dia: [X]% off no plano anual `35/45` | Termina hoje, 23h59: 2027 com dados `35/45` | Último dia para voltar com [X]% off `35/45` |
| S3 · Mensal → anual | Último dia: [X]% off no plano anual `35/45` | Termina hoje, 23h59: 2027 com dados `35/45` | Último dia para trocar para o anual `35/45` |

**Pré-header (os três):** Termina hoje, 30/11, às 23h59. Depois, o plano anual volta ao preço normal. `75/90`

#### E06-S1 · Free engajado

> Olá, [NOME].
>
> Hoje é o último dia da **Black Friday TradeMap**. A condição termina às 23h59.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Em 2027, você pode acompanhar o mercado como já faz hoje, só que com o dado completo:
> cotações e notícias em tempo real, fundamentos das empresas e sua carteira consolidada, tudo
> num só lugar.
>
> A partir de amanhã, o plano anual volta ao preço normal. `[VALIDAR: confirmar que o preço volta ao cheio em 01/12]`

**CTA:** Assinar antes das 23h59 `23/30` · `utm_content=e06-cyber-monday`

#### E06-S2 · Ex-assinante

> Olá, [NOME].
>
> Hoje é o último dia para voltar ao TradeMap com a condição da Black Friday. Termina às 23h59.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Cotações, notícias, fundamentos e sua carteira de várias corretoras de novo numa tela só, por
> 12 meses, com uma assinatura.
>
> A partir de amanhã, o plano anual volta ao preço normal.

**CTA:** Voltar antes das 23h59 `22/30` · `utm_content=e06-cyber-monday`

#### E06-S3 · Assinante mensal → anual

> Olá, [NOME].
>
> Hoje é o último dia para trocar o plano mensal pelo anual com a condição da Black Friday.
> Termina às 23h59.
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses**, R$ [ECONOMIA]
> a menos que 12 meses no mensal. `[VALIDAR: cálculo e regra de migração]`
>
> Mesma conta, mesmos dados, mesma carteira. Você só paga menos e esquece a renovação até o fim
> de 2027.

**CTA:** Trocar para o anual hoje `24/30` · `utm_content=e06-cyber-monday`

**Rodapé (os três):** AL-1 + AL-2 + AL-3.

---

### E07 · seg 30/11, 19h · Última chance · quem **clicou** em qualquer e-mail e não comprou

> Fallback (`02-dados.md` §3.1): se a Wake não segmentar por clique, enviar para S1a + S2 + S3.

**Assuntos:**
1. Termina às 23h59: [X]% off no plano anual `41/45`
2. Últimas horas da Black Friday TradeMap `38/45`
3. Até 23h59 de hoje. Depois, preço normal. `40/45`

**Pré-header:** Faltam poucas horas para a condição do plano anual terminar. Hoje, às 23h59. `76/90`

**Corpo:**

> Olá, [NOME].
>
> A Black Friday TradeMap termina **hoje, às 23h59** (horário de Brasília).
>
> **Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.**
>
> Se a decisão ainda está em aberto, faça como no mercado: olhe os dados. São 12 meses de
> cotações, notícias, fundamentos e carteira consolidada num só lugar, com uma assinatura só.
>
> Depois das 23h59, o plano anual volta ao preço normal.
>
> Equipe TradeMap

**CTA:** Assinar até 23h59 `17/30` · `utm_content=e07-ultima-chance`

**Rodapé:** AL-1 + AL-2 + AL-3.

---

## 2. Push (P1 a P8)

Limites: título ≤ 40 · texto ≤ 110 (regra do redator, mais restrita que os 120 de `03-midia.md`).
Deep link: tela da oferta/planos com `utm_source=push&utm_medium=push&utm_campaign=bf2026-trademap&utm_content=<id>`.
Mesma supressão de compradores dos e-mails.

> **Aviso legal no push:** o AL-1 completo (65 caracteres) não cabe junto da mensagem. Proposta:
> push leva prazo ("até 30/11, 23h59"), e o AL-1 + AL-2 aparecem na tela de destino do deep link.
> `[VALIDAR com compliance]`

| ID | Quando | Título (≤ 40) | Texto (≤ 110) | `utm_content` |
|---|---|---|---|---|
| P1 | qua 25/11, 19h | Black Friday TradeMap vem aí `28/40` | De 27 a 30/11, o plano anual terá uma condição especial. Fique de olho no app na sexta. `87/110` | `p01-esquenta` |
| P2 | qui 26/11, 20h | É amanhã: Black Friday TradeMap `31/40` | A partir da 0h de sexta, o plano anual entra em condição especial. Vale até 30/11, 23h59. `89/110` | `p02-amanha` |
| P3-A | sex 27/11, 08h | Começou: [X]% off no plano anual `32/40` | Black Friday TradeMap no ar. Decida com dados o ano inteiro. Até 30/11, 23h59. `78/110` | `p03-abertura-a` |
| P3-B | sex 27/11, 08h | 2027 inteiro com o dado completo `32/40` | Plano anual com [X]% off na Black Friday TradeMap. Condição válida até 30/11, 23h59. `84/110` | `p03-abertura-b` |
| P4 | sex 27/11, 20h | Plano anual com [X]% off `24/40` | Cotações, notícias, fundamentos e carteira numa tela só. Condição válida até 30/11, 23h59. `90/110` | `p04-bf-noite` |
| P5 | sáb 28/11, 11h | Menos abas, mais clareza `24/40` | Sua carteira de várias corretoras numa tela só. Plano anual com [X]% off até 30/11, 23h59. `90/110` | `p05-fim-de-semana` |
| P6 | dom 29/11, 18h | Amanhã é o último dia `21/40` | A Black Friday TradeMap termina segunda, 30/11, às 23h59. Plano anual com [X]% off. `83/110` | `p06-vespera-fim` |
| P7-A | seg 30/11, 12h | Último dia: [X]% off no anual `29/40` | A condição termina hoje, às 23h59. Depois, o plano anual volta ao preço normal. `79/110` | `p07-ultimo-dia-a` |
| P7-B | seg 30/11, 12h | Termina hoje, às 23h59 `22/40` | Último dia para assinar o plano anual do TradeMap com [X]% off. Decida com dados em 2027. `89/110` | `p07-ultimo-dia-b` |
| P8 | seg 30/11, 21h | Últimas horas: termina às 23h59 `31/40` | A Black Friday TradeMap acaba hoje. Plano anual com [X]% off só até 23h59. `74/110` | `p08-ultimas-horas` |

**A/B:** P3 testa oferta no título (A) × benefício no título (B); P7 testa número no título (A) ×
prazo no título (B). Métrica: abertura do push → `begin_checkout`.

**Variações por segmento (opcional, se a ferramenta de push segmentar):**

| Para | Título (≤ 40) | Texto (≤ 110) |
|---|---|---|
| S2 em P3 | Volte ao TradeMap com [X]% off `30/40` | Plano anual na Black Friday: cotações, notícias e sua carteira num só lugar. Até 30/11, 23h59. `94/110` |
| S3 em P3 | Troque para o anual com [X]% off `32/40` | Mesma conta, mesmos dados, pagando menos por mês. Condição válida até 30/11, 23h59. `83/110` |

---

## 3. In-app

Limites sugeridos até a confirmação do SDK `[VALIDAR]`: título ≤ 40, texto ≤ 110, botão ≤ 25.
Exibição: 1× por sessão; não exibir para quem já tem plano anual ou comprou na campanha.

### I2-A · Banner home · Esquenta (24–26/11)
- **Título:** Black Friday TradeMap: de 27 a 30/11 `36/40`
- **Texto:** Uma condição especial no plano anual começa na sexta. Fique de olho. `68/110`
- **Botão:** Saiba mais `10/25` → página de planos · `utm_content=i2-banner-esquenta`

### I2-B · Banner home · Oferta (27–30/11)
- **Título:** Plano anual com [X]% off `24/40`
- **Texto:** Decida com dados o ano inteiro. Até 30/11, 23h59. Consulte condições. `69/110`
- **Botão:** Ver oferta `10/25` · `utm_content=i2-banner-oferta`
- **Troca em 30/11 (opcional):** título Último dia: [X]% off no anual `29/40`

### I1-A · Modal · Abertura da BF (27/11)
- **Sobretítulo:** Black Friday TradeMap `21/30`
- **Título:** Decida com dados o ano inteiro `30/40`
- **Texto:** Plano anual com [X]% off: R$ [PREÇO] por 12 meses. Mercado em tempo real e carteira numa tela só. `97/110`
- **Botão principal:** Assinar o plano anual `21/25` · `utm_content=i1-modal-abertura`
- **Botão secundário:** Agora não `9/25`
- **Rodapé (fonte menor):** "Até 30/11, 23h59. Consulte condições. Conteúdo informativo. Não constitui recomendação de investimento."

**Variante paywall** (exibir quando o free tocar num recurso bloqueado, se o SDK permitir — maior
intenção do funil, `01-produto.md` §3) `[VALIDAR]`:
- **Título:** Este dado faz parte do plano anual `34/40`
- **Texto:** Na Black Friday, o plano anual está com [X]% off. Desbloqueie o dado completo por 12 meses. `91/110`
- **Botão:** Desbloquear com [X]% off `24/25` · `utm_content=i1-paywall`

### I1-B · Modal · Último dia (30/11)
- **Sobretítulo:** Cyber Monday · último dia `25/30`
- **Título:** Termina hoje, às 23h59 `22/40`
- **Texto:** Plano anual com [X]% off: R$ [PREÇO] por 12 meses. Depois de hoje, volta ao preço normal. `89/110`
- **Botão principal:** Assinar agora `13/25` · `utm_content=i1-modal-ultimo-dia`
- **Botão secundário:** Agora não `9/25`
- **Rodapé:** "Até 30/11, 23h59. Consulte condições. Conteúdo informativo. Não constitui recomendação de investimento."

---

## 4. Meta Ads (M1–M7)

Regras: texto principal com a mensagem nos **primeiros 125 caracteres** (contados); o aviso vai
logo depois, na mesma caixa de texto. Título ≤ 40. Descrição ≤ 30 (o feed corta descrições
longas). Toda peça com oferta leva prazo e "consulte condições"; todas levam AL-1. Sem citar a
Bloomberg nem concorrentes. Prova = **print real do app** na arte.

**Aviso fixo após o texto principal (todas as peças):**
> Conteúdo informativo. Não constitui recomendação de investimento.

**Aviso adicional nas peças com oferta:**
> Oferta válida até 30/11/2026, 23h59 (horário de Brasília). Consulte condições.

UTMs: `utm_source=meta&utm_medium=paid_social&utm_campaign=bf2026-trademap&utm_content=<id>&utm_term=<remkt|lal>`
(padrão de `02-dados.md`; ver divergência em §9).

### 4.1 Esquenta (M6 · 24–26/11 · sem preço)

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| ESQ-1 | A Black Friday TradeMap começa na sexta, 27/11. Condição especial no plano anual, até segunda, 30/11. `101/125` | Black Friday TradeMap vem aí `28/40` | De 27 a 30/11 `13/30` | Saiba mais |
| ESQ-2 | Como você vai decidir em 2027? Cotações, notícias, fundamentos e carteira num só lugar. Na sexta, o anual fica mais em conta. `125/125` | 2027 com dados, do começo ao fim `32/40` | Black Friday a partir de 27/11 `30/30` | Saiba mais |
| ESQ-3 | Mercado em tempo real e sua carteira de várias corretoras numa tela só. De 27 a 30/11, condição especial no plano anual. `120/125` | Tudo num só lugar. Em breve, por menos `38/40` | Black Friday TradeMap `21/30` | Saiba mais |

**Texto na arte (M6, 4:5 e 9:16):** "BLACK FRIDAY TRADEMAP" · "27 a 30/11" · "Decida com dados o ano inteiro." · rodapé: AL-1.

### 4.2 Black Friday (27–30/11) · Ângulo "Oferta" (A) — R1, R2, P1/P2

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| OF-1 | Black Friday TradeMap: plano anual com [X]% off. Decida com dados o ano inteiro, por R$ [PREÇO]. Até 30/11, 23h59. `114/125` | Plano anual com [X]% off `24/40` | Até 30/11, 23h59 `16/30` | Assinar |
| OF-2 | 2027 tem 12 meses de mercado. Acompanhe todos com cotações, notícias, fundamentos e carteira num só lugar. [X]% off no anual. `125/125` | Decida com dados o ano inteiro `30/40` | [X]% off até 30/11, 23h59 `25/30` | Assinar |
| OF-3 | Você já acompanha o mercado. Agora, com o dado completo por 12 meses: plano anual do TradeMap com [X]% off na Black Friday. `123/125` | O dado completo, 12 meses, [X]% off `35/40` | Consulte condições `18/30` | Assinar |

**Texto na arte (M1/M2 "Oferta"):** "[X]% OFF NO PLANO ANUAL" · "Decida com dados o ano inteiro." · "R$ [PREÇO] por 12 meses" · "Até 30/11, 23h59. Consulte condições." · AL-1.

### 4.3 Black Friday · Ângulo "Produto" (B · prospecção P1/P2 e R2)

> "Nível profissional" só com print real do app mostrando profundidade de dados. `[VALIDAR com marca/jurídico]`

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| PR-1 | Informação de nível profissional, preço de pessoa física. E na Black Friday, o plano anual do TradeMap sai [X]% menor. `118/125` | Dados profissionais, preço de PF `32/40` | [X]% off até 30/11, 23h59 `25/30` | Saiba mais |
| PR-2 | Cotação qualquer site mostra. O TradeMap junta cotação, notícia, fundamento e sua carteira numa tela, para decidir melhor. `122/125` | Mais que cotação: contexto `26/40` | Plano anual com [X]% off `24/30` | Saiba mais |
| PR-3 | Mercado em tempo real, no Brasil e lá fora, com fundamentos e notícias ao lado. Plano anual com [X]% off até 30/11, 23h59. `122/125` | O mercado inteiro numa tela só `30/40` | Black Friday TradeMap `21/30` | Assinar |

**Texto na arte (M1/M2 "Produto"):** "Informação de nível profissional. Preço de pessoa física." · print real do app · "[X]% off no plano anual até 30/11, 23h59" · AL-1.

### 4.4 Black Friday · Ângulo "Win-back" (C + A · R3 ex-assinantes)

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| WB-1 | Volte a acompanhar o mercado com o dado completo. Na Black Friday, o plano anual do TradeMap está com [X]% off. `111/125` | Volte ao TradeMap com [X]% off `30/40` | Até 30/11, 23h59 `16/30` | Assinar |
| WB-2 | Cotações, notícias, fundamentos e sua carteira de várias corretoras de novo numa tela só. Plano anual com [X]% off até 30/11. `125/125` | Tudo num só lugar, de novo `26/40` | Consulte condições `18/30` | Assinar |
| WB-3 | Menos abas, mais clareza. Se você já usou o TradeMap, sabe a diferença. Plano anual com [X]% off na Black Friday. `113/125` | Menos abas, mais clareza `24/40` | [X]% off até 30/11, 23h59 `25/30` | Assinar |

> Segmentação por lista de ex-assinantes depende de base legal `[VALIDAR com DPO]`. O texto não
> afirma que a pessoa é ex-assinante ("se você já usou"), para não expor dado de relacionamento
> caso o anúncio apareça para outra pessoa.

**Texto na arte (M1/M2 "Win-back"):** "Volte a decidir com dados." · "[X]% off no plano anual" · "Até 30/11, 23h59. Consulte condições." · AL-1.

### 4.5 Black Friday · Ângulo "Upsell mensal → anual" (R4)

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| UP-1 | Já assina o TradeMap no mensal? Na Black Friday, trocar para o anual sai [X]% mais em conta. Mesma conta, mesmos dados. `119/125` | Troque para o anual e pague menos `33/40` | Até 30/11, 23h59 `16/30` | Assinar |
| UP-2 | 12 meses de dado completo com uma assinatura só. Plano anual do TradeMap com [X]% off até 30/11, 23h59. `103/125` | Uma assinatura para 2027 inteiro `32/40` | Consulte condições `18/30` | Assinar |
| UP-3 | Faça a conta: plano anual por R$ [PREÇO] na Black Friday TradeMap. Menos por mês, nenhuma renovação até o fim de 2027. `118/125` | Faça a conta do anual `21/40` | [X]% off até 30/11, 23h59 `25/30` | Assinar |

> UP-1: "[X]% mais em conta" só se o desconto for calculado sobre 12× o mensal. Se o desconto for
> sobre o anual cheio, trocar por "o anual está com [X]% off". `[VALIDAR cálculo]`

**Texto na arte (M1/M2 "Upsell"):** "Troque o mensal pelo anual." · "[X]% off · R$ [PREÇO] por 12 meses" · "Até 30/11, 23h59. Consulte condições." · AL-1.

### 4.6 Últimas horas (M5 · só 30/11)

| Var. | Texto principal (≤ 125 visíveis) | Título (≤ 40) | Descrição (≤ 30) | CTA |
|---|---|---|---|---|
| UH-1 | Termina hoje, às 23h59: plano anual do TradeMap com [X]% off. Depois, volta ao preço normal. `92/125` | Termina hoje, às 23h59 `22/40` | Plano anual com [X]% off `24/30` | Assinar |
| UH-2 | Cyber Monday é o último dia da Black Friday TradeMap. Decida com dados o ano inteiro, por R$ [PREÇO] no anual. `110/125` | Último dia: [X]% off no anual `29/40` | Até 23h59 de hoje `17/30` | Assinar |
| UH-3 | Últimas horas para assinar o plano anual com [X]% off. Cotações, notícias e carteira num só lugar em 2027. `106/125` | Últimas horas da Black Friday `29/40` | Encerra às 23h59 `16/30` | Assinar |

**Texto na arte (M5):** "ÚLTIMAS HORAS" · "[X]% off no plano anual" · "Termina hoje, 30/11, às 23h59" · "Consulte condições." · AL-1.

### 4.7 Carrossel M3 · "O que o plano anual libera" (1:1, 5 cards)

`[VALIDAR: cada recurso precisa estar no plano em oferta]`

| Card | Texto na arte | Título do card (≤ 40) |
|---|---|---|
| 1 | "Black Friday TradeMap: [X]% off no plano anual" | O que o plano anual libera `26/40` |
| 2 | "Mercado em tempo real" + print de cotações | Cotações e notícias em tempo real `33/40` |
| 3 | "Fundamentos das empresas" + print | Fundamentos para comparar `25/40` |
| 4 | "Sua carteira de várias corretoras numa tela só" + print | Carteira consolidada `20/40` |
| 5 | "R$ [PREÇO] por 12 meses · Até 30/11, 23h59" | Assine com [X]% off `19/40` |

**Texto principal:** Arraste para ver o que o plano anual do TradeMap libera. Na Black Friday, com [X]% off até 30/11, 23h59. `104/125`
+ AL-1 + aviso de oferta.

### 4.8 Vídeo curto M4 (9:16, 6–15 s, sem locução) · textos na tela

**M4-1 "Um ano de decisões com dados" (≈12 s)**
1. (0–3 s) "Como você vai decidir em 2027?"
2. (3–6 s) print: cotações em tempo real → "Mercado em tempo real"
3. (6–9 s) print: carteira → "Sua carteira numa tela só"
4. (9–12 s) "Plano anual com [X]% off · Até 30/11, 23h59" + logo
- Legenda fixa no rodapé: "Conteúdo informativo. Não constitui recomendação de investimento. Consulte condições."

**M4-2 "Menos abas, mais clareza" (≈8 s)**
1. (0–2 s) várias abas abertas/apps alternando → "5 apps para acompanhar a carteira?"
2. (2–5 s) tela única do TradeMap → "Ou tudo num só lugar."
3. (5–8 s) "Black Friday TradeMap · [X]% off no anual · Até 30/11, 23h59"
- Mesma legenda fixa.

Textos de anúncio para M4: reaproveitar OF-2 (M4-1) e WB-3 (M4-2).

---

## 5. Instagram orgânico

### O1 · Posts Feed/Reels (3)

**O1-1 · ter 24/11 · Anúncio da BF (sem preço)**
- **Texto na arte:** "BLACK FRIDAY TRADEMAP" · "27 a 30/11" · "Decida com dados o ano inteiro."
- **Legenda:**
> Black Friday TradeMap: de 27 a 30/11.
>
> Por quatro dias, o plano anual do TradeMap terá uma condição especial. Cotações e notícias em
> tempo real, fundamentos das empresas e sua carteira consolidada, num só lugar, para você
> acompanhar 2027 inteiro com clareza.
>
> Ative as notificações do perfil para saber quando abrir.
>
> Conteúdo informativo. Não constitui recomendação de investimento.
- **Hashtags:** #TradeMap #BlackFriday #MercadoFinanceiro #Investimentos #BolsaDeValores #EducaçãoFinanceira

**O1-2 · sex 27/11 · Abertura (também vira impulsionamento C3)**
- **Texto na arte:** "COMEÇOU" · "[X]% off no plano anual" · "R$ [PREÇO] por 12 meses" · "Até 30/11, 23h59. Consulte condições."
- **Legenda:**
> Começou a Black Friday TradeMap.
>
> Plano anual [VALIDAR: nome do plano] com [X]% off: R$ [PREÇO] por 12 meses.
>
> Em 2027, decida com o dado completo:
> → Mercado em tempo real, no Brasil e lá fora
> → Fundamentos das empresas para comparar
> → Sua carteira de várias corretoras numa tela só
>
> Condição válida até 30/11/2026, às 23h59 (horário de Brasília). Link na bio. Consulte condições.
>
> Conteúdo informativo. Não constitui recomendação de investimento.
- **Hashtags:** #TradeMap #BlackFriday #BlackFriday2026 #Investimentos #MercadoFinanceiro #BolsaDeValores

**O1-3 · seg 30/11 · Cyber Monday (também vira impulsionamento C3)**
- **Texto na arte:** "ÚLTIMO DIA" · "[X]% off no plano anual" · "Termina hoje, às 23h59"
- **Legenda:**
> Último dia da Black Friday TradeMap.
>
> O plano anual com [X]% off (R$ [PREÇO] por 12 meses) fica disponível até hoje, 30/11, às 23h59.
> Depois disso, volta ao preço normal.
>
> Cotações, notícias, fundamentos e carteira consolidada. Menos abas, mais clareza, o ano inteiro.
>
> Link na bio. Consulte condições.
>
> Conteúdo informativo. Não constitui recomendação de investimento.
- **Hashtags:** #TradeMap #CyberMonday #BlackFriday #Investimentos #MercadoFinanceiro

### O2 · Stories 1080×1920 (12)

Todos com rodapé pequeno: "Conteúdo informativo. Não constitui recomendação de investimento." e,
nos de oferta, "Até 30/11, 23h59. Consulte condições." Respeitar zona segura (250 px em cima e
embaixo).

**Contagem regressiva (5 · template com o número trocado)**

| # | Quando | Texto |
|---|---|---|
| ST-1 | 24/11 | "Faltam 3 dias" · "Black Friday TradeMap · 27 a 30/11" · sticker de lembrete |
| ST-2 | 25/11 | "Faltam 2 dias" · "Condição especial no plano anual" · sticker de lembrete |
| ST-3 | 26/11 | "É amanhã" · "Black Friday TradeMap começa à 0h" · sticker de lembrete |
| ST-4 | 29/11 | "Amanhã é o último dia" · "[X]% off no plano anual até 30/11, 23h59" · link |
| ST-5 | 30/11 | "Termina hoje, às 23h59" · "[X]% off no plano anual" · link (repostar a cada ~3 h trocando para "Últimas horas") |

**Recursos do app (4 · print real em cada um)**

| # | Quando | Texto |
|---|---|---|
| ST-6 | 25/11 | "O que o plano anual libera (1/4)" · "Mercado em tempo real" · print de cotações |
| ST-7 | 25/11 | "(2/4)" · "Notícias no momento em que acontecem" · print do feed |
| ST-8 | 25/11 | "(3/4)" · "Fundamentos para comparar empresas" · print |
| ST-9 | 25/11 | "(4/4)" · "Sua carteira de várias corretoras numa tela só" · print · "Na sexta, com condição especial" |

`[VALIDAR: cada recurso precisa estar no plano em oferta; prints sem nomes de ativos em destaque e sem dados de clientes reais]`

**Lembrete com link (3)**

| # | Quando | Texto | Link (sticker) |
|---|---|---|---|
| ST-10 | 27/11 manhã | "Começou" · "[X]% off no plano anual · R$ [PREÇO] por 12 meses" | Ver oferta `10/25` |
| ST-11 | 27/11 noite | "Decida com dados o ano inteiro" · "[X]% off até 30/11, 23h59" | Assinar o anual `15/25` |
| ST-12 | 28/11 | "Menos abas, mais clareza" · "Carteira, cotações e notícias num só lugar · [X]% off no anual" | Ver oferta `10/25` |

`utm_source=instagram&utm_medium=organic_social&utm_campaign=bf2026-trademap&utm_content=st-<nn>`

---

## 6. Landing page / página de planos

### L · Banner topo da página de planos (2 formatos, mesmo texto)

| Elemento | Desktop 1920×480 | Mobile 750×750 |
|---|---|---|
| Selo | BLACK FRIDAY TRADEMAP `21/30` | idem |
| Headline | Decida com dados o ano inteiro `30/40` | idem |
| Oferta | Plano anual com [X]% off: R$ [PREÇO] `36/40` | idem |
| Prazo + condição | Até 30/11, 23h59. Consulte condições. `37/45` | idem |
| Botão | Assinar o plano anual `21/25` | idem |

Antes de 27/11 (se a página já estiver no ar): selo + "De 27 a 30/11" + "Condição especial no plano anual".

### Blocos da landing (página da oferta)

**1. Hero**
- **Headline:** Decida com dados o ano inteiro. `31/60`
- **Subheadline:** Black Friday TradeMap: plano anual [VALIDAR: nome do plano] com [X]% off. R$ [PREÇO] por 12 meses, até 30/11, às 23h59. `119/140`
- **CTA:** Assinar o plano anual `21/25`
- **Microtexto abaixo do botão:** "Pagamento [VALIDAR: cartão / Pix / parcelamento]. Consulte as condições."

**Variação de hero por UTM (opcional):**
- `utm_term=s2` → headline Volte a decidir com o dado completo. `36/60`
- `utm_term=s3` → headline Troque para o anual e pague menos por mês. `42/60` `[VALIDAR cálculo]`

**2. Três benefícios**
1. **Mercado em tempo real.** Cotações e notícias no momento em que acontecem, no Brasil e lá fora.
2. **Contexto para decidir.** Fundamentos das empresas e dados de mercado ao lado da cotação, para comparar com clareza.
3. **Tudo num só lugar.** Sua carteira de várias corretoras consolidada numa tela só. Menos abas, mais clareza.

`[VALIDAR: lista free × pago; incluir aqui só recursos do plano em oferta]`

**3. Prova**
- Print real do app (cotações + carteira consolidada), sem ativo em destaque com recomendação e sem dado de cliente.
- Linha de prova: "[N] investidores usam o TradeMap" `[VALIDAR: número oficial e data]` · "Nota [N] na App Store / Google Play" `[VALIDAR]`.
- Sem depoimentos de clientes, a menos que haja autorização registrada (exige jurídico).

**4. Bloco "por que o anual"**
> 2027 tem 12 meses de mercado. Com o plano anual, você acompanha todos eles com o dado completo,
> paga uma vez `[VALIDAR forma de cobrança]` e tira a renovação da cabeça até o fim do ano.
> Na Black Friday, com [X]% off.

**5. CTA final**
- **Título:** A condição termina em 30/11, às 23h59. `38/60`
- **Botão:** Assinar com [X]% off `20/25`
- Contador regressivo até 30/11/2026, 23h59 (BRT) — real, sem reinício.

**6. FAQ curto**

> **Até quando vale a oferta?**
> Até 30/11/2026, às 23h59 (horário de Brasília). Depois, o plano anual volta ao preço normal.
>
> **O que está incluído no plano anual?**
> [VALIDAR: lista oficial de recursos do plano em oferta.]
>
> **Já sou assinante mensal. Posso trocar para o anual com o desconto?**
> [VALIDAR: regra de migração mensal → anual e crédito proporcional.]
>
> **Já fui assinante. A oferta vale para mim?**
> [VALIDAR: elegibilidade de ex-assinantes.]
>
> **Quais as formas de pagamento?**
> [VALIDAR: cartão, Pix, parcelamento, cobrança à vista.]
>
> **Posso cancelar?**
> [VALIDAR: política de cancelamento e reembolso do plano anual.]
>
> **O TradeMap recomenda investimentos?**
> Não. O TradeMap reúne dados, notícias e informações de mercado para você decidir com clareza.
> Não recomenda a compra ou venda de ativos nem promete resultado.

**7. Rodapé legal**
> Conteúdo informativo. Não constitui recomendação de investimento. Oferta válida para novas
> assinaturas do plano anual [VALIDAR: nome do plano] feitas de 27/11/2026, 00h00, a 30/11/2026,
> 23h59 (horário de Brasília). Consulte as condições completas em [link do regulamento/termos].

---

## 7. Google Search · marca (opcional, cenário recomendado/agressivo)

**15 títulos (≤ 30):**
1. TradeMap Oficial `16/30`
2. Black Friday TradeMap `21/30`
3. Plano Anual com [X]% Off `24/30`
4. Decida com Dados o Ano Todo `27/30`
5. Mercado em Tempo Real `21/30`
6. Sua Carteira numa Tela Só `25/30`
7. Cotações, Notícias e Dados `26/30`
8. Fundamentos das Empresas `24/30`
9. Oferta Válida até 30/11 `23/30`
10. Termina 30/11 às 23h59 `22/30`
11. Assine o Plano Anual `20/30`
12. Tudo num Só Lugar `17/30`
13. Menos Abas, Mais Clareza `24/30`
14. Brasil e Mercado Internacional `30/30`
15. Plano Anual por R$ [PREÇO] `26/30`

**4 descrições (≤ 90):**
1. Black Friday TradeMap: plano anual com [X]% off até 30/11, 23h59. Consulte condições. `85/90`
2. Cotações e notícias em tempo real, fundamentos e sua carteira consolidada num só lugar. `87/90`
3. Decida com dados o ano inteiro. Assine o plano anual do TradeMap com condição especial. `87/90`
4. Conteúdo informativo. Não constitui recomendação de investimento. Oferta até 30/11. `83/90`

> Fixar o título 1 na posição 1 e a descrição 4 na posição 2 garante a presença do aviso. `[VALIDAR com mídia]`

---

## 8. Checklist de compliance (autoverificação do redator)

| Regra (`compliance/regras.md`) | Situação |
|---|---|
| Sem promessa de ganho/rentabilidade; sem "garantido", "sem risco", "lucre", "renda extra" | OK em todas as peças. E04 e FAQ deixam explícito que o TradeMap não recomenda ativos nem promete resultado. |
| Sem recomendação de ativo | OK. Nenhum ticker citado. Prints devem evitar ativo em destaque. |
| Preço/desconto/prazo só confirmados | Preço e desconto como `[X]%` / `R$ [PREÇO]`. Prazo 27–30/11, 23h59 vem do brief. |
| AL-1 em todas as peças | E-mails (rodapé), anúncios (texto + arte), IG, stories, landing, in-app (rodapé), Google (descrição 4). **Push: proposto na tela de destino** `[VALIDAR]`. |
| Prazo com data e hora + "consulte condições" | Em todas as peças com oferta. |
| Urgência real (CONAR) | Só o prazo real (30/11, 23h59). Sem "últimas vagas", "menor preço da história", "última vez". "Volta ao preço normal" depende de confirmação. |
| LGPD: descadastro e consentimento | AL-3 em todos os e-mails. Anúncio win-back não expõe relação com a pessoa. |
| Sem depoimentos sem autorização | Nenhum depoimento usado. |
| Tom de voz TradeMap | Analítico, direto, sem emoji, sem euforia; palavras-chave: dados, decisão, clareza, carteira, tempo real, num só lugar. |

---

## 9. Pendências e divergências `[VALIDAR]`

1. **Bloqueiam as peças com oferta:** `[X]%`, `R$ [PREÇO]`, nome do plano, equivalente mensal
   `R$ [Y]`, economia do mensal → anual `R$ [ECONOMIA]`.
2. **Lista oficial free × pago** (sustenta os bullets de benefícios e a variante paywall do in-app).
3. Elegibilidade de ex-assinantes (S2) e regra de migração mensal → anual (S3).
4. Preço volta ao cheio em 01/12? (sustenta "depois, volta ao preço normal").
5. Política de cancelamento/reembolso e formas de pagamento (FAQ).
6. Número de usuários / nota nas lojas para o bloco de prova da landing.
7. **Divergências entre `02-dados.md` e `03-midia.md` (segui o 02 nos e-mails):**
   - E03: 08h (02) × 07h (03). E04: quem **clicou** e não comprou (02) × não abridores (03).
     E07: quem clicou (02) × quem não abriu/clicou (03).
   - UTMs de Meta: `utm_medium=paid_social` + `utm_campaign=bf2026-trademap` (02) ×
     `utm_medium=paid` + `utm_campaign=bf26_trademap` (03). Recomendo padronizar no 02.
   - Limite de texto de push: 120 (03) × 110 (regra do redator). Todos os textos cabem em 110.
8. Aviso legal no push (AL-1 na tela de destino) precisa de OK do compliance.
9. "Informação de nível profissional" (ângulo B): exige prova visual e OK de marca/jurídico.
