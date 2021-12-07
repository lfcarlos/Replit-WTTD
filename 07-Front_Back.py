"""
07. front_back
Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.
Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.
Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back_1(a, b):
    # +++ SUA SOLUÇÃO +++
  if len(a) % 2 == 0:
    a_frente = a[:len(a)//2]
    a_tras = a[len(a)//2:]
    print(a_frente, a_tras)
  else:
    a_frente = a[:len(a)//2+1]
    a_tras = a[len(a)//2+1:]
    print(a_frente, a_tras)
  
  if len(b) % 2 == 0:
    b_frente = b[:len(b)//2]
    b_tras = b[len(b)//2:]
    print(b_frente, b_tras)
  else:
    b_frente = b[:len(b)//2+1]
    b_tras = b[len(b)//2+1:]
    print(b_frente, b_tras)
  
  return a_frente + b_frente + a_tras + b_tras

import math
def front_back(a, b):
    return ''.join([a[:(math.ceil(len(a) / 2))],b[:(math.ceil(len(b) / 2))],a[(math.ceil(len(a) / 2)):], b[(math.ceil(len(b) / 2)):]])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')