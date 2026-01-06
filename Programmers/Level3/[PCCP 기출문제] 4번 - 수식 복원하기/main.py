def solution(expressions):
    def dec2base(base, num):
        if num == 0:
            return 0
        
        val = []
        while num >= base:
            val.append(str(num % base))
            num //= base
        val.append(str(num))
        return int(''.join(val[::-1]))

    def convert(base, num_list):
        ret = 0
        power = 1
        for value in num_list:
            ret += value * power
            power *= base
        return ret
    
    def satisfied_number_base(base, expression):
        numA = list(map(int, list(expression[0])))[::-1]
        numB = list(map(int, list(expression[2])))[::-1]
        numC = list(map(int, list(expression[4])))[::-1]
        
        
        if any(num >= base for num in numA) or any(num >= base for num in numB) or any(num >= base for num in numC):
            return False
        
        converted_A = convert(base, numA)
        converted_B = convert(base, numB)
        converted_C = convert(base, numC)
        
        return converted_A - converted_B == converted_C if expression[1] == '-' else converted_A + converted_B == converted_C
    
    answer = []
    
    base_expressions = [expression.split(' ') for expression in expressions if expression[-1] != 'X']
    question_expressions = [expression.split(' ') for expression in expressions if expression[-1] == 'X']

    
    nomi = set()
    for number_system in range(2, 10):
        if all(satisfied_number_base(number_system, base_expression) for base_expression in base_expressions):
            nomi.add(number_system)
    
    
    for question_expression in question_expressions:
        numA = list(map(int, list(question_expression[0])))[::-1]
        numB = list(map(int, list(question_expression[2])))[::-1]
        maxx = max(max(numA), max(numB))
        nomi = {n for n in nomi if n > maxx}

    
    for question_expression in question_expressions:
        numA = list(map(int, list(question_expression[0])))[::-1]
        numB = list(map(int, list(question_expression[2])))[::-1]
        val = set()
        for base in nomi:
            converted_A = convert(base, numA)
            converted_B = convert(base, numB)
            
            if question_expression[1] == '-':
                calc = converted_A - converted_B
            else:
                calc = converted_A + converted_B
            
            val.add(dec2base(base, calc))
        
        if len(val) == 1:
            question_expression[-1] = str(list(val)[0])
        else:
            question_expression[-1] = '?'

        answer.append(' '.join(question_expression))
    
    return answer
