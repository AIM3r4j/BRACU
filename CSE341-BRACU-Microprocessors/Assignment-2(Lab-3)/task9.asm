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
    mov al,080h
    mov bl,080h
    add al,bl
 
    ;Status Flags
  
    ; Zero Flag= 1 
    ; Carry Flag= 1
    ; Parity Flag= 1 
    ; Overflow Flag= 1
    ; Sign Flag= 0
    ; Auxilary Flag= 0 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



