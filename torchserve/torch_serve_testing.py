import requests
import cv2


url = "http://172.17.13.16:8443/predictions/RFB_320"

image_path = 'imgs/16.jpg'
with open(image_path, 'rb') as fs1:
  data = fs1.read()

payload=data
headers = {
  'Content-Type': 'image/jpeg'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
result_path = 'imgs/16.jpg' + '.mod'
orig_image = cv2.imread(image_path)
image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)

boxes, labels, probs = response.json()[0].values()

for i in range(len(boxes)):
  box = boxes[i]
  cv2.rectangle(orig_image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 0, 255), 2)
  # label = f"""{voc_dataset.class_names[labels[i]]}: {probs[i]:.2f}"""
  label = f"{probs[i]:.2f}"
  # cv2.putText(orig_image, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.putText(orig_image, str(len(boxes)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv2.imwrite(result_path, orig_image)
print(f"Found {len(probs)} faces. The output image is {result_path}")