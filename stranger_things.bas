01 REM  Stanger Things - S02E08 16:00
02 REM  -----------------------------
10 DIM FourDigitPassword INTEGER
20 FOR i = 0 TO 9
30     FOR j = 0 TO 9
40         FOR k = 0 TO 9
50             FOR l = 0 TO 9
60                 FourDigitPassword = getFourDigits (i,j,k,l)
70                 IF checkPasswordMatch(FourDigitPassword) = TRUE THEN
80                     GOTO 140
90                 END
100            NEXT l
110        NEXT k
120    NEXT j
130 NEXT i
140 PRINT FourDigitPassword
150 END
