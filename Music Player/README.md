# Reversing.kr -- Music Player

## 1. Challenge

Just 3 files `msvbvm60.dll`, `Music_Player.exe` and `ReadMe.txt`:

> This MP3 Player is limited to 1 minutes.  
> You have to play more than one minute.  
>   
> There are exist several 1-minute-check-routine.  
> After bypassing every check routine, you will see the perfect flag.  

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Open `Music_Player.exe` and choose a MP3 to play. 

After one minute, a message box poped up. So we can known that `MessageBox*` must be called and we can set up breakpoints on all of those functions. Actually, I did not find related symbols in `music_player.exe` module. However, I found `MessageBoxA` and `MessageBoxIndirectA` in `msvbvm60.dll` module.

When the breakpoint on `MessageBoxIndirectA` was triggered, I checked out the call stack and found that `MessageBoxIndirectA` was called because of `call rtcMsgBox` at __music_player.004045D8__. 

This call is part of function `sub_4044C0`. We can look up function `sub_4044C0` in IDA. 

Use __F5__ to decompiler. We can see there is a if-statement looking like:

```cpp
if (v35 < 60000) {
    ...
    ...
```

Obviously, "60000" means 60000ms and we want to enter this if-statement without any condition. So we just wipe out this judgement by modifing

```asm
0040456B    jl loc_4045FE
```

to 

```asm
0040456B    jmp loc_4045FE
00404570    nop
```

However, after restart this player and playing a song until one minute, an error occured. That is because function `_vbaHresultCheckObj` was called at __music_player.004046B9__. We just modify

```asm
004046AB    jge short loc_4046BF
```

to 

```asm
004046AB    jmp short loc_4046BF
```

so that `_vbaHresultCheckObj` would never be called.

After that, restart this player again and play a song. One minuate later you will see the flag on title: __LIstenCare__
