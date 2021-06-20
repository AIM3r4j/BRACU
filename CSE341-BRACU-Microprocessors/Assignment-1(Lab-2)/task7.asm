;X * Y 
mov al , 3
mov bl , 4
mul bl
          
;X / Y 
mov al , 6
mov bl , 2 
div bl

;X * Y / Z 
mov al , 3
mov bl , 4

mul bl 

mov ax , al
mov bl , 5 

div bl 