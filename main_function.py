
def max_number(numbers):

    str_num = [str(x) for x in numbers]
    word = ""
    while len(str_num) != 0:
        maxi = "0"
        for x in str_num:
            if ord(x[0]) > ord(maxi[0]):
                maxi = x
            else:
                if ord(x[0]) == ord(maxi[0]):
                    i = len(x)
                    j = len(maxi)
                    ii = 0
                    while ii < max(i, j):
                        if ord(x[-i + ii]) != ord(maxi[-j + ii]):
                            if ord(x[-i + ii]) > ord(maxi[-j + ii]):
                                maxi = x
                            # else maxi = maxi
                            break
                        ii = ii + 1
                        if -i + ii == 0 and -j + ii == 0:
                            break
                        if -i + ii == 0:
                            i = ii + len(x)
                        if -j + ii == 0:
                            j = ii + len(maxi)
        str_num.remove(maxi)
        word = word + maxi
    return word

tab = [5000, 5, 50]
print(max_number(tab))
