.MODEL SMALL
 
.STACK 100H

.DATA 

;variables

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;setting counter as 0
mov cl , 0
 
mov ah , 2
mov dl , '*'
  
  
start: 
cmp cl , 80   ;checking if counter reached 80
je finish
int 21h    ;printing *
inc cl     ;incrementing counter
jmp start

    
finish:




 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN