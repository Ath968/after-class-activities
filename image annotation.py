import cv2
import numpy as np


image = np.ones((400, 600, 3), dtype=np.uint8) * 255


start_point = (150, 150)
end_point = (450, 300)
cv2.rectangle(image, start_point, end_point, (0, 0, 255), 2)


width = end_point[0] - start_point[0]
height = end_point[1] - start_point[1]


cv2.arrowedLine(image, (start_point[0], end_point[1] + 30),(end_point[0], end_point[1] + 30), (255, 0, 0), 2, tipLength=0.05)
cv2.arrowedLine(image, (end_point[0], end_point[1] + 30),(start_point[0], end_point[1] + 30), (255, 0, 0), 2, tipLength=0.05)


cv2.putText(image, f'Width: {width}px', (start_point[0] + 50, end_point[1] + 60),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


cv2.arrowedLine(image, (end_point[0] + 30, start_point[1]),(end_point[0] + 30, end_point[1]), (0, 255, 0), 2, tipLength=0.05)
cv2.arrowedLine(image, (end_point[0] + 30, end_point[1]),(end_point[0] + 30, start_point[1]), (0, 255, 0), 2, tipLength=0.05)


cv2.putText(image, f'Height: {height}px', (end_point[0] + 40, start_point[1] + 80),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


cv2.imshow("Annotated Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
