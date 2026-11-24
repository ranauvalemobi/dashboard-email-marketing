# Padrões de vídeo

## Formatos
| Uso | Proporção | Resolução | Duração |
|---|---|---|---|
| Reels / TikTok / Shorts | 9:16 | 1080×1920 | 15–45 s (máx. 60 s) |
| Feed | 1:1 ou 4:5 | 1080×1080 / 1080×1350 | até 60 s |
| YouTube | 16:9 | 1920×1080 | livre |
| Anúncio Meta | 9:16 e 1:1 | idem | 6–15 s |

## Regras de edição
- Gancho nos 3 primeiros segundos, com texto na tela.
- Legendas sempre queimadas (maioria assiste sem som): fonte sem serifa, 2 linhas no máximo,
  dentro da área segura (evitar 250 px de cima e 350 px de baixo no 9:16).
- Áudio normalizado (`loudnorm` −14 LUFS para redes).
- Final com logo do produto + CTA + aviso legal quando aplicável (mín. 2 s legível).
- Cores e tipografia: ver `tom-de-voz.md` de cada produto (Valemobi Design System; títulos
  Metropolis, texto Open Sans).
- Exportar H.264, AAC, `-movflags +faststart`.

## Comandos ffmpeg de referência
```bash
# corte sem reencode aproximado
ffmpeg -ss 00:12:30 -to 00:13:05 -i live.mp4 -c copy corte.mp4
# 16:9 -> 9:16 com fundo desfocado
ffmpeg -i in.mp4 -filter_complex "[0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20[bg];[0]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:a copy out.mp4
# legenda queimada + loudnorm
ffmpeg -i in.mp4 -vf "subtitles=legenda.srt:force_style='Fontsize=14,Outline=2,MarginV=120'" -af loudnorm=I=-14 -c:v libx264 -c:a aac -movflags +faststart out.mp4
```
