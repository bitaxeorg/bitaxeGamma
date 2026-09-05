#!/usr/bin/env python3
"""apply_eco603.py — parche semiautomático 601→603 (incluye herencia 602).
Uso: python3 apply_eco603.py /tmp/opencode/bitaxeGamma
- Hace backup .bak601
- rev 601→603, R22/R23 100→10, marca R21 como DNI (herencia 602), chequea pendientes E0/E1/E2/E4/E5.
- NO coloca footprints nuevos ni borra símbolos; usar ADDITIONS snippets + KiCad.
"""
import sys, shutil, re
from pathlib import Path
root = Path(sys.argv[1] if len(sys.argv)>1 else "/tmp/opencode/bitaxeGamma")
for f in ["power.kicad_sch","fan.kicad_sch","bm1370.kicad_sch","esp32.kicad_sch","bitaxeGamma.kicad_sch"]:
    p = root/f
    if not p.exists(): continue
    txt = p.read_text()
    if ".bak601" not in str(p):
        shutil.copy(p, str(p)+".bak601")
    txt = txt.replace('(rev "601")','(rev "603")')
    txt = txt.replace('(date "2024-09-26")','(date "2026-09-05")')
    if f=="fan.kicad_sch":
        # R22/R23: cambia Value 100 que sigue a Reference R22/R23
        def _repl(m):
            return m.group(1) + "10" + m.group(2)
        txt = re.sub(r'(property "Reference" "R2[23]".*?property "Value" ")100(")', _repl, txt, flags=re.S)
        txt = txt.replace("311-100LRCT-ND","311-10.0LRCT-ND").replace("RC0402FR-07100RL","RC0402FR-0710RL")
    if f=="bm1370.kicad_sch":
        # E0 herencia 602: marcar R21 como DNI (borrado manual en KiCad + net a 1V2)
        txt = txt.replace('(property "Reference" "R21"', '(property "Reference" "R21_DNI-E0"')
    p.write_text(txt)
    print(f"OK {f}")
print("\nPENDIENTES MANUALES en Eeschema (ver ECO-603.md):")
print("- E0: quitar R21 (ya marcado DNI), net→1V2 directo, fix B4 U9 no flotante (#6)")
print("- E1: SYNC(38)+BCX_CLK(39)+BCX_DAT(40) U2 → GND")
print("- E2: añadir R30-32 4.7k a 3V3 en PMB_DATA/CLK/SMB_ALRT")
print("- E4: añadir F1 5A + D1 SMAJ5.0A + C60 100uF en J1")
print("- E5: añadir R33-34 5.1k CC1/CC2→GND en J5")
print("- E6: revisar J1/L1/C13 + actualizar PCB, silk, BOM-603.csv")
