from file_manager import *
from PIL import Image
import numpy as np
from multiprocessing import Process

#constants:
choicer = [True, False, False, False, False, False, False, False, True]
blocksize = 3
tflevel = 0.8
answers = np.zeros((10,20))

def preprocess(tflevel):
    io = tflevel[2]
    blocksize = tflevel[1]
    tflevel = tflevel[0]
    x, y = io.shape

    # make avg array:
    x_n, y_n = x // blocksize, y // blocksize
    im = np.zeros((x_n, y_n))
    for i in range(x_n):
        for j in range(y_n):
            im[i, j] = np.average(io[blocksize * i:blocksize * (i + 1), blocksize * j:blocksize * (j + 1)])

    # normalize array to 1..0
    im = np.array((im - np.min(im)) > np.max(im) * tflevel)

    # show result:
    # oim = Image.fromarray(im)
    # oim.show()

    # clear cells
    flag = True
    for i in range(3):
        for i in range(x_n):
            for j in range(y_n):
                tim = choicer[im[max(0, i - 1): min(i + 2, x_n), max(0, j - 1):min(j + 2, y_n)].sum() - im[i, j]] and \
                      im[i, j]
                #                 ^---------------------------number of alive neighbours--------------------^
                if tim != im[i, j]:
                    im[i, j] = tim
                    flag = False
        if flag: break

    # show result:
    # oim = Image.fromarray(im)
    # oim.show()
    print(im.sum(), blocksize, tflevel)
    return tflevel, blocksize, im.sum()

if __name__ == '__main__':
    # open file and convert to array:
    io = Image.open(
        'C:/Users/palpa/Desktop/Death/MIPT/ICT/Algorithms_bioinformatics/Cell_counter/tryphoto/Fluorescent-E.-coli.tif')  # get_dir_path(DirPathMode.File, title='Open image')
    io = io.convert("L")
    io = np.array(io)

    # show result:
    # oim = Image.fromarray(io)
    # oim.show()
    args = []
    for blocksize in range(1,11):
        for tfleveliter in range(0,20):
            tflevel = tfleveliter * 0.05

            args.append([tflevel, blocksize, io.copy()])


    def processing(args):
        p = []
        for i in range(0, len(args)):
            p.append(Process(target=preprocess, args=(args[i],)))
        for i in range(0, len(args)):
            p[i].start()
        for i in range(0, len(args)):
            p[i].join()
        return p


    print(processing(args))