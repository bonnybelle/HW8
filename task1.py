def phones_fixer(func):
    def wrapper(nlist):
        for x in nlist:
            ln = len(x)
            print('+91', ' ', sep='', end='')
            if ln == 10:
                print(x[0:5], ' ', x[5:10], '\n', sep='', end='')
            elif x[0] == '0' and ln == 11:
                print(x[1:6], ' ', x[6:11], '\n', sep='', end='')
            elif x[0:2] == '91' and ln == 12:
                print(x[2:7], ' ', x[7:12], '\n', sep='', end='')
            elif x[0:3] == '+91' and ln == 13:
                print(x[3:8], ' ', x[8:13], '\n', sep='', end='')
            else:
                print(x[0:5], ' ', x[5:10], '\n', sep='', end='')
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
