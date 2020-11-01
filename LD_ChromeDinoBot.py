# By: Lalit Dumka
#! For Fullscreen chrome://dino/ in chrome web browser 
from PIL import ImageGrab
from pyautogui import press
# import time
def hit(key):
    press(key)
def chkWhite(data):
    for i in range(320,150,-1):
        for j in (451,419):
            if data[i,j] < 100:
                hit('up')
                return         
    return
def chkBlack(data):
    for i in range(320,150,-1):
        for j in (451,419):
            if data[i,j] > 100:
                hit('up')
                return         
    return                   
def main():
    print("started...")
    hit('up')
    while True:
        # t1=time.time()
        imgData = ImageGrab.grab().convert('L').load()
        if imgData[1,588] < 100:
            chkBlack(imgData)
            print('chk blk')
        else:
            chkWhite(imgData)
            print('chk wht')
        # t2=time.time()
        # print(t2-t1) # the no is the FPS it should be less than 0.0625 for good results
if __name__ == "__main__":

    main()
    #! uncomment below code and comment above line: to find the right position to test. For best results is is recommended that you calliberate the points according to your display and software.
    # import time
    # print('Capturing SS in 3 seconds...')
    # time.sleep(2)
    # img = ImageGrab.grab().convert('L')
    # imgData = img.load()
    # for i in range(320,150,-1):
    #     for j in (451,419):
    #         imgData[i,j] = 79
    # imgData[1,588] = 100
    # img.show()
