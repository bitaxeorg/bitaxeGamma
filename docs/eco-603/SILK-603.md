# Serigrafía + PCB 603 (F.SilkS / B.SilkS, F.Fab)

## 3.1 Textos a añadir (altura 1.0-1.27mm, grosor 0.15mm)
- `F.SilkS` junto a J1: `5V ONLY 5A MAX` + `+` en pin central.
- `F.SilkS` sobre U2: `Gamma 603` (reemplaza 601).
- `F.SilkS` junto a F1: `F1 5A` + marco. Junto a D1: `D1 SMAJ5.0A` + barra cátodo.
- `F.SilkS` junto a R30-32: `PU 4K7 PMBus`. Junto a R33-34: `CC 5K1`. Junto a R35: `PGD 10K`.
- `F.SilkS` junto a D2: `ESD USB`. Junto a D3/D4: `ESD I2C`. Junto a C61/C62: `47u+100n PVIN`.
- `B.SilkS`: `R21 REMOVED→1V2 | R22 R23=10R | SYNC/BCX→GND` + `603=601+602fixes`.
- `F.Fab`: valores + DK de F1/D1/R30-35/C60-62/D2-D4/TPs.

## 3.2 Reglas
- No silk sobre pads/vías. Clearance silk→pad ≥0.2mm.
- Polaridad: D1 barra hacia 5V, F1 sin polaridad pero marcar 1-2. D2 pin1 punto, D3/D4 barra a GND.
- TPs: rotular `VCORE PGD 3V3 GND GND SDA SCL` en F.SilkS junto a cada pad 2mm.
- Keepout antena ESP32-S3: rectángulo hatch en F.SilkS `ANT KEEPOUT`, sin cobre/silk denso.
- Fiduciales: 3x círculo 1mm + máscara 2mm en esquinas, fuera de silk.

## 3.3 Placement recomendado (origen esquina J1)
- F1 1206 en serie +5V entre J1 y D1, pista ≥2.5mm ancho (5A). Pour 1V2 ≥3mm post-U2.
- D1 SMA DO-214AC a <10mm de J1, vías GND 2x0.5mm.
- C60 1206 a <8mm de J1. C61 47u + C62 100n a <5mm de PVIN/AVIN U2.
- R30-32 0402 a <15mm de U2 pins 2/3/6, pull a net 3V3 existente. R35 10k PGD(1)→3V3 <10mm.
- R33-34 a <10mm de J5. D2 a <8mm de J5 en D+/D-. D3/D4 a <10mm de U2 en SDA/SCL.
- Vías térmicas 0.3/0.6mm: 3x3 bajo U2, 4x4 bajo BM1370 a In2.Cu/GND. TEMP_DP/DN diff + guard.
- TPs 2mm en borde: VCORE/PGD/3V3/GND accesibles con punta.

## 3.4 Stackup/fab (sin cambio)
4L 1.6mm FR4, 1oz ext/0.5oz int, 6mil/0.3mm, ENIG, pasta top+bottom para stencil.
