# Reversing.kr -- Ransomware

## 1. Challenge

Just three files `file`, `run.exe` and `readme.txt`:

> Decrypt File (EXE)  
> By Pyutic


Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Drop `run.exe` into IDA. However, this program is packed. And you can see there is a section named `UPX1`. So you can use UPX to unpack it.

```bash
$ upx.exe -d -k run.exe
```

Drop unpacked `run.exe` into IDA. However, there is a lot of obscure assembly code which looks like:

```asm
pusha
popa
nop
push eax
pop eax
push ebx
pop ebx
...
```

I don't know how to remove those instructions, so I read assembly code directly.

It seems function `main` is equivalent to the following python code:

```python
key = input('Key : ').encode()

f = open('file', 'rb')
enc_content = f.read()
f.close()

dec_content = []
for i in range(len(enc_content)):
    dec_content.append(enc_content[i] ^ key[i % len(key)] ^ 0xFF)
dec_content = bytes(dec_content)

f = open('file', 'wb')
f.write(dec_content)
f.close()
```

`readme.txt` has given a hint that `file` is an `exe` file. Generally speaking, an `exe` file contains a `IMAGE_DOS_STUB` structure where there is a string "This program cannot be run in DOS mode".

So we can play known plaintext attack.

Run `Ransomware.py` and you will see the decrypt key is __letsplaychess__.

Use `run.exe` to decrypt `file` by the key and run. Then you will see the flag: __Colle System__
