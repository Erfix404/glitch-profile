#!/usr/bin/env python3
"""NEURAL SENTINEL v7 — final polish pass."""
import math, random

random.seed(42)
W, H = 1000, 320

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
PX, COLS, ROWS = 8, len(I[0]), len(I)
IX, IY = 340, 72
GX, GY = IX + COLS*PX/2, IY + ROWS*PX/2

N = [
    (50, 50,   "PYTHON",   12, 0),
    (50, 148,  "AI/LLM",   12, 0),
    (50, 246,  "n8n",      12, 0),
    (155, 52,  "AGENTS",   15, 1),
    (155, 148, "ORCH",     15, 1),
    (155, 245, "DEPLOY",   15, 1),
    (265, 100, "CORE",     20, 2),
    (265, 215, "SHIP",     20, 2),
]
C = [(0,3),(1,3),(1,4),(2,5),(3,6),(4,6),(4,7),(5,7),(3,4)]

CODE = [
    (0.045,"#22d3ee",9,"class NeuralSentinel:"),
    (0.050,"#a855f7",8,"    def __init__(self):"),
    (0.040,"#c084fc",8,"        self.agents = [Agent()]"),
    (0.045,"#ff3278",7,"        self.mode = Mode.AUTO"),
    (0.040,"#22d3ee",8,"    async def deploy(self, t):"),
    (0.045,"#a855f7",9,"        return await core.run(t)"),
    (0.035,"#c084fc",9,"from dataclasses import dataclass"),
    (0.040,"#ff3278",8,"@dataclass"),
    (0.035,"#a855f7",7,"class AgentConfig:"),
    (0.032,"#22d3ee",9,"    model: str = 'opencode'"),
    (0.035,"#c084fc",8,"    temp: float = 0.618"),
    (0.030,"#ff3278",9,"    max_tokens: int = 8192"),
    (0.038,"#22d3ee",8,"agent = Agent('erfix')"),
    (0.032,"#a855f7",8,"result = await agent.run()"),
    (0.035,"#c084fc",7,"# gh deploy --prod"),
    (0.030,"#22d3ee",10,"def system_prompt():"),
    (0.032,"#a855f7",8,"    return 'ship agents'"),
]

D = '''  <defs>
    <radialGradient id="screenG" cx="48%" cy="50%" r="72%">
      <stop offset="0%" stop-color="#180a30"/>
      <stop offset="45%" stop-color="#0c0518"/>
      <stop offset="100%" stop-color="#04020a"/>
    </radialGradient>
    <linearGradient id="panelBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#140e1e" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#080312" stop-opacity="0.96"/>
    </linearGradient>
    <filter id="g" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3"/>
    </filter>
    <filter id="gS" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="7"/>
    </filter>
    <filter id="gE" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="15"/>
    </filter>
    <filter id="gL" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2"/>
    </filter>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#a855f7" stroke-width="0.3" opacity="0.035"/>
    </pattern>
    <pattern id="scn" width="3" height="3" patternUnits="userSpaceOnUse">
      <rect width="3" height="1" fill="rgba(0,0,0,0.08)"/>
    </pattern>
    <style>
      .bk{animation:b 1.6s infinite}@keyframes b{0%,100%{opacity:1}50%{opacity:0.15}}
    </style>
  </defs>'''

def bg(): return f'''  <rect width="{W}" height="{H}" fill="#030108"/>
  <rect width="{W}" height="{H}" fill="url(#screenG)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>'''

def code_mat():
    parts=['  <g font-family="\'JetBrains Mono\',\'Courier New\',monospace" opacity="0.3">']
    for i,(op,clr,sz,t) in enumerate(CODE):
        col=i%4; x=36+col*90; y=78+i*14+(i%5)*5
        parts.append(f'    <text x="{x}" y="{y}" fill="{clr}" opacity="{op}" font-size="{sz}">{t}</text>')
        if random.random()<0.35:
            parts.append(f'    <text x="{x+80}" y="{y+150}" fill="{clr}" opacity="{op*0.15}" font-size="{sz}">{t}</text>')
    parts.append('  </g>'); return '\n'.join(parts)

def neural():
    parts=[]
    for fi,ti in C:
        x1,y1,_,_,_=N[fi]; x2,y2,_,_,_=N[ti]
        op=0.15+0.04*fi
        parts.append(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#a855f7" stroke-width="2" opacity="{op}" filter="url(#g)"/>')
        parts.append(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7c3aed" stroke-width="0.6" opacity="{op*0.3}"/>')
    cx,cy=N[6][0],N[6][1]
    parts.append(f'  <line x1="{cx}" y1="{cy}" x2="{GX}" y2="{GY}" stroke="#00ffff" stroke-width="2.5" opacity="0.2" filter="url(#gL)"/>')
    parts.append(f'  <line x1="{cx}" y1="{cy}" x2="{GX}" y2="{GY}" stroke="#22d3ee" stroke-width="0.5" opacity="0.1"/>')
    for idx,(nx,ny,label,r,layer) in enumerate(N):
        clr="#c084fc" if layer==2 else "#a855f7" if layer==1 else "#7c3aed"
        fill="#2a0a4e" if layer==2 else "#1a0a2e" if layer==1 else "#120a1e"
        if layer>0:
            parts.append(f'  <circle cx="{nx}" cy="{ny}" r="{r+4}" fill="none" stroke="{clr}" stroke-width="1" opacity="0.08" filter="url(#g)"/>')
        parts.append(f'  <circle cx="{nx}" cy="{ny}" r="{r}" fill="{fill}" stroke="{clr}" stroke-width="1.5" opacity="0.92"/>')
        parts.append(f'  <circle cx="{nx-r//3}" cy="{ny-r//3}" r="{r//4}" fill="{clr}" opacity="0.2"/>')
        parts.append(f'  <text x="{nx}" y="{ny+3}" font-family="\'JetBrains Mono\',\'Courier New\',monospace" font-size="{8+layer*2}" fill="{clr}" text-anchor="middle" font-weight="800" opacity="0.95">{label}</text>')
    return '\n'.join(parts)

def sentinel():
    parts=['  <!-- 👾 sentinel -->']
    parts.append(f'  <circle cx="{GX+2}" cy="{GY+2}" r="90" fill="#00ffff" opacity="0.025" filter="url(#gE)"/>')
    parts.append(f'  <circle cx="{GX}" cy="{GY}" r="65" fill="#a855f7" opacity="0.04" filter="url(#gS)"/>')
    parts.append(f'  <circle cx="{GX}" cy="{GY}" r="45" fill="#00ffff" opacity="0.035" filter="url(#gS)"/>')
    for ri,iv in [(2,0.18),(4,0.12),(7,0.2),(8,0.1)]:
        gy=IY+ri*PX; parts.append(f'  <rect x="{IX-4}" y="{gy}" width="{COLS*PX+8}" height="{PX}" fill="#444" opacity="{iv}"/>')
    for r in range(ROWS):
        for c in range(COLS):
            if I[r][c]==0: continue
            x=IX+c*PX; y=IY+r*PX
            if r<=1: f,o="#a855f7",0.55
            elif r==3 and c in(2,3,9,10): f,o="#00ffff",1.0
            elif r==4: f,o="#c084fc",0.7
            elif r in(7,8,9) and c in(3,7): f,o="#00ffff",0.55
            elif r>=7: f,o="#9ca3af",0.6
            else: f,o="#e2e8f0",0.88
            if random.random()<0.08: o*=random.uniform(0.3,0.7); x+=random.randint(-1,1)
            parts.append(f'  <rect x="{x}" y="{y}" width="{PX}" height="{PX}" fill="{f}" opacity="{o}" rx="1.2"/>')
    for ecx in (IX+2*PX, IX+9*PX):
        ey=IY+3*PX
        parts.append(f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="16" fill="#00ffff" opacity="0.3" filter="url(#gE)"/>')
        parts.append(f'  <circle cx="{ecx+PX//2}" cy="{ey+PX//2}" r="6" fill="#ffffff" opacity="0.95"/>')
        parts.append(f'  <rect x="{ecx+2}" y="{ey+2}" width="4" height="4" fill="#00ffff" opacity="1" rx="1"/>')
    for _ in range(5):
        gy2=IY+random.randint(0,ROWS-1)*PX; gh=PX//2 if random.random()<0.5 else PX
        parts.append(f'  <rect x="{IX}" y="{gy2}" width="{COLS*PX}" height="{gh}" fill="#000" opacity="{random.uniform(0.04,0.15)}"/>')
    ly2=IY+ROWS*PX+24
    parts.append(f'  <text x="{GX}" y="{ly2}" font-family="\'JetBrains Mono\',monospace" font-size="11" fill="#e9d5ff" text-anchor="middle" opacity="0.85" letter-spacing="4">[[ ERFIX_404 ]]</text>')
    return '\n'.join(parts)

def panel():
    px,py=670,48; pw,ph=295,228
    parts=[]
    parts.append(f'  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8" fill="url(#panelBg)" stroke="#2a2a2a" stroke-width="1"/>')
    parts.append(f'  <line x1="{px+14}" y1="{py+48}" x2="{px+pw-14}" y2="{py+48}" stroke="#333" stroke-width="1"/>')
    parts.append(f'  <line x1="{px+14}" y1="{py+142}" x2="{px+pw-14}" y2="{py+142}" stroke="#333" stroke-width="1"/>')
    parts.append(f'  <text x="{px+14}" y="{py+20}" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold">SYSTEM STATUS</text>')
    for i,(l,v,c) in enumerate([("Unit","ERFIX_404","#22d3ee"),("Role","ARCHITECT","#c084fc"),("Status","● ONLINE / SHIP","#22d3ee")]):
        iy=py+35+i*16
        parts.append(f'  <text x="{px+14}" y="{iy}" font-family="\'Courier New\',monospace" font-size="9" fill="#666">{l}</text>')
        parts.append(f'  <text x="{px+70}" y="{iy}" font-family="\'Courier New\',monospace" font-size="9" fill="{c}">{v}</text>')
    ny=py+60
    parts.append(f'  <text x="{px+14}" y="{ny}" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold">NEURAL METRICS</text>')
    bw=155
    for i,(n,v,c) in enumerate([("PYTHON",88,"#22d3ee"),("AGENTS",72,"#a855f7"),("N8N",65,"#c084fc"),("SHIP",94,"#ff3278")]):
        my=ny+18+i*18
        parts.append(f'  <text x="{px+14}" y="{my}" font-family="\'Courier New\',monospace" font-size="9" fill="#777">{n}</text>')
        ix=px+80
        parts.append(f'  <rect x="{ix}" y="{my-7}" width="{bw}" height="8" rx="4" fill="#0a0414" stroke="#333" stroke-width="0.4"/>')
        fw=int(bw*v/100)
        parts.append(f'  <rect x="{ix}" y="{my-7}" width="{fw}" height="8" rx="4" fill="{c}" opacity="0.85"/>')
        parts.append(f'  <text x="{ix+bw+6}" y="{my}" font-family="\'Courier New\',monospace" font-size="9" fill="#eee" font-weight="bold">{v}%</text>')
    logy=ny+90
    parts.append(f'  <text x="{px+14}" y="{logy}" font-family="\'JetBrains Mono\',monospace" font-size="10" fill="#7c3aed" font-weight="bold">AGENT LOG</text>')
    for i,(t,msg) in enumerate([("19:22","Neural core init"),("19:26","Agent online"),("19:31","Deploy v2.1"),("19:38","Orbit sync ok")]):
        ly2=logy+16+i*14
        parts.append(f'  <text x="{px+14}" y="{ly2}" font-family="\'Courier New\',monospace" font-size="8" fill="#555">{t}</text>')
        parts.append(f'  <text x="{px+54}" y="{ly2}" font-family="\'Courier New\',monospace" font-size="8" fill="#c4b5fd">{msg}</text>')
    return '\n'.join(parts)

def wave():
    x0,y0=50,H-85; pw=W-100
    parts=[]
    parts.append(f'  <line x1="{x0}" y1="{y0}" x2="{x0+pw}" y2="{y0}" stroke="#333" stroke-width="1"/>')
    pts,pts2=[],[]
    for x in range(0,pw,2):
        t=x/pw*math.pi*4
        y=y0+14+math.sin(t)*8+math.sin(t*2.3)*3.5+math.sin(t*0.6)*4
        pts.append(f"{x0+x},{y:.1f}")
        y2=y0+14+math.sin(t+1.2)*5+math.sin(t*1.8)*3
        pts2.append(f"{x0+x},{y2:.1f}")
    parts.append(f'  <polyline points="{" ".join(pts)}" fill="none" stroke="#00ffff" stroke-width="1.8" opacity="0.5" filter="url(#gL)"/>')
    parts.append(f'  <polyline points="{" ".join(pts2)}" fill="none" stroke="#a855f7" stroke-width="0.8" opacity="0.22"/>')
    return '\n'.join(parts)


# ── Assemble ──
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    D, bg(),
    # Monitor bezel
    '  <rect x="6" y="6" width="988" height="308" rx="20" fill="#1a1a1a" stroke="#444" stroke-width="2"/>',
    '  <rect x="12" y="12" width="976" height="296" rx="16" fill="#222" stroke="#333" stroke-width="1"/>',
    '  <rect x="18" y="18" width="964" height="284" rx="12" fill="none" stroke="#111" stroke-width="4"/>',
    '  <rect x="26" y="26" width="948" height="268" rx="8" fill="none" stroke="#2a2a2a" stroke-width="1.5"/>',
    '  <rect x="32" y="32" width="936" height="256" rx="6" fill="#0a0414"/>',
    '  <rect x="32" y="32" width="936" height="256" rx="6" fill="url(#scn)"/>',
    # Top bar — BRIGHTENED text
    '  <rect x="36" y="36" width="928" height="30" rx="4" fill="#1c0a32" opacity="0.6"/>',
    '  <rect x="36" y="36" width="928" height="30" rx="4" fill="none" stroke="#a855f7" stroke-width="0.4" opacity="0.3"/>',
    '  <text x="48" y="55" font-family="\'JetBrains Mono\',\'Courier New\',monospace" font-size="13" fill="#e9d5ff" font-weight="bold">ERFIX_404 // NEURAL SENTINEL</text>',
    '  <text x="880" y="55" font-family="\'Courier New\',monospace" font-size="9" fill="#22d3ee" class="bk">● SYSTEM ONLINE</text>',
    '  <circle cx="930" cy="48" r="4" fill="#22d3ee" class="bk"/>',
    '  <circle cx="930" cy="48" r="7" fill="none" stroke="#22d3ee" stroke-width="0.5" opacity="0.2"/>',
    # Bolts
    '  <circle cx="26" cy="26" r="5" fill="#444" stroke="#555" stroke-width="1"/>',
    f'  <circle cx="{W-26}" cy="26" r="5" fill="#444" stroke="#555" stroke-width="1"/>',
    f'  <circle cx="26" cy="{H-26}" r="5" fill="#444" stroke="#555" stroke-width="1"/>',
    f'  <circle cx="{W-26}" cy="{H-26}" r="5" fill="#444" stroke="#555" stroke-width="1"/>',
    # Bottom label — BRIGHTENED
    '  <rect x="430" y="278" width="120" height="14" rx="3" fill="none" stroke="#555" stroke-width="0.5" opacity="0.6"/>',
    '  <text x="440" y="288" font-family="\'Courier New\',monospace" font-size="8" fill="#888" letter-spacing="1">NEURAL SENTINEL v3.0.0</text>',
    code_mat(), neural(), sentinel(), panel(), wave(),
    '</svg>'
]

svg = '\n'.join(parts)
with open("/opt/data/glitch-profile/assets/banner.svg","w") as f: f.write(svg)
print(f"✅ v7 ({len(svg)} bytes)")
