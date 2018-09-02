# Reversing.kr -- CSHOP

## 1. Challenge

Just a exe file `CSHOP.exe`.

Please goto [http://reversing.kr/challenge.php](http://reversing.kr/challenge.php) to download.

## 2. Solution

Drop it into .NET Reflector and go to see `FrmMain`.

You will see there is a button click handler. However you cannot see a button after you open `CSHOP.exe`.

So let's go to see function `FrmMain.InitializeComponent()` and find out how buttons are created.

You will see a button named `btnStart` is created, but its size is (0, 0) which means you cannot see it.

However, we can use __TAB__ to set foucus on this button and type __ENTER__ to trigger `Click` event. After that you will see the flag: `P4W6RP6SES`
