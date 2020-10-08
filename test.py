def evenNumber():
    numbers = [ i for i in range(1, 51)]
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return  result
