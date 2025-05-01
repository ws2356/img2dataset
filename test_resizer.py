import sys
sys.path.insert(0, '/Users/ws2356/Developer/apps/img2dataset')
import io
from img2dataset.resizer import Resizer

rz = Resizer(256, 'keep_ratio', True)
with open('/Users/ws2356/Developer/apps/img2dataset/a0.heic.jpg', 'rb') as f:
    img_bytes = f.read()

byte_stream = io.BytesIO(img_bytes)

output_img_bytes, *_ = rz(byte_stream)

with open('/Users/ws2356/Developer/apps/img2dataset/a0.256.jpg', 'wb') as file:
    file.write(output_img_bytes)
    print('done')