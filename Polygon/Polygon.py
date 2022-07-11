import numpy as np
import cv2

detect_zone = []
plate_zone = []

with open('Polygon/detect_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        detect_zone.append((int(x), int(y)))

with open('Polygon/plate_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        plate_zone.append((int(x), int(y)))

points_detect = []
points_plate = []

for point in detect_zone:
    points_detect.append((point[0], point[1]))
points_detect = np.array(points_detect, dtype=np.int32)

for point in plate_zone:
    points_plate.append((point[0], point[1]))
points_plate = np.array(points_plate, dtype=np.int32)

detect_polygon = points_detect.reshape((-1, 1, 2))
plate_polygon = points_plate.reshape((-1, 1, 2))

yellow_bgr = (0, 255, 255)
# green_yellow_bgr = (0, 255, 127)
black_bgr = (0, 0, 0)

alpha_inside = 0.5
alpha_outside = 0.5


def draw_transparent_polygon(frame, green_yellow_bgr):
    height, width = frame.shape[:2]
    out_side_points = [[0, 0], [0, height]]
    for p in points_detect:
        out_side_points.append(p)
    out_side_points.append([width, height])
    out_side_points.append([width, 0])
    out_side_points = np.array(out_side_points, dtype=np.int32)

    frame_copy = frame.copy()
    frame_copy_2 = frame.copy()
    cv2.fillPoly(frame_copy_2, [out_side_points], black_bgr)
    cv2.fillPoly(frame_copy, [points_detect], yellow_bgr)
    cv2.fillPoly(frame_copy, [points_plate], green_yellow_bgr)
    res1 = cv2.addWeighted(frame, alpha_inside, frame_copy, 1 - alpha_inside, 0)
    res = cv2.addWeighted(res1, alpha_outside, frame_copy_2, 1 - alpha_outside, 0)
    return res
