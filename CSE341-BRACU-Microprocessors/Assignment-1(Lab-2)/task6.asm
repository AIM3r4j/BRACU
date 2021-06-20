;A=B-A 
mov ax , 3
mov bx , 4                                     
mov cx , 5
sub bx, ax
mov ax, bx
   
;A=-(A+1) 
add ax , 1
neg ax

;C=A+(B+1);use inc   
mov ax , 3
mov bx , 4
mov cx , 5
inc bx
add ax , bx
mov cx, ax  
   
;A=B-(A-1);use dec
mov ax , 3
mov bx , 4
mov cx , 5
dec ax
sub bx , ax
mov ax , bx