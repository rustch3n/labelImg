#!/usr/bin/env python
import os
import sys


def split_data(target_dir, sp_train, sp_val, sp_test):
    prefix_dir = os.path.join(target_dir, "ImagesSet/Main");
    
    os.system("mkdir -p " + prefix_dir)
    f_train = open(os.path.join(prefix_dir, "train.txt"), 'w')
    f_val = open(os.path.join(prefix_dir, "val.txt"), 'w')
    f_trainval = open(os.path.join(prefix_dir, "trainval.txt"), 'w')
    f_test = open(os.path.join(prefix_dir, "test.txt"), 'w')

    images_dir = os.path.join(target_dir, "JPEGImages")
    images = os.listdir(images_dir)
    images = filter(lambda img:len(img) == 10 and img[-3:] == "jpg", images)

    
    total = sp_train + sp_val + sp_test
    cnt_train = 0
    cnt_val = 0
    cnt_test = 0
    for i, img in enumerate(images):
        img_id = img[:-4] + '\n'
        md = i % total
        if md < sp_train:
            f_train.write(img_id)
            f_trainval.write(img_id)
            cnt_train = cnt_train + 1
            print "train", img
        elif md < (sp_train + sp_val):
            f_val.write(img_id)
            f_trainval.write(img_id)
            cnt_val = cnt_val + 1
            print "validate", img

        else:
            f_test.write(img_id)
            cnt_test = cnt_test + 1
            print "test", img


    f_train.close()
    f_val.close()
    f_trainval.close()
    f_test.close()

    print "DONE total=%d train=%d validate=%d test=%d" % (len(images), cnt_train, cnt_val, cnt_test)



if __name__ == "__main__":

    if len(sys.argv) != 5:
        print '''USAGE split_data target_dir train val test
e.g., split_data mydir 10 3 3
        '''
        exit()

    split_data(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
