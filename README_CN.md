本地语音助手

本地 ASR-LLM-TTS

如果您使用 Nvidia GPU 来运行它，

将以下代码添加到文件“chatollama.py”和“demo.py”

import torch device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



如何使用

转到链接：https://alphacephei.com/vosk/models 下载 ASR 模型。

使用 git clone https://huggingface.co/2Noise/ChatTTS 获取 TTS 模型。cd 进入 ChatTTS/asset，复制里面的所有内容并粘贴在 ChatTTS 下

进入“demo.py”的方向，使用代码“python demo.py”运行它。

将 Ollama 下载到您自己的电脑上，将您需要的模型拉到文件 LocalGPT 下。

将路径更改为您自己的路径！！！

当它显示：INFO:CHatTTS.core:All initialized

按键盘上的“b”开始录制 按键盘上的“s”停止录制 按键盘上的“e”退出



Cuda 要求

Cuda >= 11.8 Cuda 工具包遵循 Cuda 版本
