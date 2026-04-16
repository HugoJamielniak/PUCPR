import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso de todos enderecos na memoria principal
#    tente otimizar o seu mecanismo de mapeamento
#    tente otimizar o seu mecanismo de substituicao


tabelaMapeamento =[ -1 for _ in range(0, 8)]
indice = 0


def mapeamentoCustomizado(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global tabelaMapeamento
    global indice

    paginaRequisitada = endereco >> 2
    BtyeRequisitado = endereco & 3


    print("Pagina requisitada:", paginaRequisitada)
    print("Byth requisitado:", BtyeRequisitado)
    print("tabela de mapeamento", tabelaMapeamento)

    #verifica se ja mapeou
    if not paginaRequisitada in tabelaMapeamento:
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        memoriaPrincipal.setPagina(pagina, indice)
        tabelaMapeamento[indice] = paginaRequisitada
        indice = indice + 1
        return indice - 1
    else:
        for i in range(0, len(tabelaMapeamento)):
            if paginaRequisitada == tabelaMapeamento[i]:
                return i
    #retorna endereco
    return 0

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoCustomizado,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=300, 
                               nPaginasMemoriaPrincipal=128, 
                               nPaginasMemoriaSecundaria=512, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoCustomizado, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

