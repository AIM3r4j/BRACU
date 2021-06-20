.MODEL SMALL
 
.STACK 100H

.DATA 

;variables            
    a db "Please Enter First Number:$"
    b db "Please Enter Second Number:$"
    c db "Summation of the numbers:$"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here  

;Performing Summation

    ;First Number
    lea dx, a
    mov ah, 9
    int 21h          
    
    
    mov ah,1 
    int 21h 
    mov bh , al  
    
    mov dl, 0ah
    mov ah,2 
    int 21h  
    mov dl, 13
    int 21h
    
    ;Second Number
    lea dx, b
    mov ah, 9
    int 21h           
    
    
    mov ah,1 
    int 21h 
    mov bl , al 
    
    
    sub bh , 030h
    sub bl , 030h   
    
    
    add bh , bl   
    add bh , 030h
    
    mov dl, 0ah
    mov ah,2 
    int 21h  
    mov dl, 13
    int 21h
              
    ;Creating a line gap between the result and input          
    mov dl,0dh
    int 21h 
    mov dl,0ah 
    int 21h 
    
    ;Printing the result
    lea dx, c
    mov ah, 9
    int 21h  
    
    mov dl,bh 
    mov ah,2  
    int 21h

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN