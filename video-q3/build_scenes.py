import json
HEAD = """<!doctype html>
<html lang="ms" class="light">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="../ui.css">
<script src="../icons.js"></script>
<script src="../motion.js"></script>
<style>
%s
</style>
</head>
<body>
<div class="bg"></div>
%s
</body>
</html>
"""
COMMON = """
.grid338 { --cs:calc(var(--u)*2.3); --cg:calc(var(--u)*1.2); display:grid; grid-template-columns:repeat(26, var(--cs)); gap:var(--cg); justify-content:center; }
.cell { width:var(--cs); height:var(--cs); border-radius:50%; background:#c3d0dc; }
.cell.ok { background:var(--accent); }
.cell.todo { background:var(--accent-2); }
.card { background:var(--bg-2); border-radius:calc(var(--u)*2.2); box-shadow:0 calc(var(--u)*.6) calc(var(--u)*3) rgba(27,58,92,.10); }
.warn { color:var(--warn-ink); }
"""
def dots(kind_fn, t0, step):
    out=[]
    for i in range(338):
        out.append(f'<i class="cell {kind_fn(i)} m" style="--in:pop; --t:{t0}s; --i:{i}; --stagger:{step}s; --in-dur:.45s"></i>')
    return "\n".join(out)

# 01
s1 = HEAD % (COMMON + """
.safe { align-content:center; justify-items:center; gap:calc(var(--u)*4); }
h1.title { max-width:none; text-align:center; }
""", f"""<main class="stage"><div class="safe">
<div class="grid338" data-texture>{dots(lambda i:'', -1.4, 0.0025)}</div>
</div></main>
<header class="hud"><div class="safe" style="align-content:start; justify-items:center; padding-top:calc(var(--u)*5)">
<h1 class="title m" data-headline style="--in:rise; --t:-0.8s; text-align:center; max-width:none">Laporan SGTGU Q3 2026</h1>
</div><div class="safe" style="align-content:end; justify-items:center; padding-bottom:calc(var(--u)*5)">
<p class="sub m" style="--in:rise; --t:.5s; text-align:center; max-width:none">338 kes dalam FRAME Q3</p>
</div></header>""")

# 02
s2 = HEAD % (COMMON + """
.safe { align-content:center; justify-items:center; gap:calc(var(--u)*4); }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:calc(var(--u)*3); width:100%; max-width:calc(var(--u)*150); }
.kpi { padding:calc(var(--u)*2.4) calc(var(--u)*3); display:grid; gap:.2em; justify-items:start; }
.kpi .n { font-size:calc(var(--u)*9); font-weight:800; line-height:1; letter-spacing:-.03em; font-variant-numeric:tabular-nums; }
.kpi .l { font-size:var(--fs-body); font-weight:600; color:var(--fg); }
""", f"""<main class="stage"><div class="safe" style="padding-top:calc(var(--u)*23)">
<div class="grid338" data-texture style="--cs:calc(var(--u)*1.9); --cg:calc(var(--u)*.9)">{dots(lambda i:'ok' if i<330 else 'todo', -0.4, 0.0005)}</div>
<div class="kpis">
<div class="card kpi m" style="--in:rise; --t:.5s"><span class="n accent"><span data-count="330" data-at=".7" data-dur="1.2" data-ease="linear" data-sfx="ticker" data-sfx-intent="count-up">330</span></span><span class="l">kes berkod</span></div>
<div class="card kpi m" style="--in:rise; --t:.65s"><span class="n warn"><span data-count="8" data-at=".85" data-dur="1.0">8</span></span><span class="l">belum keyin</span></div>
<div class="card kpi m" style="--in:rise; --t:.8s"><span class="n accent"><span data-count="97.6" data-decimals="1" data-suffix="%" data-at="1.9" data-dur="1.0" data-ease="linear" data-sfx="ticker" data-sfx-intent="count-up">97.6%</span></span><span class="l">siap</span></div>
</div></div></main>
<header class="hud"><div class="safe" style="align-content:start; justify-items:start; padding-top:calc(var(--u)*3)">
<p class="kicker m" style="--in:fade; --t:-0.2s"><b>00</b>Ringkasan</p>
<h1 class="title m" data-headline style="--in:rise; --t:-0.2s; max-width:none">Hampir siap</h1>
</div></header>""")

# 03
fes=[("AFIF",113,113),("ELIYANA",112,111),("IZAT",113,106)]
rows=[]
for k,(n,j,b) in enumerate(fes):
    t=0.5+k*0.45
    pct=b/j*100
    orange = f'<div class="seg todo m" style="--in:fade; --t:{t+1.0}s; left:{pct:.3f}%; width:{100-pct:.3f}%"></div>' if b<j else ''
    rows.append(f"""<div class="row">
<span class="who m" style="--in:left; --t:{t}s">{n}</span>
<div class="track"><div class="seg ok m" style="--in:grow-x; --t:{t+0.1}s; --in-dur:1.1s; --in-ease:var(--ease-out); transform-origin:left; width:{pct:.3f}%"></div>{orange}</div>
<span class="cnt m" style="--in:fade; --t:{t+0.9}s">{b}/{j} berkod</span>
<span class="rest m {'warn' if b<j else 'accent'}" style="--in:fade; --t:{t+1.0}s">{j-b} baki</span>
</div>""")
s3 = HEAD % (COMMON + """
.safe { align-content:center; gap:calc(var(--u)*4.5); }
.row { display:grid; grid-template-columns:calc(var(--u)*20) 1fr calc(var(--u)*27) calc(var(--u)*13); align-items:center; gap:calc(var(--u)*2); }
.who { font-size:var(--fs-sub); font-weight:800; letter-spacing:-.01em; }
.track { position:relative; height:calc(var(--u)*5.6); border-radius:calc(var(--u)*1.2); background:#dde6ee; overflow:hidden; }
.seg { position:absolute; top:0; bottom:0; left:0; }
.seg.ok { background:var(--accent); }
.seg.todo { background:var(--accent-2); }
.cnt { font-size:var(--fs-body); font-weight:700; }
.rest { font-size:var(--fs-body); font-weight:800; text-align:right; }
""", f"""<main class="stage"><div class="safe" style="padding-top:calc(var(--u)*10)">
{''.join(rows)}
</div></main>
<header class="hud"><div class="safe" style="align-content:start; justify-items:start; padding-top:calc(var(--u)*3)">
<p class="kicker m" style="--in:fade; --t:-0.2s"><b>01</b>Mengikut FE</p>
<h1 class="title m" data-headline style="--in:rise; --t:-0.2s; max-width:none">Kemajuan mengikut FE</h1>
</div></header>""")

# 04
codes=[("11",261),("22",42),("12",17),("31",5),("40",3),("13",1),("23",1)]
rows=[]
for k,(c,v) in enumerate(codes):
    t=0.4+k*0.28
    w=max(v/261*100,0.9)
    rows.append(f"""<div class="row">
<span class="who m" style="--in:left; --t:{t}s">Kod {c}</span>
<div class="track"><div class="seg ok m" style="--in:grow-x; --t:{t+0.05}s; --in-dur:.9s; transform-origin:left; width:{w:.3f}%"></div></div>
<span class="cnt m num" style="--in:fade; --t:{t+0.6}s">{v}</span>
</div>""")
s4 = HEAD % (COMMON + """
.safe { align-content:center; gap:calc(var(--u)*2.6); }
.row { display:grid; grid-template-columns:calc(var(--u)*17) 1fr calc(var(--u)*11); align-items:center; gap:calc(var(--u)*2); }
.who { font-size:var(--fs-body); font-weight:800; }
.track { position:relative; height:calc(var(--u)*4); border-radius:calc(var(--u)*1); background:#dde6ee; overflow:hidden; }
.seg { position:absolute; top:0; bottom:0; left:0; }
.seg.ok { background:var(--accent); }
.cnt { font-size:var(--fs-body); font-weight:800; text-align:right; }
""", f"""<main class="stage"><div class="safe" style="padding-top:calc(var(--u)*12)">
{''.join(rows)}
</div></main>
<header class="hud"><div class="safe" style="align-content:start; justify-items:start; padding-top:calc(var(--u)*3)">
<p class="kicker m" style="--in:fade; --t:-0.2s"><b>02</b>Keputusan</p>
<h1 class="title m" data-headline style="--in:rise; --t:-0.2s; max-width:none">Pecahan kod keputusan Q3</h1>
</div></header>""")

# 05
s5 = HEAD % (COMMON + """
.safe { align-content:center; justify-items:center; gap:calc(var(--u)*3); }
.big { font-size:calc(var(--u)*22); font-weight:800; line-height:1; letter-spacing:-.04em; color:var(--warn-ink); text-align:center; }
""", """<main class="stage"><div class="safe">
<div class="big m" style="--in:zoom; --t:-0.2s" data-sfx="thud" data-sfx-intent="soft-impact"><span data-count="8" data-at="0" data-dur=".8">8</span></div>
<p class="title m" style="--in:rise; --t:.1s; text-align:center; max-width:none">kes lagi untuk 100%</p>
<p class="sub m" style="--in:fade; --t:.7s; text-align:center; max-width:none">IZAT 7 · ELIYANA 1</p>
</div></main>
<header class="hud"><div class="safe" style="align-content:end; justify-items:center; padding-bottom:calc(var(--u)*3)">
<p class="body m" style="--in:fade; --t:.6s; color:var(--muted); text-align:center; max-width:none">Kemaskini 22 Oktober 2026 · SGTGU Q3 2026</p>
</div></header>""")

for n,(name,html) in enumerate([("01-hook",s1),("02-siap",s2),("03-fe",s3),("04-kod",s4),("05-tutup",s5)]):
    open(f"scenes/{name}.html","w").write(html)
json.dump({"width":1920,"height":1080,"fps":30,"output":"out/video.mp4","scenes":[
 {"file":"scenes/01-hook.html","duration":2.5},{"file":"scenes/02-siap.html","duration":3.5},
 {"file":"scenes/03-fe.html","duration":5},{"file":"scenes/04-kod.html","duration":4.5},{"file":"scenes/05-tutup.html","duration":3.5}]},
 open("video.json","w"),indent=2)
