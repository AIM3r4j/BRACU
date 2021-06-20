.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter a five-character password: $"
x db 0dh,"XXXXX$"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts input and goes to next line
lea dx,s
mov ah,9
int 21h
mov dl, 0dh
mov ah,2
int 21h
mov dl, 0ah
mov ah,2
int 21h

;setting counter as 0
mov cl,0

start:
cmp cl,5
je print
mov ah,1
int 21h
inc cl
jmp start

;gets here after getting five char input and prints XXXXX
print:
lea dx,x
mov ah,9
int 21h


;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN