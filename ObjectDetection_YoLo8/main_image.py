from PIL import Image
from ultralytics import YOLO

model = YOLO('models/yolov8n.pt')
results = model('test/London.png')
for r in results:
    im_array = r.plot()
    im = Image.fromarray(im_array[..., ::-1])
    im.show()
    im.save('results/London-Results.png')