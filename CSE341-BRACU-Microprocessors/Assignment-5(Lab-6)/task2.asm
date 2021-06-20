.MODEL SMALL
 
.STACK 100H

.DATA 

;variables 
a db 5 dup(?)
s db 0ah,0dh,"Enter five numbers one after another: $"
ans db 0ah,0dh,"Sorted: $"
.CODE 
MAIN PROC 

;initialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

;Prompt for number
lea dx,s
mov ah,9
int 21h


;taking input
mov ah,1
mov si,0
mov cx,5
input:
    int 21h
    mov bh,al
    mov a[si],bh
    inc si
    loop input

;sorting
mov bx,0
mov si,1
mov ch,0   ;sort count
sort:
    mov al,a[bx]
    mov cl,a[si]
    cmp al,cl
    jg swap
    inc bx
    inc si
    cmp bx,4
    jne sort
    inc ch
    cmp ch,5
    je next
    mov bx,0
    mov si,1
    jmp sort
        
    swap:                   ;swaps the two numbers if n1>n2
        mov a[si],al
        mov a[bx],cl
        jmp sort
        
        

;next line
next:  
lea dx,ans
mov ah,9
int 21h

;printing the name
mov ah,2
mov si,0
mov cx,5
print:
    mov dl,a[si]
    int 21h
    inc si
    loop print
  
;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
END MAIN