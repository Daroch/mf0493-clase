"""Genera web/index.html con las fichas de alumnos/. Lo ejecuta GitHub Actions al fusionar en main."""
import html
import pathlib
import re
from datetime import datetime, timezone

fichas = []
for f in sorted(pathlib.Path("alumnos").glob("*.md")):
    if f.name.startswith("_"):
        continue
    texto = f.read_text(encoding="utf-8")
    nombre = re.search(r"^#\s+(.+)$", texto, re.M)
    comando = re.search(r"Comando de Linux favorito:\s*(.+)$", texto, re.M)
    para_que = re.search(r"Para qué sirve:\s*(.+)$", texto, re.M)
    if not nombre or not comando:
        continue
    fichas.append((nombre.group(1).strip(), comando.group(1).strip().strip("`"),
                   para_que.group(1).strip() if para_que else ""))

tarjetas = "\n".join(
    f"""    <article>
      <h2>{html.escape(n)}</h2>
      <pre><span>$</span> {html.escape(c)}</pre>
      {f'<p>{html.escape(p)}</p>' if p else ''}
    </article>"""
    for n, c, p in fichas
)
ahora = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")

pagina = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MF0493 · Comandos favoritos</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 2rem 1rem; }}
    h1 {{ text-align: center; margin: 0 0 .25rem; }}
    .sub {{ text-align: center; color: #94a3b8; margin: 0 0 2rem; }}
    main {{ display: grid; gap: 1rem; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); max-width: 1100px; margin: auto; }}
    article {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1rem 1.25rem; }}
    h2 {{ font-size: 1.1rem; margin: 0 0 .75rem; }}
    pre {{ background: #020617; color: #4ade80; padding: .6rem .8rem; border-radius: 8px; overflow-x: auto; margin: 0; }}
    pre span {{ color: #64748b; }}
    p {{ color: #cbd5e1; margin: .75rem 0 0; font-size: .95rem; }}
    footer {{ text-align: center; color: #64748b; margin-top: 2rem; font-size: .85rem; }}
  </style>
</head>
<body>
  <h1>Comandos favoritos de la clase</h1>
  <p class="sub">{len(fichas)} fichas · cada una llegó con una pull request</p>
  <main>
{tarjetas}
  </main>
  <footer>Generada por GitHub Actions el {ahora}</footer>
</body>
</html>
"""
pathlib.Path("web").mkdir(exist_ok=True)
pathlib.Path("web/index.html").write_text(pagina, encoding="utf-8")
print(f"web/index.html: {len(fichas)} fichas")
