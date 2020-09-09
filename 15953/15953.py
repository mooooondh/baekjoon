join_count = int(input())

price_1 = [5000000, 3000000, 2000000, 500000, 300000, 100000]
price_2 = [5120000, 2560000, 1280000, 640000, 320000]
get_total_price = []

for i in range(join_count):
    get_price_1 = 0
    get_price_2 = 0

    grade_1, grade_2 = input().split()
    grade_1 = int(grade_1)
    grade_2 = int(grade_2)

    for i in range(1, len(price_1) + 1):
        check_price = int((i * (1 + i)) / 2)

        if (grade_1 == 0):
            get_price_1 = 0
            break

        elif (grade_1 <= check_price):
            get_price_1 = price_1[i - 1]
            break  # end of if

        pass  # end of for

    for i in range(1, len(price_2) + 1):
        check_price = int((1 * ((2 ** i) - 1)) / (2 - 1))

        if (grade_2 == 0):
            get_price_2 = 0
            break

        elif (grade_2 <= check_price):
            get_price_2 = price_2[i - 1]
            break  # end of if

        pass  # end of for

    get_total_price.append(get_price_1 + get_price_2)
    pass  # end of for

for i in range(len(get_total_price)):
    print(get_total_price[i])
    pass  # end of for