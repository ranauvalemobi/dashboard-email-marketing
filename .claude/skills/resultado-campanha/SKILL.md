---
name: resultado-campanha
description: Registra e analisa o resultado de uma campanha já veiculada e alimenta a memória do time (historico.md do produto). Use quando o usuário enviar números, prints, planilhas da Wake/compras ou disser como uma campanha performou.
---

# /resultado-campanha — fazer o time aprender

1. Identifique a campanha em `time-marketing/entregas/` (pelo nome ou pela mais recente do produto).
2. Chame `analista-dados-crm` com os dados recebidos (planilhas: analisar em memória/pasta
   temporária, **nunca** versionar dados pessoais). Saída: `<pasta>/07-resultado.md` com
   meta × realizado, leitura por segmento/canal/peça, o que funcionou, o que não funcionou e
   3 recomendações para a próxima.
3. Acrescente um bloco ao `time-marketing/conhecimento/<produto>/historico.md`:
   data, campanha, público, ângulo, canais, KPIs reais, aprendizados (3 bullets).
4. Se os dados confirmarem algum `[VALIDAR]` nos arquivos de conhecimento, atualize-os.
5. Atualize `STATUS.md` para "✅ Concluída" e faça commit + push.
6. Responda ao usuário com 5 linhas: resultado, principal aprendizado, próxima recomendação.
