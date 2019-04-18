from PIL import Image


def choiseSize(numberImage):
    width, height = [0, 0]

    for i in range(10):
        for j in range(numberImage):
            image = Image.open("numbers/{}_{}.jpg".format(i, j + 1))
            imageSize = image.size
            image.close()
            width += imageSize[0]
            height += imageSize[1]

    print("sum width = ", width, "sum height", height)
    newWidth = width / (numberImage * 10)
    newHeight = height / (numberImage * 10)
    print("new width without round", newWidth, "new Height without round", newHeight)
    newWidth = int(round(width / (numberImage * 10), 0))
    newHeight = int(round(height / (numberImage * 10), 0))
    print("new width", newWidth, "new Height", newHeight)
    return newWidth, newHeight


if __name__ == '__main__':
    numberImage = 4
    print(choiseSize(numberImage))