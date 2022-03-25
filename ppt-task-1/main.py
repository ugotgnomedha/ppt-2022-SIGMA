from datetime import datetime, date

import cv2 as cv
import cv2.aruco as aruco
import numpy as np
import math
import socket
import base64
import os
import json

final_result = {}


def get_img():
    # socket_address = ('127.0.0.1', 5005)

    UDP_IP = os.environ['host']
    UDP_PORT = os.environ['port']

    # UDP_IP = "198.0.0.1"
    # UDP_PORT = 5005

    addr = (UDP_IP, int(UDP_PORT))

    BUFF_SIZE = 65536
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)

    client_socket.sendto(b'GET_IMG', addr)

    packet, _ = client_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet, ' /')
    npdata = np.fromstring(data, dtype=np.uint8)
    img = cv.imdecode(npdata, 1)

    return img


def writeJson():
    # Serializing json
    json_object = json.dumps(final_result)

    now = datetime.now()

    current_time = now.strftime("%H %M")

    today = date.today()

    date_ = today.strftime("%d %m %y")

    # Writing to .json
    with open("SIGMA_" + str(current_time) + "_" + str(date_) + ".json", "w", encoding="utf-8") as outfile:
        json.dump(final_result, outfile, ensure_ascii=False)


def drawLineFunc(x1, x2, y1, y2):
    if x1 != x2:
        tangalpha = (math.atan((y1 - y2) / (x1 - x2)) * 180) / math.pi
        atan_numbers = (y1 - y2) / (x1 - x2)
    elif x1 == x2:
        if y2 > y1:
            return 90
        else:
            return 270

    x1 = x2 - x1
    y1 = y2 - y1
    x2 = 10
    y2 = 0
    cosalpha = ((x1 * x2) + (y1 * y2)) / (math.sqrt(x1 ** 2 + y1 ** 2) * math.sqrt(x2 ** 2 + y2 ** 2))

    acos_numbers = cosalpha

    cosalpha = math.acos(cosalpha) * 180 / math.pi
    if acos_numbers >= 0 and atan_numbers >= 0:
        return cosalpha
    elif acos_numbers <= 0 and atan_numbers <= 0:
        return tangalpha + 180
    elif acos_numbers <= 0 and atan_numbers >= 0:
        return tangalpha + 180
    else:
        return 360 + tangalpha


def idQuantityParser(part_id, center):
    key_name = "unknown"
    if part_id == 14:
        if "Крышка лампы" in final_result:
            final_result.update({"Крышка лампы": {'quantity': final_result["Крышка лампы"]["quantity"] + 1}})
            final_result.update({"Стекло лампы": {'quantity': final_result["Крышка лампы"]["quantity"] + 1}})
        else:
            final_result.update(
                {"Крышка лампы": {'quantity': 1},
                 "Стекло лампы": {'quantity': 1}})
        key_name = "Крышка лампы"
    if part_id == 13:
        if "Основание лампы" in final_result:
            final_result.update({"Основание лампы": {'quantity': final_result["Основание лампы"]["quantity"] + 1}})
        else:
            final_result.update(
                {"Основание лампы": {'quantity': 1}})
        key_name = "Основание лампы"
    if part_id == 11:
        if "Винт М4" in final_result:
            final_result.update(
                {"Винт М4": {'quantity': final_result["Винт М4"]["quantity"] + 2,
                             'rotate': [final_result["Винт М6"]["rotate"], 0]}})
        else:
            final_result.update(
                {"Винт М4": {'quantity': 2, 'rotate': 0}})
        key_name = "Винт М4"

    if part_id == 12:
        if "Винт М6" in final_result:
            final_result.update(
                {"Винт М6": {'quantity': final_result["Винт М6"]["quantity"] + 2,
                             'rotate': [final_result["Винт М6"]["rotate"], 0]}})
        else:
            final_result.update(
                {"Винт М6": {'quantity': 2, 'rotate': 0}})
        key_name = "Винт М6"

    return key_name


def angleCount(coords):
    angle = math.atan(math.tan(coords[0] / coords[1])) * 180 / math.pi
    return angle


# def center_point(mask):
#     coords = []
#     contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#     # print("--------------------")
#     for cnt in contours:
#         approx = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
#         cv.drawContours(img, [approx], 0, 0, 1)
#         x = approx.ravel()[0]
#         y = approx.ravel()[1]
#         # The first order of the contours
#         # image moment
#         M = cv.moments(cnt)
#         # The centroid point
#         try:
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])
#         except ZeroDivisionError:
#             iii = 0
#         if 12 < len(approx) < 19 and len(cnt) > 65 or 9 < len(approx) < 13 and 70 < len(cnt) < 85:
#             cv.putText(img, "Конус", (x, y), font, 0.5, 0)
#             # print("Конус - 6")
#             print("Координаты:", cx, cy)
#             coords.append([cx, cy])
#             # print("")
#         elif 3 < len(approx) < 14 and 35 < len(cnt) < 110 or 3 < len(approx) < 9 and 10 < len(cnt) < 50:
#             cv.putText(img, "Пирамида", (x, y), font, 1, 0)
#             coords.append([cx, cy])
#     return coords


def second_scan(frame):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    # aruco.drawDetectedMarkers(frame, corners, ids)
    # aruco.drawDetectedMarkers(frame, rejectedImgPoints, borderColor=(100, 0, 240))

    struct0 = {}  # кординаты цетра метки
    struct1 = {}  # координаты края метки (левый верхний угол метки)
    struct2 = {}  # координаты края метки (первый элемент - левый верхний угол метки)

    centers = {}

    if (ids is None) == False:
        for i in range(len(corners)):
            X_Cent = (corners[i][0][0][0] + corners[i][0][1][0] + corners[i][0][2][0] + corners[i][0][3][0]) / 4
            Y_Cent = (corners[i][0][0][1] + corners[i][0][1][1] + corners[i][0][2][1] + corners[i][0][3][1]) / 4

            cv.circle(frame, (int(corners[i][0][0][0]), int(corners[i][0][0][1])), 5, (0, 0, 255), -1)

            angle = drawLineFunc(int(corners[i][0][0][0]), int(corners[i][0][3][0]), int(corners[i][0][0][1]),
                                 int(corners[i][0][3][1]))

            # fontScale
            fontScale = 1

            # Blue color in BGR
            color = (255, 0, 0)

            # Line thickness of 2 px
            thickness = 2

            cv.putText(frame, str(int(angle)), (int(corners[i][0][2][0]), int(corners[i][0][2][1])), font,
                       fontScale, color, thickness, cv.LINE_AA)

            cv.circle(frame, (int(corners[i][0][3][0]), int(corners[i][0][3][1])), 5, (0, 0, 150), -1)

            cv.circle(frame, (int(X_Cent), int(Y_Cent)), 5, (0, 0, 255), -1)

            struct0[ids[i][0]] = [X_Cent, Y_Cent]
            struct1[ids[i][0]] = [corners[i][0][0][0], corners[i][0][0][1]]
            struct2[ids[i][0]] = [[corners[i][0][0][0], corners[i][0][0][1]],
                                  [corners[i][0][1][0], corners[i][0][1][1]],
                                  [corners[i][0][2][0], corners[i][0][2][1]],
                                  [corners[i][0][3][0], corners[i][0][3][1]]]

            centers.update({ids[i][0]: [int(struct0[ids[i][0]][0]), int(struct0[ids[i][0]][1])]})
            key = idQuantityParser(ids[i], centers)

            if "rotate" in final_result[key].keys() and key != "Винт М6" and key != "Винт М4":
                final_result.update({final_result[key]: {'rotate': (final_result[key]["rotate"], int(angle))}})
            elif key != "Винт М6" and key != "Винт М4":
                final_result[key].update({'rotate': int(angle)})

            if key == "Основание лампы":
                coords_osnovanie = osnovanieCoords(int(corners[i][0][0][0]), int(corners[i][0][0][1]),
                                                   int(corners[i][0][1][0]), int(corners[i][0][1][1]), frame)
                if "coordinates" in final_result[key].keys():
                    final_result.update(
                        {final_result[key]: {'coordinates': (final_result[key]["coordinates"], coords_osnovanie)}})
                else:
                    final_result[key].update({'coordinates': coords_osnovanie})

            if key == "Крышка лампы":
                coords_steklo = stekloCoords(centers.get(ids[i][0]), angle, frame)

                if "coordinates" in final_result[key].keys():
                    final_result.update(
                        {final_result[key]: {'coordinates': (final_result[key]["coordinates"], coords_steklo)}})
                else:
                    final_result[key].update({'coordinates': coords_steklo})

    print(centers)
    print(final_result)
    cv.imshow("img", frame)
    cv.waitKey(0)
    return centers


def osnovanieCoords(x1, y1, x2, y2, frame):
    coords = [int(((x1 + x2) // 2) // 0.8), int(((y1 + y2) // 2) // 0.8)]
    # cv.circle(frame, [(x1+x2)//2, (y1+y2)//2], 5, (0, 0, 30), -1)
    return coords


def stekloCoords(aruco_center, angle, frame):
    coords = [int(aruco_center[0] / 0.8 - 110 * math.cos((270 - angle - 1) * math.pi / 180)),
              int(aruco_center[1] / 0.8 + 110 * math.sin((270 - angle + 2) * math.pi / 180))]
    # cv.circle(frame, [int(coords[0] * 0.8), int(coords[1] * 0.8)], 2, (255, 255, 255), -1)
    return coords


def krishkaCoords():
    coords = []
    return coords


def aruco_scan(frame):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    struct0 = {}  # кординаты цетра метки
    struct1 = {}  # координаты края метки (левый верхний угол метки)
    struct2 = {}  # координаты края метки (первый элемент - левый верхний угол метки)

    centers = {}

    if (ids is None) == False:
        for i in range(len(corners)):
            X_Cent = (corners[i][0][0][0] + corners[i][0][1][0] + corners[i][0][2][0] + corners[i][0][3][0]) / 4
            Y_Cent = (corners[i][0][0][1] + corners[i][0][1][1] + corners[i][0][2][1] + corners[i][0][3][1]) / 4

            struct0[ids[i][0]] = [X_Cent, Y_Cent]
            struct1[ids[i][0]] = [corners[i][0][0][0], corners[i][0][0][1]]
            struct2[ids[i][0]] = [[corners[i][0][0][0], corners[i][0][0][1]],
                                  [corners[i][0][1][0], corners[i][0][1][1]],
                                  [corners[i][0][2][0], corners[i][0][2][1]],
                                  [corners[i][0][3][0], corners[i][0][3][1]]]

            centers.update({ids[i][0]: [int(struct0[ids[i][0]][0]), int(struct0[ids[i][0]][1])]})
            # idQuantityParser(ids[i])

    return centers


def rotateImgAruco(image, aruco_coords):
    pt_A = aruco_coords[0]
    pt_B = aruco_coords[3]
    pt_C = aruco_coords[2]
    pt_D = aruco_coords[1]

    # Here, I have used L2 norm. You can use L1 also.
    width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
    width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
    # maxWidth = max(int(width_AD), int(width_BC))

    height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
    height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
    # maxHeight = max(int(height_AB), int(height_CD))

    input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
    maxHeight = int(350 * 0.8)
    maxWidth = int(400 * 0.8)
    output_pts = np.float32([[0, 0],
                             [0, maxHeight - 1],
                             [maxWidth - 1, maxHeight - 1],
                             [maxWidth - 1, 0]])

    # Compute the perspective transform M
    M = cv.getPerspectiveTransform(input_pts, output_pts)
    out = cv.warpPerspective(image, M, (maxWidth, maxHeight), flags=cv.INTER_LINEAR)
    cv.imshow("perspective", out)
    cv.waitKey(0)
    return out


font = cv.FONT_HERSHEY_COMPLEX
# img = cv.imread("/Users/darthvader/Desktop/Datasets/S_98.png")
img = get_img()
coords_aruco = aruco_scan(img)
cropped_image = rotateImgAruco(img, coords_aruco)
coords_aruco = second_scan(cropped_image)

writeJson()


# img_hsv = cv.cvtColor(cropped_image, cv.COLOR_BGR2HSV)
# threshold = cv.inRange(img_hsv, (10, 0, 0), (50, 255, 200))
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (4, 8))
# threshold = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
# cv.imshow("mask", threshold)
# cv.waitKey(0)
#
# coordinates = center_point(threshold)
# print(coordinates)
