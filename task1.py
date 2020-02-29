def phones_fixer(func):
    def wrapper(nlist):
        for x in range(len(nlist)):
            element = nlist[x]
            ln = len(element)
            nlist[x] = str('+91 ' + element[ln - 10:ln - 5] + ' ' + element[ln - 5:ln])
        print(nlist)
        return func(nlist)

    return wrapper


@phones_fixer
def sort_numbers(number_list):
    return '\n'.join(sorted(number_list))


def read_numbers():
    n = int(input())
    numbers = []
    for i in range(n):
        number = input()
        numbers.append(number)

    return numbers


if __name__ == '__main__':
    numbers = read_numbers()
    sort_numbers(numbers)

'''
3
07895462130
919875641230
9195969878

3
09191919191
9100256236
+919593621456
'''
