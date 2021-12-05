from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
import time
import json
import streamlit as st
from streamlit import uploaded_file_manager

with open('secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

#自分がAPIを使う許可を得ているのかココで認証している
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def get_tags(filepath):
    local_image = open(filepath, "rb")

    #local画像タグの取得
    tags_result_local = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result_local.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

def detect_objects(filepath):
    local_image = open(filepath, "rb")
    #物体の検出
    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    #ローカルのファイルを扱いたい時は基本的にドキュメントよりメソッドに_in_streamを付ける
    objects = detect_objects_results.objects
    #メソッドを使用し、objectのリストを取得して変数に格納
    #ここにobject名と座標が入っている
    return objects

st.title("Object Detection App")

#ファイルのアップロード機能
uploaded_file = st.file_uploader('Choose an image ... ', type = ['jpg', 'png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    #描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype(font = './Helvetica 400.ttf', size = 50)
        text_w, text_h = draw.textsize(caption, font = font)
        draw.rectangle([(x,y), (x + w, y + h)], fill =None, outline = 'red', width = 5)
        draw.rectangle([(x,y), (x + text_w, y + text_h)], fill ='green')
        draw.text((x, y),caption, fill = 'white', font = font)

    st.image(img)

    tags_name = get_tags(img_path)
    tags_name = ", ".join(tags_name)
    st.markdown('**contents tags**')
    st.markdown(f'> {tags_name}')
