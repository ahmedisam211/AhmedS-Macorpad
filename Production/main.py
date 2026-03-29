import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP28, board.GP29, board.GP0, board.GP1, board.GP4)
keyboard.row_pins = (board.GP26, board.GP27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP2, board.GP3, None, False),)

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.LCTL(KC.C),   # K1  Copy
        KC.LCTL(KC.V),   # K2  Paste
        KC.LCTL(KC.X),   # K3  Cut
        KC.LCTL(KC.Z),   # K4  Undo
        KC.LCTL(KC.Y),   # K5  Redo
        KC.MPLY,          # K6  Play/Pause
        KC.MNXT,          # K7  Next Track
        KC.MPRV,          # K8  Previous Track
        KC.LCTL(KC.S),   # K9  Save
        KC.NO,            # K10 Empty
    ]
]

encoder_handler.map = [((KC.VOLD, KC.VOLU),)]

if __name__ == '__main__':
    keyboard.go()
