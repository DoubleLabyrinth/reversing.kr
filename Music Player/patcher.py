import sys

def help():
    print('Usage:')
    print('    patcher.py <path to music_player.exe>')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        help()
    else:
        f = open(sys.argv[1], 'rb')
        content = f.read()
        f.close()

        content = content.replace(b'\x0f\x8c\x8d\x00\x00\x00', 
                                  b'\xe9\x8e\x00\x00\x00\x90')
        content = content.replace(b'\xFF\x91\xBC\x00\x00\x00\x85\xC0\xDB\xE2\x7D\x12',
                                  b'\xFF\x91\xBC\x00\x00\x00\x85\xC0\xDB\xE2\xEB\x12')

        f = open('music_player_patched.exe', 'wb')
        f.write(content)
        f.close()

        print('Success!')
