# 156-2FA-QR_code-Identification

用于无法识别双因素认证（2FA）二维码的设备或软件

本项目是一个2FA 备用密钥提取工具，通过二维码解码技术，帮助用户从 2FA 二维码中提取出备用密钥（Secret Key），以便在无法直接扫描二维码的设备或软件中手动配置两步验证。

---

## 🎯 项目背景

许多网站开启两步验证（2FA）时，会提供一个二维码供认证器应用（如 Google Authenticator、Microsoft Authenticator 等）扫描绑定。然而，部分设备或软件不支持直接扫描二维码，导致用户无法完成绑定。

本项目正是为了解决这一问题——将二维码图片解码为文本格式的 otpauth URI，从中提取出密钥信息，方便用户手动输入。

---

## ✨ 功能特性

· 📷 上传二维码图片：支持从本地选择 2FA 二维码图片
· 🔍 自动解码识别：使用 OpenCV 二维码检测器解码二维码内容
· 📋 提取备用密钥：从 otpauth URI 中解析出密钥（Secret）
· 🖥️ 图形化界面：基于 PyWebView 构建，操作简单直观
· 🔒 纯本地运行：所有解码在本地完成，不上传任何数据，保障隐私安全

---

## 🛠️ 技术栈

组件 技术
后端 Python + PyWebView
二维码解码 OpenCV (cv2.QRCodeDetector)
图像处理 Pillow + NumPy
前端 HTML + JavaScript（位于 web/ 目录）

---

## 📦 安装与运行

### 1. 克隆仓库

```bash
git clone https://github.com/bCreeper156/156-2FA-QR_code-Identification.git
cd 156-2FA-QR_code-Identification
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
pip install -r requirements.txt
```

依赖列表：

· pywebview >= 4.0 — 桌面应用图形界面框架
· opencv-python >= 4.8 — 二维码解码
· Pillow >= 10.0 — 图像处理

### 3. 启动应用

```bash
python main.py
```

---

## 🚀 使用方法

1. 运行 python main.py 启动图形界面窗口
2. 点击界面上的上传按钮，选择包含 2FA 二维码的图片
3. 工具自动解码并显示提取出的 otpauth URI 及备用密钥
4. 复制密钥，在目标设备或软件中手动配置两步验证

---

## 📁 项目结构

```
156-2FA-QR_code-Identification/
├── main.py              # 主程序入口，PyWebView 后端逻辑[reference:4]
├── requirements.txt     # Python 依赖列表[reference:5]
├── web/
│   └── index.html       # 前端界面页面[reference:6]
└── LICENSE              # MIT 许可证
```

---

## 📄 许可证

本项目采用 MIT License 开源协议。

Copyright (c) 2026 bCreeper156

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## ⚠️ 免责声明

本工具仅供学习和辅助用途，请勿用于非法目的。使用本工具提取的密钥请妥善保管，避免泄露导致账户安全风险。
