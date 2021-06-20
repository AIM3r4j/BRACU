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

mov bx, 080h    ;setting bx to 80h ascii char
mov cl, 0       ;counter as 0


start: 
cmp bx, 0ffh
je finish

mov ah, 2
mov dx, bx
int 21h
mov ah,2
mov dx,' '
int 21h
inc cl

cmp cl,10
je newline
inc bx
jmp start


newline:
mov cl,0
inc bx
jmp start


finish:




;exit to DOS 
   
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN