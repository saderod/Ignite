import pytesseract
from PIL import Image
import os, io
from google.cloud import vision
from google.cloud.vision import types
import re


# this finds all jpg images in the python folder and places in the the list called pic_list
images_in_python_folder = os.listdir("c:/Users/kiki/PycharmProjects/Procore Bot System")
pic_list = []
for a in entries:
    if a.endswith(".jpg"):
        pic_list.append(a)


# for some reason you need this line to make pytesseract work
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


# this allows you to use google cloud vision, needed to "read" the handwriting on the text
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

# this is the image name along with the folder its located in

for analyzed_image in pic_list:
    folder_path = r"C:\Users\kiki\PycharmProjects\Procore Bot System"
    image_file = analyzed_image

    # this creates a path from the statement above
    file_path = os.path.join(folder_path, image_file)

    # this loads the image into the IDE
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    # this formats the image so google cloud vision can analyze it
    image = vision.types.Image(content=content)

    # this puts the image into the google cloud vision engine
    response = client.document_text_detection(image=image)

    # these are the results of the vision scan
    docText = response.full_text_annotation.text

    # can use multiple if or elif statements to filter
    if "Drewall" in docText:
        print("found Drewall")
        # this is where you choose what to rename the image, left old name and the right is the new name
        os.rename(analyzed_image, 'MacDrywall.jpg')
    else:
        print("no")
        print(docText)

# this is where you choose what to rename the image, left old and the right is the new
# os.rename('image005.jpg', 'image3.jpg')


