import base64

from potencent.lib.Config import potencentConfig

from potencent.lib.CommonUtils import get_error_info

import json

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models


class OCR(potencentConfig):
    def __init__(self):
        self.TENCENT_AI_CFG = None
        self.TENCENTCLOUD_SECRET_ID = None
        self.TENCENTCLOUD_SECRET_KEY = None
        self.CLIENT = None

    def set_config(self, configPath):
        self.TENCENT_AI_CFG = self.get_config(configPath)
        if self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_ID'] and self.TENCENT_AI_CFG['tencent-ai'][
            'TENCENTCLOUD_SECRET_KEY']:
            self.TENCENTCLOUD_SECRET_ID = self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_ID']
            self.TENCENTCLOUD_SECRET_KEY = self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_KEY']
        cred = credential.Credential(self.TENCENTCLOUD_SECRET_ID, self.TENCENTCLOUD_SECRET_KEY)

        httpProfile = HttpProfile()

        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()

        clientProfile.httpProfile = httpProfile

        self.client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
        return self.client

    def VatInvoiceOCR(self, ImageBase64):
        """
        增值税发票的识别
        :return:
        """

        try:

            req = models.VatInvoiceOCRRequest()

            params = '{\"ImageBase64\":\"%s\"} ' % ImageBase64

            req.from_json_string(params)

            resp = self.client.VatInvoiceOCR(req)
            return resp

        except TencentCloudSDKException as err:
            print(err)
