.MODEL SMALL

.STACK 100H

.DATA 

;variables
s1 db "Please enter the first number for multiplication: $"
s2 db 0dh,0ah,"Please enter the second number for multiplication: $"
s3 db 0dh,0ah,"Product: $"

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 

; enter your code here 

;taking first input
lea dx,s1
mov ah,9
int 21h
mov ah, 1
int 21h   
sub al, 48
mov bl, al

;taking second input
lea dx,s2
mov ah,9
int 21h
mov ah, 1
int 21h
sub al, 48
mov cl, al


start: 
dec cl
cmp cl, 0       ;checking when counter gets to 0
je finish
add bl,bl       ;adding M to product
jmp start

finish:
mov cl,bl        ;saving the product in cl


;exit to DOS 
       
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN 
