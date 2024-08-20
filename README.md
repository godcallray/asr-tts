# Local talking assitant
Local ASR-LLM-TTS

Change the path to your own path!

Download Ollama to your own PC, Pull the model you need!

## If you are using Nvida GPU to run this, 

Add following code to file "chatollama.py" and "demo.py"

--
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
--

## How to use

Get into the direction of "demo.py", use the code python demo.py to run it.

# Cuda requirment

Cuda >= 11.8
Cuda toolkit follow Cuda version

# Ollama

Pull the model under Local GPT
