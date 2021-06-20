.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
    s db '**********',0dh,0ah,'$'

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here
    
    lea dx, s
    mov ah, 9
    
    ;Displaying string 10 times
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    
;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



