# 6502 opcode reference

Official NMOS 6502 instruction set: **151 opcodes, 56 mnemonics**. The 2A03/2A07 in the NES uses the same encodings and cycles, but decimal mode is disabled. Illegal/undocumented opcodes are intentionally omitted; they differ across chips and emulators.

## Opcode matrix

Rows are the high nibble, columns the low nibble. `---` is an undocumented/illegal encoding on the NMOS 6502.

### `0x00–0x7F`

|   | $0 | $1 | $2 | $3 | $4 | $5 | $6 | $7 |
|---|---|---|---|---|---|---|---|---|
| **$00** | BRK impl | ORA (zp,X) | --- | --- | --- | ORA zp | ASL zp | --- |
| **$10** | BPL rel | ORA (zp),Y | --- | --- | --- | ORA zp,X | ASL zp,X | --- |
| **$20** | JSR abs | AND (zp,X) | --- | --- | BIT zp | AND zp | ROL zp | --- |
| **$30** | BMI rel | AND (zp),Y | --- | --- | --- | AND zp,X | ROL zp,X | --- |
| **$40** | RTI impl | EOR (zp,X) | --- | --- | --- | EOR zp | LSR zp | --- |
| **$50** | BVC rel | EOR (zp),Y | --- | --- | --- | EOR zp,X | LSR zp,X | --- |
| **$60** | RTS impl | ADC (zp,X) | --- | --- | --- | ADC zp | ROR zp | --- |
| **$70** | BVS rel | ADC (zp),Y | --- | --- | --- | ADC zp,X | ROR zp,X | --- |
| **$80** | --- | STA (zp,X) | --- | --- | STY zp | STA zp | STX zp | --- |
| **$90** | BCC rel | STA (zp),Y | --- | --- | STY zp,X | STA zp,X | STX zp,Y | --- |
| **$A0** | LDY # | LDA (zp,X) | LDX # | --- | LDY zp | LDA zp | LDX zp | --- |
| **$B0** | BCS rel | LDA (zp),Y | --- | --- | LDY zp,X | LDA zp,X | LDX zp,Y | --- |
| **$C0** | CPY # | CMP (zp,X) | --- | --- | CPY zp | CMP zp | DEC zp | --- |
| **$D0** | BNE rel | CMP (zp),Y | --- | --- | --- | CMP zp,X | DEC zp,X | --- |
| **$E0** | CPX # | SBC (zp,X) | --- | --- | CPX zp | SBC zp | INC zp | --- |
| **$F0** | BEQ rel | SBC (zp),Y | --- | --- | --- | SBC zp,X | INC zp,X | --- |

### `0x80–0xFF`

|   | $8 | $9 | $A | $B | $C | $D | $E | $F |
|---|---|---|---|---|---|---|---|---|
| **$00** | PHP impl | ORA # | ASL A | --- | --- | ORA abs | ASL abs | --- |
| **$10** | CLC impl | ORA abs,Y | --- | --- | --- | ORA abs,X | ASL abs,X | --- |
| **$20** | PLP impl | AND # | ROL A | --- | BIT abs | AND abs | ROL abs | --- |
| **$30** | SEC impl | AND abs,Y | --- | --- | --- | AND abs,X | ROL abs,X | --- |
| **$40** | PHA impl | EOR # | LSR A | --- | JMP abs | EOR abs | LSR abs | --- |
| **$50** | CLI impl | EOR abs,Y | --- | --- | --- | EOR abs,X | LSR abs,X | --- |
| **$60** | PLA impl | ADC # | ROR A | --- | JMP (abs) | ADC abs | ROR abs | --- |
| **$70** | SEI impl | ADC abs,Y | --- | --- | --- | ADC abs,X | ROR abs,X | --- |
| **$80** | DEY impl | --- | TXA impl | --- | STY abs | STA abs | STX abs | --- |
| **$90** | TYA impl | STA abs,Y | TXS impl | --- | --- | STA abs,X | --- | --- |
| **$A0** | TAY impl | LDA # | TAX impl | --- | LDY abs | LDA abs | LDX abs | --- |
| **$B0** | CLV impl | LDA abs,Y | TSX impl | --- | LDY abs,X | LDA abs,X | LDX abs,Y | --- |
| **$C0** | INY impl | CMP # | DEX impl | --- | CPY abs | CMP abs | DEC abs | --- |
| **$D0** | CLD impl | CMP abs,Y | --- | --- | --- | CMP abs,X | DEC abs,X | --- |
| **$E0** | INX impl | SBC # | NOP impl | --- | CPX abs | SBC abs | INC abs | --- |
| **$F0** | SED impl | SBC abs,Y | --- | --- | --- | SBC abs,X | INC abs,X | --- |

## Instructions by mnemonic

Cycles are base counts. `*` = add 1 when a read crosses a page boundary. `†` = branches: 2 cycles not taken, 3 taken, 4 if the branch crosses a page.

| Mnemonic | Modes and cycles | Flags |
|---|---|---|
| **ADC** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N V Z C |
| **AND** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N Z |
| **ASL** | A 2, zp 5, zp,X 6, abs 6, abs,X 7 | N Z C |
| **BCC** | rel 2† | — |
| **BCS** | rel 2† | — |
| **BEQ** | rel 2† | — |
| **BIT** | zp 3, abs 4 | N V Z |
| **BMI** | rel 2† | — |
| **BNE** | rel 2† | — |
| **BPL** | rel 2† | — |
| **BRK** | impl 7 | B I |
| **BVC** | rel 2† | — |
| **BVS** | rel 2† | — |
| **CLC** | impl 2 | C=0 |
| **CLD** | impl 2 | D=0 |
| **CLI** | impl 2 | I=0 |
| **CLV** | impl 2 | V=0 |
| **CMP** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N Z C |
| **CPX** | # 2, zp 3, abs 4 | N Z C |
| **CPY** | # 2, zp 3, abs 4 | N Z C |
| **DEC** | zp 5, zp,X 6, abs 6, abs,X 7 | N Z |
| **DEX** | impl 2 | N Z |
| **DEY** | impl 2 | N Z |
| **EOR** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N Z |
| **INC** | zp 5, zp,X 6, abs 6, abs,X 7 | N Z |
| **INX** | impl 2 | N Z |
| **INY** | impl 2 | N Z |
| **JMP** | abs 3, (abs) 5 | — |
| **JSR** | abs 6 | — |
| **LDA** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N Z |
| **LDX** | # 2, zp 3, zp,Y 4, abs 4, abs,Y 4* | N Z |
| **LDY** | # 2, zp 3, zp,X 4, abs 4, abs,X 4* | N Z |
| **LSR** | A 2, zp 5, zp,X 6, abs 6, abs,X 7 | N Z C |
| **NOP** | impl 2 | — |
| **ORA** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N Z |
| **PHA** | impl 3 | — |
| **PHP** | impl 3 | — |
| **PLA** | impl 4 | N Z |
| **PLP** | impl 4 | all |
| **ROL** | A 2, zp 5, zp,X 6, abs 6, abs,X 7 | N Z C |
| **ROR** | A 2, zp 5, zp,X 6, abs 6, abs,X 7 | N Z C |
| **RTI** | impl 6 | all |
| **RTS** | impl 6 | — |
| **SBC** | # 2, zp 3, zp,X 4, abs 4, abs,X 4*, abs,Y 4*, (zp,X) 6, (zp),Y 5* | N V Z C |
| **SEC** | impl 2 | C=1 |
| **SED** | impl 2 | D=1 |
| **SEI** | impl 2 | I=1 |
| **STA** | zp 3, zp,X 4, abs 4, abs,X 5, abs,Y 5, (zp,X) 6, (zp),Y 6 | — |
| **STX** | zp 3, zp,Y 4, abs 4 | — |
| **STY** | zp 3, zp,X 4, abs 4 | — |
| **TAX** | impl 2 | N Z |
| **TAY** | impl 2 | N Z |
| **TSX** | impl 2 | N Z |
| **TXA** | impl 2 | N Z |
| **TXS** | impl 2 | — |
| **TYA** | impl 2 | N Z |

## Timing notes

- **Page-cross penalty**: `abs,X`, `abs,Y`, and `(zp),Y` reads take +1 cycle when the effective address crosses a 256-byte page. Stores do not pay it (`STA abs,X` is fixed 5).
- **Branches**: 2 cycles if not taken, 3 if taken, 4 if taken across a page. The branch offset is signed 8-bit (`-128..+127`) from the byte after the operand.
- **JMP (`abs`)**: 3 cycles; **JMP (`abs`)** indirect is 5 and has the NMOS page-boundary bug: `JMP ($xxFF)` reads the high byte from `$xx00`, not `$xx+1:00`. The 65C02 fixes this.
- **Indexed crossing**: `abs,X`/`abs,Y` with a carry into the high byte costs the extra cycle; `zp,X`/`zp,Y` wrap inside zero page and never cross.
- **Decimal mode**: on the 2A03/2A07 `SED` sets D but `ADC`/`SBC` ignore it. On a real 6502, decimal mode adds a cycle on some parts; do not rely on it for NES code.

## Flag quick reference

| Flag | Bit | Set by | Cleared by |
|---|---|---|---|
| N | 7 | result bit 7 (most operations) | result bit 7 clear |
| V | 6 | ADC/SBC/BIT/CLV | ADC/SBC/BIT |
| B | 4 | BRK/PHP push (not a real register bit) | PLP/RTI |
| D | 3 | SED | CLD |
| I | 2 | SEI/IRQ/NMI/BRK | CLI/RTI |
| Z | 1 | zero result | non-zero result |
| C | 0 | ADC/SBC/ASL/LSR/ROL/ROR/CMP | CLC, no carry/borrow |
