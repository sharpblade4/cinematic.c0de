; The Terminator - 37:19 
;     Source: https://a2central.com/1050/key-perfect-now-available-for-free-from-nibble/

INSTALL      LDY#10
]LOOP        LDA VCT,Y
             STA PG3VEC,Y
             DEY
             BPL[LOOP
             LDA S3F3
             EOR #SA5
             STA S3F4

       ; and aux mem

             LDA #PG3VEC/
             LDY #PG3VEC
             STA A1H
             STA A4H
             STY A1L
             STY A4L
             LDA #PG3VEC+10/
             LDY #PG3VEC+10
             STA A2H
             STY A2L
             SEC
             JSR AUXMOVE

        ; Copy program to aux memory

             LDA #BEGIN/
             LDY #BEGIN
             STA A1H
             STA A4H
             STY A1L
             STY A4L
             LDA #END/
             LDY #END
