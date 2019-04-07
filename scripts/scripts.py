import numpy as np



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



def largest(arrays):
    return np.amax(arrays)

def palinedrome(list_):
    l = len(list_)
    if l % 2 == 1:
        cond = False
        for i in range(0,int(l/2)):
            if list_[i] == list_[l-1-i]:
                cond = True
        if cond == True:
            print('Palinedrome')
    else:
        print('Not palinedrome')


def countvowels(lists_):
    count = 0
    for i in range(0, len(lists_)):
        if lists_[i] in ['a', 'u', 'e', 'i', 'o']:
            count +=1
    return count


def main():
    funct1()
    squaring(2)
    convertftoc()
    # arrays = input('Enter a sequence of numbers separated by a space: ')
    # arrays = arrays.split(' ')
    # arrays = np.array(arrays)
    # print(arrays)
    arrays = np.array([1, 2, 3, 4, 5])
    print('largest element is {0} is '.format(np.amax(arrays)))
    lists_= input('Enter a string: ')
    palinedrome(lists_)
    print('number of vowels in {0} is {1}'.format((lists_),countvowels(lists_)))


if __name__ == "__main__":
    main()
