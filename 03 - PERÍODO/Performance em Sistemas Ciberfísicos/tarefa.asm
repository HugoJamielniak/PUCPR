inicio:
mov eax, 8
mov ebx, 10
mov ecx, 9
mov edx, 8
mov esi, 0

condicao1:
cmp eax, ebx
jz condicao1b
jmp condicao2

condicao1b:
add esi, 1
jmp fim



condicao2:
cmp eax, ecx
jz condicao2b
jmp condicao3

condicao2b:
add esi, 2
jmp fim



condicao3:
cmp eax, edx
jz condicao3b
jmp condicao4

condicao3b:
add esi, 3
jmp fim


condicao4:
add esi, 4
jmp fim

fim:
