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

    mov ax,07fh
    mov bx,07fh
    add ax,bx
    
    ;Here,as both of them are signed positive numbers..
    ;therefore, if the MSB gets a carry in, the result should be a positive number.
    ;So even if there is an overflow bit, it will be discarded.
    ;because the result will be a negative number if the carry out overflow
    ;bit is counted
    ;this is only for signed overflow
    
    

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



