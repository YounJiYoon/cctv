import requests
import urllib
import json
import pandas as pd
import cv2
from ultralytics import solutions
from ultralytics import YOLO
import time
from datetime import datetime


def cctvURL(X, Y):
    # Get URL of CCTV within the range based on X, Y
    minX = f"{X - 0.02:.4f}"
    maxX = f"{X + 0.02:.4f}"
    minY = f"{Y - 0.02:.4f}"
    maxY = f"{Y + 0.02:.4f}"
    url_cctv = f'https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type=ex&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType=json'
    response = urllib.request.urlopen(url_cctv)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    cctv_play  = pd.json_normalize(json_object["response"]["data"], sep=',')
    print(cctv_play)

    return cctv_play

def data_appending(counter, car_IN, car_OUT, truck_IN, truck_OUT, bus_IN, bus_OUT):
    # Input Data
    if 'car' in counter.classwise_counts.keys():
        car_IN.append(counter.classwise_counts['car']['IN'])
        car_OUT.append(counter.classwise_counts['car']['OUT'])
    else:
        car_IN.append(0)
        car_OUT.append(0)
    if 'truck' in counter.classwise_counts.keys():
        truck_IN.append(counter.classwise_counts['truck']['IN'])
        truck_OUT.append(counter.classwise_counts['truck']['OUT'])
    else:
        truck_IN.append(0)
        truck_OUT.append(0)
    if 'bus' in counter.classwise_counts.keys():
        bus_IN.append(counter.classwise_counts['bus']['IN'])
        bus_OUT.append(counter.classwise_counts['bus']['OUT'])
    else:
        bus_IN.append(0)
        bus_OUT.append(0)

start_time = time.time()  # set time
interval = 5*60  # 초 단위

key = "YourOwnKey"    # API key

YeongjongBr_X = 126.5622    # 경도
YeongjongBr_Y = 37.5366    # 위도

IncheonBr_X = 126.561342    # 경도
IncheonBr_Y = 37.417100    # 위도

# Init Data List
car_IN_1 = [] 
car_OUT_1 = []
bus_IN_1 = []
bus_OUT_1 = []
truck_IN_1 = []
truck_OUT_1 = []

car_IN_2 = [] 
car_OUT_2 = []
bus_IN_2 = []
bus_OUT_2 = []
truck_IN_2 = []
truck_OUT_2 = []

index = []

# 영종대교
cctv_play1 = cctvURL(YeongjongBr_X, YeongjongBr_Y)    # list of cctv
YeongjongBr_url = cctv_play1['cctvurl'][0]    # choose one from list of cctv
capture1 = cv2.VideoCapture(YeongjongBr_url)
assert capture1.isOpened(), "Error reading video file"
w, h, fps = (int(capture1.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# 인천대교
cctv_play2 = cctvURL(IncheonBr_X, IncheonBr_Y)
IncheonBr_url = cctv_play2['cctvurl'][1]
capture2 = cv2.VideoCapture(IncheonBr_url)
assert capture2.isOpened(), "Error reading video file"
w, h, fps = (int(capture2.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
region_points = [(10, 300), (710, 300)]  # For line counting

# Init Object Counter
counter1 = solutions.ObjectCounter(
    show=False,  # Display the output
    region=region_points,  # Pass region points
    model = "yolo11n.pt"
)
counter2 = solutions.ObjectCounter(
    show=False,  # Display the output
    region=region_points,  # Pass region points
    model = "yolo11n.pt"
)

# Process video
while capture1.isOpened() and capture2.isOpened():
    success_1, im0_1 = capture1.read()
    success_2, im0_2 = capture2.read()
    if not success_1 or not success_2:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    im0_1 = counter1.count(im0_1)
    im0_2 = counter2.count(im0_2)

    cv2.imshow("im0_1", im0_1)
    cv2.imshow("im0_2", im0_2)

    # Update data file
    current_time = time.time()  # set time
    if current_time - start_time >= interval:
        data_appending(counter1, car_IN_1, car_OUT_1, truck_IN_1, truck_OUT_1, bus_IN_1, bus_OUT_1)
        data_appending(counter2, car_IN_2, car_OUT_2, truck_IN_2, truck_OUT_2, bus_IN_2, bus_OUT_2)
        index.append(datetime.now().strftime("%H:%M:%S"))
        
        df1 = pd.DataFrame({'car_IN': car_IN_1,
                            'car_OUT': car_OUT_1,
                            'truck_IN': truck_IN_1,
                            'truck_OUT': truck_OUT_1,
                            'bus_IN': bus_IN_1,
                            'bus_OUT': bus_OUT_1}, index=index)

        df2 = pd.DataFrame({'car_IN': car_IN_2,
                            'car_OUT': car_OUT_2,
                            'truck_IN': truck_IN_2,
                            'truck_OUT': truck_OUT_2,
                            'bus_IN': bus_IN_2,
                            'bus_OUT': bus_OUT_2}, index=index)
        
        df1.to_csv('YeongjongBr.csv')
        df2.to_csv('IncheonBr.csv')
 
        start_time = current_time  # reset time

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#print(counter.classwise_counts['car']['IN'])
print(counter1.classwise_counts)
print(counter2.classwise_counts)
print(df1)
print(df2)

capture1.release()
capture2.release()
cv2.destroyAllWindows()
