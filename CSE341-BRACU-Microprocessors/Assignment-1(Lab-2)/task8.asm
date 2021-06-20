;236DF * AF
;This is not possible

;8A32F4D5 / C9A5
;This is also not possible

;CA92 * BAF9
mov ax, 0CA92h
mov bx, 0BAF9h
mul bx

;C2A2 * ABCD / BED
mov ax, 0C2A2h
mov bx, 0ABCDh
mul bx
mov cx, 0BEDh
div cx