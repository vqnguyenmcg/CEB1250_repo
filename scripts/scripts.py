def funct1():
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        print('Even number')
    else:
        print('Odd number')

def squaring(number):
    # number = float(input('Enter a number: '))
    print(number**2)
    return number**2

def convertftoc():
    fahr = float(input('Enter Fahrenheit: '))
    print('Celcius is {0}'.format((fahr-32)*5/9))


def main():
    funct1()
    squaring(2)
    convertftoc()


if __name__ == "__main__":
    main()
