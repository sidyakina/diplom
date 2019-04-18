# необходимо удалить файл test/examplenumbers.txt перед запуском
from PIL import Image


def resizeImage(nameImage, newWidth, newHeight, file):
    number = Image.open(nameImage)
    number_gray = number.convert('L')
    number_gray = number_gray.resize((newWidth, newHeight), Image.ANTIALIAS)

    with open(file, "a") as f:
        for i in range(number_gray.size[0]):
            for j in range(number_gray.size[1]):
                f.write(str(number_gray.getpixel((i, j))/255))
                if i == number_gray.size[0] - 1 and j == number_gray.size[1] - 1:
                    pass
                else:
                    f.write(",")
        f.write('\n')

    number.close()
    number_gray.close()


if __name__ == '__main__':
    numbers = ["numbers/1_227.jpg", "numbers/7_294.jpg", "numbers/7_330.jpg"]
    newWidth, newHeight = (32, 53)
    for strName in numbers:
        resizeImage(strName, newWidth, newHeight, "test/examplenumbers.txt")
