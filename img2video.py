import cv2
import os
import random

img = cv2.imread('D:\\ouyang_project\\innovation\\dance2\\EverybodyDanceNow_reproduce_pytorch\\results\\target\\test_latest\\images\\00000_synthesized_image.jpg')
fps = 24 # 根据第二节介绍的方法获取视频的 fps
size = (img.shape[1],img.shape[0])  #获取视频中图片宽高度信息
print(size)
fourcc = cv2.VideoWriter_fourcc(*"XVID") # 视频编码格式
videoWrite = cv2.VideoWriter('D:\ouyang_project\\innovation\\dance2\\EverybodyDanceNow_reproduce_pytorch\\test.avi',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，帧率，视频大小（图片大小））

files = os.listdir('D:\\ouyang_project\\innovation\\dance2\\EverybodyDanceNow_reproduce_pytorch\\results\\target\\test_latest\\images\\')
out_num = len(files)
for j in range(0,5):
    for i in range(0, 120):
        fileName = "D:\\ouyang_project\\innovation\\dance2\\EverybodyDanceNow_reproduce_pytorch\\results\\target\\test_latest\\images\\"+str(i).zfill(5)+'_synthesized_image.jpg'
        print(fileName)
        img = cv2.imread(fileName)
        videoWrite.write(img)# 将图片写入所创建的视频对象
