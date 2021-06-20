.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
    a db "THE SUM OF $"
    b db " AND $"
    c db " IS $"


.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here
    
    ;Printing ?
    mov dl, 03fh     
    mov ah , 2
    INT 21h 
    
    ;First input
    mov ah,1
    int 21h
    mov cl , al
    mov bl, cl 
    
    ;Second input
    mov ah,1
    int 21h
    mov ch , al
    
    ;Summation
    mov dl , cl
    add cl, ch
    sub cl, 030h
     
    
    ;Printing result
    mov dl, 0ah
    mov ah , 2
    int 21h
    
    mov dl,0dh
    int 21h
    mov dl,0ah 
    int 21h
    
    lea dx, a
    mov ah, 9
    int 21h
    
    mov dl,bl
    mov ah,2
    int 21h
    
    lea dx, b
    mov ah, 9
    int 21h
    
    mov dl,ch
    mov ah,2
    int 21h 
    
    lea dx, c
    mov ah, 9
    int 21h
    
    
   
    mov dl,cl
    mov ah,2
    int 21h 




 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



