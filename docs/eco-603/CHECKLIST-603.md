# CHECKLIST-603 — fabricación, ensamblaje y bring-up

## Fab (JLC/PCBWay/Seeed)
- 4L, 1.6mm, TG150, ENIG, 6mil/0.3mm. Gerbers 601 + delta ECO. Pedir stencil top+bottom.
- Verificar footprint J1 PJ-002A vs Gerber Edge+Pads antes de panelizar.

## SMT
- Pasta Sn63/Pb37 T3 fría, horno convección: soak 140-150C 2min → reflow 200-220C 30s, termopar sobre PCB.
- Orden: bottom chico → top. U2 QFN + BM1370 con lupa/microscopio, sin puentes.
- No montar J7 si usas OLED externo. Limpiar IPA.

## Bring-up sin ASIC-hash (primera vez)
1. Sin alimentar: F1 0Ω, D1/D2/D3/D4 diodo OK, SYNC/BCX 0Ω→GND, pull-ups 4.7k→3V3 + PGD 10k→3V3, CC 5.1k→GND, R21 ausente + net=1V2, B4 no flotante.
2. 5V lab con límite 1A: corriente <150mA, 3V3=3.3±0.07V, Vcore=0V (EN off).
3. USB-C cable A-C: enumera ESP32-S3, flashea AxeOS/ESP-Miner.
4. Set Vcore 1.15V vía PMBus, mide en test point, PGD=3V3.
5. Hash 525MHz: ~1.2TH/s, temp estable ±2C, fan PWM OK. Si fluctúa >5C revisa R22/23=10R y soldadura BM1370.
6. Stress 12h + prueba 12V accidental NO hacer — el TVS+fusible es última defensa, no prueba.

## Archivos entrega
ECO-603.md, BOM-603.csv, SILK-603.md, ADDITIONS snippets, apply_eco603.py, este checklist.
Licencia derivada: CERN-OHL-S-2.0 (mantener).
