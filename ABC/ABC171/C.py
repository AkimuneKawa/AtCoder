N = int(input())

def get_name(N):

    alphabets = [chr(i) for i in range(97, 97+26)]
    length = len(alphabets)

    shou = (N - 1) // length
    amari = N % length

    if N <= 26:
        return alphabets[amari-1]
    else:
        return get_name(shou) + get_name(amari)

print(get_name(N))