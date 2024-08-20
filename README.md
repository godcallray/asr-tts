# Local talking assistant
Local ASR-LLM-TTS


## If you are using Nvidia GPU to run this, 

Add following code to file "chatollama.py" and "demo.py"


import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


## How to use

Go to link: https://alphacephei.com/vosk/models to download ASR model.

Use git clone https://huggingface.co/2Noise/ChatTTS to get TTS model.
cd into ChatTTS/asset, copy everything inside and paste is under ChatTTS

Get into the direction of "demo.py", use the code 'python demo.py' to run it.

Download Ollama to your own PC, Pull the model you need to the direction under file Local GPT.

Change the path to your own path!!!


WHen it is showing:
INFO:CHatTTS.core:All initialized

Press 'b' on keyboard to start recording
Press 's' on keyboard to stop recording
Press 'e' on keyboard to exit


# Cuda requirment

Cuda >= 11.8
Cuda toolkit follow Cuda version

