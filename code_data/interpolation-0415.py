# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:53:55 2019

import the Tracking2Ddata ==> Rolling Matrix completion(TODAY!) ==> visualize the openpose results

@author: Zhuorong Li
"""

import numpy as np
import cv2
import os

'''SVD'''
def mysvd(dataMat):
    U, Sigma, VT = np.linalg.svd(dataMat)
    #print(Sigma) # Sigma is a row vector
    #Sigma_mat = np.mat(np.eye(75) * Sigma[:75]) # change Sigma to a matrix 
    #print(Sigma_mat)
    return U

'''function that replaces the zero entities in A1 with A*'''    
def replaceZeros(dataMat1,dataMat2):
    """
    dataMat1: the deficiency matrix A1
    dataMat2: A*
    return newMat that shares the non-zero entities of A1, 
                  while the zeroes are replaced with the corresponding element in A*
    """
    newMat = dataMat1
    for i in range(len(dataMat1)):
        for j in range(len(dataMat1[i])):
            if dataMat1[i][j]==0:
                newMat[i][j] = dataMat2[i][j]
                #print([i,j])
    return newMat

def findzeros(Mat):
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            if Mat[i][j]==0:
                print([i,j],Mat[i][j])
                
def setzeros(A0,A1):
    for i in range(len(A1)):
        for j in range(len(A1[i])):
            if A1[i][j] == 0:
                A0[i][j] = 0
    return A0

def findandsaveindex(Mat):
    list = []
    for i in range(len(Mat)):
        print(i)
        for j in range(len(Mat[i])):
            if Mat[i][j]==0:
                list.append([i,j]) 
                print([i,j],Mat[i][j])
    arr = np.array(list)
    arr = arr.astype(int)
    np.savetxt('indexes.txt',arr)
    
def interpolation(A,A1):
    A_MeanVec = np.mean(A,0)
    A_MeanMat = np.tile(A_MeanVec,(A.shape[0],1))
    A_new = A-A_MeanMat
    
    A1_MeanVec = A1.sum(0) / (A1 != 0).sum(0)
    #colMean = a.sum(0) / (a != 0).sum(0)
    #rowMean = a.sum(1) / (a != 0).sum(1)  
    A1_MeanMat = np.tile(A1_MeanVec,(A1.shape[0],1))
    A1_new = A1-A1_MeanMat
    A1_new = setzeros(A1_new,A1)
    
    A0 = A
    A0_new = A0-A_MeanMat
    A0_new = setzeros(A0_new,A1)
    
    '''compute U'''
    U = mysvd(np.matmul(A_new.T,A_new)) 
    #S = np.matmul(U,U.T)
        
    '''compute U0'''
    U0 = mysvd(np.matmul(A0_new.T,A0_new)) 
    #S0 = np.matmul(U0,U0.T)
    
    '''compute TMat'''
    TMat = np.matmul(U0.T,U)  #U = U0TMat
        
    '''compute U1'''
    U1 = mysvd(np.matmul(A1_new.T,A1_new)) 
    #S1 = np.matmul(U1,U1.T)
    
    '''compute A*'''
    Astar =  np.matmul(np.matmul(np.matmul(A1_new,U1),TMat),U.T)
    Astar = Astar + A1_MeanMat
    #print('finding zeros in Astar')
    findzeros(Astar)#no zero in Astar
    
    '''replace zero entities'''
    newMat = replaceZeros(A1,Astar)
    return newMat

def drawline(img,a,b,Xs,Ys,c):
	 cv2.line(img, (int(Xs[a]), int(Ys[a])), (int(Xs[b]), int(Ys[b])), colors[c], 2)    
        
if __name__ == '__main__':
    
    '''import the Tracking2Ddata'''
    cwd = os.getcwd()
    print cwd
    directory = cwd[:-10] + '/tracking2d'
    save_directory = cwd
    files = os.listdir(directory)
    Tracking2D = []
    fullfilename = directory+'/'+files[0]
    
    fps = 30 
    img1= cv2.imread(fullfilename)
    size = (img1.shape[1], img1.shape[0]) 
    video = cv2.VideoWriter("FastSong_Man_5.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, size)
    
    data_link = cwd+'/9_Fast Song 05.data'
    f=open(data_link, 'r')
    j=0
    for line in f:
        Tracking2D.append([])
        elements = line.split(',')
        Tracking2D[j].append( [elements[i] for i in range(len(elements))] )
        j+=1
    f.close()
    print len(Tracking2D)
    colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [0, 255, 255], \
              [85, 0, 255], [0, 255, 0], [255, 0, 170], [255, 0, 0], [0, 255, 255], \
              [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 255, 0], [170, 255, 0], \
              [255, 0, 255], [255, 0, 170], [255, 0, 85],[255, 0, 0], [255, 85, 0], \
              [255, 170, 0], [255, 255, 0], [170, 255, 0],[0, 255, 255], [0, 170, 255]]
                 
    #print(type(Tracking2D)) #list
    Tracking2D = np.array(Tracking2D) # list can not read by index while arr can be
    Tracking2D = np.squeeze(Tracking2D) 
    #Tracking2D=Tracking2D.ravel().reshape(498,25,3)
    
    '''Rolling Matrix Completion'''
    A = Tracking2D[9:109].astype(float)
    A1 = Tracking2D[0:100].astype(float)
    Tracking2D[0:100] = interpolation(A,A1)
    
    A = Tracking2D[0:109].astype(float)
    A1 = Tracking2D[19:128].astype(float)
    Tracking2D[19:128] = interpolation(A,A1)
    
    
    A = Tracking2D[0:120].astype(float)
    A1 = Tracking2D[40:160].astype(float)
    Tracking2D[40:160] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[60:190].astype(float)
    Tracking2D[60:190] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[70:200].astype(float)
    Tracking2D[70:200] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[80:210].astype(float)
    Tracking2D[80:210] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[90:220].astype(float)
    Tracking2D[90:220] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[100:230].astype(float)
    Tracking2D[100:230] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[110:240].astype(float)
    Tracking2D[110:240] = interpolation(A,A1)
    
    
    A = Tracking2D[0:130].astype(float)
    A1 = Tracking2D[120:250].astype(float)
    Tracking2D[120:250] = interpolation(A,A1)
    
    
    A = Tracking2D[0:150].astype(float)
    A1 = Tracking2D[110:260].astype(float)
    Tracking2D[110:260] = interpolation(A,A1)
    
    
    A = Tracking2D[0:150].astype(float)
    A1 = Tracking2D[120:270].astype(float)
    Tracking2D[120:270] = interpolation(A,A1)
    
    
    A = Tracking2D[0:150].astype(float)
    A1 = Tracking2D[130:280].astype(float)
    Tracking2D[130:280] = interpolation(A,A1)
    
    
    A = Tracking2D[0:160].astype(float)
    A1 = Tracking2D[130:290].astype(float)
    Tracking2D[130:290] = interpolation(A,A1)
    
    
    A = Tracking2D[0:160].astype(float)
    A1 = Tracking2D[140:300].astype(float)
    Tracking2D[140:300] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[110:310].astype(float)
    Tracking2D[110:310] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[120:320].astype(float)
    Tracking2D[120:320] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[130:330].astype(float)
    Tracking2D[130:330] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[140:340].astype(float)
    Tracking2D[140:340] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[150:350].astype(float)
    Tracking2D[150:350] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[160:360].astype(float)
    Tracking2D[160:360] = interpolation(A,A1)
    
    
    A = Tracking2D[0:200].astype(float)
    A1 = Tracking2D[170:370].astype(float)
    Tracking2D[170:370] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[130:380].astype(float)
    Tracking2D[130:380] = interpolation(A,A1)
    
   
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[140:390].astype(float)
    Tracking2D[140:390] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[150:400].astype(float)
    Tracking2D[150:400] = interpolation(A,A1)
    
   
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[160:410].astype(float)
    Tracking2D[160:410] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[170:420].astype(float)
    Tracking2D[170:420] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[180:430].astype(float)
    Tracking2D[180:430] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[190:440].astype(float)
    Tracking2D[190:440] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[200:450].astype(float)
    Tracking2D[200:450] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[210:460].astype(float)
    Tracking2D[210:460] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[220:470].astype(float)
    Tracking2D[220:470] = interpolation(A,A1)
    
    
    A = Tracking2D[0:250].astype(float)
    A1 = Tracking2D[230:480].astype(float)
    Tracking2D[230:480] = interpolation(A,A1)
    
    
    A = Tracking2D[0:300].astype(float)
    A1 = Tracking2D[190:490].astype(float)
    Tracking2D[190:490] = interpolation(A,A1)
    
    
    A = Tracking2D[0:300].astype(float)
    A1 = Tracking2D[Tracking2D.shape[0]-300:Tracking2D.shape[0]].astype(float)
    Tracking2D[Tracking2D.shape[0]-300:Tracking2D.shape[0]] = interpolation(A,A1)
    print('Tracking2D.shape:',Tracking2D.shape)
    
    '''VISUALIZE'''
    Tracking2D=Tracking2D.ravel().reshape(Tracking2D.shape[0],25,3)
    print('Tracking2D.shape:',Tracking2D.shape)

    for i in range(Tracking2D.shape[0]):
        if i>=100 :
            break  
        fullfilenames = directory+'/'+files[i]
        img = cv2.imread(fullfilenames)
        Xs=[]
        Ys=[]
        for j in range(Tracking2D.shape[1]):
            x=round(float(Tracking2D[i][j][0]))
            y=round(float(Tracking2D[i][j][1]))
            Xs.append(x)
            Ys.append(y)
            #cv2.circle(img,(x,y),2,(0,0,0),thickness=-1)
        drawline(img,0,1,Xs,Ys,0)
        drawline(img,1,2,Xs,Ys,1)
        drawline(img,1,8,Xs,Ys,14)
        drawline(img,2,3,Xs,Ys,3)
        drawline(img,3,4,Xs,Ys,4)
        drawline(img,1,5,Xs,Ys,5)
        drawline(img,5,6,Xs,Ys,3)
        drawline(img,6,7,Xs,Ys,4)
        drawline(img,0,15,Xs,Ys,8)
        drawline(img,0,16,Xs,Ys,9)
        drawline(img,15,17,Xs,Ys,10)
        drawline(img,16,18,Xs,Ys,11)
        drawline(img,8,9,Xs,Ys,12)
        drawline(img,8,12,Xs,Ys,11)
        drawline(img,9,10,Xs,Ys,0)
        drawline(img,10,11,Xs,Ys,15)
        drawline(img,11,22,Xs,Ys,22)
        drawline(img,22,23,Xs,Ys,23)
        drawline(img,11,24,Xs,Ys,18)
        drawline(img,12,13,Xs,Ys,0)
        drawline(img,13,14,Xs,Ys,15)
        drawline(img,14,21,Xs,Ys,18)
        drawline(img,14,19,Xs,Ys,22)
        drawline(img,19,20,Xs,Ys,23)
        #cv.imshow("Image",img)
        #cv.waitKey(0)
        #print(i)
    
        for j in range(Tracking2D.shape[1]):
            x=round(float(Tracking2D[i][j][0]))
            y=round(float(Tracking2D[i][j][1]))
            Xs.append(x)
            Ys.append(y)
            cv2.circle(img,(int(x),int(y)),2,(0,0,0),thickness=-1)
            
        out_img=save_directory +'/'+files[i]
        cv2.imwrite(out_img, img)
        video.write(img)
    video.release()
    
    cap = cv2.VideoCapture('FastSong_Man_5.avi')
     
    while(True):
        ret,frame = cap.read()#capture one frame
        if ret:
            cv2.imshow('frame',frame)
            cv2.waitKey(25)
            #cv.waitKey(0)
        else:
            break 
    cap.release()
    cv2.destroyAllWindows()
    