import cv2 as cv
import cv2.aruco as aruco
import numpy as np
import math

final_result = {}


def angleCount(coords):
    angle = math.atan(math.tan(coords[0] / coords[1])) * 180 / math.pi
    return angle


def center_point(mask):
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]
    for contour in contours:
        # image moment
        M = cv.moments(contour)
        # The centroid point
        try:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        except ZeroDivisionError:
            print("exception in centroid point calculation")
    center = [cx, cy]
    return center


def aruco_scan(frame):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    aruco.drawDetectedMarkers(frame, corners, ids)
    aruco.drawDetectedMarkers(frame, rejectedImgPoints, borderColor=(100, 0, 240))

    struct0 = {}  # кординаты цетра метки
    struct1 = {}  # координаты края метки (левый верхний угол метки)
    struct2 = {}  # координаты края метки (первый элемент - левый верхний угол метки)

    centers = {}

    if (ids is None) == False:
        for i in range(len(corners)):
            X_Cent = (corners[i][0][0][0] + corners[i][0][1][0] + corners[i][0][2][0] + corners[i][0][3][0]) / 4
            Y_Cent = (corners[i][0][0][1] + corners[i][0][1][1] + corners[i][0][2][1] + corners[i][0][3][1]) / 4

            cv.circle(frame, (int(X_Cent), int(Y_Cent)), 5, (0, 0, 255), -1)

            struct0[ids[i][0]] = [X_Cent, Y_Cent]
            struct1[ids[i][0]] = [corners[i][0][0][0], corners[i][0][0][1]]
            struct2[ids[i][0]] = [[corners[i][0][0][0], corners[i][0][0][1]],
                                  [corners[i][0][1][0], corners[i][0][1][1]],
                                  [corners[i][0][2][0], corners[i][0][2][1]],
                                  [corners[i][0][3][0], corners[i][0][3][1]]]
            centers.update({ids[i][0]: [int(struct0[ids[i][0]][0]), int(struct0[ids[i][0]][1])]})

    print(centers)
    cv.imshow("img", frame)
    cv.waitKey(0)
    return centers
    # return [struct0, struct1, struct2]


def rotateImgAruco(image, aruco_coords):
    pt_A = aruco_coords[0]
    pt_B = aruco_coords[3]
    pt_C = aruco_coords[2]
    pt_D = aruco_coords[1]

    # Here, I have used L2 norm. You can use L1 also.
    width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
    width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
    maxWidth = max(int(width_AD), int(width_BC))

    height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
    height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
    maxHeight = max(int(height_AB), int(height_CD))

    input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
    output_pts = np.float32([[0, 0],
                             [0, maxHeight - 1],
                             [maxWidth - 1, maxHeight - 1],
                             [maxWidth - 1, 0]])

    # Compute the perspective transform M
    M = cv.getPerspectiveTransform(input_pts, output_pts)
    out = cv.warpPerspective(image, M, (maxWidth, maxHeight), flags=cv.INTER_LINEAR)
    cv.imshow("perspective", out)
    cv.waitKey(0)


img = cv.imread("/Users/darthvader/Documents/code/nti/NTI_PPT_final-master/Финал/preview.jpg")
coords_aruco = aruco_scan(img)
rotateImgAruco(img, coords_aruco)

final_result.update({"ABS": {'quantity': 2, 'coordinates': [(200, 200), (123, 123)]},
                     "CDC": {'quantity': 1, 'coordinates': [323, 232]}})

print(final_result)
