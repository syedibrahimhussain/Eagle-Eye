import OCR
#import OcrCamera
import searchnp
#import serial
#import ardino

#ardinodata=serial.Serial('COM4',9600)


def main():
    plate_no=OCR.predict()
    #plate_no = OcrCamera.predict()
    print("License plate is :{}".format(plate_no))
    result=(searchnp.mysql_searchdata(plate_no))
    if result==1:
        ardino.main()
        print("gates open")
    else:
        print("gates will not open")


main()