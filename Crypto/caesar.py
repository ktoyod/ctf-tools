##### ASCIIコード #####
# 65: 'A' ~  90: 'Z'
# 97: 'a' ~ 122: 'z'

def caesar(s, n):
    flag = ''
    for c in s:
        if 65 <= ord(c) <= 90:
            flag += chr(65 + (ord(c) + n - 65) % 26)
        elif 97 <= ord(c) <= 122:
            flag += chr(97 + (ord(c) + n - 97) % 26)
        else:
            flag += c
    return flag


if __name__ == '__main__':
    s = input('暗号文を入力: ')
    n = int(input('シフトさせたい文字数を入力: '))
    print(f'復号文: {Caesar(s, n)}')
