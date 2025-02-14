import sys

def caesar_cipher(text, shift, action):
    result = []
    for char in text:
        if not char.isascii() and not char.isspace():
            raise Exception("The script does not support your language yet.")
    for char in text:
        if char.isalpha(): #только буквы, остальные символы оставляем как есть
            start = ord('a') if char.islower() else ord('A')
            if action == 'encode':
                result.append(chr((ord(char) - start + shift) % 26 + start))
            elif action == 'decode':
                result.append(chr((ord(char) - start - shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 4:
        raise Exception("The script requires exactly 3 arguments.")
    
    action = sys.argv[1].lower()
    if action not in ['encode', 'decode']:
        raise Exception("The first argument should be 'encode' or 'decode'.")
    
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("The shift value must be an integer.")
    
    result = caesar_cipher(text, shift, action)
    print(result)

if __name__ == '__main__':
    main()
