import sys
import math
class BiquadrateRoots:
    def __init__(self):
        self.coef_a = 0.0
        self.coef_b = 0.0
        self.coef_c = 0.0
        self.roots_list = []
    def get_coef(self, *, index:int, prompt:str)->float:
            coef = 0
            try:
                coef_str = sys.argv[index]
            except:
                print(prompt)
                coef_str = input()
            try:
                coef = float(coef_str)
            except:
                is_correct = False
                while True:
                    try:
                        is_correct = True
                        print(prompt)
                        coef_str = input()
                        coef = float(coef_str)
                    except:
                        is_correct = False
                    if is_correct:
                        break
            return coef
    def get_coefs(self)->None:
        self.coef_a = self.get_coef(index=1, prompt='Введите коэффициент А:')
        self.coef_b = self.get_coef(index=2, prompt='Введите коэффициент B:')
        self.coef_c = self.get_coef(index=3, prompt='Введите коэффициент C:')

    def get_simple_kv_roots(self, *, coefficient)->list:
            result = []
            if coefficient > 0:
                result.append(math.sqrt(coefficient))
                result.append(-math.sqrt(coefficient))
            if coefficient == 0:
                result.append(0)
            return result
    def get_roots_bikv(self)->None:
            d = self.coef_b * self.coef_b - 4 * self.coef_a * self.coef_c
            if d == 0.0:
                bikv_root = -self.coef_b / (2.0 * self.coef_a)
                self.roots_list += self.get_simple_kv_roots(coefficient=bikv_root)
            elif d > 0.0:
                sq_d = math.sqrt(d)
                bikv_root1 = (-self.coef_b + sq_d) / (2.0 * self.coef_a)
                bikv_root2 = (-self.coef_b - sq_d) / (2.0 * self.coef_a)
                self.roots_list += self.get_simple_kv_roots(coefficient=bikv_root1)
                self.roots_list += self.get_simple_kv_roots(coefficient=bikv_root2)
    def print_roots(self)->None:
            len_roots = len(self.roots_list)
            if not len_roots:
                print('Нет корней')
                return
            print(f'Корней {len_roots}.')
            for i in range(len_roots):
                print(f'Корень номер {i + 1} равен {self.roots_list[i]}')

def main():
    equation = BiquadrateRoots()
    equation.get_coefs()
    equation.get_roots_bikv()
    equation.print_roots()
if __name__ == "__main__":
    main()
