.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter a number: $"
a db 0ah,0dh,'Odd$'
b db 0ah,0dh,'Even$'

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts to enter a number
lea dx,s
mov ah,9
int 21h

;takes a input
mov ah,1
int 21h
mov bl,al           

;checks if it's even
and bl,01h
jz even

;carries on if odd
lea dx,a
mov ah,9
int 21h
jmp exit


;gets here if it's even
even:
lea dx,b
mov ah,9
int 21h



exit:


;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



