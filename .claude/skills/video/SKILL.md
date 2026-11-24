---
name: video
description: Transforma um vídeo bruto (live, gravação, webinar, tela do app) em cortes prontos para Reels/TikTok/Shorts/YouTube, ou produz um vídeo a partir de um roteiro com IA. Use quando o usuário enviar/apontar um vídeo, pedir cortes, edição, legendas, reenquadramento ou "transformar a live em conteúdo".
---

# /video — edição com o Editor de Vídeo IA

1. Localize o vídeo (arquivo enviado, caminho, ou link de mídia já importada no Higgsfield). Se
   não houver vídeo nem roteiro, peça só isso ao usuário, em uma linha.
2. Pasta: `time-marketing/conteudo/AAAA-MM-DD-video-<slug>/` (documentação, versionada) e
   `time-marketing/midia/AAAA-MM-DD-video-<slug>/` (arquivos de vídeo, fora do Git).
3. **`editor-video-ia`**: decupagem → plano de edição → cortes locais com ffmpeg (sem custo).
   Se o plano usar geração/edição paga, ele devolve o orçamento: peça o OK ao usuário antes de
   continuar.
4. **`copywriter`** (em paralelo com o passo 3 quando a decupagem estiver pronta): títulos, legendas
   de post e textos na tela de cada corte.
5. **`compliance`** revisa textos na tela, legendas e avisos.
6. Envie os cortes ao usuário com SendUserFile (status normal), commit da documentação, e peça o
   OK para publicar. Publicação em rede social só com OK explícito.
