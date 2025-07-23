## Real-time pedestrian counting using YOLO11 👨‍🏫

# This Jupyter notebook is part of the research project for counting pedestrians in regular
# street scenes. The code needs to be run the "YOLO-Torch-2.1_ultralytics" environment.

# ----- Importamos las librerías necesarias ------ #
import cv2
import torch
import ultralytics
import webbrowser
import os
import multiprocessing
import time
from ultralytics import solutions
# ------------------------------------------------ #

# ----- Loading a specific model ------ #
# If you want to use a specific model, you can use the following line:
# from ultralytics import YOLO
# custom_model = YOLO(model="yolo12n.pt")

# ----- Checking if GPU is available ------ #
if torch.cuda.is_available():
	print("GPU is available. Using GPU for inference.")
else:
	print("GPU is not avaailable. Using CPU for inference.")

# Checking the version of ultralytics
print(ultralytics.checks())
# ----------------------------------------- #

# ----- Spcifying the video path ----- #
cap = cv2.VideoCapture(filename="Resources/videos/MS6_SD.mp4")
# Verifying that the file was correctly opened
assert cap.isOpened(), "Error opening the video file"
# assert verifica si el archivo de video se abrió correctamente.
# El método isOpened() devuelve True si el archivo de video se cargó correctamente y False en caso contrario.
# Si el archivo no se puede abrir, la aserción generará un error con el mensaje "Error opening video file".
# ------------------------------------ #

# ----- Opening the Selector_puntos.html ----- #
file_path = os.path.abspath("Selector_puntos.html")
webbrowser.open(f"file:///{file_path}")
# -------------------------------------------- #

# ----- Specifying the region points ----- #
x1 = input("Introduce the x1 coordinate: ")
y1 = input("Introduce the y1 coordinate: ")
x2 = input("Introduce the x2 coordinate: ")
y2 = input("Introduce the y2 coordinate: ")
x1 = int(x1); y1 = int(y1); x2 = int(x2); y2 = int(y2)
region_points = [(x1, y1), (x2, y2)]
# ---------------------------------------- #

# ----- Getting the video properties ----- #
# We are going to extract the width(), height() and the FPS from the video using CV2
w, h, fps = (int(cap.get(x))
	for x in (cv2.CAP_PROP_FRAME_WIDTH,
			cv2.CAP_PROP_FRAME_HEIGHT,
			cv2.CAP_PROP_FPS))
# ---------------------------------------- #

# ----- Video writer object to save the output video ----- #
video_writer = cv2.VideoWriter(filename="Resources/videos_output/Cruce_Estacionamiento_CU_2.mp4",
							fourcc=cv2.VideoWriter_fourcc(*"mp4v"),
							frameSize=(w,h),
							fps=fps)
# -------------------------------------------------------- #

# ----- Initializing the instance of the ObjectCounter ----- #
counter = solutions.ObjectCounter(model="Models/yolo11l.pt",
								show=False, # For the FPS Originalmnte era True
								region=region_points,
								line_width=2,
								classes=[0], # Class Id for persons
								iou=0.5,
								conf=0.2)
#----------------------------------------------------------- #

# ----- Processsing the video ----- #
prev_time = time.time() # For the FPS
frame_count = 0 # For the FPS

multiprocessing.freeze_support() # se utiliza para asegurar la compatibilidad del módulo multiprocessing en Windows

start_time = time.time() # <-- INICIO DEL TIMER

while cap.isOpened():
	success, im0 = cap.read()
	if not success:
		print("Video frame is empty or video processing has been successfully completed. 😃")
		break

	frame_count +=1 # For the FPS
	curr_time = time.time() # For the FPS
	elapsed = curr_time - prev_time # For the FPS
	if elapsed > 0: # For the FPS
		fps_text = f"FPS: {1/elapsed:.2f}" # For the FPS
	else:
		fps_text = "FPS: --" # For the FPS
	prev_time =curr_time # For the FPS

	results = counter(im0) # Counting the objects in the frame
	cv2.putText(img=results.plot_im, # For the FPS
			text=fps_text,
			org=(10,30),
			fontFace=cv2.FONT_HERSHEY_SIMPLEX,
			fontScale=1,
			color=(255,0,0),
			thickness=2,
			lineType=cv2.LINE_AA)
	
	cv2.imshow("Video con FPS", results.plot_im) # For the FPS

	video_writer.write(results.plot_im) # Writing the video frames

	if cv2.waitKey(1) & 0xFF == ord("q"): # For the FPS
		break # For the FPS

end_time = time.time() # <-- FIN DEL TIMER

print(f"Tiempo total de ejecución: {end_time-start_time:.2f} segundos")

cap.release() # For the FPS
video_writer.release() # For the FPS
cv2.destroyAllWindows() # For the FPS
# --------------------------------- #