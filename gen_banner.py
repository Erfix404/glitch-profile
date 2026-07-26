#!/usr/bin/env python3
"""NEURAL SENTINEL v5 — final polish. Ready for GitHub."""
import math, random
random.seed(7)

W, H = 1000, 300

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
IX = (W - C*PX)//2
IY = 38
GX, GY = IX + C*PX//2, IY + R*PX//2

stars = [(random.randint(0,W), random.randint(0,40), random.uniform(0.1,0.4)) for _ in range(15)]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="72%">
      <stop offset="0%" stop-color="#180a30"/>
      <stop offset="55%" stop-color="#0a0414"/>
      <stop offset="100%" stop-color="#030108"/>
    </radialGradient>
    <radialGradient id="glowE" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00ffff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00ffff" stop-opacity="0"/>
    </radialGradient>
    <filter id="bigGlow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="20"/>
    </filter>
    <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="#a855f7" stroke-width="0.3" opacity="0.025"/>
    </pattern>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  {"".join(f'<circle cx="{x}" cy="{y}" r="0.6" fill="#fff" opacity="{o}"/>' for x,y,o in stars)}
  <rect width="{W}" height="{H}" fill="url(#grid)"/>

  <!-- Top bar -->
  <rect x="0" y="0" width="{W}" height="30" fill="#1c0a32" opacity="0.5"/>
  <circle cx="16" cy="15" r="3" fill="#22d3ee" opacity="0.5"/>
  <text x="28" y="20" font-family="'Courier New',monospace" font-size="11" fill="#a855f7" font-weight="bold">ERFIX_404 // NEURAL SENTINEL</text>
  <circle cx="958" cy="15" r="3" fill="#22d3ee"/>
  <text x="930" y="20" font-family="'Courier New',monospace" font-size="10" fill="#22d3ee">● ONLINE</text>

  <!-- Sentinel -->
  <circle cx="{GX}" cy="{GY}" r="130" fill="url(#glowE)"/>
  <circle cx="{GX}" cy="{GY}" r="90" fill="#a855f7" opacity="0.03" filter="url(#bigGlow)"/>

  <rect x="{IX-4}" y="{IY+2*PX}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="0.18"/>
  <rect x="{IX-4}" y="{IY+4*PX}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="0.1"/>
  <rect x="{IX-4}" y="{IY+7*PX}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="0.2"/>
  <rect x="{IX-4}" y="{IY+8*PX}" width="{C*PX+8}" height="{PX}" fill="#444" opacity="0.08"/>
'''

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
        svg += f'  <rect x="{x}" y="{y}" width="{PX}" height="{PX}" fill="{f}" opacity="{o}" rx="1.5"/>\n'

# Eyes
for ecx in (IX+2*PX, IX+9*PX):
    ey=IY+3*PX
    svg += f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="28" fill="#00ffff" opacity="0.2" filter="url(#bigGlow)"/>\n'
    svg += f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="9" fill="#fff" opacity="0.95"/>\n'

# Glitch overlays
for _ in range(4):
    gy=IY+random.randint(0,R-1)*PX
    gh=PX//2 if random.random()<0.5 else PX
    svg += f'  <rect x="{IX}" y="{gy}" width="{C*PX}" height="{gh}" fill="#000" opacity="{random.uniform(0.04,0.12)}"/>\n'

# Text
y1 = IY+R*PX+32
y2 = y1+26
y3 = y2+26

svg += f'''
  <text x="{GX}" y="{y1}" font-family="'JetBrains Mono','Courier New',monospace" font-size="26" fill="#e9d5ff" text-anchor="middle" font-weight="800" letter-spacing="10">ERFIX_404</text>
  <text x="{GX}" y="{y2}" font-family="'Courier New',monospace" font-size="13" fill="#a855f7" text-anchor="middle" opacity="0.7" letter-spacing="5">AUTONOMOUS ARCHITECT</text>

  <g font-family="'Courier New',monospace" font-size="13" fill="#888" text-anchor="middle">
    <text x="325" y="{y3}">python</text>
    <text x="408" y="{y3}">◆</text>
    <text x="432" y="{y3}">ai agents</text>
    <text x="520" y="{y3}">◆</text>
    <text x="542" y="{y3}">n8n</text>
    <text x="615" y="{y3}">◆</text>
    <text x="638" y="{y3}">vibe code</text>
  </g>

  <line x1="0" y1="{H-6}" x2="{W}" y2="{H-6}" stroke="#222" stroke-width="1"/>
'''

pts = []
for x in range(0,W,2):
    t = x/W*math.pi*3
    y = H-6 + math.sin(t)*5 + math.sin(t*2.3)*2.5
    pts.append(f"{x},{y:.1f}")
svg += f'  <polyline points="{" ".join(pts)}" fill="none" stroke="#a855f7" stroke-width="1" opacity="0.15"/>\n'

svg += f'  <text x="{W-155}" y="{H-14}" font-family="\'Courier New\',monospace" font-size="8" fill="#444" letter-spacing="1">NEURAL SENTINEL v3.0.0</text>\n'

svg += '</svg>'

with open("/opt/data/glitch-profile/assets/banner.svg","w") as f:
    f.write(svg)
print(f"✅ v5 ({len(svg)} bytes)")
