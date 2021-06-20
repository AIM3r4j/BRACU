.MODEL SMALL
 
.STACK 100H

.DATA 

;variables
s db "Please enter a digit: $"
i db 0ah,0dh,'i$'
k db 0ah,0dh,'k$'
l db 0ah,0dh,'l$'
m db 0ah,0dh,'m$'

.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here
;Prompt and Taking the digit input
lea dx,s
mov ah,9
int 21h
mov ah,1
int 21h
mov cl,al

;checking if n>=0
cmp al,30h
jge line1
jmp exit

;checking if n<=3
line1:
cmp cl,33h
jle io          

;checking if n>=4
cmp cl,34h
jge line2

;checking if n<=6
line2:
cmp cl,36h
jle ko

;checking if n>=7
cmp cl,37h
jge line3

;checking if n<=9
line3:
cmp cl,39h
jle lo

;prints m as n=10
lea dx,m
mov ah,9
int 21h
jmp exit


io:
lea dx,i
mov ah,9
int 21h
jmp exit

ko:
lea dx,k
mov ah,9
int 21h
jmp exit 

lo:
lea dx,l
mov ah,9
int 21h
jmp exit

exit:




 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



