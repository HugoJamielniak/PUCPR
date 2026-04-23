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
# Altere a funcao para fazer uso da tecnica de mapeamento associativo


tabelaMapeamento =[ -1 for _ in range(0, 7)]

def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global tabelaMapeamento
    # TIRA ISSO AQUI -> global indice

    # o índice não pode ser global, pq dai ao inves dele ser aleatorio
    # vc vai aleatorizar ele uma única vez e usar o mesmo numero sempre
    indice = random.randint(0, 7)

    paginaRequisitada = endereco >> 2
    BtyeRequisitado = endereco & 3


    print("Pagina requisitada:", paginaRequisitada)
    print("Byth requisitado:", BtyeRequisitado)
    print("tabela de mapeamento", tabelaMapeamento)
    print("valor", indice)

    if not paginaRequisitada in tabelaMapeamento:
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        memoriaPrincipal.setPagina(pagina, indice)
        tabelaMapeamento[indice] = paginaRequisitada
        return indice
    else:
        for i in range(0, len(tabelaMapeamento)):
            if paginaRequisitada == tabelaMapeamento[i]:
                return i

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
                               funcaoMapeamento=mapeamentoAssociativo,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativo, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

