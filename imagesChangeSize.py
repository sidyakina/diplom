from PIL import Image
import choiseSize as ch


def resizeImage(nameImage, newWidth, newHeight, responseNN, file="test/examples.txt"):
    number = Image.open(nameImage)
    number_gray = number.convert('L')
    number_gray = number_gray.resize((newWidth, newHeight), Image.ANTIALIAS)

    with open(file, "a") as f:
        yVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        yVector[int(responseNN)] = 1
        for y in yVector:
            f.write(str(y))
            f.write(",")
        for i in range(number_gray.size[0]):
            for j in range(number_gray.size[1]):
                f.write(str(number_gray.getpixel((i, j))/255))
                if i == number_gray.size[0] - 1 and j == number_gray.size[1] - 1:
                    pass
                else:
                    f.write(",")
                # print(array[i, j][0])
        f.write('\n')

    number.close()
    number_gray.close()


if __name__ == '__main__':
    numberImage = 150
    newWidth, newHeight = ch.choiseSize(numberImage=200)
    for j in range(numberImage):
        for i in range(10):
            resizeImage("numbers/{}_{}.jpg".format(i, j + 1), newWidth, newHeight, str(i) + " ")
    numberTrains = 50
    for i in range(10):
        for j in range(numberTrains):
            resizeImage("numbers/{}_{}.jpg".format(i, j + 151), newWidth, newHeight, str(i) + " ", "test/examplesTest.txt")