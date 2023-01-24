# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 15:23
@Description     ：
'''

from potencent.core.OCR import OCR
from potencent.lib.CommonUtils import img2base64


def get_ocr(configPath):
    ocr = OCR()
    ocr.set_config(configPath)
    return ocr


def VatInvoiceOCR(img_path=None, configPath=None):
    ocr = get_ocr(configPath)
    ImageBase64 = img2base64(img_path)
    ocr_res = ocr.VatInvoiceOCR(ImageBase64)
    print(ocr_res)
    return ocr_res
