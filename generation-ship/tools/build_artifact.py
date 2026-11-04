"""Build dist/artifact.html: the prototype page in the form the hosted Artifact page expects.

The Artifact host wraps the page in its own <!doctype>/<head>/<body>, so this strips those
from index.html and adds the hosted-page title, viewport and side-gutter rules. Scripts,
styles and data stay as separate files published alongside it.

    python3 tools/build_artifact.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text()
head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", src, re.S).group(1)
head = re.sub(r'<meta charset="utf-8">\s*|<meta name="viewport"[^>]*>\s*', "", head)
page = f"""<title>Generation Ship</title>
<meta name="claude:viewport-fit-sides" content="cover">
{head.strip()}
<style>
  body {{ padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
</style>
{body.strip()}
"""
page = page.replace("<title>Generation Ship</title>\n<title>Generation Ship</title>", "<title>Generation Ship</title>")
page = re.sub(r"(<title>Generation Ship</title>\n<meta[^>]*>\n)<title>[^<]*</title>\n?", r"\1", page)
out = ROOT / "dist"
out.mkdir(exist_ok=True)
(out / "artifact.html").write_text(page)
print("wrote dist/artifact.html", len(page), "bytes")
