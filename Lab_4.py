import sys
import math
def get_coef(*,index:int, prompt:str):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    try:
        coef = float(coef_str)
    except:
        isCorrect = False
        while True:
            try:
                isCorrect = True
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
            except:
                isCorrect = False
            if isCorrect:
                break
    return coef
def get_simple_kv_roots(coefficient):
    result =[]
    if coefficient > 0:
        result.append(math.sqrt(coefficient))
        result.append(-math.sqrt(coefficient))
    if coefficient == 0:
        result.append(0)
    return result
def get_roots_bikv(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        bikv_root = -b/(2.0*a)
        result += get_simple_kv_roots(coefficient=bikv_root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        bikv_root1 = (-b + sqD) / (2.0*a)
        bikv_root2 = (-b - sqD) / (2.0*a)
        result += get_simple_kv_roots(coefficient=bikv_root1)
        result += get_simple_kv_roots(coefficient=bikv_root2)
    return result
def print_roots(roots):
    len_roots = len(roots)
    if not len_roots:
        print('Нет корней')
        return
    print(f'Корней {len_roots}.')
    for i in range(len_roots):
        print(f'Корень номер {i+1} равен {roots[i]}')
def main():
    a = get_coef(index=1, prompt='Введите коэффициент А:')
    b = get_coef(index=2, prompt='Введите коэффициент B:')
    c = get_coef(index=3, prompt='Введите коэффициент C:')
    print_roots(get_roots_bikv(a,b,c))
if __name__ == "__main__":
    main()
