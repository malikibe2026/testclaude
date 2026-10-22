import json, re

# palet app sebenar (index.html KOORDINATe)
css = open('base.css').read()
tok = """  --bg: #0f1117;
  --bg-2: #1a1d27;
  --fg: #e8eaf6;
  --muted: #8b92ad;
  --accent: #4ade80;
  --accent-2: #22d3ee;
  --accent-ink: #4ade80;
  --surface-2: #22263a;
  --line: #2e3347;
  --danger: #f87171;
  --warning: #fbbf24;"""
css = re.sub(r"  --bg: #0f1012;.*?--accent-ink: var\(--accent\);", tok, css, count=1, flags=re.S)
css = css.replace('--font: "Inter", sans-serif;', '--font: "Plus Jakarta Sans Variable", "Plus Jakarta Sans", sans-serif;')
css = css.replace('--mono: "JetBrains Mono", monospace;', '--mono: "IBM Plex Mono", monospace;')
open('base.css','w').write(css)

HEAD = """<!doctype html>
<html lang="ms">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../fonts/plus-jakarta-sans.css">
<link rel="stylesheet" href="../fonts/ibm-plex-mono.css">
<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="../ui.css">
<script src="../icons.js"></script>
<script src="../motion.js"></script>
<style>
%s
</style>
</head>
<body>
<div class="bg" style="background:radial-gradient(ellipse 60%% 40%% at 10%% 10%%, rgba(74,222,128,.09), transparent 60%%), radial-gradient(ellipse 50%% 40%% at 90%% 85%%, rgba(34,211,238,.08), transparent 60%%), var(--bg)"></div>
%s
</body>
</html>
"""
COMMON = """
.panel { background:var(--bg-2); border:1px solid var(--line); border-radius:calc(var(--u)*1.8); padding:calc(var(--u)*3); }
.slabel { font-size:var(--fs-label); font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin:0 0 calc(var(--u)*1.4); }
.logo { width:calc(var(--u)*9); height:calc(var(--u)*9); border-radius:calc(var(--u)*2.4); background:linear-gradient(135deg,var(--accent),var(--accent-2)); display:grid; place-items:center; color:#06210f; font-size:calc(var(--u)*5); }
.safe.hudslot { align-content:start; justify-items:start; padding-top:calc(var(--u)*3); text-align:left; }
.btn2 { display:inline-flex; align-items:center; gap:.6em; font-size:var(--fs-body); font-weight:600; padding:.6em 1.1em; border-radius:calc(var(--u)*1.2); border:1px solid var(--line); background:var(--surface-2); color:var(--fg); }
.btn2.go { background:var(--accent); border-color:var(--accent); color:#06210f; }
.mono { font-family:var(--mono); }
"""
def hud(kicker, n, title, t='-0.2s'):
    return f'''<header class="hud"><div class="safe hudslot">
<p class="kicker m" style="--in:fade; --t:{t}"><b>{n}</b>{kicker}</p>
<h1 class="title m" data-headline style="--in:rise; --t:{t}; max-width:none">{title}</h1>
</div></header>'''

# 01
s1 = HEAD % (COMMON + ".safe{align-content:center;justify-items:center;gap:calc(var(--u)*3);text-align:center}", """<main class="stage"><div class="safe">
<div class="logo m" style="--in:pop; --t:calc(-1 * var(--dur-in))"><i data-icon="map-pin"></i></div>
<h1 class="hero m" style="--in:rise; --t:calc(-1 * var(--dur-in)); max-width:none">Cari Koordinat GPS</h1>
<p class="sub m" style="--in:rise; --t:calc(-1 * var(--dur-in)); max-width:none; color:var(--muted)">Masukkan alamat <i data-icon="arrow-right" style="color:var(--accent)"></i> dapat Latitud &amp; Longitud</p>
</div></main>""")

# 02
s2 = HEAD % (COMMON + """
.safe{align-content:center; padding-top:calc(var(--u)*14)}
.panel{width:calc(var(--u)*118); justify-self:center}
.ta{background:var(--surface-2); border:1px solid var(--line); border-radius:calc(var(--u)*1.2); padding:calc(var(--u)*2.2); min-height:calc(var(--u)*11); font-size:var(--fs-sub); line-height:1.4}
.ta.on{border-color:var(--accent)}
.brow{display:flex; gap:calc(var(--u)*1.4); margin-top:calc(var(--u)*2)}
.brow .go{flex:1; justify-content:center}
""", f"""<main class="stage"><div class="safe">
<div class="panel m" style="--in:rise; --t:.1s">
<p class="slabel">Masukkan alamat</p>
<div class="ta on"><span data-type data-at=".7" data-cps="15" data-sfx="type">Jabatan Perangkaan Malaysia, Putrajaya</span></div>
<div class="brow"><span class="btn2">Padam</span><span class="btn2 go m" style="--in:press; --t:3.6s" data-sfx="click" data-sfx-intent="button-press"><i data-icon="search"></i> Cari Koordinat</span></div>
</div></div></main>
{hud("Taip alamat","01","Nama tempat + kawasan + negeri")}""")

# 03
pairs=[("Jln","Jalan"),("Tmn","Taman"),("Kg","Kampung")]
rows=""
for i,(a,b) in enumerate(pairs):
    t=-.3+i*.7
    rows+=f'''<div class="pair">
<span class="chip bad m" style="--in:left; --t:{t}s">{a}</span>
<i data-icon="arrow-right" class="m" style="--in:fade; --t:{t+.25}s"></i>
<span class="chip good m" style="--in:right; --t:{t+.35}s"><i data-icon="check"></i>{b}</span>
</div>'''
s3 = HEAD % (COMMON + """
.safe{align-content:center; padding-top:calc(var(--u)*10); gap:calc(var(--u)*3.5)}
.pair{display:flex; align-items:center; gap:calc(var(--u)*3); font-size:var(--fs-sub); color:var(--muted)}
.chip{display:inline-flex; align-items:center; gap:.4em; padding:.35em .9em; border-radius:999px; font-weight:700; font-size:var(--fs-sub); font-family:var(--mono)}
.chip.bad{color:var(--danger); border:1px solid rgba(248,113,113,.4); background:rgba(248,113,113,.08); text-decoration:line-through}
.chip.good{color:var(--accent); border:1px solid rgba(74,222,128,.45); background:rgba(74,222,128,.10)}
""", f"""<main class="stage"><div class="safe">{rows}</div></main>
{hud("Tulis penuh","02","Elak singkatan")}""")

# 04
steps=[("Sedang mencari koordinat...",.4),('Cuba tambah "Malaysia"...',1.3),("Cuba variasi alamat...",2.2)]
li=""
for i,(txt,t) in enumerate(steps):
    li+=f'<li class="step m" style="--in:rise; --t:{t}s"><i data-icon="refresh-cw"></i><span>{txt}</span></li>'
s4 = HEAD % (COMMON + """
.safe{align-content:center; padding-top:calc(var(--u)*10)}
ul{list-style:none; margin:0; padding:0; display:grid; gap:calc(var(--u)*2.2); width:calc(var(--u)*100)}
.step{display:flex; align-items:center; gap:calc(var(--u)*2); font-size:var(--fs-sub); background:var(--bg-2); border:1px solid var(--line); border-radius:calc(var(--u)*1.4); padding:calc(var(--u)*2) calc(var(--u)*2.6)}
.step i{color:var(--accent-2)}
""", f"""<main class="stage"><div class="safe"><ul>{li}</ul></div></main>
{hud("Tak jumpa?","03","Ia cuba beberapa variasi")}""")

# 05
btns=[("clipboard","Salin Koordinat"),("copy","Salin Semua"),("map","Google Maps"),("navigation","Waze")]
bb="".join(f'<span class="btn2 m" style="--in:pop; --t:{1.3+i*.25}s"><i data-icon="{ic}"></i>{tx}</span>' for i,(ic,tx) in enumerate(btns))
s5 = HEAD % (COMMON + """
.safe{align-content:center; padding-top:calc(var(--u)*24)}
.panel{width:calc(var(--u)*142); justify-self:center}
.cg{display:grid; grid-template-columns:1fr 1fr; gap:calc(var(--u)*1.6)}
.cb{background:var(--surface-2); border:1px solid var(--line); border-radius:calc(var(--u)*1.2); padding:calc(var(--u)*1.8) calc(var(--u)*2.2)}
.cl{font-size:var(--fs-label); font-weight:700; color:var(--muted); letter-spacing:.08em; text-transform:uppercase; display:flex; align-items:center; gap:.6em}
.dot{width:.8em; height:.8em; border-radius:50%}
.cv{font-family:var(--mono); font-size:calc(var(--u)*4.4); font-weight:600; margin-top:.2em}
.addr{margin-top:calc(var(--u)*1.6)}
.bar{height:calc(var(--u)*1.4); border-radius:999px; background:var(--line); margin-top:calc(var(--u)*1.2)}
.arow .btn2{font-size:calc(var(--u)*2.7)}
.arow{display:flex; flex-wrap:nowrap; gap:calc(var(--u)*1.4); margin-top:calc(var(--u)*2.2)}
.note{margin-top:calc(var(--u)*1.6); font-size:var(--fs-label); color:var(--muted)}
""", f"""<main class="stage"><div class="safe">
<div class="panel m" style="--in:rise; --t:.1s">
<p class="slabel">Keputusan</p>
<div class="cg">
<div class="cb"><div class="cl"><span class="dot" style="background:var(--accent)"></span>Latitud</div><div class="cv" style="color:var(--accent)">x.xxxxxx</div></div>
<div class="cb"><div class="cl"><span class="dot" style="background:var(--accent-2)"></span>Longitud</div><div class="cv" style="color:var(--accent-2)">xxx.xxxxxx</div></div>
</div>
<div class="cb addr"><div class="cl">Alamat disahkan oleh sistem</div><div class="bar" style="width:92%"></div><div class="bar" style="width:64%"></div></div>
<div class="arow">{bb}</div>
<p class="note">Nilai di atas ialah format contoh: enam tempat perpuluhan</p>
</div></div></main>
{hud("Keputusan","04","Salin terus atau buka di peta")}""")

# 06
hist=[("Jabatan Perangkaan Malaysia, Putrajaya"),("Hospital Shah Alam, Selangor")]
hh="".join(f'<div class="h m" style="--in:rise; --t:{.5+i*.5}s"><i data-icon="clock"></i><span>{h}</span></div>' for i,h in enumerate(hist))
s6 = HEAD % (COMMON + """
.safe{align-content:center; padding-top:calc(var(--u)*10)}
.panel{width:calc(var(--u)*118); justify-self:center; display:grid; gap:calc(var(--u)*1.6)}
.h{display:flex; align-items:center; gap:calc(var(--u)*1.8); font-size:var(--fs-sub); background:var(--surface-2); border:1px solid var(--line); border-radius:calc(var(--u)*1.2); padding:calc(var(--u)*1.8) calc(var(--u)*2.4)}
.h i{color:var(--muted)}
""", f"""<main class="stage"><div class="safe"><div class="panel"><p class="slabel">Carian terkini</p>{hh}</div></div></main>
{hud("Sejarah","05","Carian terkini tersimpan")}""")

# 07
s7 = HEAD % (COMMON + ".safe{align-content:center;justify-items:center;gap:calc(var(--u)*3);text-align:center}", """<main class="stage"><div class="safe">
<div class="logo m" style="--in:pop; --t:-0.2s"><i data-icon="map-pin"></i></div>
<h1 class="title m" style="--in:rise; --t:0s; max-width:none">Cari Koordinat GPS</h1>
<p class="sub m" style="--in:fade; --t:.6s; max-width:none">Data: OpenStreetMap Nominatim</p>
</div></main>""")

scenes=[("01-hook",s1,3),("02-taip",s2,4.8),("03-singkatan",s3,4),("04-variasi",s4,4),("05-keputusan",s5,4.5),("06-sejarah",s6,3.5),("07-tutup",s7,2.8)]
for n,h,_ in scenes: open(f"scenes/{n}.html","w").write(h)
json.dump({"width":1920,"height":1080,"fps":30,"output":"out/video.mp4","scenes":[{"file":f"scenes/{n}.html","duration":d} for n,_,d in scenes]},open("video.json","w"),indent=2)
