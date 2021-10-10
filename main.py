def printMenu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2.")
    print("4. Iesire")

def citireLista():
    l = []
    stringCitit = input("Dati lista: ")
    numere = stringCitit.split(",")
    for x in numere:
        l.append(int(x))
    return l

def is_prime(n):
    """
    input:
      n - numarul dat
    output:
      True  - n este un numar prim
      False - n nu este un numar prim
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def toate_numerele_prime(n):
    """
    verfica daca toate numerele sunt prime
    input:
      n - lista de nr intregi
    output:
      return: True, daca toate elementele din lista sunt prime, False in caz contrar
    """
    for x in n:
        if is_prime(x) == 0:
            return False
    return True
def test_toate_numerele_prime():
    assert([2, 3, 5]) is True
    assert([1, 4]) is False

def get_longest_all_primes(l):
    """
    determina una din cele mai lungi subsecvente de nr prime
    :param l: lista de nr intregi
    :return: una din subsecventele maxime de nr prime
    """
    rez=[]
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if(toate_numerele_prime(l[i:j+1]) and len(l[i:j+1]) > len(rez)):
                rez = l[i:j+1]
    return rez

def test_get_longest_all_primes():
    assert get_longest_all_primes([3, 5, 8]) == [3, 5]
    assert get_longest_all_primes([1,4,5]) == [5]

def toate_cifrele_prime(n):
    """
    verifica daca toate cifrele numarului n sunt prime
    :param n: numarul n
    :return: True, in cazul in care toate cifrele numarului sunt prime, False in caz contrar
    """
    while n:
        if is_prime(n % 10) == 0:
            return False
        n = n // 10
    return True
def nr_liste_prime(l):
    """
    verifica daca toate numerele indeplinesc conditia ca toate cifrele sunt prime
    :param l: lista de numere
    :return: True, in caz ca toate numerele au toate cifrele prime, False in caz contrar
    """
    for x in l:
        if(toate_cifrele_prime(x) == 0):
            return False
    return True
def get_longest_prime_digits(l):
    """
    determina una dintre cele mai lungi subsecvente de numere cu toate cifrele prime
    :param l: lista de nr.
    :return: una din subsecventele maxime cu numerele avand toate cifrele prime
    """
    lista = []
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if (nr_liste_prime(l[i:j+1]) and len(l[i:j+1]) > len(lista)):
                lista = l[i:j+1]
    return lista

def test_get_longest_prime_digits():
    assert (get_longest_prime_digits([2, 55, 4])) == [2, 55]
    assert (get_longest_prime_digits([4, 6, 8])) == []

def main():
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea")
        if optiune == '1':
            l = citireLista()
        elif optiune == '2':
            print(get_longest_all_primes(l))
        elif optiune == '3':
            print(get_longest_prime_digits(l))
        else:
            break
if __name__ == '__main__':
    main()