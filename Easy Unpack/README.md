# Reversing.kr -- Easy Unpack

## 1. Challenge

Just an exe file and a `ReadMe.txt`:

> ReversingKr UnpackMe
> 
> Find the OEP
> 
> ex) 00401000

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

This exe file was packed and you should find the OEP.

So drop it into `x32dbg` and trap thae process step by step. Finally you will see a big jump at `0x0040A1FB`. Follow it and you will see OEP = 00401150.
