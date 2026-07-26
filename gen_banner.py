#!/usr/bin/env python3
"""NEURAL SENTINEL v4 — big sentinel, clean layout, no clutter."""
import math, random
random.seed(7)

W, H = 1000, 300

# ── BIG invader (14×10, PX=14) ──
I = [
    [0,0,0,1,1,0,1,0,1,1,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,0,0,1,1,1,0,0,1,1,0,0],
    [0,1,0,1,0,1,1,1,0,1,0,1,0,0],
    [1,1,0,1,0,1,0,1,0,1,0,1,1,0],
    [0,1,1,0,0,1,1,1,0,0,1,1,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,0,1,1,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,1,1,1,0,1,0,0,0,0],
]
PX = 14
C, R = len(I[0]), len(I)
# Center it
IX = (W - C*PX) // 2
IY = (H - R*PX) // 2 - 10  # shift up a bit for text below
GX, GY = IX + C*PX//2, IY + R*PX//2

stars = [(random.randint(0,W), random.randint(0,H-50), random.uniform(0.1,0.5)) for _ in range(40)]

def D():
    return '''  <defs>
    <radialGradient id="bgG" cx="50%" cy="50%" r="68%">
      <stop offset="0%" stop-color="#160828"/>
      <stop offset="45%" stop-color="#0a0414"/>
      <stop offset="100%" stop-color="#030108"/>
    </radialGradient>
    <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00ffff" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
    </radialGradient>
    <filter id="gE" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="18"/>
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#a855f7" stroke-width="0.3" opacity="0.02"/>
    </pattern>
    <pattern id="scn" width="3" height="3" patternUnits="userSpaceOnUse">
      <rect width="3" height="1" fill="rgba(0,0,0,0.06)"/>
    </pattern>
  </defs>'''

def bg():
    scn = '<rect width="1000" height="300" fill="url(#scn)"/>'
    return f'''  <rect width="{W}" height="{H}" fill="url(#bgG)"/>
  {"".join(f'<circle cx="{x}" cy="{y}" r="0.6" fill="#fff" opacity="{o}"/>' for x,y,o in stars)}
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  {scn}'''

def inv():
    p = []
    # Aura
    p.append(f'  <circle cx="{GX}" cy="{GY}" r="110" fill="url(#eyeGlow)"/>')
    p.append(f'  <circle cx="{GX}" cy="{GY}" r="75" fill="#a855f7" opacity="0.04" filter="url(#gE)"/>')
    # Glitch stripes
    for ri, iv in [(2,0.22),(4,0.15),(7,0.25),(8,0.12)]:
        gy = IY+ri*PX
        p.append(f'  <rect x="{IX-4}" y="{gy}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="{iv}"/>')
    if hasattr(random, 'randint'):
        pass  # will use below
    # Pixels
    for r in range(R):
        for c in range(C):
            if I[r][c]==0: continue
            x=IX+c*PX; y=IY+r*PX
            if r<=1: f,o="#a855f7",0.5
            elif r==3 and c in(2,3,9,10): f,o="#00ffff",1.0
            elif r==4: f,o="#c084fc",0.65
            elif r in(7,8,9) and c in(3,7): f,o="#00ffff",0.55
            elif r>=7: f,o="#9ca3af",0.55
            else: f,o="#e2e8f0",0.85
            if random.random()<0.08:
                o*=random.uniform(0.3,0.7); x+=random.randint(-1,1)
            p.append(f'  <rect x="{x}" y="{y}" width="{PX}" height="{PX}" fill="{f}" opacity="{o}" rx="1.5"/>')
    # Eyes
    for ecx in (IX+2*PX, IX+9*PX):
        ey=IY+3*PX
        p.append(f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="24" fill="#00ffff" opacity="0.25" filter="url(#gE)"/>')
        p.append(f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="8" fill="#fff" opacity="0.95"/>')
    # Random glitch overlays
    for _ in range(5):
        gy2=IY+random.randint(0,R-1)*PX
        gh=PX//2 if random.random()<0.5 else PX
        p.append(f'  <rect x="{IX}" y="{gy2}" width="{C*PX}" height="{gh}" fill="#000" opacity="{random.uniform(0.04,0.15)}"/>')
    # Label below
    ly = IY + R*PX + 28
    p.append(f'  <text x="{GX}" y="{ly}" font-family="\'JetBrains Mono\',monospace" font-size="20" fill="#e9d5ff" text-anchor="middle" font-weight="800" letter-spacing="8">ERFIX_404</text>')
    p.append(f'  <text x="{GX}" y="{ly+24}" font-family="\'Courier New\',monospace" font-size="11" fill="#a855f7" text-anchor="middle" opacity="0.75" letter-spacing="4">AUTONOMOUS ARCHITECT</text>')
    return '\n'.join(p)

def side_panels():
    p = []
    # === LEFT ===
    x = 28
    # Title line
    p.append(f'  <text x="{x}" y="28" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold"># STATUS</text>')
    rows = [
        ("UNIT","ERFIX_404","#22d3ee",60),
        ("ROLE","AUTONOMOUS","#c084fc",48),
        ("STACK","PY · AI · n8n","#a855f7",48),
    ]
    for i,(l,v,c,w) in enumerate(rows):
        iy = 52 + i*24
        p.append(f'  <text x="{x}" y="{iy}" font-family="\'Courier New\',monospace" font-size="12" fill="#666">{l}</text>')
        p.append(f'  <text x="{x+75}" y="{iy}" font-family="\'Courier New\',monospace" font-size="12" fill="{c}">{v}</text>')

    # Metrics below
    my = 52 + 3*24 + 8
    p.append(f'  <line x1="{x}" y1="{my}" x2="{x+220}" y2="{my}" stroke="#333" stroke-width="1"/>')
    p.append(f'  <text x="{x}" y="{my+20}" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold"># METRICS</text>')
    bw = 160
    for i,(n,v,c) in enumerate([
        ("PYTHON",88,"#22d3ee"), ("AI",72,"#a855f7"),
        ("AUTO",65,"#c084fc"), ("SHIP",94,"#ff3278"),
    ]):
        my2 = my+40+i*22
        p.append(f'  <text x="{x}" y="{my2}" font-family="\'Courier New\',monospace" font-size="10" fill="#888">{n}</text>')
        ix = x+55
        fw = int(bw*v/100)
        p.append(f'  <rect x="{ix}" y="{my2-8}" width="{bw}" height="10" rx="4" fill="#0a0414" stroke="#444" stroke-width="0.4"/>')
        p.append(f'  <rect x="{ix}" y="{my2-8}" width="{fw}" height="10" rx="4" fill="{c}" opacity="0.85"/>')
        p.append(f'  <text x="{ix+bw+8}" y="{my2}" font-family="\'Courier New\',monospace" font-size="10" fill="#eee" font-weight="bold">{v}%</text>')

    # === RIGHT ===
    rx = 720
    p.append(f'  <text x="{rx}" y="28" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold"># LOG</text>')
    for i,(t,msg) in enumerate([
        ("19:22","Neural core init"),
        ("19:26","Agent online"),
        ("19:31","Deploy v2.1"),
        ("19:38","Orbit sync ok"),
        ("19:44","👾 sentinel active"),
    ]):
        iy = 52 + i*20
        p.append(f'  <text x="{rx}" y="{iy}" font-family="\'Courier New\',monospace" font-size="11" fill="#555">{t}</text>')
        p.append(f'  <text x="{rx+55}" y="{iy}" font-family="\'Courier New\',monospace" font-size="11" fill="#c4b5fd">{msg}</text>')

    # Project link
    my2 = 52 + 5*20 + 6
    p.append(f'  <line x1="{rx}" y1="{my2}" x2="{rx+200}" y2="{my2}" stroke="#333" stroke-width="1"/>')
    p.append(f'  <text x="{rx}" y="{my2+20}" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold"># PROJECTS</text>')
    for i,(n,s) in enumerate([("cafe-mehras","JS"),("hermes","PY"),("glitch-profile","SVG")]):
        iy = my2+40+i*22
        p.append(f'  <text x="{rx}" y="{iy}" font-family="\'Courier New\',monospace" font-size="11" fill="#888">▸ {n}</text>')
        p.append(f'  <text x="{rx+145}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="#555">{s}</text>')

    # Status
    sy = my2+40+3*22+5
    p.append(f'  <rect x="{rx-4}" y="{sy}" width="195" height="18" rx="5" fill="none" stroke="#444" stroke-width="0.5" opacity="0.5"/>')
    p.append(f'  <circle cx="{rx+8}" cy="{sy+9}" r="3" fill="#22d3ee"/>')
    p.append(f'  <text x="{rx+18}" y="{sy+12}" font-family="\'Courier New\',monospace" font-size="10" fill="#22d3ee">SYSTEM ONLINE // v3.0.0</text>')

    return '\n'.join(p)

def wave():
    pts = []
    for x in range(0,W,2):
        t = x/W*math.pi*3
        y = H-6 + math.sin(t)*5 + math.sin(t*2.3)*2.5
        pts.append(f"{x},{y:.1f}")
    return '\n'.join([
        f'  <line x1="0" y1="{H-6}" x2="{W}" y2="{H-6}" stroke="#222" stroke-width="1"/>',
        f'  <polyline points="{" ".join(pts)}" fill="none" stroke="#a855f7" stroke-width="1" opacity="0.2"/>',
    ])


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{D()}
{bg()}
{inv()}
{side_panels()}
{wave()}
</svg>'''

with open("/opt/data/glitch-profile/assets/banner.svg","w") as f:
    f.write(svg)
print(f"✅ v4 ({len(svg)} bytes) — sentinel at {C*PX}x{R*PX}px")
