def solution(number, k):
    numbers = []
    
    for num in number:
        while numbers and k > 0 and numbers[-1] < num:
            numbers.pop()
            k -= 1
        numbers.append(num)
    
    if k > 0:
        numbers = numbers[:-k]
    
    return ''.join(numbers)
