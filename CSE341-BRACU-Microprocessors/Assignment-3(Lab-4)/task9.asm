.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter a number: $"
a db 0ah,0dh,'Yes$'
b db 0ah,0dh,'No$'
f db 5
e db 11

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts for char input
lea dx,s
mov ah,9
int 21h
      
;takes input
mov ah,1
int 21h
mov bl,al

;checks if divisible by 5
div f
cmp al,0
je line1
jmp exit


;gets here if divisible by 5 and check if divisible by 11
line1:
mov al,bl
div e
cmp ah,0
je line2
jmp exit
        
;gets here if divisible by 11
line2:
lea dx,a
mov ah,9
int 21h 

;gets here if not divisible by 5 and 11
exit:
lea dx,b
mov ah,9
int 21h 



;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 