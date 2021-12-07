"""
09. front_x
Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.
Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']
Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""

def front_x_01(words):
    # +++ SUA SOLUÇÃO +++
    lista_a = []
    lista_b = []
    for word in words:
      if word[0] == 'x':
        lista_a.append(word)
      else:
        lista_b.append(word)
    #lista_a.sort()
    #lista_b.sort()
    #resultado = ''.join([lista_a, lista_b])
    #return resultado
    #return lista_a + lista_b
    return sorted(lista_a) + sorted(lista_b)

def front_x(words):
  lista_x = sorted([word for word in words if word[0] == 'x'])
  lista_r = sorted([word for word in words if word[0] != 'x'])
  return lista_x + lista_r
    

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])