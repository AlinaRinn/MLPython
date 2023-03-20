import cv2
import os
import binascii
import codecs
import Common
import time 
import numpy as np
from PIL import Image

def imgToBlackWhite(pathToImg, threshold):
    imgGrey = cv2.imread(pathToImg, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Grayscale", imgGrey)
    img_binary = cv2.threshold(imgGrey, threshold, 255, cv2.THRESH_BINARY)[1] 
    parsed_filename = os.path.splitext(os.path.basename(pathToImg))[0]
    new_filename = parsed_filename + 'B&W.bmp'
    cv2.imwrite(new_filename, img_binary)
    cv2.imshow("BlackWhite", img_binary)
    cv2.waitKey()

def imgToBinary(filename):
    with open(filename, 'rb') as file:
        image_data = file.read()

    data = binascii.hexlify(image_data)
    binary = bin(int(data, 16))
    binary = binary[2:].zfill(32)

    parsed_filename = os.path.splitext(os.path.basename(filename))[0]
    binary_filename = parsed_filename + '.bin'
    with open(binary_filename, 'wb') as file:
        file.write(binary.encode());

def binaryToImg(filename):
    binFile = open(filename,'rb')
    binaryData = binFile.read()
    hexData = '%0*X' % ((len(binaryData) + 3) // 4, int(binaryData, 2))

    decode_hex = codecs.getdecoder("hex_codec")
    hexData = decode_hex(hexData)[0]

    parsed_filename = os.path.splitext(os.path.basename(filename))[0]
    png_filename = parsed_filename + '_from_binary.png'
    with open(png_filename, 'wb') as file:
        file.write(hexData)

def imageRecognizer():
    img = Image.open('img1.bmp')
    img = np.array(img)
    print(img)

def binaryToArray(filename, inputArray):
    f = open(filename, 'r')
    tmplist = list()
    for i in f.read():
        if (i == '0'):
            tmplist.append(1)
        elif (i == '1'):
            tmplist.append(-1)
    inputArray.append(tmplist)
    f.close()

def Hopfield(X, Xprac):
    start = time.time()
    print(start)
    f = open(f"log{time.time()}.txt", "w")
    f.write(f"Start time {start}")
    print("X")
    f.write("\nX:\n")
    Common.NumerizedFilePrint(X, f)
    W = Common.multiply(Common.transpose(X), X)
    W = Common.diagonalNullifier(W)
    print("W calculated\nTime:", time.time() - start, end="")
    f.write("W:\n")
    Common.NumerizedFilePrint(W, f)

    for prac in range(len(Xprac)):
        Y = [Xprac[prac]] # 2.1       
        n = 1.0
        counter = 0
        print(f"\nImage {prac}:")
        f.write(f"\nImage {prac}: {Y}")
        while(n > 0.0):
            print("Iteration ", counter)
            f.write(f"\nIteration {counter}\n")
            f.write("Y:\n")
            Common.NumerizedFilePrint(Y, f)
            temp = [] 
            S = []
            for i in range(len(W)):  # 2.2
                tmp = 0
                for j in range(len(W[0])):
                    tmp += W[i][j]*Y[counter][j]
                S.append(tmp)
            f.write("S:\n")
            Common.NumerizedFilePrint(Y, f)
            temp = [] 
            for j in range(len(Y[0])): # 2.3
                temp.append(Common.SingleJump(S[j], 0))
            Y.append(temp)
            print("Y1:\n", Y[counter+1])
            f.write(f"Y1:\n{Y[counter+1]}\n")
            n = sum(Common.powList(Common.difference(Y[counter], Y[counter+1]))) # 2.4
            print("n:", n)
            f.write(f"n: {n}")
            if(counter > 1 and sum(Common.powList(Common.difference(Y[counter], Y[counter - 2]))) == 0 and sum(Common.powList(Common.difference(Y[counter - 1], Y[counter - 3]))) == 0):
                f.write("\nThis image not recognized")
                print("This image not recognized:\n", Y[counter])  
                break
            counter += 1
            print(time.time() - start, "\n")
    f.write(f"\nTotal time:{time.time() - start}")
    f.close()
    print(time.time() - start)

def main():
    #InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
     #             [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    #Practice =   [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
    #             [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    #Hopfield(InputArray, Practice)
    #imgToBlackWhite("img11.bmp", 240)
    #imgToBlackWhite("img22.bmp", 250)
    #imgToBlackWhite("img3.bmp", 240)
    imgToBinary("img1.bmp")
    imgToBinary("img2.bmp")
    imgToBinary("img3.bmp")
    #imgToBinary("img4B&Wmono.bmp")
    #binaryToImg("img11B&Wmono.bin")
    #binaryToImg("img22B&Wmono.bin")
    #binaryToImg("img3B&Wmono.bin")
    inputArray = list()
    PracticeArray = list()
    binaryToArray("img1.bin", inputArray)
    binaryToArray("img2.bin", inputArray)
    #binaryToArray("img3B&Wmono.bin", PracticeArray)
    binaryToArray("img2.bin", PracticeArray)
    imageRecognizer()
    #Hopfield(inputArray, PracticeArray)
main()