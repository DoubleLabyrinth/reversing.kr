# Reversing.kr -- Easy Crack

## 1. Challenge

Just an exe file.

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Drop it into IDA, goto function `WinMain` --> `DialogFunc` --> `sub_401080` and you will see the flag is splited into 4 part.

Join them and you will see the flag.
