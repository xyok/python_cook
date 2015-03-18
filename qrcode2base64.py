#!/usr/bin/env python
#-*- coding: utf-8 -*-

#将url生成二维码，并编码成base64
#用到第三方库qrcode

import qrcode
from base64 import b64encode

def generate_img(data):
    qr = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_Q,
        box_size = 10,
        border = 1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert('RGBA')
    img.save('qrcode.png')

def img2base(img_path):
    with open(img_path,'rb') as imgfile:
        data = imgfile.read()
        text = open('qrcode.txt','w+')
        text.write(b64encode(data))
        text.close()

if __name__=='__main__':
    filename = r'qrcode.png'
    url = raw_input('please input url:')
    generate_img(url)
    img2base(filename)
