import random
import time

A = 12345
B = 6789

def extended_euclidean_algo(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

def inverse_mod(n, p):
    gcd, x, _ = extended_euclidean_algo(n, p)
    if gcd != 1:
        raise ValueError("Обратного элемента не существует")
    return x % p

def add_points(P, Q, p):
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    if P[0] == Q[0] and P[1] != Q[1]:
        return (0, 0)
    
    if P == Q:
        m = (3 * P[0]**2 + A) * inverse_mod(2 * P[1], p) % p
    else:
        m = (P[1] - Q[1]) * inverse_mod(P[0] - Q[0], p) % p
    
    x = (m**2 - 2 * P[0]) % p
    y = (P[1] + m * (x - P[0])) % p
    return (x, -y % p)

def find_point_order(point, p):
    order = 1
    current = add_points(point, point, p)
    while current != (0, 0):
        current = add_points(current, point, p)
        order += 1
    return order

def elliptic_curve(x, y, p):
    return (y ** 2) % p == (x ** 3 + A * x + B) % p

def print_curve(p):
    print(f"y^2 = x^3 + {A} * x + {B} (% {p})")

def main():
    p = 35573

    assert (4 * A**3 + 27 * B**2) % p != 0, "Кривая сингулярна"

    print_curve(p)

    start_time = time.time()
    points = []
    for x in range(p):
        for y in range(p):
            if elliptic_curve(x, y, p):
                points.append((x, y))

    print("Нахождение точек кривой", time.time() - start_time)

    curve_order = len(points)
    print(f"Порядок кривой = {curve_order}")
    point = random.choice(points)

    timee = time.time()

    print(f"Точка: {point}, порядок: {find_point_order(point, p)}")
    print(f"Время вычисления: {time.time() - start_time:.2f} сек")

    print("Чисто нахождение порядка:", time.time() - timee)

if __name__ == '__main__':
    main()