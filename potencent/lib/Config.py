# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 18:45 
@Description     ：
'''
import toml
from potencent.lib.CONST import DEFAULT_CONFIG_PATH_NAME


class potencentConfig():
    def __init__(self):
        self.config_info = None

    def get_config(self, configPath):
        """
        解析配置文件
        :param toml_path: 存放配置文件的位置和名称，在py文件的同级路径下
        :return: 加载后的信息
        """
        try:
            if configPath == None:
                self.config_info = toml.load(DEFAULT_CONFIG_PATH_NAME)
            else:
                self.config_info = toml.load(configPath)
            print('配置文件【potencent-config.toml】读取成功')
            return self.config_info
        except:
            print('配置文件【potencent-config.toml】读取失败，请查看视频，进行配置：https://www.bilibili.com/video/BV1Zv4y1r7zq')
