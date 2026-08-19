# -*- coding: utf-8 -*-
"""
2FA 备用密钥提取工具 - PyWebView 版本
使用 OpenCV 解码二维码，无外部 DLL 依赖
MIT License
Copyright (c) 2026
"""

import webview
import base64
import io
import os
import sys
import numpy as np
from PIL import Image
import cv2


def resource_path(relative_path):
    """获取资源的绝对路径，兼容开发环境和 PyInstaller 打包后"""
    try:
        # PyInstaller 打包后，资源会解压到 sys._MEIPASS 临时目录
        base_path = sys._MEIPASS
    except AttributeError:
        # 开发环境下，使用当前工作目录
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Api:
    """暴露给 JavaScript 的 API 类（无需装饰器，所有方法默认暴露）"""

    def decode_qr_from_image(self, data_url):
        """
        接收前端传来的图片 Base64 数据，使用 OpenCV 解码二维码
        返回解码后的文本字符串，如果失败则返回 None
        """
        try:
            # 去除 Base64 前缀（例如 "data:image/png;base64,"）
            if ',' in data_url:
                _, encoded = data_url.split(',', 1)
            else:
                encoded = data_url

            # 解码 Base64 数据
            image_data = base64.b64decode(encoded)
            image = Image.open(io.BytesIO(image_data))

            # 将 PIL Image 转换为 OpenCV 格式 (BGR)
            image_rgb = np.array(image.convert('RGB'))
            image_cv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            # 使用 OpenCV 二维码检测器
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecode(image_cv)

            if data:
                return data
            else:
                return None
        except Exception as e:
            print(f"[Python] 解码错误: {e}")
            return None

    def parse_otp_uri(self, text):
        """
        保留此接口，但前端已实现完整的 URI 解析，此处仅做占位。
        """
        return {"status": "not_used"}


if __name__ == '__main__':
    api = Api()
    # 获取打包后 HTML 文件的实际路径
    html_path = resource_path('web/index.html')
    
    window = webview.create_window(
        title='2FA 备用密钥提取工具',
        url=html_path,          # 使用动态获取的路径
        width=820,
        height=950,
        resizable=True,
        js_api=api,
        confirm_close=True,
    )
    webview.start(debug=False)  # 开发时可设为 True 打开开发者工具