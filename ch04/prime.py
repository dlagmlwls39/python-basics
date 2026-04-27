   
def is_prime(list):
    result = []

    for n in list:
        flag = True
        for i in range(2, int(n**0.5) + 1):  # 제곱근
            if n % i == 0:
                flag = False

        if (flag == True):        
            result.append(n)

    return result

if __name__ == "__main__":
    L = list(range(2, 31))
    
    result = is_prime(L)
    print(result)
