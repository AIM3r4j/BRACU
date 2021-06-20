.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter an alphabet: $"
v db 0ah,0dh,'Vowel$'
c db 0ah,0dh,'Consonant$'

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;prompts to enter an alphabet
lea dx,s
mov ah,9
int 21h

;takes an input
mov ah,1
int 21h
mov bl,al           

;checks if it's a vowel
cmp bl,"a"
je vowel
cmp bl,"e"
je vowel
cmp bl,"i"
je vowel
cmp bl,"o"
je vowel
cmp bl,"u"
je vowel
cmp bl,"A"
je vowel
cmp bl,"E"
je vowel
cmp bl,"I"
je vowel
cmp bl,"O"
je vowel
cmp bl,"U"
je vowel


;carries on if it's a consonant
lea dx,c
mov ah,9
int 21h
jmp exit


;gets here if it's a vowel
vowel:
lea dx,v
mov ah,9
int 21h


exit:
 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



