def is_prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        return num == 2
    
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
        
    return True

print(is_prime(17))  # True