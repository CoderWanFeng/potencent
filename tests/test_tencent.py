import unittest

from potencent.api.ocr import *


class TestTencent(unittest.TestCase):

    def test_vin_ocr(self):
        VatInvoiceOCR(img_path=r'C:\Users\paste_2023-01-25_00-18-41.jpg')

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg',
            configPath=r'D:\test\py310\potencent-test\potencent-config.toml')
        print(res)