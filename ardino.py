import serial

ardinodata=serial.Serial('COM4',9600)

def led1():
    ardinodata.write(str.encode('1'))

def led2():
    ardinodata.write(str.encode('2'))


def led3():
    ardinodata.write(str.encode('3'))

def servo():
    ardinodata.write(str.encode("4"))


def main():
    a = (input("enter your password"))
    if a=='z':
        servo()
        print("open gates")
        exit(0)
    elif a==int(ord('Z')):
        led1()
        exit(0)
    elif a==3:
        led2()
    elif a==4:
        led3()
    else :
        pass
main()
