import cv2
import urllib.request
import numpy as np

url = "http://192.168.170.75:80"  # Ganti dengan alamat IP ESP32-CAM Anda

while True:
    try:
        img_resp = urllib.request.urlopen(url)
        img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        img = cv2.imdecode(img_np, -1)

        cv2.imshow("ESP32-CAM Video", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print("Error:", e)
        break

cv2.destroyAllWindows()
