#!/usr/bin/env python3
"""Fabrique tout ce qui est dérivé : SVG animés, image de partage, index de la page, compteurs.

Usage :  python3 tools/build_svg.py              régénère assets/*.svg et assets/social-preview.png
         python3 tools/build_svg.py --sync-docs  met aussi à jour docs/ et les compteurs des documents

Avec --sync-docs, le script relit kb/ et :
  - injecte dans docs/index.html la police et les personnages (bloc pixel-data), l'index des fiches
    et des découpages (bloc kb-data : identifiant vidéo, durée, nombre de scènes comptées dans chaque
    fichier de kb/episodes/), les compteurs (<span data-stat="...">), les balises meta et l'icône ;
  - écrit docs/404.html et docs/social-preview.png ;
  - met à jour les compteurs de README.md et STRUCTURE.md (<!--n:cle-->...<!--/n-->), les poids du
    sommaire, le texte alternatif des badges et le tableau des découpages du README.
Rien n'est écrit en dur : changer kb/ puis relancer suffit. Relancer deux fois ne change rien.

Contraintes tenues pour les SVG (un README GitHub n'exécute ni JS ni CSS externe) :
  - aucun <script>, aucun <foreignObject>, aucune police ni ressource externe ;
  - tout le texte est dessiné en pixels (glyphes 5x7 définis une fois dans <defs>, repris par <use>) ;
  - chaque SVG porte son propre fond opaque : lisible en thème clair et sombre ;
  - animations CSS @keyframes uniquement ; l'état de base (sans animation) est une image
    lisible, c'est elle qui s'affiche avec prefers-reduced-motion.
Tout le graphisme est original. Rien ne vient de la série. Aucune dépendance hors bibliothèque standard.
"""
import json
import random
import re
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "tools" / "pixel.json").read_text(encoding="utf-8"))
FONT = DATA["font"]
ACC = dict(DATA["accents"])
SPR = DATA["sprites"]

INK = "#0d0f2b"      # bleu nuit du sous-sol
DEEP = "#070818"     # écran éteint
INK2 = "#1b1f52"
PAPER = "#ece6d0"    # plastique beige
RED = "#e4252d"      # la porte
CYAN = "#2ee6e6"
YEL = "#f5d90a"
MAG = "#e23be0"
GRN = "#35d46a"
BLUE = "#2a39ff"
GREY = "#8e93b8"
ORG = "#ff8a1e"
VIO = "#a98bff"


# ---------------------------------------------------------------- pixels
def runs_path(rows, y0=0, ch="#"):
    """Chemin SVG des pixels égaux à ch, runs horizontaux fusionnés."""
    d = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            if row[x] == ch:
                w = 1
                while x + w < len(row) and row[x + w] == ch:
                    w += 1
                d.append(f"M{x} {y + y0}h{w}v1h-{w}z")
                x += w
            else:
                x += 1
    return "".join(d)


def glyph_d(c):
    comp = DATA["composed"].get(c)
    if comp:
        base, acc = comp
        d = runs_path(FONT[base].split("/"))
        if acc == "cedilla":
            d += runs_path(["..#..", ".#..."], y0=7)
        else:
            d += runs_path(ACC[acc], y0=-3)
        return d
    if c not in FONT:
        raise KeyError(f"glyphe manquant : {c!r}")
    return runs_path(FONT[c].split("/"))


class Doc:
    def __init__(self, w, h, title, desc, bg=INK, radius=14):
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.bg, self.radius = bg, radius
        self.glyphs = {}
        self.defs = []
        self.css = []
        self.body = []
        self.n = 0

    def uid(self, p="k"):
        self.n += 1
        return f"{p}{self.n}"

    def gid(self, c):
        if c not in self.glyphs:
            self.glyphs[c] = f"g{ord(c):x}"
        return self.glyphs[c]

    @staticmethod
    def tw(s, scale):
        return (6 * len(s) - 1) * scale

    def text(self, x, y, s, scale, fill, cls=None, anchor="start", extra=""):
        """Texte pixel. (x, y) = coin haut gauche (ou centre/droite selon anchor)."""
        w = self.tw(s, scale)
        if anchor == "middle":
            x -= w / 2
        elif anchor == "end":
            x -= w
        uses = "".join(
            f'<use href="#{self.gid(c)}" x="{i * 6}"/>' for i, c in enumerate(s) if c != " "
        )
        c = f' class="{cls}"' if cls else ""
        return (f'<g{c} transform="translate({x:g} {y:g}) scale({scale:g})" '
                f'fill="{fill}"{extra}>{uses}</g>')

    def sprite(self, rows, colors, scale, x=0, y=0, cls=None, flip=False):
        """rows : lignes ; colors : {'#': couleur, 'o': ..., 'a': ...}."""
        w = len(rows[0])
        parts = []
        for ch, col in colors.items():
            d = runs_path(rows, ch=ch)
            if d:
                parts.append(f'<path fill="{col}" d="{d}"/>')
        t = f"translate({x:g} {y:g}) scale({scale:g})"
        if flip:
            t = f"translate({x + w * scale:g} {y:g}) scale({-scale:g} {scale:g})"
        c = f' class="{cls}"' if cls else ""
        return f'<g{c} transform="{t}">{"".join(parts)}</g>'

    def kf(self, name, stops):
        """stops : [(pct ou 'a,b', 'prop:val;...')]."""
        body = "".join(
            f"{(p if isinstance(p, str) else f'{p:g}%')}{{{v}}}" for p, v in stops
        )
        self.css.append(f"@keyframes {name}{{{body}}}")

    def window(self, name, segs, on="opacity:1", off="opacity:0"):
        """Visible seulement pendant les intervalles [a, b] (en %)."""
        stops = []
        cur = 0.0
        e = 0.01
        for a, b in segs:
            if a > cur:
                stops.append((f"{cur:g}%,{max(cur, a - e):g}%", off))
            stops.append((f"{a:g}%,{b:g}%", on))
            cur = b + e
        if cur < 100:
            stops.append((f"{cur:g}%,100%", off))
        self.kf(name, stops)

    def add(self, *s):
        self.body.extend(s)

    def render(self):
        gl = "".join(f'<path id="{i}" d="{glyph_d(c)}"/>' for c, i in self.glyphs.items())
        css = "".join(self.css)
        css += "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
        r = self.radius
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-labelledby="t d" '
            f'shape-rendering="crispEdges">'
            f'<title id="t">{self.title}</title><desc id="d">{self.desc}</desc>'
            f"<style>{css}</style>"
            f'<defs><clipPath id="frame"><rect width="{self.w}" height="{self.h}" rx="{r}"/></clipPath>'
            f'{gl}{"".join(self.defs)}</defs>'
            f'<g clip-path="url(#frame)"><rect width="{self.w}" height="{self.h}" fill="{self.bg}"/>'
            f'{"".join(self.body)}</g></svg>\n'
        )


def rect(x, y, w, h, fill, cls=None, extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<rect{c} x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"{extra}/>'


def person(doc, key, scale, legs=None):
    """Sprite complet (corps + jambes facultatives). Renvoie (svg, largeur, hauteur)."""
    s = SPR[key]
    cols = {"#": s["color"], "o": INK, "a": s["accent"]}
    rows = list(s["body"])
    if legs:
        rows += s.get("legs" + legs, SPR["_legs" + legs])
    return doc.sprite(rows, cols, scale), len(rows[0]) * scale, len(rows) * scale


def walker(doc, key, scale, cls):
    """Personnage qui marche : deux poses de jambes alternées."""
    s = SPR[key]
    cols = {"#": s["color"], "o": INK, "a": s["accent"]}
    body = doc.sprite(s["body"], cols, scale)
    la = doc.sprite(s.get("legsA", SPR["_legsA"]), cols, scale, y=len(s["body"]) * scale, cls="la")
    lb = doc.sprite(s.get("legsB", SPR["_legsB"]), cols, scale, y=len(s["body"]) * scale, cls="lb")
    return f'<g class="{cls}"><g class="bob">{body}</g>{la}{lb}</g>'


WALK_CSS = (
    ".la{animation:la .44s steps(1) infinite}.lb{opacity:0;animation:lb .44s steps(1) infinite}"
    ".bob{animation:bob .44s steps(1) infinite}"
    "@keyframes la{0%,49.9%{opacity:1}50%,100%{opacity:0}}"
    "@keyframes lb{0%,49.9%{opacity:0}50%,100%{opacity:1}}"
    "@keyframes bob{0%,49.9%{transform:translateY(0)}50%,100%{transform:translateY(-3px)}}"
)


# ---------------------------------------------------------------- hero
def hero():
    W, H, T = 1200, 440, 22
    d = Doc(W, H, "The IT Crowd, l'encyclopédie des fans",
            "Un écran de micro-ordinateur démarre, affiche le titre The IT Crowd, plante en "
            "kernel panic, s'éteint puis se rallume. En boucle.")
    sx, sy, sw, sh = 48, 40, 1104, 360
    cx, cy = sx + sw / 2, sy + sh / 2

    # bordure de chargement façon cassette
    d.defs.append(f'<clipPath id="ring"><path clip-rule="evenodd" d="M0 0H{W}V{H}H0zM{sx} {sy}v{sh}h{sw}v-{sh}z"/></clipPath>')
    pilot = "".join(rect(0, -80 + i * 20, W, 20, RED if i % 2 else CYAN) for i in range(30))
    rnd = random.Random(7)
    y, data, i = -120, "", 0
    while y < H + 120:
        hh = rnd.choice([4, 4, 8, 8, 12, 16])
        data += rect(0, y, W, hh, YEL if i % 2 else BLUE)
        y += hh
        i += 1
    d.add(f'<g clip-path="url(#ring)"><rect width="{W}" height="{H}" fill="{INK2}"/>'
          f'<g class="pilot"><g class="roll">{pilot}</g></g>'
          f'<g class="data"><g class="jit">{data}</g></g>'
          f'<rect class="alarm" width="{W}" height="{H}" fill="{RED}"/></g>')
    d.add(rect(sx, sy, sw, sh, DEEP))

    # --- boot
    boot = [
        ("REYNHOLM INDUSTRIES BASEMENT BIOS V0.118", PAPER),
        ("", PAPER),
        ("MEMORY CHECK ............ MEMORY IS RAM", CYAN),
        ("POWER CABLE ............. DEFINITELY PLUGGED IN", CYAN),
        ("THE INTERNET ............ 1 BOX, BLINKING", CYAN),
        ("RED DOOR ................ DO NOT OPEN", RED),
        ("FIRE EXTINGUISHER ....... ON FIRE", YEL),
        (f"LOADING {ST['fiches']} FICHES, {ST['eps']} EPISODES .......... OK", GRN),
    ]
    g = ""
    t0 = 2.5
    for i, (line, col) in enumerate(boot):
        if not line:
            continue
        a = t0 + i * 2.5
        d.window(f"b{i}", [(a, 24)])
        g += d.text(84, 72 + i * 36, line, 3, col, cls=f"bl b{i}")
        d.css.append(f".b{i}{{animation-name:b{i}}}")
    d.css.append(f".bl{{opacity:0;animation:b0 {T}s linear infinite}}")

    # --- titre
    title = "THE IT CROWD"
    ts = 12
    tx = (W - d.tw(title, ts)) / 2
    uses = "".join(f'<use href="#{d.gid(c)}" x="{i * 6}"/>' for i, c in enumerate(title) if c != " ")
    d.defs.append(f'<g id="ttl">{uses}</g>')

    def ttl(dx, dy, fill, cls=""):
        return (f'<use href="#ttl" class="{cls}" fill="{fill}" '
                f'transform="translate({tx + dx:g} {96 + dy:g}) scale({ts})"/>')

    prompt = "> HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?"
    pw = d.tw(prompt, 3) + 3
    px = (W - pw - 24) / 2
    tg = (
        f'<g class="gh g1">{ttl(-14, 0, CYAN)}</g><g class="gh g2">{ttl(14, 0, MAG)}</g>'
        + ttl(8, 8, RED) + ttl(0, 0, PAPER)
        + d.text(W / 2, 214, "L'ENCYCLOPÉDIE DES FANS, RANGÉE AU SOUS-SOL", 3, CYAN, anchor="middle")
        + d.text(W / 2, 256, f"{ST['fiches']} FICHES / {ST['eps']} ÉPISODES / {ST['vus']} VISIONNÉS / PROJET NON OFFICIEL", 2, GREY, anchor="middle")
        + d.text(px, 320, prompt, 3, YEL)
        + rect(px - 4, 312, pw + 30, 40, DEEP, cls="cover")
        + f'<g class="curs">{rect(0, 320, 15, 21, YEL, cls="blink")}</g>'
    )
    n = len(prompt)
    d.css.append(
        f".cover{{transform:translateX({pw + 30}px);animation:cover {T}s steps({n}) infinite}}"
        f".curs{{transform:translateX({px + pw + 6:g}px);animation:curs {T}s steps({n}) infinite}}"
        f".blink{{animation:blink .9s steps(1) infinite}}"
        "@keyframes blink{0%,54%{opacity:1}55%,100%{opacity:0}}"
    )
    d.kf("cover", [("0%,30%", "transform:translateX(0)"), ("46%,100%", f"transform:translateX({pw + 6:g}px)")])
    d.kf("curs", [("0%,30%", f"transform:translateX({px:g}px)"), ("46%,100%", f"transform:translateX({px + pw + 6:g}px)")])
    d.window("ttlw", [(25, 64)])
    d.css.append(f".title{{animation:ttlw {T}s linear infinite,shake {T}s steps(1) infinite}}")
    d.kf("shake", [("0%,59.9%", "transform:translate(0,0)"), ("60%", "transform:translate(-9px,3px)"),
                   ("60.8%", "transform:translate(12px,-2px)"), ("61.6%", "transform:translate(-4px,6px)"),
                   ("62.4%", "transform:translate(16px,0)"), ("63.2%", "transform:translate(-20px,-5px)"),
                   ("64%,100%", "transform:translate(0,0)")])
    d.window("ghw", [(60, 64)])
    d.css.append(f".gh{{opacity:0;animation:ghw {T}s linear infinite}}")

    # --- kernel panic (texte original)
    panic = [
        "KERNEL PANIC - NOT SYNCING: TOSSED AWAY LIKE YESTERDAY'S JAM",
        "CPU 0: STRESS MACHINE READING OFF THE SCALE (MADE IN BRITAIN)",
        "CALL TRACE:",
        " [<0118999>] NEW_EMERGENCY_NUMBER+0X881/0X999",
        " [<0119725>] ...+0X3",
        " [<C0FFEE00>] TEA_BREAK+0X04/0X20",
        " [<00000404>] FLOOR_NOT_FOUND+0X1/0X1",
        " [<DEADF1RE>] DEAR_SIR_MADAM+0XF1/0XF1",
    ]
    pg = ""
    for i, line in enumerate(panic):
        a = 64 + i * 0.9
        d.window(f"p{i}", [(a, 90)])
        d.css.append(f".p{i}{{animation-name:p{i}}}")
        pg += d.text(84, 62 + i * 27, line, 2.5, PAPER, cls=f"pl p{i}")
    d.css.append(f".pl{{opacity:0;animation:p0 {T}s linear infinite}}")
    box = (rect(84, 292, W - 168, 78, RED)
           + d.text(W / 2, 306, "END TRACE. HAVE YOU TRIED", 3, PAPER, anchor="middle")
           + d.text(W / 2, 336, "TURNING IT OFF AND ON AGAIN?", 3, PAPER, anchor="middle"))
    d.window("pbox", [(73, 76), (77.5, 80.5), (82, 90)])
    d.css.append(f".pbox{{opacity:0;animation:pbox {T}s linear infinite}}")
    pg += f'<g class="pbox">{box}</g>'
    d.kf("stut", [("0%,64%", "transform:translateY(0)"), ("66%", "transform:translateY(-27px)"),
                  ("67%", "transform:translateY(0)"), ("70%", "transform:translateY(-54px)"),
                  ("71%,100%", "transform:translateY(0)")])
    d.css.append(f".panic{{animation:stut {T}s steps(1) infinite}}")

    scan = "".join(rect(sx, sy + i * 4 + 2, sw, 1, "#000", extra=' opacity=".28"') for i in range(sh // 4))

    d.defs.append(f'<clipPath id="scrc"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}"/></clipPath>')
    d.add(f'<g clip-path="url(#scrc)"><g class="scr"><g class="boot">{g}</g><g class="title">{tg}</g>'
          f'<g class="panic">{pg}</g></g></g>{scan}')
    # mise sous tension / extinction
    d.css.append(f".scr{{transform-origin:{cx}px {cy}px;animation:pwr {T}s linear infinite}}")
    d.kf("pwr", [("0%", "transform:scale(1,.004);opacity:1"), ("1.4%", "transform:scale(1,1);opacity:1"),
                 ("90%", "transform:scale(1,1);opacity:1"), ("91.6%", "transform:scale(1,.004);opacity:1"),
                 ("93%", "transform:scale(.002,.004);opacity:1"), ("93.1%,99.4%", "transform:scale(.002,.004);opacity:0"),
                 ("99.5%,100%", "transform:scale(1,.004);opacity:1")])
    d.window("pilotw", [(1.4, 20)])
    d.window("dataw", [(20, 25)])
    d.window("alarmw", [(64, 90)], on="opacity:.9")
    d.css.append(
        f".pilot{{opacity:0;animation:pilotw {T}s linear infinite}}"
        f".data{{opacity:0;animation:dataw {T}s linear infinite}}"
        f".alarm{{opacity:0;animation:alarmw {T}s linear infinite}}"
        ".roll{animation:roll .36s steps(4) infinite}.jit{animation:jit .5s steps(5) infinite}"
        "@keyframes roll{to{transform:translateY(40px)}}@keyframes jit{to{transform:translateY(80px)}}"
    )
    # diode d'alimentation + étiquette du boîtier
    d.add(rect(40, H - 34, 190, 28, INK2) + rect(W - 92, H - 34, 70, 28, INK2))
    d.add(rect(W - 78, H - 26, 12, 12, GRN, cls="led"))
    d.add(d.text(W - 58, H - 27, "ON", 2, GREY))
    d.add(d.text(52, H - 27, "REYNHOLM 48K", 2, GREY))
    d.window("ledw", [(0, 93)], on=f"fill:{GRN}", off=f"fill:{RED}")
    d.css.append(f".led{{animation:ledw {T}s linear infinite}}")
    return d.render()


# ---------------------------------------------------------------- numéro d'urgence
def emergency():
    W, H = 1200, 120
    d = Doc(W, H, "Le nouveau numéro des urgences",
            "Un panneau à diodes fait défiler un numéro d'urgence interminable : "
            "0118 999 881 999 119 725... 3.")
    msg = ("NEW EMERGENCY NUMBER: 0118 999 881 999 119 725 . . . . . . . . 3"
           "      WELL, THAT'S EASY TO REMEMBER.      ")
    s = 6
    period = len(msg) * 6 * s
    row = d.text(0, 39, msg, s, RED) + d.text(period, 39, msg, s, RED)
    d.add(rect(0, 0, W, H, DEEP))
    d.add(f'<g class="tick">{row}</g>')
    # trame de diodes
    d.defs.append(f'<pattern id="led" width="{s}" height="{s}" patternUnits="userSpaceOnUse">'
                  f'<path d="M0 0h{s}v1h-{s}zM0 0h1v{s}h-1z" fill="{DEEP}"/></pattern>')
    d.add(f'<rect width="{W}" height="{H}" fill="url(#led)"/>')
    dur = period / 190
    d.css.append(f".tick{{animation:tick {dur:.1f}s steps({period // s}) infinite}}"
                 f"@keyframes tick{{to{{transform:translateX(-{period}px)}}}}")
    # cartouche fixe
    d.add(rect(0, 0, 252, H, INK) + rect(252, 0, 6, H, RED))
    d.add(rect(24, 30, 24, 24, RED, cls="gyro") + rect(24, 66, 24, 24, BLUE, cls="gyro2"))
    d.add(d.text(66, 30, "URGENCES", 3, PAPER))
    d.add(d.text(66, 66, "NOUVEAU NUMÉRO", 2, YEL))
    d.add(d.text(66, 86, "FACILE À RETENIR", 1.5, GREY))
    d.css.append(".gyro{animation:gy .7s steps(1) infinite}.gyro2{animation:gy .7s steps(1) -.35s infinite}"
                 "@keyframes gy{0%,49%{opacity:1}50%,100%{opacity:.18}}")
    return d.render()


# ---------------------------------------------------------------- The Internet
def internet():
    W, H = 800, 340
    d = Doc(W, H, "The Internet",
            "Une petite boîte noire posée sur un socle de musée. Sa diode rouge clignote. "
            "C'est l'Internet tout entier.")
    # faisceau
    d.add(f'<path d="M150 0L20 {H}H480L270 0z" fill="{PAPER}" opacity=".05"/>')
    d.add(f'<path d="M180 0L90 {H}H410L250 0z" fill="{PAPER}" opacity=".05"/>')
    # socle
    d.add(rect(130, 236, 220, 14, PAPER) + rect(146, 250, 188, 90, "#b9b39c") + rect(146, 250, 188, 6, "#8f8a76"))
    # la boîte
    bx, by = 174, 158
    box = (f'<path d="M{bx} {by}l14 -14h132l-14 14z" fill="#2a2c40"/>'
           + rect(bx, by, 132, 78, "#05050c")
           + f'<path d="M{bx + 132} {by}l14 -14v78l-14 14z" fill="#14152a"/>'
           + rect(bx + 4, by + 4, 124, 2, "#1d1f38")
           + rect(bx + 104, by + 16, 12, 12, "#4a0a0d")
           + f'<circle class="halo" cx="{bx + 110}" cy="{by + 22}" r="26" fill="{RED}" opacity=".22"/>'
           + rect(bx + 104, by + 16, 12, 12, RED, cls="diode")
           + rect(bx + 106, by + 18, 4, 4, "#ff9a9e", cls="diode"))
    d.add(f'<g class="nudge">{box}</g>')
    # poteaux et cordon
    for x in (64, 404):
        d.add(rect(x, 196, 10, 132, YEL) + rect(x - 8, 328, 26, 8, YEL) + rect(x - 3, 186, 16, 12, YEL))
    d.add(f'<path d="M72 204Q104 262 136 244" fill="none" stroke="{RED}" stroke-width="6"/>'
          f'<path d="M344 244Q378 262 409 204" fill="none" stroke="{RED}" stroke-width="6"/>')
    # cartel
    x = 452
    d.add(d.text(x, 56, "THE", 4, GREY))
    d.add(d.text(x, 92, "INTERNET", 6.5, PAPER))
    d.add(rect(x, 150, 290, 4, RED))
    lines = [("PRÊTÉ PAR LES ANCIENS DE L'INTERNET.", CYAN, ""),
             ("D'ORDINAIRE AU SOMMET DE BIG BEN.", CYAN, ""),
             ("POIDS : AUCUN. C'EST DU SANS-FIL.", CYAN, ""),
             ("NE PAS FAIRE TOMBER.", YEL, ""),
             ("VRAIMENT.", YEL, "really")]
    for i, (t, c, cls) in enumerate(lines):
        d.add(d.text(x, 172 + i * 26, t, 1.5, c, cls=cls or None))
    d.add(d.text(x, 312, "PIÈCE N° 1 SUR 1", 1.5, GREY))
    d.css.append(
        ".diode{animation:dio 5.2s steps(1) infinite}.halo{animation:halo 5.2s steps(1) infinite}"
        "@keyframes dio{0%,18%{opacity:1}19%,24%{opacity:0}25%,43%{opacity:1}44%,49%{opacity:0}"
        "50%,68%{opacity:1}69%,74%{opacity:0}75%,80%{opacity:1}81%,84%{opacity:0}85%,88%{opacity:1}"
        "89%,92%{opacity:0}93%,100%{opacity:1}}"
        "@keyframes halo{0%,18%{opacity:.22}19%,24%{opacity:0}25%,43%{opacity:.22}44%,49%{opacity:0}"
        "50%,68%{opacity:.22}69%,74%{opacity:0}75%,80%{opacity:.22}81%,84%{opacity:0}85%,88%{opacity:.22}"
        "89%,92%{opacity:0}93%,100%{opacity:.22}}"
        ".nudge{animation:nudge 10.4s steps(1) infinite}"
        "@keyframes nudge{0%,86%{transform:translate(0,0)}87%{transform:translate(4px,0)}"
        "88.5%{transform:translate(-3px,0)}90%{transform:translate(2px,0)}91.5%,100%{transform:translate(0,0)}}"
        ".really{animation:really 10.4s steps(1) infinite}"
        "@keyframes really{0%,86%{opacity:1}87%,89%{opacity:0}90%,92%{opacity:1}93%,95%{opacity:0}96%,100%{opacity:1}}"
    )
    return d.render()


# ---------------------------------------------------------------- le feu
def flames(d, x0, base_y, cols, cell, seed, hmax, frames=4, cls="fl"):
    rnd = random.Random(seed)
    prof = []
    for i in range(cols):
        t = i / (cols - 1)
        prof.append(0.25 + 0.75 * (1 - abs(2 * t - 1) ** 1.6))
    out = ""
    for f in range(frames):
        hs = [max(1, round(hmax * p * rnd.uniform(0.55, 1.0))) for p in prof]
        rows = [["." for _ in range(cols)] for _ in range(hmax)]
        for x, hgt in enumerate(hs):
            for k in range(hgt):
                r = k / max(1, hgt)
                ch = "y" if r < 0.34 else ("o" if r < 0.7 else "r")
                rows[hmax - 1 - k][x] = ch
        # étincelles
        for _ in range(cols // 5):
            x = rnd.randrange(cols)
            y = hmax - 1 - hs[x] - rnd.randrange(1, 4)
            if y >= 0:
                rows[y][x] = "o"
        rs = ["".join(r) for r in rows]
        out += d.sprite(rs, {"y": YEL, "o": ORG, "r": RED}, cell, x0, base_y - hmax * cell, cls=f"{cls} {cls}{f}")
    return out


def fire():
    W, H = 800, 340
    d = Doc(W, H, "Un feu, traité avec flegme",
            "Un incendie de bureau en pixel art. Un personnage à lunettes reste calme et rédige "
            "un courriel aux pompiers. L'extincteur brûle avec le reste du feu.")
    floor = 286
    d.add(rect(0, floor, W, H - floor, INK2) + rect(0, floor, W, 4, GREY))
    # affiche de sécurité au mur
    d.add(rect(60, 40, 150, 84, PAPER) + d.text(135, 52, "EN CAS", 2, INK, anchor="middle")
          + d.text(135, 72, "D'INCENDIE :", 2, INK, anchor="middle")
          + d.text(135, 96, "ÉCRIRE.", 2.5, RED, anchor="middle"))
    # bureau + écran
    d.add(rect(250, 214, 250, 12, PAPER) + rect(262, 226, 12, 60, "#b9b39c") + rect(476, 226, 12, 60, "#b9b39c"))
    d.add(rect(300, 110, 180, 96, PAPER) + rect(310, 120, 160, 70, DEEP) + rect(372, 206, 36, 8, "#b9b39c"))
    d.defs.append('<clipPath id="mon"><rect x="310" y="120" width="160" height="70"/></clipPath>')
    d.add('<g clip-path="url(#mon)">' + d.text(318, 128, "TO: FIRE BRIGADE", 1.5, GREY)
          + d.text(318, 146, "DEAR SIR/MADAM,", 1.5, GRN) + d.text(318, 164, "FIRE!", 1.5, GRN, cls="l2")
          + rect(316, 144, 160, 16, DEEP, cls="cov") + rect(368, 162, 10, 12, GRN, cls="blink") + '</g>')
    # le génie, de dos au feu
    p, pw, ph = person(d, "genius", 6, legs="B")
    d.add(f'<g transform="translate(196 {floor - ph})"><g class="calm">{p}</g></g>')
    # le feu
    d.add(flames(d, 500, floor, 34, 8, 11, 22))
    # extincteur, rangé avec le reste du feu
    ex, ey = 610, floor - 78
    d.add(rect(ex, ey + 14, 34, 64, RED) + rect(ex + 8, ey, 18, 14, "#8f8a76") + rect(ex + 26, ey + 4, 16, 6, INK)
          + rect(ex + 6, ey + 30, 22, 14, PAPER) + d.text(ex + 17, ey + 33, "GB", 1, RED, anchor="middle"))
    d.add(flames(d, ex - 6, ey + 6, 8, 6, 23, 9, cls="fx"))
    # fumée
    for i, (sx, dl) in enumerate([(540, 0), (640, -1.3), (720, -2.2), (590, -3.1)]):
        d.add(f'<g class="smk" style="animation-delay:{dl}s">{rect(sx, 110, 16, 16, GREY)}{rect(sx + 12, 98, 10, 10, GREY)}</g>')
    d.add(d.text(W / 2, 306, "SITUATION : UN FEU.  ACTION : UN COURRIEL.  STATUT : ENVOYÉ.", 2, PAPER, anchor="middle"))
    css = ""
    for cls, n, dur in (("fl", 4, 0.56), ("fx", 4, 0.48)):
        step = 100 / n
        css += f".{cls}{{opacity:0;animation:{cls}k {dur}s steps(1) infinite}}.{cls}0{{opacity:1}}"
        css += f"@keyframes {cls}k{{0%,{step - .1:g}%{{opacity:1}}{step:g}%,100%{{opacity:0}}}}"
        for f in range(n):
            css += f".{cls}{f}{{animation-delay:{f * dur / n:.3f}s}}"
    css += (
        ".cov{transform:translateX(140px);animation:cov 8s steps(15) infinite}"
        "@keyframes cov{0%,8%{transform:translateX(0)}50%,100%{transform:translateX(140px)}}"
        ".l2{animation:l2 8s steps(1) infinite}@keyframes l2{0%,59%{opacity:0}60%,100%{opacity:1}}"
        ".blink{animation:blink .9s steps(1) infinite}@keyframes blink{0%,54%{opacity:1}55%,100%{opacity:0}}"
        ".calm{animation:calm 2.4s steps(1) infinite}@keyframes calm{0%,49%{transform:translateY(0)}50%,100%{transform:translateY(3px)}}"
        ".smk{opacity:.5;animation:smk 4.2s linear infinite}"
        "@keyframes smk{0%{transform:translateY(60px);opacity:0}25%{opacity:.5}100%{transform:translateY(-130px);opacity:0}}"
    )
    d.css.append(css)
    return d.render()


# ---------------------------------------------------------------- l'équipe
def crew():
    W, H, T = 1200, 330, 24
    d = Doc(W, H, "L'équipe du sous-sol",
            "Cinq personnages pixel originaux dans un couloir de sous-sol : un technicien blasé, "
            "un génie à lunettes et une cheffe enjambent un trou, le patron mégalo y tombe, "
            "un gothique observe derrière une porte rouge.")
    floor = 250
    S = 6
    # mur du fond
    d.add(rect(0, 0, W, floor, "#12143a"))
    d.add(rect(0, 26, W, 8, INK2) + rect(0, 44, W, 4, INK2))
    for x in (120, 520, 920):
        d.add(rect(x, 22, 14, 30, INK2))
    d.add(rect(300, 12, 150, 6, PAPER, cls="neon") + rect(760, 12, 150, 6, PAPER, cls="neon n2"))
    # affiches
    d.add(rect(70, 78, 96, 70, INK2) + d.text(118, 92, "SOUS-SOL", 1.5, GREY, anchor="middle") + d.text(118, 112, "-1", 4, PAPER, anchor="middle"))
    bug = SPR["bug"]
    d.add(rect(228, 86, 70, 60, PAPER) + d.sprite(bug["body"], {"#": INK, "a": RED}, 5, 240, 96))
    # compteur de direction
    d.add(rect(560, 78, 190, 62, DEEP) + rect(560, 78, 190, 4, GREY) + d.text(574, 92, "DIRECTION", 2, GREY)
          + d.text(574, 114, "EN POSTE :", 2, GREY) + d.text(706, 108, "1", 3, GRN, cls="dir1") + d.text(706, 108, "0", 3, RED, cls="dir0"))
    # panneau du trou
    hx, hw = 700, 84
    d.add(rect(hx + hw / 2 - 3, 170, 6, 56, GREY) + rect(hx + hw / 2 - 46, 150, 92, 26, YEL)
          + d.text(hx + hw / 2, 156, "ÉTAGE 404", 1.5, INK, anchor="middle"))
    # porte rouge + gothique
    dx, dw, dh = 1036, 88, 150
    gs = SPR["goth"]
    goth = d.sprite(gs["body"], {"#": gs["color"], "o": INK, "a": gs["accent"]}, 6, dx + 22, floor - 84 - 10)
    d.add(rect(dx - 8, floor - dh - 8, dw + 16, dh + 8, "#3a3d6e") + rect(dx, floor - dh, dw, dh, "#020208"))
    d.add(f'<g class="peek">{goth}{rect(dx + 40, floor - 76, 6, 6, VIO, cls="gblink")}{rect(dx + 64, floor - 76, 6, 6, VIO, cls="gblink")}</g>')
    d.add(rect(dx + dw, floor - dh, 40, dh, "#12143a"))  # cache : rien ne dépasse du cadre
    d.add(rect(dx + dw, floor - dh - 8, 8, dh + 8, "#3a3d6e"))
    door = (rect(dx, floor - dh, dw, dh, RED) + rect(dx + 8, floor - dh + 10, dw - 16, 48, "#b81a21")
            + rect(dx + 8, floor - dh + 68, dw - 16, 70, "#b81a21") + rect(dx + dw - 16, floor - 68, 8, 8, YEL))
    d.add(f'<g class="door">{door}</g>')
    d.add(d.text(dx + dw / 2, floor - dh - 26, "NE PAS OUVRIR", 1.5, RED, anchor="middle"))
    # sol et trou
    d.add(rect(0, floor, W, H - floor, INK2) + rect(0, floor, W, 4, GREY))
    d.add(rect(hx, floor, hw, 30, "#000"))
    # marcheurs
    span = W + 280
    for i, key in enumerate(("tech", "genius", "boss_lady")):
        g = walker(d, key, S, "w")
        x0 = (150, 380, 930)[i]
        d.add(f'<g class="walk" style="transform:translateX({x0}px);animation-delay:{-i * T / 4:g}s">'
              f'<g transform="translate(0 {floor - 18 * S})">'
              f'<g class="hop" style="animation-delay:{-i * T / 4:g}s">{g}</g></g></g>')
    # point d'interrogation de la cheffe : dans son groupe serait mieux, on le suit par la même animation
    bd = -3 * T / 4
    g = walker(d, "mogul", S, "w")
    bang = d.text(26, -40, "!", 4, YEL, cls="bang", extra=f' style="animation-delay:{bd:g}s"')
    d.add(f'<g class="fall" style="animation-delay:{bd:g}s"><g transform="translate(0 {floor - 18 * S})">{g}{bang}</g></g>')
    # avant-plan : ce qui est sous le plancher cache la chute
    d.add(rect(0, floor + 30, W, H - floor - 30, INK2))
    d.add(rect(hx - 4, floor, 4, 30, GREY) + rect(hx + hw, floor, 4, 30, GREY))
    d.add(d.text(24, H - 30, "5 PERSONNAGES ORIGINAUX. TOUTE RESSEMBLANCE AVEC UN SERVICE INFORMATIQUE EXISTANT EST REGRETTABLE.", 1.5, GREY))

    # x(t) = -140 + span * t ; le trou est à hx + hw/2 - 30 (demi sprite)
    def pct(x):
        return (x + 140) / span * 100
    jump = pct(hx + hw / 2 - 36)
    edge = pct(hx + 6)
    d.css.append(WALK_CSS)
    d.css.append(f".walk{{animation:walk {T}s linear infinite}}"
                 f"@keyframes walk{{from{{transform:translateX(-140px)}}to{{transform:translateX({span - 140}px)}}}}")
    d.kf("hop", [(f"0%,{jump - 4.6:.2f}%", "transform:translateY(0)"),
                 (f"{jump - 2.6:.2f}%", "transform:translateY(-28px)"),
                 (f"{jump:.2f}%", "transform:translateY(-38px)"),
                 (f"{jump + 2.6:.2f}%", "transform:translateY(-28px)"),
                 (f"{jump + 4.6:.2f}%,100%", "transform:translateY(0)")])
    d.css.append(f".hop{{animation:hop {T}s linear infinite}}")
    d.kf("fall", [("0%", "transform:translate(-140px,0)"),
                  (f"{edge:.2f}%", f"transform:translate({hx + 6}px,0)"),
                  (f"{edge + 3:.2f}%", f"transform:translate({hx + 12}px,0)"),
                  (f"{edge + 4.4:.2f}%", f"transform:translate({hx + 12}px,60px)"),
                  (f"{edge + 6.5:.2f}%,100%", f"transform:translate({hx + 12}px,260px)")])
    d.css.append(f".fall{{transform:translate(560px,0);animation:fall {T}s linear infinite}}")
    d.window("bang", [(edge + 0.3, edge + 3.4)])
    d.css.append(f".bang{{opacity:0;animation:bang {T}s linear infinite}}")
    d.window("dir0", [(edge + 5.5, 96)])
    d.window("dir1", [(0, edge + 5.5), (96, 100)])
    d.css.append(f".dir0{{opacity:0;animation:dir0 {T}s linear {bd:g}s infinite}}"
                 f".dir1{{animation:dir1 {T}s linear {bd:g}s infinite}}")
    # porte : charnière à gauche
    d.css.append(f".door{{transform-origin:{dx}px {floor}px;transform:scaleX(.42);animation:door 9s ease-in-out infinite}}")
    d.kf("door", [("0%,38%", "transform:scaleX(1)"), ("46%,80%", "transform:scaleX(.42)"),
                  ("86%,100%", "transform:scaleX(1)")])
    d.css.append(".gblink{opacity:0;animation:gb 3.1s steps(1) infinite}@keyframes gb{0%,92%{opacity:0}93%,100%{opacity:1}}"
                 ".neon{animation:neon 6s steps(1) infinite}.n2{animation-delay:-2.2s}"
                 "@keyframes neon{0%,70%{opacity:1}71%{opacity:.2}72%{opacity:1}74%{opacity:.3}76%,100%{opacity:1}}")
    return d.render()


# ---------------------------------------------------------------- séparateurs
def divider_tape():
    W, H = 1200, 36
    d = Doc(W, H, "Séparateur : chargement", "Bandes de chargement de cassette, rouges et cyan.", radius=8)
    rnd = random.Random(3)
    bars, x, i = "", 0, 0
    period = 480
    seq = []
    while x < period:
        w = rnd.choice([6, 6, 12, 12, 18, 24, 30])
        w = min(w, period - x)
        seq.append((x, w, i % 2))
        x += w
        i += 1
    if len(seq) % 2:
        seq[-1] = (seq[-1][0], seq[-1][1], 1)
    for k in range(4):
        for (x, w, c) in seq:
            bars += rect(x + k * period, 0, w, H, CYAN if c else RED)
    d.add(f'<g class="tp">{bars}</g>')
    label = "CHARGEMENT DE LA SECTION SUIVANTE"
    lw = d.tw(label, 2) + 40
    d.add(rect((W - lw) / 2, 0, lw, H, INK) + d.text(W / 2, 11, label, 2, PAPER, anchor="middle"))
    d.css.append(f".tp{{animation:tp 2.4s steps(20) infinite}}@keyframes tp{{to{{transform:translateX(-{period}px)}}}}")
    return d.render()


def divider_cable():
    W, H = 1200, 44
    d = Doc(W, H, "Séparateur : est-ce bien branché ?",
            "Un câble s'approche d'une prise, s'y branche un instant, puis se débranche.", radius=8)
    y = 20
    cable = rect(-60, y, 1010, 4, GREY) + rect(950, y - 6, 34, 16, PAPER) + rect(984, y - 2, 14, 3, YEL) + rect(984, y + 3, 14, 3, YEL)
    d.add(f'<g class="plug">{cable}</g>')
    d.add(rect(1040, 4, 44, 36, INK2) + rect(1046, y - 4, 16, 4, DEEP) + rect(1046, y + 2, 16, 4, DEEP))
    d.add(rect(1098, 15, 12, 12, RED, cls="off") + rect(1098, 15, 12, 12, GRN, cls="on"))
    d.add(d.text(1124, 15, "220 V", 2, GREY))
    d.add(rect(60, 6, 420, 32, INK) + d.text(76, 15, "IS IT DEFINITELY PLUGGED IN?", 2, PAPER))
    d.css.append(
        ".plug{animation:plug 7s steps(1) infinite}"
        "@keyframes plug{0%,20%{transform:translateX(0)}22%{transform:translateX(18px)}24%{transform:translateX(34px)}"
        "26%{transform:translateX(24px)}30%{transform:translateX(34px)}34%{transform:translateX(52px)}"
        "36%,62%{transform:translateX(62px)}64%{transform:translateX(40px)}66%{transform:translateX(12px)}68%,100%{transform:translateX(0)}}"
        ".on{opacity:0;animation:on 7s steps(1) infinite}@keyframes on{0%,35.9%{opacity:0}36%,62%{opacity:1}62.1%,100%{opacity:0}}"
    )
    return d.render()


# ---------------------------------------------------------------- compteur
def counter():
    W, H, T = 640, 230, 9
    d = Doc(W, H, "Jours sans incident : 0",
            "Un panneau de sécurité. Le compteur de jours sans incident passe péniblement à 1, "
            "puis retombe à 0.")
    d.add(rect(20, 20, W - 40, H - 40, PAPER) + rect(20, 20, W - 40, 10, YEL))
    for i in range(0, 20):
        d.add(f'<path d="M{20 + i * 30} 20h15l-10 10h-15z" fill="{INK}"/>')
    for x in (34, W - 46):
        d.add(rect(x, 40, 12, 12, "#8f8a76"))
    d.add(d.text(48, 62, "JOURS SANS", 4, INK))
    d.add(d.text(48, 98, "INCIDENT", 4, INK))
    d.add(d.text(48, 148, "RECORD À BATTRE : 0", 2, INK))
    d.add(d.text(48, 172, "DERNIER INCIDENT :", 2, INK))
    d.add(d.text(270, 172, "À L'INSTANT", 2, RED, cls="now"))
    # afficheur à volets
    bx, by, bw, bh = 446, 54, 150, 136
    d.add(rect(bx, by, bw, bh, DEEP) + rect(bx - 6, by + bh / 2 - 6, 6, 12, "#8f8a76") + rect(bx + bw, by + bh / 2 - 6, 6, 12, "#8f8a76"))
    d.add(f'<g class="flap">{d.text(bx + bw / 2, by + 19, "0", 14, YEL, cls="d0", anchor="middle")}'
          f'{d.text(bx + bw / 2, by + 19, "1", 14, GRN, cls="d1", anchor="middle")}</g>')
    d.add(rect(bx, by + bh / 2 - 1, bw, 3, INK))
    d.add(rect(bx, by, bw, bh, RED, cls="flash"))
    d.add(flames(d, bx + 19, by + bh, 14, 8, 5, 9, cls="cf"))
    cy = by + bh / 2
    d.css.append(
        f".flap{{transform-origin:0 {cy}px;animation:flap {T}s linear infinite}}"
        "@keyframes flap{0%,52%{transform:scaleY(1)}55%{transform:scaleY(.02)}58%,76%{transform:scaleY(1)}"
        "77.5%{transform:scaleY(.02)}79%,100%{transform:scaleY(1)}}"
        f".d1{{opacity:0;animation:d1 {T}s steps(1) infinite}}.d0{{animation:d0 {T}s steps(1) infinite}}"
        "@keyframes d1{0%,54.9%{opacity:0}55%,77.4%{opacity:1}77.5%,100%{opacity:0}}"
        "@keyframes d0{0%,54.9%{opacity:1}55%,77.4%{opacity:0}77.5%,100%{opacity:1}}"
        f".flash{{opacity:0;animation:fla {T}s steps(1) infinite}}"
        "@keyframes fla{0%,75.9%{opacity:0}76%{opacity:.8}77%{opacity:0}78%{opacity:.6}79%,100%{opacity:0}}"
        f".now{{animation:now {T}s steps(1) infinite}}"
        "@keyframes now{0%,54.9%{opacity:1}55%,75.9%{opacity:0}76%,100%{opacity:1}}"
        f".cf{{opacity:0;animation:cfa {T}s steps(1) infinite}}.cf1,.cf3{{animation-name:cfb}}"
        "@keyframes cfa{0%,69.9%{opacity:0}70%,71.4%{opacity:1}71.5%,72.9%{opacity:0}73%,74.4%{opacity:1}74.5%,100%{opacity:0}}"
        "@keyframes cfb{0%,71.4%{opacity:0}71.5%,72.9%{opacity:1}73%,74.4%{opacity:0}74.5%,76%{opacity:1}76.1%,100%{opacity:0}}"
        ".cf2,.cf3{display:none}"
    )
    return d.render()


# ---------------------------------------------------------------- barre de chargement
def loading():
    W, H, T = 800, 150, 18
    d = Doc(W, H, "Mise à jour en cours",
            "Une barre de chargement qui avance, recule, et dont l'estimation de temps restant "
            "passe de trois minutes à deux ans.")
    d.add(rect(0, 0, W, 34, BLUE) + d.text(18, 10, "REYNHOLM UPDATE", 2, PAPER) + rect(W - 40, 9, 16, 16, RED) + d.text(W - 36, 11, "X", 2, PAPER))
    msgs = [("MISE À JOUR 1 SUR 4 096", 0, 20),
            ("TEMPS RESTANT : 3 MINUTES", 20, 40),
            ("TEMPS RESTANT : 2 ANS", 40, 58),
            ("TEMPS RESTANT : JEUDI, 15 H", 58, 76),
            ("PRESQUE. NE PAS ÉTEINDRE. NI RALLUMER.", 76, 100)]
    for i, (m, a, b) in enumerate(msgs):
        d.window(f"m{i}", [(a, b)])
        last = i == len(msgs) - 1
        d.add(d.text(40, 54, m, 2.5, PAPER, cls=f"m m{i}", extra='' if not last else ' style="opacity:1"'))
        d.css.append(f".m{i}{{animation:m{i} {T}s steps(1) infinite}}")
    d.css.append(".m{opacity:0}")
    bx, by, bw, bh = 40, 88, W - 80, 34
    d.add(rect(bx - 4, by - 4, bw + 8, bh + 8, PAPER) + rect(bx, by, bw, bh, DEEP))
    blocks = "".join(rect(bx + 4 + i * 20, by + 4, 16, bh - 8, GRN) for i in range(36))
    d.add(f'<g class="bar">{blocks}</g>')
    d.defs.append(f'<clipPath id="barc"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}"/></clipPath>')
    d.add(f'<g clip-path="url(#barc)">{rect(bx, by, bw, bh, DEEP, cls="mask")}</g>')
    d.css.append(f".mask{{transform:translateX({bw - 20}px);animation:mask {T}s steps(36) infinite}}")
    f = lambda p: f"transform:translateX({bw * p:g}px)"
    d.kf("mask", [("0%", f(.03)), ("20%", f(.55)), ("38%", f(.92)), ("42%", f(.25)), ("58%", f(.8)),
                  ("62%", f(.5)), ("76%", f(.97)), ("96%", f(.972)), ("100%", f(.03))])
    return d.render()


# ---------------------------------------------------------------- répondeur
def answerphone():
    W, H, T = 800, 280, 12
    d = Doc(W, H, "Le répondeur du service informatique",
            "Un magnétophone à bandes répond au téléphone à la place du technicien, qui boit son thé.")
    floor = 236
    d.add(rect(0, floor, W, H - floor, INK2) + rect(0, floor, W, 4, GREY))
    # bureau
    d.add(rect(40, floor - 54, 470, 12, PAPER) + rect(56, floor - 42, 12, 42, "#b9b39c") + rect(482, floor - 42, 12, 42, "#b9b39c"))
    # téléphone
    ty = floor - 54
    phone = (rect(70, ty - 22, 78, 22, PAPER) + rect(62, ty - 36, 94, 12, RED) + rect(62, ty - 30, 16, 14, RED) + rect(140, ty - 30, 16, 14, RED)
             + rect(100, ty - 16, 18, 10, INK))
    d.add(f'<g class="ring">{phone}</g>')
    for k, (x, yy) in enumerate([(44, ty - 56), (166, ty - 56), (104, ty - 70)]):
        d.add(rect(x, yy, 8, 8, YEL, cls="rr"))
    # magnétophone
    mx, my, mw, mh = 196, ty - 126, 250, 126
    d.add(rect(mx, my, mw, mh, "#b9b39c") + rect(mx, my, mw, 8, PAPER) + rect(mx + 14, my + 92, mw - 28, 22, INK))
    for i in range(5):
        d.add(rect(mx + 24 + i * 22, my + 97, 14, 12, RED if i == 1 else PAPER))
    d.add(rect(mx + mw - 60, my + 97, 40, 12, DEEP) + rect(mx + mw - 58, my + 99, 12, 8, GRN, cls="vu") + rect(mx + mw - 44, my + 99, 10, 8, YEL, cls="vu v2"))
    for cx in (mx + 66, mx + mw - 66):
        cyy = my + 48
        reel = (f'<circle cx="{cx}" cy="{cyy}" r="36" fill="{INK}"/><circle cx="{cx}" cy="{cyy}" r="30" fill="#6b4a2a"/>'
                f'<circle cx="{cx}" cy="{cyy}" r="16" fill="{PAPER}"/>'
                + "".join(f'<rect x="{cx - 4}" y="{cyy - 28}" width="8" height="12" fill="{INK}" transform="rotate({a} {cx} {cyy})"/>' for a in (0, 120, 240))
                + f'<circle cx="{cx}" cy="{cyy}" r="5" fill="{INK}"/>')
        d.add(f'<g class="reel" style="transform-origin:{cx}px {cyy}px">{reel}</g>')
    d.add(rect(mx + 66, my + 82, mw - 132, 3, "#6b4a2a"))
    # bulle
    bx, by, bw, bh = 470, 16, 306, 100
    d.add(rect(bx, by, bw, bh, PAPER) + f'<path d="M{bx} {by + 70}l-28 22l28 -6z" fill="{PAPER}"/>')
    says = [(["HELLO, IT."], 8, 28), (["HAVE YOU TRIED", "TURNING IT OFF", "AND ON AGAIN?"], 28, 62),
            (["IS IT DEFINITELY", "PLUGGED IN?"], 62, 96)]
    for i, (lines, a, b) in enumerate(says):
        d.window(f"s{i}", [(a, b)])
        g = ""
        y0 = by + (bh - len(lines) * 26 + 5) / 2
        for k, ln in enumerate(lines):
            g += d.text(bx + bw / 2, y0 + k * 26, ln, 3, INK, anchor="middle")
        st = ' style="opacity:1"' if i == 1 else ""
        d.add(f'<g class="say s{i}"{st}>{g}</g>')
        d.css.append(f".s{i}{{animation:s{i} {T}s steps(1) infinite}}")
    d.css.append(".say{opacity:0}")
    # le technicien, tasse en main, ne décroche pas
    p, pw, ph = person(d, "tech", 6, legs="B")
    d.add(f'<g transform="translate(596 {floor - ph})"><g class="sip">{p}</g></g>')
    d.add(d.text(584, floor + 14, "NE DÉCROCHE PAS", 2, GREY))
    d.add(d.text(40, floor + 14, "RÉPONDEUR AUTOMATIQUE, BREVET EN ATTENTE", 2, GREY))
    d.css.append(
        f".reel{{animation:reel 2.4s steps(12) infinite}}@keyframes reel{{to{{transform:rotate(360deg)}}}}"
        f".ring{{animation:ring {T}s steps(1) infinite}}"
        "@keyframes ring{0%{transform:translate(0,0)}1%{transform:translate(-3px,-2px)}2%{transform:translate(3px,0)}"
        "3%{transform:translate(-3px,-2px)}4%{transform:translate(3px,0)}5%{transform:translate(-3px,-2px)}6%,100%{transform:translate(0,0)}}"
        f".rr{{opacity:0;animation:rr {T}s steps(1) infinite}}@keyframes rr{{0%,1%{{opacity:1}}2%{{opacity:0}}3%,4%{{opacity:1}}5%{{opacity:0}}6%{{opacity:1}}7%,100%{{opacity:0}}}}"
        ".vu{animation:vu .5s steps(1) infinite}.v2{animation-delay:-.2s}@keyframes vu{0%,59%{opacity:1}60%,100%{opacity:.15}}"
        ".sip{animation:sip 3s steps(1) infinite}@keyframes sip{0%,69%{transform:translateY(0)}70%,100%{transform:translateY(3px)}}"
    )
    return d.render()


# ---------------------------------------------------------------- tnetennba
def tnetennba():
    W, H, T = 800, 210, 12
    d = Doc(W, H, "Tnetennba",
            "Neuf tuiles de jeu de lettres se retournent une à une et composent un mot qui "
            "n'existe pas : tnetennba.")
    word = "TNETENNBA"
    tw, th, gap = 66, 80, 10
    x0 = (W - (9 * tw + 8 * gap)) / 2
    d.add(rect(x0 - 20, 34, 9 * tw + 8 * gap + 40, th + 32, INK2))
    for i, c in enumerate(word):
        x = x0 + i * (tw + gap)
        a = 6 + i * 4.5
        tile = rect(x, 50, tw, th, BLUE) + rect(x, 50, tw, 5, "#5d68ff") + d.text(x + tw / 2, 69, c, 6, PAPER, anchor="middle")
        d.add(rect(x, 50, tw, th, DEEP))
        d.add(f'<g class="tile t{i}" style="transform-origin:0 90px">{tile}</g>')
        d.kf(f"t{i}", [(f"0%,{a:g}%", "transform:scaleY(0)"), (f"{a + 2:g}%,90%", "transform:scaleY(1)"),
                       ("93%,100%", "transform:scaleY(0)")])
        d.css.append(f".t{i}{{animation:t{i} {T}s linear infinite}}")
    cap = "GOOD MORNING, THAT'S A NICE TNETENNBA."
    d.add(d.text(W / 2, 162, cap, 2.5, YEL, cls="cap", anchor="middle"))
    d.add(d.text(W / 2, 12, "MOT DE NEUF LETTRES. DÉFINITION : AUCUNE.", 1.5, GREY, anchor="middle"))
    d.window("cap", [(50, 90)])
    d.css.append(f".cap{{animation:cap {T}s steps(1) infinite}}")
    # sablier : une barre qui se vide
    d.add(rect(x0 - 20, 190, 9 * tw + 8 * gap + 40, 6, INK2))
    d.add(rect(x0 - 20, 190, 9 * tw + 8 * gap + 40, 6, RED, cls="clk"))
    d.css.append(f".clk{{transform-origin:{x0 - 20}px 0;transform:scaleX(.5);animation:clk {T}s steps(30) infinite}}"
                 "@keyframes clk{0%{transform:scaleX(1)}90%,100%{transform:scaleX(0)}}")
    return d.render()


# ---------------------------------------------------------------- badges
def badge(label, values, T=8):
    """values : [(texte, couleur de fond, couleur du texte)], alternés en boucle."""
    s = 2
    d0 = Doc(10, 10, "", "")
    lw = d0.tw(label, s) + 24
    vw = max(d0.tw(v[0], s) for v in values) + 24
    W, H = lw + vw + 20, 34
    d = Doc(W, H, f"{label} : {values[0][0]}", "Badge animé : " + ", ".join(v[0] for v in values) + ".", radius=6)
    d.add(rect(0, 0, 20, H, INK2) + rect(7, 13, 8, 8, GRN, cls="led"))
    d.add(rect(20, 0, lw, H, INK2) + d.text(20 + 6, 10, label, s, PAPER))
    n = len(values)
    for i, (v, bg, fg) in enumerate(values):
        g = rect(20 + lw, 0, vw, H, bg) + d.text(20 + lw + vw / 2, 10, v, s, fg, anchor="middle")
        if n == 1:
            d.add(g)
        else:
            a, b = i * 100 / n, (i + 1) * 100 / n
            d.window(f"v{i}", [(a, b)])
            st = ' style="opacity:1"' if i == 0 else ""
            d.add(f'<g class="v v{i}"{st}>{g}</g>')
            d.css.append(f".v{i}{{animation:v{i} {T}s steps(1) infinite}}")
    d.css.append(".v{opacity:0}.led{animation:led 1.6s steps(1) infinite}@keyframes led{0%,59%{opacity:1}60%,100%{opacity:.2}}")
    return d.render()


def badges():
    """Les cinq badges. Ceux qui comptent quelque chose le comptent dans kb/."""
    miss = ST["n_eps"] - ST["n_vus"]
    reste = "TOUS, ENFIN" if miss == 0 else "IL EN MANQUE UN" if miss == 1 else f"IL EN MANQUE {miss}"
    return {
        "badge-fan-made": ("PROJET DE FANS", [("NON OFFICIEL", RED, PAPER)]),
        "badge-fiches": ("FICHES", [(ST["fiches"], CYAN, INK), (f"+ {ST['decoupages']} DÉCOUPAGES", CYAN, INK),
                                    (f"{ST['kb_poids'].upper()} DE TEXTE", CYAN, INK)]),
        "badge-episodes-vus": ("ÉPISODES VISIONNÉS", [(f"{ST['vus']} / {ST['eps']}", YEL, INK), (reste, YEL, INK)]),
        "badge-power": ("ALIMENTATION", [("ON", GRN, INK), ("OFF", RED, PAPER), ("ON AGAIN", GRN, INK)]),
        "badge-preuve": ("ÉTIQUETTE", [("[VÉRIFIÉ]", GRN, INK), ("[PROBABLE]", YEL, INK), ("[À VÉRIFIER]", ORG, INK),
                                        ("[ANALYSE]", VIO, INK), ("[VU À L'IMAGE]", CYAN, INK)]),
    }


SCENES = {
    "hero": hero, "emergency-number": emergency, "the-internet": internet, "fire": fire,
    "crew": crew, "divider-tape": divider_tape, "divider-cable": divider_cable,
    "counter": counter, "loading": loading, "answerphone": answerphone, "tnetennba": tnetennba,
}

# ---------------------------------------------------------------- lecture de kb/
REPO = "agencekoeki/the-it-crowd"                     # dépôt de référence (liens absolus des pages)
SITE = "https://agencekoeki.github.io/the-it-crowd/"  # adresse publique (balises de partage)
TAGS = ["VÉRIFIÉ", "PROBABLE", "À VÉRIFIER", "ANALYSE", "VU À L'IMAGE", "SOUS-TITRES AUTO"]
KB = None   # index complet, rempli par main()
ST = None   # compteurs prêts à afficher (chaînes), rempli par main()


def frontmatter(txt):
    meta = {}
    fm = re.match(r"---\n(.*?)\n---\n", txt, flags=re.S)
    if fm:
        for line in fm.group(1).splitlines():
            m = re.match(r'(\w+):\s*"?(.*?)"?\s*$', line)
            if m:
                meta[m.group(1)] = m.group(2)
    return meta


def size_fr(n):
    """Poids lisible : « 695 Ko », « 1,5 Mo »."""
    ko = n / 1024
    if ko < 1000:
        return f"{ko:.0f} Ko"
    return f"{ko / 1024:.1f} Mo".replace(".", ",")


def count_scenes(txt):
    """Scènes numérotées (« ### 12. … » ou « ### Scène 12 — … ») de la section « Découpage »."""
    m = re.search(r"^## Découpage[^\n]*\n(.*?)(?=^## |\Z)", txt, flags=re.S | re.M)
    return len(re.findall(r"^### (?:Scène\s+)?\d+\b", m.group(1), flags=re.M)) if m else 0


def episode_files():
    """Index de kb/episodes/ : un enregistrement par fichier qui déclare « episode: » dans son frontmatter."""
    found = {}
    folder = ROOT / "kb" / "episodes"
    for f in sorted(folder.glob("*.md")) if folder.is_dir() else []:
        txt = f.read_text(encoding="utf-8")
        meta = frontmatter(txt)
        code = meta.get("episode", "").upper()
        if not code:
            continue
        video = meta.get("source_video", "")
        video = video if re.fullmatch(r"[\w-]{11}", video) else ""
        duree = meta.get("duree", "")
        dur = re.match(r"\d+:\d\d(?::\d\d)?", duree)
        start = re.search(r"de (\d+):(\d\d) à", duree)
        scenes = count_scenes(txt)
        rec = {"file": f"episodes/{f.name}", "bytes": len(txt.encode()),
               "ok": bool(video and scenes and meta.get("statut") != "non_traite")}
        if rec["ok"]:
            rec.update(video=video, dur=dur.group(0) if dur else "", scenes=scenes)
            if start:
                rec["t"] = int(start.group(1)) * 60 + int(start.group(2))
                rec["from"] = f"{start.group(1)}:{start.group(2)}"
        if code not in found or (rec["ok"] and not found[code]["ok"]):
            found[code] = rec
    return found


def kb_data():
    """Index des fiches, table des 25 épisodes complétée par les découpages, annexes, compteurs."""
    kb = ROOT / "kb"
    fiches = []
    for f in sorted(kb.glob("[0-9][0-9]-*.md")):
        txt = f.read_text(encoding="utf-8")
        meta = frontmatter(txt)
        title = re.sub(r"^The IT Crowd\s*[—-]\s*", "", meta.get("title", f.stem))
        counts = {t: len(re.findall(r"\[" + re.escape(t) + r"\b", txt)) for t in TAGS}
        fiches.append({
            "n": f.name[:2], "file": f.name, "title": title, "scope": meta.get("scope", ""),
            "bytes": len(txt.encode()), "lines": txt.count("\n"),
            "sections": [re.sub(r"^\d+\.\s*", "", h) for h in re.findall(r"^## (.+)$", txt, flags=re.M)],
            "tags": counts,
        })
    readme = (kb / "README.md").read_text(encoding="utf-8")
    eps = []
    for m in re.finditer(r"^\| (\d+) \| (\S+)[^|]*\| ([^|]+) \| [^|]+ \| (\d{4}-\d\d-\d\d) \|(?:[^|\n]*\|)*$", readme, flags=re.M):
        code = "SP" if m.group(2).startswith("Sp") else m.group(2)
        eps.append({"n": int(m.group(1)), "code": code, "title": m.group(3).strip(), "date": m.group(4)})
    fr = {}
    for m in re.finditer(r"^\| (S\dE\d|Spécial) \| ([^|]+) \| ([^|]+) \| [^|]+ \|$", readme, flags=re.M):
        fr["SP" if m.group(1) == "Spécial" else m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    files = episode_files()
    for e in eps:
        e["fr"], e["alt"] = fr.get(e["code"], ("", ""))
        e.update(files.get(e["code"], {"ok": False}))
    assert len(eps) == 25, f"table de référence de kb/README.md : {len(eps)} épisodes lus au lieu de 25"

    annexes = []
    for key, rel, label in (("readme", "README.md", "Mode d'emploi de la base"),
                            ("index", "episodes/README.md", "Index des découpages"),
                            ("methode", "_methode/visionnage.md", "Méthode de visionnage"),
                            ("corrections", "episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md",
                             "Ce que le visionnage corrige")):
        f = kb / rel
        if f.is_file():
            annexes.append({"key": key, "file": rel, "title": label, "bytes": f.stat().st_size})

    seen = [e for e in eps if e["ok"]]
    all_md = [f for f in kb.rglob("*.md")]
    stats = {
        "n_fiches": len(fiches), "n_eps": len(eps), "n_vus": len(seen),
        "fiches": str(len(fiches)), "fiches_poids": size_fr(sum(f["bytes"] for f in fiches)),
        "eps": str(len(eps)), "vus": str(len(seen)), "manquants": str(len(eps) - len(seen)),
        "decoupages": str(len(seen)), "decoupages_poids": size_fr(sum(e["bytes"] for e in seen)),
        "scenes": str(sum(e["scenes"] for e in seen)),
        "kb_fichiers": str(len(all_md)), "kb_poids": size_fr(sum(f.stat().st_size for f in all_md)),
        "premiere": fiches[0]["n"], "derniere": fiches[-1]["n"],
        "svg": str(len(SCENES) + 5),
    }
    return {"fiches": fiches, "episodes": eps, "annexes": annexes, "stats": stats}


# ---------------------------------------------------------------- pixels hors SVG animés
def glyph_cells(c):
    """Pixels allumés d'un glyphe : [(x, y)], y de -3 (accents) à 8 (cédille)."""
    cells = []

    def put(rows, y0):
        cells.extend((x, y + y0) for y, row in enumerate(rows) for x, ch in enumerate(row) if ch == "#")
    comp = DATA["composed"].get(c)
    if comp:
        put(FONT[comp[0]].split("/"), 0)
        put(["..#..", ".#..."], 7) if comp[1] == "cedilla" else put(ACC[comp[1]], -3)
    else:
        put(FONT[c].split("/"), 0)
    return cells


def text_svg(s, scale, fill, shadow=None, cls="px"):
    """Texte pixel en SVG autonome, pour les pages HTML générées."""
    w = 6 * len(s) - 1
    grid = [["."] * w for _ in range(12)]
    for i, c in enumerate(s):
        if c != " ":
            for x, y in glyph_cells(c):
                grid[y + 3][i * 6 + x] = "#"
    d = runs_path(["".join(r) for r in grid], y0=-3)
    pad = 1 if shadow else 0
    sh = f'<path transform="translate(.7 .7)" fill="{shadow}" d="{d}"/>' if shadow else ""
    return (f'<svg class="{cls}" aria-hidden="true" viewBox="0 -3 {w + pad} {12 + pad}" width="{(w + pad) * scale}" '
            f'height="{(12 + pad) * scale}" shape-rendering="crispEdges">{sh}<path fill="{fill}" d="{d}"/></svg>')


def sprite_rows(key, legs="A"):
    s = SPR[key]
    return list(s["body"]) + list(s.get("legs" + legs, SPR["_legs" + legs]))


def sprite_svg(key, scale, legs="A"):
    s = SPR[key]
    rows = sprite_rows(key, legs)
    paths = "".join(f'<path fill="{col}" d="{runs_path(rows, ch=ch)}"/>'
                    for ch, col in (("#", s["color"]), ("o", INK), ("a", s["accent"])) if runs_path(rows, ch=ch))
    return (f'<svg aria-hidden="true" viewBox="0 0 {len(rows[0])} {len(rows)}" width="{len(rows[0]) * scale}" '
            f'height="{len(rows) * scale}" shape-rendering="crispEdges">{paths}</svg>')


def favicon():
    """Icône : le bug du projet (sprite original), en SVG, en ligne dans la page."""
    from urllib.parse import quote
    bug = SPR["bug"]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 12" shape-rendering="crispEdges">'
           f'<rect width="13" height="12" rx="2" fill="{INK}"/>'
           f'<path transform="translate(2 2)" fill="{bug["color"]}" d="{runs_path(bug["body"])}"/>'
           f'<path transform="translate(2 2)" fill="{bug["accent"]}" d="{runs_path(bug["body"], ch="a")}"/></svg>')
    return "data:image/svg+xml," + quote(svg, safe="")


class Canvas:
    """Image RVB en mémoire, dessinée au rectangle : de quoi écrire un PNG sans dépendance."""

    def __init__(self, w, h, bg):
        self.w, self.h = w, h
        self.px = bytearray(bytes.fromhex(bg[1:]) * (w * h))

    def rect(self, x, y, w, h, col):
        x0, y0, x1, y1 = max(0, int(x)), max(0, int(y)), min(self.w, int(x + w)), min(self.h, int(y + h))
        if x1 <= x0:
            return
        row = bytes.fromhex(col[1:]) * (x1 - x0)
        for yy in range(y0, y1):
            self.px[(yy * self.w + x0) * 3:(yy * self.w + x1) * 3] = row

    def text(self, x, y, s, scale, col, anchor="start"):
        w = (6 * len(s) - 1) * scale
        x -= w / 2 if anchor == "middle" else w if anchor == "end" else 0
        for i, c in enumerate(s):
            if c != " ":
                for gx, gy in glyph_cells(c):
                    self.rect(x + (i * 6 + gx) * scale, y + gy * scale, scale, scale, col)

    def sprite(self, rows, colors, scale, x, y):
        for ry, row in enumerate(rows):
            for rx, ch in enumerate(row):
                if ch in colors:
                    self.rect(x + rx * scale, y + ry * scale, scale, scale, colors[ch])

    def png(self):
        def chunk(tag, data):
            return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data))
        stride = self.w * 3
        raw = b"".join(b"\x00" + bytes(self.px[y * stride:(y + 1) * stride]) for y in range(self.h))
        return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def social_preview():
    """Image de partage 1280 x 640 : l'écran-titre, l'équipe, la question. Aucun chiffre : elle ne périme pas."""
    W, H = 1280, 640
    c = Canvas(W, H, INK2)
    for i in range(H // 20 + 1):                      # bordure de chargement, comme la bannière
        c.rect(0, i * 20, W, 20, RED if i % 2 else CYAN)
    sx, sy, sw, sh = 56, 56, W - 112, H - 112
    c.rect(sx, sy, sw, sh, DEEP)
    ts = 14
    c.text(W / 2 + 10, 112 + 10, "THE IT CROWD", ts, RED, anchor="middle")
    c.text(W / 2, 112, "THE IT CROWD", ts, PAPER, anchor="middle")
    c.text(W / 2, 244, "L'ENCYCLOPÉDIE DES FANS, RANGÉE AU SOUS-SOL", 4, CYAN, anchor="middle")
    # l'équipe, sur le sol du couloir
    S, floor = 8, 468
    keys = ("tech", "genius", "boss_lady", "mogul", "goth")
    gap = 150
    x0 = (W - (gap * (len(keys) - 1) + 12 * S)) / 2
    c.rect(sx, floor, sw, 6, GREY)
    c.rect(sx, floor + 6, sw, 22, INK2)
    for i, k in enumerate(keys):
        s = SPR[k]
        rows = sprite_rows(k, "A" if i % 2 == 0 else "B")
        c.sprite(rows, {"#": s["color"], "o": INK, "a": s["accent"]}, S, x0 + i * gap, floor - len(rows) * S)
    c.text(W / 2, 516, "> HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?", 3, YEL, anchor="middle")
    c.text(W / 2, 554, "PROJET DE FANS, NON OFFICIEL. PIXEL ART ORIGINAL.", 2, GREY, anchor="middle")
    return c.png()


# ---------------------------------------------------------------- pages et documents
PAGE_404 = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Étage 404 : cette page est tombée dans le trou</title>
<meta name="robots" content="noindex">
<meta name="color-scheme" content="dark light">
<link rel="icon" href="@ICON@">
<style>
:root{--bg:#0d0f2b;--fg:#ece6d0;--dim:#9aa0c8;--rule:#2c3172;--link:#2ee6e6;--hot:#f5d90a}
@media (prefers-color-scheme:light){:root{--bg:#ece6d0;--fg:#0d0f2b;--dim:#4b4f7c;--rule:#b9b39c;--link:#1a27c9;--hot:#b3141b}}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:grid;place-items:center;background:var(--bg);color:var(--fg);
  font:16px/1.6 ui-monospace,"Cascadia Mono","SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace;padding:24px 16px}
main{width:min(100%,640px)}
svg{display:block;max-width:100%;height:auto}
h1{margin:0 0 8px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.pit{position:relative;height:160px;margin:28px 0 24px;overflow:hidden;background:#12143a;border:4px solid var(--rule)}
.pit .floor{position:absolute;left:0;right:0;bottom:0;height:34px;background:#1b1f52;border-top:4px solid #8e93b8}
.pit .hole{position:absolute;left:50%;bottom:0;width:96px;height:34px;margin-left:-48px;background:#000;border-inline:4px solid #8e93b8}
.pit .sign{position:absolute;left:50%;bottom:92px;margin-left:66px;background:#f5d90a;color:#0d0f2b;font-size:12px;font-weight:700;padding:2px 8px}
.pit .sign::after{content:"";position:absolute;left:50%;top:100%;width:4px;height:60px;background:#8e93b8}
.pit .who{position:absolute;left:50%;bottom:34px;margin-left:-30px;animation:fall 5s cubic-bezier(.6,0,1,.6) infinite}
@keyframes fall{0%{transform:translate(-190px,0)}34%,40%{transform:translate(0,0)}54%,100%{transform:translate(0,170px)}}
p{margin:0 0 14px;max-width:60ch}
.dim{color:var(--dim);font-size:14px}
ol{margin:0 0 22px;padding-left:1.4em}
a{color:var(--link);text-underline-offset:3px}
a:focus-visible{outline:3px solid var(--hot);outline-offset:3px}
.go{display:inline-block;border:4px solid var(--fg);background:var(--fg);color:var(--bg);padding:9px 16px;font-weight:700;text-decoration:none;margin:0 12px 12px 0}
.go.ghost{background:none;color:var(--fg)}
.go:hover{background:#f5d90a;border-color:#f5d90a;color:#0d0f2b}
@media (prefers-reduced-motion:reduce){.pit .who{animation:none;transform:translate(0,22px)}}
</style>
</head>
<body>
<main>
  <h1><span class="sr">Étage 404 : cette page n'existe pas</span>@TITLE@</h1>
  <p class="dim">Erreur 404. Cet étage n'est desservi par aucun ascenseur.</p>
  <div class="pit" aria-hidden="true">
    <div class="who">@WHO@</div>
    <div class="floor"></div><div class="hole"></div><span class="sign">ÉTAGE 404</span>
  </div>
  <p>La page demandée n'existe pas, ou elle est rangée derrière la porte rouge. La direction vient d'aller vérifier en personne. Elle ne répond plus.</p>
  <p>Le service informatique a été prévenu. Il recommande la procédure habituelle :</p>
  <ol>
    <li>Éteindre, puis rallumer.</li>
    <li>Vérifier que l'adresse est bien branchée.</li>
    <li>Revenir à l'accueil, où tout fonctionne à peu près.</li>
  </ol>
  <a class="go" id="home" href="./">Retour à l'accueil</a>
  <a class="go ghost" href="https://github.com/@REPO@">Le dépôt sur GitHub</a>
  <p class="dim" style="margin-top:22px">Projet de fans, non officiel. Aucun lien avec Channel 4 ni avec les ayants droit de <i>The IT Crowd</i>. Pixel art original.</p>
</main>
<script>
// GitHub Pages sert cette page à n'importe quelle adresse : le lien d'accueil doit viser la racine du site.
(function () {
  var seg = location.pathname.split("/")[1] || "";
  if (/\\.github\\.io$/.test(location.hostname) && seg) document.getElementById("home").href = "/" + seg + "/";
})();
</script>
</body>
</html>
"""


def page_404():
    return (PAGE_404.replace("@ICON@", favicon()).replace("@REPO@", REPO)
            .replace("@TITLE@", text_svg("ÉTAGE 404", 9, "currentColor", shadow=RED))
            .replace("@WHO@", sprite_svg("mogul", 5)))


def meta_block():
    desc = (f"Base de connaissances de fans sur la sitcom britannique The IT Crowd : {ST['fiches']} fiches sourcées, "
            f"{ST['vus']} épisodes sur {ST['eps']} découpés scène par scène, une discipline de preuve. Projet non officiel.")
    short = "L'encyclopédie des fans, rangée au sous-sol. Have you tried turning it off and on again?"
    title = "The IT Crowd, l'encyclopédie des fans (non officielle)"
    lines = [
        f'<meta name="description" content="{desc}">',
        f'<link rel="canonical" href="{SITE}">',
        f'<link rel="icon" href="{favicon()}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:locale" content="fr_FR">',
        '<meta property="og:site_name" content="The IT Crowd, l\'encyclopédie des fans">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{short}">',
        f'<meta property="og:url" content="{SITE}">',
        f'<meta property="og:image" content="{SITE}social-preview.png">',
        '<meta property="og:image:width" content="1280">',
        '<meta property="og:image:height" content="640">',
        '<meta property="og:image:alt" content="Écran de micro-ordinateur en pixels : The IT Crowd, '
        'l\'encyclopédie des fans, et cinq personnages originaux.">',
        '<meta name="twitter:card" content="summary_large_image">',
    ]
    return "\n".join(lines)


def put_block(text, name, body, where):
    """Remplace le contenu entre <!-- BEGIN:name ... --> et <!-- END:name -->."""
    out, n = re.subn(rf"(<!-- BEGIN:{name}\b[^>]*-->\n).*?(<!-- END:{name} -->)",
                     lambda m: m.group(1) + body + "\n" + m.group(2), text, flags=re.S)
    assert n == 1, f"repère BEGIN:{name} introuvable dans {where}"
    return out


def put_stats(text, pattern, where):
    def sub(m):
        assert m.group(2) in ST, f"compteur inconnu « {m.group(2)} » dans {where}"
        return m.group(1) + ST[m.group(2)] + m.group(3)
    return re.sub(pattern, sub, text)


def write_if_changed(path, data):
    old = path.read_bytes() if path.exists() else None
    new = data if isinstance(data, bytes) else data.encode("utf-8")
    if old != new:
        path.write_bytes(new)
        return True
    return False


def sync_page():
    page = ROOT / "docs" / "index.html"
    html = page.read_text(encoding="utf-8")
    blocks = {
        "pixel-data": {k: DATA[k] for k in ("font", "accents", "composed", "sprites")},
        "kb-data": KB,
    }
    for bid, obj in blocks.items():
        payload = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        html, n = re.subn(rf'(<script id="{bid}" type="application/json">).*?(</script>)',
                          lambda m: m.group(1) + payload + m.group(2), html, flags=re.S)
        assert n == 1, f"bloc {bid} introuvable dans docs/index.html"
    html = put_block(html, "meta", meta_block(), "docs/index.html")
    html = put_stats(html, r'(<span data-stat="(\w+)">)[^<]*(</span>)', "docs/index.html")
    return write_if_changed(page, html)


def readme_episodes():
    """Tableau des découpages du README, une ligne par épisode de la table de référence."""
    rows = ["| Épisode | Titre | Durée | Scènes | Découpage | Vidéo officielle |", "|---|---|---|---|---|---|"]
    for e in KB["episodes"]:
        if e["ok"]:
            url = f"https://www.youtube.com/watch?v={e['video']}" + (f"&t={e['t']}s" if e.get("t") else "")
            where = f"[YouTube, à partir de {e['from']}]({url})" if e.get("t") else f"[YouTube]({url})"
            rows.append(f"| {e['code']} | *{e['title']}* | {e['dur']} | {e['scenes']} | "
                        f"[lire](kb/{e['file']}) ({size_fr(e['bytes'])}) | {where} |")
        else:
            link = f"[le constat](kb/{e['file']})" if e.get("file") else "à faire"
            rows.append(f"| {e['code']} | *{e['title']}* | — | — | non traité : {link} | pas en entier sur la chaîne officielle |")
    return "\n".join(rows)


def sync_documents():
    """Compteurs, poids et tableaux des documents de la racine."""
    changed = []
    alts = {
        "badge-fiches": f"Fiches thématiques : {ST['fiches']}, plus {ST['decoupages']} découpages d'épisodes",
        "badge-episodes-vus": f"Épisodes visionnés : {ST['vus']} sur {ST['eps']}",
    }
    for name in ("README.md", "STRUCTURE.md"):
        path = ROOT / name
        if not path.exists():
            continue
        txt = path.read_text(encoding="utf-8")
        txt = put_stats(txt, r"(<!--n:(\w+)-->).*?(<!--/n-->)", name)
        if name == "README.md":
            txt = put_block(txt, "decoupages", readme_episodes(), name)
            for badge, alt in alts.items():
                txt, n = re.subn(rf'(<img src="assets/{badge}\.svg"[^>]*\balt=")[^"]*(")',
                                 lambda m: m.group(1) + alt + m.group(2), txt)
                assert n == 1, f"badge {badge} introuvable dans README.md"

            def weight(m):
                f = ROOT / m.group(2)
                return m.group(1) + (size_fr(f.stat().st_size) if f.is_file() else m.group(3)) + m.group(4)
            txt = re.sub(r"^(\| \[[^\]]+\]\((kb/[^)\s]+\.md)\) \|.*\| )([^|\n]+?)( \|)$", weight, txt, flags=re.M)
        if write_if_changed(path, txt):
            changed.append(name)
    return changed


def main():
    global KB, ST
    KB = kb_data()
    ST = KB["stats"]
    out = ROOT / "assets"
    out.mkdir(exist_ok=True)
    res = {name: fn() for name, fn in SCENES.items()}
    for name, (label, values) in badges().items():
        res[name] = badge(label, values)
    assert len(res) == int(ST["svg"])
    for name, svg in res.items():
        assert "<script" not in svg and "foreignObject" not in svg and "http" not in svg.replace("http://www.w3.org/2000/svg", "")
        write_if_changed(out / f"{name}.svg", svg)
        kb = len(svg.encode()) / 1024
        assert kb < 150, f"{name} trop lourd : {kb:.0f} Ko"
        print(f"{name}.svg  {kb:6.1f} Ko")
    png = social_preview()
    write_if_changed(out / "social-preview.png", png)
    print(f"social-preview.png  {len(png) / 1024:6.1f} Ko")
    print(f"kb/ : {ST['fiches']} fiches ({ST['fiches_poids']}), {ST['vus']} épisodes sur {ST['eps']} découpés "
          f"({ST['scenes']} scènes, {ST['decoupages_poids']}), {ST['kb_fichiers']} fichiers, {ST['kb_poids']}")
    if "--sync-docs" in sys.argv:
        docs = ROOT / "docs"
        done = ["docs/index.html"] if sync_page() else []
        done += ["docs/404.html"] if write_if_changed(docs / "404.html", page_404()) else []
        done += ["docs/social-preview.png"] if write_if_changed(docs / "social-preview.png", png) else []
        done += sync_documents()
        print("synchronisé : " + (", ".join(done) if done else "rien à changer, tout était à jour"))


if __name__ == "__main__":
    main()
