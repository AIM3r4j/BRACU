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

    ;Taking input of Uppercase letter
    mov ah,1
    int 21h
    mov cl , al
    
    ;Next line without carriage return
    mov dl, 0ah
    mov ah , 2
    int 21h  
    
    ;To lowercase
    mov bl, cl
    add bl, 32
    
    ;Printing on the next position    
    mov dl,bl 
    mov ah,2  
    int 21h

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 