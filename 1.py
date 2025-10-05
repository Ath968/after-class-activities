import cv2
import matplotlib.pyplot as plt

image_path = "🗿🗿🗿.png"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

rect1_w, rect1_h = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_w, top_left1[1] + rect1_h)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)

rect2_w, rect2_h = 200, 150
top_left2 = (width - rect2_w - 20, height - rect2_h - 20)
bottom_right2 = (top_left2[0] + rect2_w, top_left2[1] + rect2_h)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

center1 = (top_left1[0] + rect1_w // 2, top_left1[1] + rect1_h // 2)
center2 = (top_left2[0] + rect2_w // 2, top_left2[1] + rect2_h // 2)

cv2.circle(image_rgb, center1, 15, (0, 255, 0), -1)
cv2.circle(image_rgb, center2, 15, (255, 0, 0), -1)
cv2.line(image_rgb, center1, center2, (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, "Region 1", (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Region 2", (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Center 1", (center1[0] - 40, center1[1] + 40),font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Center 2", (center2[0] - 40, center2[1] + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

height_label_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f'Height: {height}px', height_label_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Bi-Directional Height Arrow')
plt.axis('off')
plt.show()
