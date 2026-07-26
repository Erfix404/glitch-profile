#!/usr/bin/env python3
"""SENTINEL X — wide canvas, big sentinel, breathing room."""
import math, random
random.seed(7)

W, H = 1000, 340

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
PX = 20
C, R = len(I[0]), len(I)
IX = (W - C*PX) // 2
IY = 32
GX = IX + C*PX//2
GY = IY + R*PX//2

STARS = [(random.randint(0,W), random.randint(0,H), random.uniform(0.2,0.6)) for _ in range(40)]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="340" viewBox="0 0 1000 340">
<defs>
  <radialGradient id="bg" cx="50%" cy="36%" r="70%">
    <stop offset="0%" stop-color="#1a0a35"/>
    <stop offset="60%" stop-color="#0a0414"/>
    <stop offset="100%" stop-color="#030108"/>
  </radialGradient>
  <radialGradient id="eg" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00ffff" stop-opacity="0.35"/>
    <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
  </radialGradient>
  <filter id="gf" x="-80%" y="-80%" width="260%" height="260%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="18"/>
  </filter>
  <pattern id="grd" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M 48 0 L 0 0 0 48" fill="none" stroke="#a855f7" stroke-width="0.3" opacity="0.02"/>
  </pattern>
  <style>
    @keyframes fp {{0%,100%{{opacity:0.2}}50%{{opacity:0.4}}}}
    @keyframes g1 {{0%,92%,100%{{transform:translate(0,0);opacity:0.1}}94%{{transform:translate(3px,0);opacity:0.2}}96%{{transform:translate(-2px,0);opacity:0.07}}98%{{transform:translate(1px,0);opacity:0.15}}}}
    @keyframes g2 {{0%,88%,100%{{transform:translate(0,0);opacity:0.08}}90%{{transform:translate(-4px,1px);opacity:0.18}}92%{{transform:translate(2px,-1px);opacity:0.05}}95%{{transform:translate(-1px,0);opacity:0.14}}}}
    @keyframes ep {{0%,100%{{transform:scale(1);opacity:0.15}}50%{{transform:scale(1.15);opacity:0.3}}}}
    @keyframes egl {{0%,100%{{transform:scale(1);opacity:0.85}}50%{{transform:scale(1.12);opacity:1}}}}
    @keyframes fk {{0%,100%{{opacity:1}}50%{{opacity:0.96}}}}
    @keyframes tg {{0%,100%{{opacity:0.7}}50%{{opacity:1}}}}
    .fk{{animation:fk 0.08s infinite}}
    .ep{{animation:ep 2.2s ease-in-out infinite;transform-origin:center}}
    .egl{{animation:egl 2.2s ease-in-out infinite;transform-origin:center}}
    .tg{{animation:tg 3s ease-in-out infinite}}
  </style>
</defs>
<rect width="1000" height="340" fill="url(#bg)"/>
'''
for x,y,o in STARS:
    sz = 0.5 + random.random()*0.6
    svg += f'<circle class="fk" cx="{x}" cy="{y}" r="{sz}" fill="#fff" opacity="{o}"/>\n'
svg += '<rect width="1000" height="340" fill="url(#grd)"/>\n'

svg += f'<circle class="ep fk" cx="{GX}" cy="{GY-8}" r="90" fill="url(#eg)"/>\n'

for r in range(R):
    for c in range(C):
        if I[r][c]==0: continue
        x=IX+c*PX; y=IY+r*PX
        if r<=1: f,o="#a855f7",0.5
        elif r==3 and c in(2,3,9,10): f,o="#00ffff",1
        elif r==4 and c in(2,3,9,10): f,o="#fff",0.9
        elif r==4: f,o="#c084fc",0.65
        elif r in(7,8,9) and c in(3,7): f,o="#00ffff",0.5
        elif r>=7: f,o="#9ca3af",0.55
        else: f,o="#e2e8f0",0.85
        svg += f'<rect class="fk" x="{x}" y="{y}" width="{PX-1}" height="{PX-1}" fill="{f}" opacity="{o}" rx="1.5"/>\n'

for ecx in (IX+2*PX, IX+9*PX):
    ey=IY+3*PX+PX//2
    svg += f'<circle class="ep" cx="{ecx}" cy="{ey}" r="28" fill="#00ffff" filter="url(#gf)"/>\n'
    svg += f'<circle class="egl" cx="{ecx}" cy="{ey}" r="8" fill="#fff"/>\n'
    svg += f'<circle class="egl" cx="{ecx}" cy="{ey}" r="3" fill="#00ffff"/>\n'

for i,gy in enumerate([IY+2*PX+2, IY+4*PX+4, IY+7*PX]):
    svg += f'<rect class="fk" x="{IX-6}" y="{gy}" width="{C*PX+12}" height="3" fill="#fff" opacity="0.08" style="animation:g1 {1.8+i*0.3}s infinite"/>\n'
    svg += f'<rect class="fk" x="{IX-6}" y="{gy+7}" width="{C*PX+12}" height="2" fill="#a855f7" opacity="0.05" style="animation:g2 {2+i*0.4}s infinite"/>\n'

svg += '''<g class="fk">
  <pattern id="scn" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#000" opacity="0.05"/>
  </pattern>
  <rect width="1000" height="340" fill="url(#scn)"/>
</g>
'''

y_label = IY + R*PX + 28
svg += f'''<text x="{GX}" y="{y_label}" font-family="'JetBrains Mono','Courier New',monospace" font-size="26" fill="#e9d5ff" text-anchor="middle" font-weight="800" letter-spacing="10">ERFIX_404</text>
<text class="tg" x="{GX}" y="{y_label+28}" font-family="'Courier New',monospace" font-size="14" fill="#a855f7" text-anchor="middle" letter-spacing="6">AUTONOMOUS ARCHITECT</text>
'''

yt = y_label + 54
tags = ["python", "ai agents", "n8n", "vibe code"]
for i,t in enumerate(tags):
    delay = i * 0.7
    tx = GX - 195 + i*130
    svg += f'<text x="{tx}" y="{yt}" font-family="\'Courier New\',monospace" font-size="12" fill="#a855f7" text-anchor="middle" opacity="0.8" style="animation:tg {2.5+delay*0.3}s ease-in-out infinite;animation-delay:{delay}s">{t}</text>\n'

svg += f'<line x1="0" y1="334" x2="1000" y2="334" stroke="#222" stroke-width="1"/>\n'
svg += f'<text x="985" y="328" font-family="\'Courier New\',monospace" font-size="8" fill="#777" text-anchor="end" letter-spacing="2" font-weight="bold">SENTINEL X</text>\n'
svg += '</svg>'

with open("/opt/data/glitch-profile/assets/banner.svg","w") as f:
    f.write(svg)
print(f"✅ X ({len(svg)}b)")
