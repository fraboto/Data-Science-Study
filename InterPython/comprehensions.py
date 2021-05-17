def run():
    #even_squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    #print(even_squares)

    four_six_nine_multiple = [i for i in range(4, 100000, 4) if i % 18 == 0]
    print(four_six_nine_multiple)


if __name__ == '__main__':
    run()