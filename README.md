# Ahmed's Macropad
This is a 10-key macropad with a rotary encoder and OLED display.
Its my Submission for Blueprint.

<img width="657" height="436" alt="image" src="https://github.com/user-attachments/assets/cf4e1ea0-043a-4634-a037-44d5b4d63e81" /> 


## Features
* 10x MX switches in a 2×5 matrix
* EC11 Rotary encoder — rotate for volume, push to mute
* 0.91" OLED display showing live volume level
* KMK firmware
* 3D printed case
* #KEEP_EYES_ON_SUDAN

## PCB
Made in KiCad. 2 layer board, just under 100×100mm.

<img width="634" height="574" alt="image" src="https://github.com/user-attachments/assets/98c69402-d512-4590-b1ab-2ce8d3e13efc" />

### Schematic
<img width="1108" height="625" alt="image" src="https://github.com/user-attachments/assets/407ed2da-3c50-40b2-9887-458e7dc7f7d1" />




## CAD 
Made in SolidWorks. Everything fits together using 
5x M3x16mm screws, screws and 5x M3x5x4mm heatset inserts.
5 printed parts: Top, Middle, Bottom, Base, Cover.

<img width="786" height="495" alt="image" src="https://github.com/user-attachments/assets/b8894e62-4366-4c73-b716-c4b42f0055ea" />
<img width="599" height="530" alt="image" src="https://github.com/user-attachments/assets/8de6860e-697d-4120-9d57-1401ffa1f869" />



## Firmware
I used KMK for the firmware, each key has a seprate function, the rotary encoder controls the Vol level and the OLED displays the level.


## BOM
| Part | Quantity |
|---|---|
| Seeed XIAO RP2040 | 1 |
| MX Switches | 10 |
| 1N4148 Diodes | 10 |
| EC11 Rotary Encoder | 1 |
| 0.91" OLED Display | 1 |
| DSA Keycaps | 10 |
| M3x16mm Screws | 5 |
| M3x5x4mm Heatset Inserts | 5 |
