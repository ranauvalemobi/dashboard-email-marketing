# Black Friday TradeMap 2026 — resumo executivo

**Status:** 🧪 Campanha de teste do time, não será veiculada · Compliance: ⚠️ aprovado com ajustes (1 alto corrigido, 8 médios, 6 baixos)

| | |
|---|---|
| **Objetivo** | Converter free engajado, ex-assinantes e assinantes mensais em **plano anual** |
| **KPI** | Novas assinaturas anuais de 24/11 a 30/11 às 23h59, descontados os estornos em 7 dias. Meta: 3× a média semanal das 4 semanas anteriores `[VALIDAR com histórico]` |
| **Conceito** | Na copy: **"Decida com dados o ano inteiro."** No visual: "a Régua", barra de 12 meses de 2027 que se acende sobre um print real do app (fundo escuro, acento ciano). Internamente o conceito se chama "Ano inteiro, dado inteiro" |
| **Ângulos** | A: um ano de decisões com dados (canais próprios) · C: tudo num lugar só (fim de semana e win-back) · B: nível profissional com preço de pessoa física (prospecção, depende de OK de marca e jurídico) |
| **Oferta** | Plano anual com `[X]%` de desconto, por `R$ [PREÇO]` `[VALIDAR]`, válido até 30/11 às 23h59 |
| **Canais** | 7 e-mails (Wake), 8 pushes, 4 peças in-app, Meta Ads (60% da verba em remarketing, 30% em prospecção), Instagram orgânico, landing page |
| **Verba de mídia paga** | Enxuto: R$ 12 mil · **Recomendado: R$ 30 mil** · Agressivo: R$ 60 mil `[VALIDAR]` |
| **Mensuração** | `utm_campaign=bf2026-trademap` · grupo de controle de 5% · A/B de assunto no esquenta · leitura em D+1/D+3/D+7 no `dashboard_final_v1.py` |

## Calendário
- **24/11 (ter):** esquenta 1 (e-mail com A/B de assunto, push, in-app)
- **25/11:** leitura do A/B às 10h · anúncios enviados para revisão da Meta até 18h
- **26/11 (qui):** esquenta 2, "é amanhã"
- **27/11 (sex):** Black Friday, abertura da oferta
- **28–29/11:** fim de semana, ângulo "tudo num lugar só" e win-back
- **30/11 (seg):** último dia. "Últimas horas" só a partir das 18h; encerramento às 23h59

## Arquivos
| Arquivo | Agente | Conteúdo |
|---|---|---|
| [00-brief.md](00-brief.md) | Orquestrador | Brief e premissas |
| [01-produto.md](01-produto.md) | Especialista TradeMap | Proposta de valor, ângulos, segmentos, objeções |
| [02-dados.md](02-dados.md) | Analista de dados e CRM | Segmentação, metas, régua, A/B, UTMs, leitura (**prevalece sobre o 03 quando os dois divergem**) |
| [03-midia.md](03-midia.md) | Estrategista de mídia | Canais, verba, estrutura da Meta, cronograma, lista de peças |
| [04-copy.md](04-copy.md) | Redator | 59 peças de texto prontas para copiar |
| [05-criativo.md](05-criativo.md) | Diretor criativo | Conceito, direção de arte, 47 arquivos visuais, 2 roteiros de vídeo, 25 prompts |
| [06-compliance.md](06-compliance.md) | Compliance | Apontamentos, avisos legais, bloqueios |

## Pendências que só a empresa resolve (bloqueiam as peças com oferta)
1. **% de desconto, preço e nome do plano** (produto/finanças). É o item mais urgente: destrava quase tudo.
2. Lista oficial do que é grátis e do que é pago, para confirmar "tempo real" e "dado completo" (produto).
3. Compromisso de **não prorrogar** a oferta e hora de início em 27/11 (produto/finanças).
4. Ex-assinantes e a troca do mensal para o anual entram na oferta? (produto)
5. Base legal para enviar marketing a ex-assinantes e subir listas na Meta (DPO).
6. Categoria especial de serviços financeiros na Meta e checagem do pixel/CAPI (mídia).
7. Razão social, endereço e CNPJ no rodapé dos e-mails, mais o link de condições (jurídico/CRM).
8. Prints reais do app (T1–T8) de conta demo, aprovados pelo compliance (produto).
9. Paleta e tipografia oficiais do TradeMap (marca).

> As peças de **esquenta** (24 e 26/11) não citam preço e podem sair assim que os ajustes
> médios estiverem aplicados e os itens 7 e 8 forem resolvidos.

## Checklist do OK
Com o OK, o time faz:
- [ ] Atualiza as peças com preço, plano e desconto oficiais e roda o compliance de novo
- [ ] Deixa a régua da Wake pronta para importar (e-mails E01–E07 e segmentos)
- [ ] Deixa a estrutura da Meta Ads pronta no cenário escolhido. **Publicar e gastar verba continuam dependendo do seu OK final**
- [ ] Gera as imagens e vídeos a partir dos prompts do `05-criativo.md`
