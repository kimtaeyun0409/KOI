def gcd(a, b):  # a와 b의 최대공약수를 구하는 함수
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):  # a와 b의 최소공배수를 구하는 함수
    return a * b // gcd(a, b)
print(lcm(6, 4.8))