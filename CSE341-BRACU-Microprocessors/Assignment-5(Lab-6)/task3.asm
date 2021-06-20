.MODEL SMALL
 
.STACK 100H

.DATA 

;variables 
a db 3 dup(?)
s1 db "Enter first number: $"
s2 db 0ah,0dh,'Enter second number: $'
s3 db 0ah,0dh,'Enter third number: $'
m db 0ah,0dh,'Maximum number is $'
max db 0

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts for three numbers and takes three inputs
lea dx,s1
mov ah,9
int 21h

mov ah,1
int 21h
mov a[0],al

       
lea dx,s2
mov ah,9
int 21h

mov ah,1
int 21h
mov a[1],al


lea dx,s3
mov ah,9
int 21h

mov ah,1
int 21h
mov a[2],al

;sorting to get the maximum
mov bx,0
mov si,1
mov ch,0   ;sort count
sort:
    mov al,a[bx]
    mov cl,a[si]
    cmp al,cl
    jg swap
    inc bx
    inc si
    cmp bx,2
    jne sort
    inc ch
    cmp ch,2
    je print
    mov bx,0
    mov si,1
    jmp sort
        
    swap:                   ;swaps the two numbers if n1>n2
        mov a[si],al
        mov a[bx],cl
        jmp sort 

print:
lea dx,m
mov ah,9
int 21h
mov dl,a[2]  ;max number is in the last index
mov ah,2
int 21h



;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN