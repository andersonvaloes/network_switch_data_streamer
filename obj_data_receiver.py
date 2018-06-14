import socket
import sys
import cv2
import pickle
import numpy as np
import struct 
from PIL import Image, ImageDraw



f = 1.5

HOST='localhost'
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()
data = bytearray()

### new
payload_size = struct.calcsize("L") 
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    
    data = data[payload_size:]
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_type_data = data[:payload_size]
    type_data = struct.unpack("L", packed_type_data)[0]

    data = data[payload_size:]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    ###
    if(type_data == 0):
        # print(frame_data[7:-3].decode("utf-8"))

        # Create a black image
        img = np.zeros((512,512,3), np.uint8)

        # Write some Text
        cv2.putText(img,frame_data[7:-3].decode("utf-8"), 
            (10,500), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1,
            (255,255,255),
            2)

        #Display the image
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        frame=pickle.loads(frame_data)
        cv2.imshow('frame', cv2.resize(frame, (0,0), fx=f, fy=f))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break