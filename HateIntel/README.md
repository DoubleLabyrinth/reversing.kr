# Reversing.kr -- HateIntel

## 1. Challenge

Just a Mach-O file and a `ReadMe`:

> Reversing.Kr
> 
> Find The Password
> 
> By ezbeat

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Drop it into IDA, and search strings. You will find there are `"Input key: "`, `"Wrong Key! "` and `"Correct Key! "`.

Look for the cross-reference and you will find that the strings are used in function `sub_2224`.

The following is what `sub_2224` did:

```cpp
int sub_2224() {
    char str[80];
    int len;

    printf("Input key : ");
    scanf("%s", str);

    len = strlen(str);
    
    sub_232C(str, 4);

    for (int i = 0; i < len; ++i) {
        if (str[i] != byte_3004[i]) {
            puts("Wrong Key! ");
            return 0;
        }
    }

    puts("Correct Key! ");
    return 0;
}
```

That means function `sub_232C` does something towards `str`.
So we have to go to see function `sub_232C`:

```cpp
void sub_232C(char* str, int shift) {
    for (int i = 0; i < shift; ++i) 
        for (int j = 0; j < strlen(str); ++j)
            str[j] = sub_2494(str[j], 1);
}
```

That means function `sub_2494` does something towards each chars in `str`.
So we have to go to see function `sub_2494`:

```cpp
unsigned char sub_2494(unsigned char c, int shift) {
    int tmp;

    tmp = c;
    for (int i = 0; i < shift; ++i) {
        tmp *= 2;
        if (tmp & 0x100)
            tmp |= 1;
    }
    return v3;
}
```

That means function `sub_2494` is equivalent to `__rorb`. 

So we just rotating shift each chars in `byte_3004` left by 4 bits and we will get the flag.

```bash
$ gcc show_pass.c -o show_pass
$ ./show_pass
```
