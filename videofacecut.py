#仅限于真人视频中的头像剪切，不适用于动漫头像数据集的制作。
import face_recognition
import cv2
from PIL import Image
import datetime
# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
 
# Open the input movie file

"""测试图片"""
# Load some sample pictures and learn how to recognize them.
lmm_image = face_recognition.load_image_file('image/test2.jpg')
lmm_face_locations = face_recognition.face_locations(lmm_image,number_of_times_to_upsample=2,model='cnn')
print(len(lmm_face_locations))
i=0
for top,right,bottom,left in lmm_face_locations:
		face_image=lmm_face_locations[top:bottom,left:right]
		print(face_image.shape)
		im = Image.fromarray(face_image)
		im.save('output/image'+str(frame_number)+'_'+str(i).png)
		i+=1
		
		
		
"""针对视频
input_movie = cv2.VideoCapture("video/yourname.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
frame_number=1
i=1
starttime = datetime.datetime.now()
print(starttime)
while True:
    # Grab a single frame of video
	ret, frame = input_movie.read()
	frame_number += 1
 
    # Quit when the input video file ends
	if not ret:
		break
 
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_frame = frame[:, :, ::-1]
 
    # Find all the faces and face encodings in the current frame of video
	face_locations = face_recognition.face_locations(rgb_frame)
	for top,right,bottom,left in face_locations:
		face_image=face_locations[top:bottom,left:right]
		print(face_image.shape)
		im = Image.fromarray(face_image)
		im.save('output/image'+str(frame_number)+'_'+str(i).png)
		i+=1
# All done!
endtime = datetime.datetime.now()
print(endtime)
print((endtime - starttime).seconds)
input_movie.release()
"""
