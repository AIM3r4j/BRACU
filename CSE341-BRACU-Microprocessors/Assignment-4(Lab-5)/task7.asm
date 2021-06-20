.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s1  db  'ENTER A STRING OF CAPITAL LETTERS: $'
s2  db  0dh,0ah,'THE LONGEST CONSECUTIVELY INCREASING STRING IS: $'

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompt
lea dx,s1
mov ah,9
int 21h


start:
;taking first input and checking if carriage entered directly
mov ah,1                     
int 21h
cmp al,0dh
je endinput


mov cl,1
mov bl,al
mov dh,al
mov ch,0
;taking next inputs
input:
    mov ah,1                     
    int 21h
    cmp al,0dh    ;checking if got carriage return
    je endinput
    
    inc bl
    cmp al,bl     ;checking if it's the next char in consecutively
    jne chainbreak
    
    inc cl
jmp input

chainbreak:
cmp ch,cl
jl update

mov cl,1
mov bl,al
mov dh,al
jmp input

update:
mov ch,cl
mov bh,dh
mov cl,1
mov bl,al
mov dh,al
jmp input

endinput:
cmp ch,cl
jl reupdate
jmp endinput2

reupdate:
mov ch,cl
mov bh,dh
jmp endinput2


endinput2:
lea dx,s2
mov ah,9
int 21h
mov ah,2
mov dl,bh

print:
cmp ch,0
je exit

dec ch
int 21h
inc dl
jmp print

exit:



;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN