# Reversing.kr -- Easy Keygen

## 1. Challenge

Just an exe file and a `ReadMe.txt`:

> ReversingKr KeygenMe
> 
> Find the Name when the Serial is 5B134977135E7D13

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Drop it into IDA, goto function `main` and you will see that your name will be XORed by `\x10\x20\x30` circularly and be converted into hex string after you input your name. Then you will be asked to input serial and program will check if it is the same with that hex string.

So convert serial to bytes and XOR it by `\x10\x20\x30` circularly again and you will the flag.
