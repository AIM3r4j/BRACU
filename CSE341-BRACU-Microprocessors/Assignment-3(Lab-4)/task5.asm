.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter a character: $" 
a db 64
b db 91

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

;checks if it's ascii value greater than 64
cmp bl,a
jg line1
jmp exit


;gets here if greater than 64  and checks if less than 91
line1:
cmp bl,b
jl line2
jmp exit
        
;gets here if less than 91
line2:
mov dl,0ah
mov ah,2
int 21h
mov dl,0dh
mov ah,2
int 21h 
;prints the char
mov dl,bl
mov ah,2
int 21h

exit:


 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



