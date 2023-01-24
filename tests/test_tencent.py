import unittest

from potencent.api.ocr import VatInvoiceOCR


class TestTencent(unittest.TestCase):

    def test_vin_ocr(self):
        VatInvoiceOCR(img_path=r'C:\Users\paste_2023-01-25_00-18-41.jpg')
