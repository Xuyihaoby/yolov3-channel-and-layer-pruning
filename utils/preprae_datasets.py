import  glob
import os
import os.path as osp
import pdb


def cocoFoldStructureYolo3_Tag8(src_path, dstpath=None):
    labelpath =osp.join(src_path, 'labels')
    imgpath = osp.join(src_path, 'images')
    dst_txt = osp.join(dstpath, 'custom_test.txt')
    imglist = glob.glob(osp.join(imgpath, '*.jpg'))
    labellist = glob.glob(osp.join(labelpath, '*.txt'))
    with open(dst_txt, 'w') as f:
        for img in imglist:
            print(img+'\n')
            f.write(img+'\n')
    print('number of img ::', len(imglist))
    print('number of label :', len(labellist))

def count_cate(path):
    num=[]
    emptynum = 0
    labelpath = osp.join(path, 'labels')
    labellist = glob.glob(osp.join(labelpath, '*.txt'))
    for label in labellist:
        # print('file list : ', label)
        with open(label, 'r') as f:
            lines = f.readlines()
            if len(lines) == 0:
                print(label)
                emptynum+=1
            for line in lines:
                temp = int(line.split()[0])
                num.append(temp)
    max_num = max(num)
    print(emptynum)
    print('the max num is: ', max_num)

def checkexist(src):
    content = []
    with open(src, 'r') as f:
        img_files = f.readlines()
    label_files = [x.replace('images', 'labels').replace(os.path.splitext(x)[-1], '.txt')
                        for x in img_files]
    for i, file in enumerate(label_files):
        if os.path.isfile(file):
            img = file.replace('labels', 'images').replace(os.path.splitext(file)[-1], '.jpg')+'\n'
            content.append(img)
    print(len(content))
    with open(src, 'w') as f:
        for cont in content:
            f.write(cont)




if __name__ == '__main__':
    cocoFoldStructureYolo3_Tag8('/data3/shannon/Udacity_extend_yolo/test',
                                '/home/xyh/yolov3-channel-and-layer-pruning/data')

    # count_cate('/data3/shannon/Udacity_extend_yolo/test')

    checkexist('./data/custom_test.txt')