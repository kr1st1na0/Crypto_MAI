import math
import time
from sympy import isprime, factorint

def read_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file if line.strip()]
    return numbers

def gcd(n, numbers):
    for m in numbers:
        d = math.gcd(n, m)
        if 1 < d < n:
            return d
    return None 

def factorize(n, numbers):
    if isprime(n):
        return [n]
    d = gcd(n, numbers)
    if d is None:
        raise ValueError("Делители не были найдены")
    return factorize(d, numbers) + factorize(n // d, numbers)

def print_results(factors, start_time):
    for i, factor in enumerate(factors, 1):
        print(f"делитель_{i} = {factor}")
        # print(isprime(factor))
    print(f"Затраченное время: {(time.time() - start_time):.6f} секунд")

def main():
    a = 74824937442907644295447904672755907842966347185456200207511741852189014011791
    print("Число a простое:", isprime(a))
    print("Факторизация числа a =", a)

    print("\n-С использованием factorint из sumpy:")
    start_time = time.time()
    factors = factorint(a)
    print_results(factors, start_time)

    print("\n-С использованием НОД:")
    a_filename = "a_numbers.txt"
    a_numbers = read_from_file(a_filename)
    start_time = time.time()
    a_factors = factorize(a, a_numbers)
    print_results(a_factors, start_time)
    print("Проверка a == делитель_1 * делитель_2:", a == a_factors[0] * a_factors[1])

    print("_________________________________________\n")

    b = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088153086249419559718052131324767711886673879844433992185285976186206340313183340137864755107892990120576580413399428088195869109036509736457212250441125434177525335001187530188218311657731855730123657446894274587405502726816767124723352811243072600265824682176283556416804961236941300520689054546642102638901234155400995358178915906382875255568849558104166115836357997125293994556137842600090153653134581721878743761264181745746251017544787820640271803922422107354962879880541
    print("Число b простое:", isprime(b))
    print("Факторизация числа b =", b, "\n")
    
    b_filename = "b_numbers.txt"
    b_numbers = read_from_file(b_filename)
    start_time = time.time()
    b_factors = factorize(b, b_numbers)
    print_results(b_factors, start_time)
    print("Проверка b == делитель_1 * делитель_2:", b == b_factors[0] * b_factors[1])
    

if __name__ == '__main__':
    main()