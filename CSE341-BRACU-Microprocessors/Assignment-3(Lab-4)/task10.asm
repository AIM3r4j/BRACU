.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s1 db "Enter first number: $"
s2 db 0ah,0dh,'Enter second number: $'
s3 db 0ah,0dh,'Enter third number: $'
m db 0ah,0dh,'Maximum number is $'
n db 0ah,0dh,'Minimum number is $'
max db 0
min db 0

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts for three numbers and take three inputs
lea dx,s1
mov ah,9
int 21h

mov ah,1
int 21h
mov max,al
       
lea dx,s2
mov ah,9
int 21h

mov ah,1
int 21h
mov min,al

lea dx,s3
mov ah,9
int 21h

mov ah,1
int 21h
mov bl,al

;checks if n1>n2 and goes to line1 if true
mov al,min
cmp max,al
jg line1
  
;gets here if n1<n2
mov cl,max
mov al,min
mov max,al
mov min,cl

;checks if n1<n3 and goes to line2 if true 
line1:
cmp max,bl
jl line2

;gets here if n1>n3 and checks if n2<n3
cmp min,bl
jl exit

;gets here if n2>n3
mov min,bl
jmp exit

;gets here if n1<n3
line2:
mov max,bl

;prints the output
exit:
lea dx,m
mov ah,9
int 21h
mov dl,max
mov ah,2
int 21h


lea dx,n
mov ah,9
int 21h
mov dl,min
mov ah,2
int 21h




;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN