def sumOfDigits(num):
    numlist = map(int, list(num))
    return sum(numlist)
    
if __name__ == "__main__":
    print(sumOfDigits(input()))
