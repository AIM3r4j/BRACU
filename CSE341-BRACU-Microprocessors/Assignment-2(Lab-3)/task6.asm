.MODEL SMALL
 
.STACK 100H

.DATA 

;variables 
    s db "ENTER THREE INITIALS: $"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here
    
    ;Printing the prompt
    lea dx, s
    mov ah, 9
    int 21h
    
    ;First intial input
    mov ah,1 
    int 21h
    mov bh , al
    
    ;Second intial input
    mov ah,1 
    int 21h
    mov bl , al        
    
    ;Third intial input
    mov ah,1 
    int 21h
    mov cl, al
    
    ;Printing the initials in new lines
    mov dl, 0ah
    mov ah , 2
    int 21h
    mov dL,0dh 
    int 21h 
    mov dL,0ah 
    int 21h 
    
    mov dl,bh
    mov ah,2
    int 21h
    
    mov dl, 0ah
    mov ah , 2
    int 21h
    mov dL,0dh 
    int 21h 
    mov dL,0ah 
    int 21h 
    
    mov dl,bl
    mov ah,2
    int 21h 
    
    mov dl, 0ah
    mov ah , 2
    int 21h
    mov dL,0dh
    int 21h 
    mov dL,0ah 
    int 21h 
    
    mov dl,cl
    mov ah,2
    int 21h




 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



