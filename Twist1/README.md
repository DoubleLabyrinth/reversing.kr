# Reversing.kr -- Twist1

## 1. Challenge

Just 2 files `Twist1.exe` and `ReadMe.txt`:

> Twist1.exe is run in x86 windows.

## 2. Solution

Since `ReadMe.txt` has said that it should be run in x86 Windows, I drop it into Windows XP virual machine.

This challenge is very disgusting. You have to debug this program step by step. Here I give you some hints:

  1. You can use `attach` method to debug this program for this program has anti-debug when initializing.

  2. At `twist1.00407294`, the program called `ZwQueryInformationProcess` while `ProcessInformationClass = ProcessDebugPort`. You must set the buffer where the result is stored to zero after this call returned.

  3. At `twist1.004072BF`, the program called `ZwQueryInformationProcess` again while `ProcessInformationClass = ProcessDebugObjectHandle`. But this time, it checked return value and return value should be `0xC0000353`. You must set `eax = 0xc0000353` after this call returned.

  4. At `twist1.004072BF`, the program called `ZwQueryInformationProcess` again while `ProcessInformationClass = ProcessDebugFlags`. You must set the buffer where the result is stored to 1 after this call returned.

  5. From `twist1.004075C4` to `twist1.004075Fa`, the program checked registers from `DR0` to `DR7`. If you have not set hardware breakpoints, you do not need to care about them.

The flag is __RIBENA__
