.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s1 db "Enter name length: $"
s2 db 0ah,0dh,"Enter name: $" 
a db 10 dup(?)

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;Prompt for length
lea dx,s1
mov ah,9
int 21h

;taking length input
mov ah,1
int 21h
mov cl,al

;prompt for name
lea dx,s2
mov ah,9
int 21h

;taking name input
mov ah,1
mov si,0
mov bl,30h
input:
    int 21h
    mov bh,al
    mov a[si],bh
    inc si
    inc bl
    cmp cl,bl
    jne input

;next line  
mov ah,2
mov dl,0ah
int 21h

mov dl,0dh
int 21h

;printing the name
mov si,0
mov bl,30h
print:
    mov dl,a[si]
    int 21h
    inc si
    inc bl
    cmp cl,bl
    jne print
  
;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN