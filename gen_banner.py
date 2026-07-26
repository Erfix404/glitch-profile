#!/usr/bin/env python3
"""ERFIX_404 banner — clean, big sentinel, no overlap. v2."""
import math, random
random.seed(7)

W, H = 1000, 300

# Sentinal 14x10, PX=16
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
PX = 16
C, R = len(I[0]), len(I)
IX = (W - C*PX) // 2
IY = 26
GX = IX + C*PX//2
GY = IY + R*PX//2

STARS = [(random.randint(0,W), random.randint(0,70), random.uniform(0.1,0.4)) for _ in range(25)]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="300" viewBox="0 0 1000 300">
<defs>
  <radialGradient id="bg" cx="50%" cy="42%" r="70%">
    <stop offset="0%" stop-color="#180a30"/>
    <stop offset="50%" stop-color="#0a0414"/>
    <stop offset="100%" stop-color="#030108"/>
  </radialGradient>
  <radialGradient id="eg" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00ffff" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
  </radialGradient>
  <filter id="bgf" x="-80%" y="-80%" width="260%" height="260%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="20"/>
  </filter>
  <pattern id="grd" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M 48 0 L 0 0 0 48" fill="none" stroke="#a855f7" stroke-width="0.25" opacity="0.02"/>
  </pattern>
  <pattern id="scn" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="rgba(0,0,0,0.04)"/>
  </pattern>
</defs>
<rect width="1000" height="300" fill="url(#bg)"/>
'''
for x,y,o in STARS:
    svg += f'<circle cx="{x}" cy="{y}" r="0.7" fill="#fff" opacity="{o}"/>\n'
svg += '<rect width="1000" height="300" fill="url(#grd)"/>\n'

# Sentinel glow
svg += f'<circle cx="{GX}" cy="{GY}" r="130" fill="url(#eg)"/>\n'
svg += f'<circle cx="{GX}" cy="{GY}" r="90" fill="#a855f7" opacity="0.04" filter="url(#bgf)"/>\n'

# Glitch stripes on sentinel
for yy,op in [(IY+2*PX,0.12),(IY+4*PX,0.06),(IY+7*PX,0.15)]:
    svg += f'<rect x="{IX-4}" y="{yy}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="{op}"/>\n'

# Pixels
for r in range(R):
    for c in range(C):
        if I[r][c]==0: continue
        x=IX+c*PX; y=IY+r*PX
        if r<=1: f,o="#a855f7",0.45
        elif r==3 and c in(2,3,9,10): f,o="#00ffff",1.0  # eyes
        elif r==4: f,o="#c084fc",0.6
        elif r in(7,8,9) and c in(3,7): f,o="#00ffff",0.5
        elif r>=7: f,o="#9ca3af",0.5
        else: f,o="#e2e8f0",0.85
        svg += f'<rect x="{x}" y="{y}" width="{PX}" height="{PX}" fill="{f}" opacity="{o}" rx="1.5"/>\n'

# Eyes glow
for ecx in (IX+2*PX, IX+9*PX):
    ey=IY+3*PX
    svg += f'<circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="30" fill="#00ffff" opacity="0.18" filter="url(#bgf)"/>\n'
    svg += f'<circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="9" fill="#fff" opacity="0.95"/>\n'
    svg += f'<circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="4" fill="#00ffff" opacity="0.9"/>\n'

# Extra random glitch
for _ in range(3):
    gy=IY+random.randint(0,R-1)*PX
    gh=PX//2 if random.random()<0.5 else PX
    svg += f'<rect x="{IX}" y="{gy}" width="{C*PX}" height="{gh}" fill="#000" opacity="{random.uniform(0.03,0.1)}"/>\n'

svg += '<rect width="1000" height="300" fill="url(#scn)"/>\n'

# ── LEFT PANEL ──
lx = 22
svg += f'''<rect x="{lx-8}" y="22" width="178" height="152" rx="6" fill="#0c0518" stroke="#2a0a4e" stroke-width="1" opacity="0.7"/>
<text x="{lx}" y="34" font-family="'JetBrains Mono','Courier New',monospace" font-size="11" fill="#7c3aed" font-weight="bold"># STATUS</text>
'''
for i,(l,v,c) in enumerate([
    ("UNIT","ERFIX_404","#22d3ee"),
    ("ROLE","AUTONOMOUS","#c084fc"),
    ("STACK","PY · AI · n8n","#a855f7"),
    ("MOOD","SHIPPING","#22d3ee"),
]):
    iy = 55 + i*20
    svg += f'<text x="{lx}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="#666">{l}</text>\n'
    svg += f'<text x="{lx+62}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="{c}">{v}</text>\n'

# Gap spacer (sentinel body sits here, no panel content overlaps)
bot_y = 55 + 4*20 + 4
svg += f'<line x1="{lx}" y1="{bot_y}" x2="{lx+155}" y2="{bot_y}" stroke="#333" stroke-width="1"/>\n'

svg += f'<text x="{lx}" y="{bot_y+17}" font-family="\'JetBrains Mono\',\'Courier New\',monospace" font-size="11" fill="#7c3aed" font-weight="bold"># METRICS</text>\n'
bw = 110
for i,(n,v,c) in enumerate([
    ("PYTHON","88","#22d3ee"), ("AI","72","#a855f7"),
    ("N8N","65","#c084fc"), ("SHIP","94","#ff3278"),
]):
    my = bot_y+32+i*18
    ix = lx+42
    fw = int(bw*int(v)/100)
    svg += f'<text x="{lx}" y="{my}" font-family="\'Courier New\',monospace" font-size="9" fill="#888">{n}</text>\n'
    svg += f'<rect x="{ix}" y="{my-6}" width="{bw}" height="9" rx="3" fill="#0a0414" stroke="#444" stroke-width="0.4"/>\n'
    svg += f'<rect x="{ix}" y="{my-6}" width="{fw}" height="9" rx="3" fill="{c}" opacity="0.85"/>\n'
    svg += f'<text x="{ix+bw+8}" y="{my}" font-family="\'Courier New\',monospace" font-size="9" fill="#eee" font-weight="bold">{v}%</text>\n'

# ── RIGHT PANEL ──
rx = 742
svg += f'''<rect x="{rx-8}" y="22" width="191" height="152" rx="6" fill="#0c0518" stroke="#2a0a4e" stroke-width="1" opacity="0.7"/>
<text x="{rx}" y="34" font-family="'JetBrains Mono','Courier New',monospace" font-size="11" fill="#7c3aed" font-weight="bold"># LOG</text>
'''
for i,(t,msg) in enumerate([
    ("19:22","Neural core init"),
    ("19:26","Agent online"),
    ("19:31","Deploy v2.1"),
    ("19:38","Orbit sync ok"),
    ("19:44","Sentinel active"),
]):
    iy = 55 + i*20
    svg += f'<text x="{rx}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="#555">{t}</text>\n'
    svg += f'<text x="{rx+50}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="#c4b5fd">{msg}</text>\n'

rb = 55 + 5*20 + 4
svg += f'<line x1="{rx}" y1="{rb}" x2="{rx+180}" y2="{rb}" stroke="#333" stroke-width="1"/>\n'

svg += f'<text x="{rx}" y="{rb+17}" font-family="\'JetBrains Mono\',\'Courier New\',monospace" font-size="11" fill="#7c3aed" font-weight="bold"># PROJECTS</text>\n'
for i,(n,s) in enumerate([("cafe-mehras","JS"),("hermes","PY"),("glitch-profile","SVG")]):
    iy = rb+32+i*18
    svg += f'<text x="{rx}" y="{iy}" font-family="\'Courier New\',monospace" font-size="10" fill="#888">▸ {n}</text>\n'
    svg += f'<text x="{rx+130}" y="{iy}" font-family="\'Courier New\',monospace" font-size="9" fill="#555">{s}</text>\n'

# Online indicator
sy = rb+32+3*18+6
svg += f'<circle cx="{rx+8}" cy="{sy+4}" r="3" fill="#22d3ee"/>\n'
svg += f'<text x="{rx+18}" y="{sy+8}" font-family="\'Courier New\',monospace" font-size="9" fill="#22d3ee">SYSTEM ONLINE // v3.0.0</text>\n'

# ── CENTER TEXT ──
y_label = IY + R*PX + 18
svg += f'''<text x="{GX}" y="{y_label}" font-family="'JetBrains Mono','Courier New',monospace" font-size="22" fill="#e9d5ff" text-anchor="middle" font-weight="800" letter-spacing="8">ERFIX_404</text>
<text x="{GX}" y="{y_label+22}" font-family="'Courier New',monospace" font-size="13" fill="#a855f7" text-anchor="middle" opacity="0.85" letter-spacing="4">AUTONOMOUS ARCHITECT</text>
'''

# Tags
yt = y_label + 44
tags = ["python","ai agents","n8n","vibe code"]
for i,t in enumerate(tags):
    tx = GX - 195 + i*130
    svg += f'<text x="{tx}" y="{yt}" font-family="\'Courier New\',monospace" font-size="11" fill="#a855f7" text-anchor="middle" opacity="0.8">{t}</text>\n'

# Footer
svg += f'<line x1="0" y1="292" x2="1000" y2="292" stroke="#222" stroke-width="1"/>\n'
pts = [f"{x},{292+math.sin(x/W*math.pi*3)*4+math.sin(x/W*math.pi*7)*2}" for x in range(0,W,2)]
svg += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#a855f7" stroke-width="1" opacity="0.12"/>\n'
svg += f'<text x="985" y="286" font-family="\'Courier New\',monospace" font-size="7" fill="#444" text-anchor="end" letter-spacing="1">SENTINEL v3</text>\n'

svg += '</svg>'

with open("/opt/data/glitch-profile/assets/banner.svg","w") as f:
    f.write(svg)
print(f"✅ v2 ({len(svg)} bytes)")
