import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

folder_path = r"C:\Users\kiki\PycharmProjects\Procore Bot System"
image_file = 'Test Pic.jpg'

file_path = os.path.join(folder_path, image_file)

with io.open(file_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text
print(docText)


