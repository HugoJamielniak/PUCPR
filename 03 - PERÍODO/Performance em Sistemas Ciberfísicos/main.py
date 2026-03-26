import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

# memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
# memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
# memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')


# memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    if instrucao == 0x40:
        print('MOV Reg, Byte')
        return instrucao

    if instrucao == 0x41:
        print('MOV Reg, Reg')
        return instrucao

    if instrucao == 0x00:
        print('ADD Reg, Byte')
        return instrucao

    if instrucao == 0x01:
        print('ADD Reg, Reg')
        return instrucao

    if instrucao == 0x10:
        print('INC reg')
        return instrucao

    if instrucao == 0x20:
        print('DEC reg')
        return instrucao

    if instrucao == 0x30:
        print('SUB Reg, Byte')
        return instrucao

    if instrucao == 0x31:
        print('SUB Reg, Reg')
        return instrucao
    if instrucao == 0x50:
        print('JMP Byte')
        return instrucao

    if instrucao == 0x60:
        print('CMP Reg, Byte')
        return instrucao

    if instrucao == 0x61:
        print('CMP Reg, Reg')
        return instrucao

    if instrucao == 0x79:
        print('JZ Byte')
        return instrucao

    return -1


def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    print('Implementar a lerOperadoresExecutarInstrucao')

    #MOV REG BYTE
    if idInstrucao == 0x40:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            registrador_ax = operador2
        elif operador1 == 0x03:
            registrador_bx = operador2
        elif operador1 == 0x04:
            registrador_cx = operador2
        elif operador1 == 0x05:
            registrador_dx = operador2

    #ADD REG BYTE
    if idInstrucao == 0x00:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            registrador_ax += operador2
        elif operador1 == 0x03:
            registrador_bx += operador2
        elif operador1 == 0x04:
            registrador_cx += operador2
        elif operador1 == 0x04:
            registrador_dx += operador2

    #ADD REG REG
    if idInstrucao == 0x01:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02 and operador2 == 0x02:
            registrador_ax += registrador_ax
        elif operador1 == 0x02 and operador2 == 0x03:
            registrador_ax += registrador_bx
        elif operador1 == 0x02 and operador2 == 0x04:
            registrador_ax += registrador_cx
        elif operador1 == 0x02 and operador2 == 0x05:
            registrador_ax += registrador_dx

        if operador1 == 0x03 and operador2 == 0x02:
            registrador_bx += registrador_ax
        elif operador1 == 0x03 and operador2 == 0x03:
            registrador_bx += registrador_bx
        elif operador1 == 0x03 and operador2 == 0x04:
            registrador_bx += registrador_cx
        elif operador1 == 0x03 and operador2 == 0x05:
            registrador_bx += registrador_dx

        if operador1 == 0x04 and operador2 == 0x02:
            registrador_cx += registrador_ax
        elif operador1 == 0x04 and operador2 == 0x03:
            registrador_cx += registrador_bx
        elif operador1 == 0x04 and operador2 == 0x04:
            registrador_cx += registrador_cx
        elif operador1 == 0x04 and operador2 == 0x05:
            registrador_cx += registrador_dx

        if operador1 == 0x05 and operador2 == 0x02:
            registrador_dx += registrador_ax
        elif operador1 == 0x05 and operador2 == 0x03:
            registrador_dx += registrador_bx
        elif operador1 == 0x05 and operador2 == 0x04:
            registrador_dx += registrador_cx
        elif operador1 == 0x05 and operador2 == 0x05:
            registrador_dx += registrador_dx

    #INC REG
    if idInstrucao == 0x10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)

        if operador1 == 0x02:
            registrador_ax += 1
        elif operador1 == 0x03:
            registrador_bx += 1
        elif operador1 == 0x04:
            registrador_cx += 1
        elif operador1 == 0x04:
            registrador_dx += 1

    #DEC REG
    if idInstrucao == 0x20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)

        if operador1 == 0x02:
            registrador_ax -= 1
        elif operador1 == 0x03:
            registrador_bx -= 1
        elif operador1 == 0x04:
            registrador_cx -= 1
        elif operador1 == 0x04:
            registrador_dx -= 1

    #SUB REG BYTE
    if idInstrucao == 0x30:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            registrador_ax -= operador2
        elif operador1 == 0x03:
            registrador_bx -= operador2
        elif operador1 == 0x04:
            registrador_cx -= operador2
        elif operador1 == 0x04:
            registrador_dx -= operador2

    #SUB REG REG
    if idInstrucao == 0x31:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02 and operador2 == 0x02:
            registrador_ax -= registrador_ax
        elif operador1 == 0x02 and operador2 == 0x03:
            registrador_ax -= registrador_bx
        elif operador1 == 0x02 and operador2 == 0x04:
            registrador_ax -= registrador_cx
        elif operador1 == 0x02 and operador2 == 0x05:
            registrador_ax -= registrador_dx

        if operador1 == 0x03 and operador2 == 0x02:
            registrador_bx -= registrador_ax
        elif operador1 == 0x03 and operador2 == 0x03:
            registrador_bx -= registrador_bx
        elif operador1 == 0x03 and operador2 == 0x04:
            registrador_bx -= registrador_cx
        elif operador1 == 0x03 and operador2 == 0x05:
            registrador_bx -= registrador_dx

        if operador1 == 0x04 and operador2 == 0x02:
            registrador_cx -= registrador_ax
        elif operador1 == 0x04 and operador2 == 0x03:
            registrador_cx -= registrador_bx
        elif operador1 == 0x04 and operador2 == 0x04:
            registrador_cx -= registrador_cx
        elif operador1 == 0x04 and operador2 == 0x05:
            registrador_cx -= registrador_dx

        if operador1 == 0x05 and operador2 == 0x02:
            registrador_dx -= registrador_ax
        elif operador1 == 0x05 and operador2 == 0x03:
            registrador_dx -= registrador_bx
        elif operador1 == 0x05 and operador2 == 0x04:
            registrador_dx -= registrador_cx
        elif operador1 == 0x05 and operador2 == 0x05:
            registrador_dx -= registrador_dx

    #MOV REG REG
    if idInstrucao == 0x41:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02 and operador2 == 0x02:
            registrador_ax = registrador_ax
        elif operador1 == 0x02 and operador2 == 0x03:
            registrador_ax = registrador_bx
        elif operador1 == 0x02 and operador2 == 0x04:
            registrador_ax = registrador_cx
        elif operador1 == 0x02 and operador2 == 0x05:
            registrador_ax = registrador_dx

        if operador1 == 0x03 and operador2 == 0x02:
            registrador_bx = registrador_ax
        elif operador1 == 0x03 and operador2 == 0x03:
            registrador_bx = registrador_bx
        elif operador1 == 0x03 and operador2 == 0x04:
            registrador_bx = registrador_cx
        elif operador1 == 0x03 and operador2 == 0x05:
            registrador_bx = registrador_dx

        if operador1 == 0x04 and operador2 == 0x02:
            registrador_cx = registrador_ax
        elif operador1 == 0x04 and operador2 == 0x03:
            registrador_cx = registrador_bx
        elif operador1 == 0x04 and operador2 == 0x04:
            registrador_cx = registrador_cx
        elif operador1 == 0x04 and operador2 == 0x05:
            registrador_cx = registrador_dx

        if operador1 == 0x05 and operador2 == 0x02:
            registrador_dx = registrador_ax
        elif operador1 == 0x05 and operador2 == 0x03:
            registrador_dx = registrador_bx
        elif operador1 == 0x05 and operador2 == 0x04:
            registrador_dx = registrador_cx
        elif operador1 == 0x05 and operador2 == 0x05:
            registrador_dx = registrador_dx

    #JMP BYTE
    if idInstrucao == 0x50:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        registrador_cp = operador1

    #JZ BYTE
    if idInstrucao == 0x79:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if flag_zero:
            registrador_cp = operador1

    #CMP REG BYTE
    elif idInstrucao == 0x60:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            if registrador_ax == operador2:
                flag_zero = True

        elif operador1 == 0x03:
            if registrador_bx == operador2:
                flag_zero = True

        elif operador1 == 0x04:
            if registrador_cx == operador2:
                flag_zero = True

        elif operador1 == 0x05:
            if registrador_dx == operador2:
                flag_zero = True


    #CMP REG REG
    elif idInstrucao == 0x61:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        flag_zero = False

        if operador1 == 0x02:
            if operador2 == 0x02 and registrador_ax == registrador_ax:
                flag_zero = True
            elif operador2 == 0x03 and registrador_ax == registrador_bx:
                flag_zero = True
            elif operador2 == 0x04 and registrador_ax == registrador_cx:
                flag_zero = True
            elif operador2 == 0x05 and registrador_ax == registrador_dx:
                flag_zero = True

        elif operador1 == 0x03:
            if operador2 == 0x02 and registrador_bx == registrador_ax:
                flag_zero = True
            elif operador2 == 0x03 and registrador_bx == registrador_bx:
                flag_zero = True
            elif operador2 == 0x04 and registrador_bx == registrador_cx:
                flag_zero = True
            elif operador2 == 0x05 and registrador_bx == registrador_dx:
                flag_zero = True

        elif operador1 == 0x04:
            if operador2 == 0x02 and registrador_cx == registrador_ax:
                flag_zero = True
            elif operador2 == 0x03 and registrador_cx == registrador_bx:
                flag_zero = True
            elif operador2 == 0x04 and registrador_cx == registrador_cx:
                flag_zero = True
            elif operador2 == 0x05 and registrador_cx == registrador_dx:
                flag_zero = True

        elif operador1 == 0x05:
            if operador2 == 0x02 and registrador_dx == registrador_ax:
                flag_zero = True
            elif operador2 == 0x03 and registrador_dx == registrador_bx:
                flag_zero = True
            elif operador2 == 0x04 and registrador_dx == registrador_cx:
                flag_zero = True
            elif operador2 == 0x05 and registrador_dx == registrador_dx:
                flag_zero = True


def calcularProximaInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    print('Implementar a calcularProximaInstrucao')

    if idInstrucao == 0x40:
        registrador_cp += 3

    elif idInstrucao == 0x41:
        registrador_cp += 3

    elif idInstrucao == 0x00:
        registrador_cp += 3

    elif idInstrucao == 0x01:
        registrador_cp += 3

    elif idInstrucao == 0x10:
        registrador_cp += 2

    elif idInstrucao == 0x20:
        registrador_cp += 2

    elif idInstrucao == 0x30:
        registrador_cp += 3

    elif idInstrucao == 0x31:
        registrador_cp += 3

    elif idInstrucao == 0x60:
        registrador_cp += 3

    elif idInstrucao == 0x61:
        registrador_cp += 3

    elif idInstrucao == 0x79:
        registrador_cp += 2



def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')


if __name__ == '__main__':
    while (True):
        # Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        # ULA
        lerOperadoresExecutarInstrucao(idInstrucao)

        dumpRegistradores()

        # Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        # apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)