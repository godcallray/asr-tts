import ChatTTS
import torch
import torchaudio
import soundfile
import time
import torch
import random

from modelscope import snapshot_download

module_name = "chatutil"

MODELPATH = "<Path of ChatTTS>"
class ChatTTSUtil:
    def __init__(self ,
                 modelPath = MODELPATH,
                 saveFilePath = "output/" ,
                 fixSpkStyle = True):
        self.modelPath = modelPath
        self.wavfilePath = saveFilePath
        self.fixSpkStyle = fixSpkStyle
        print(self.modelPath)
        self.chat = ChatTTS.Chat()
        self.chat.load_models(local_path = modelPath)
        self.params_refine_text = {"prompt": "[oral_0][laugh_0][break_0]"}
        # Config the speech style with random generation
        std , mean = torch.load(f"{MODELPATH}/spk_stat.pt").chunk(2)
        rand_spk = torch.randn(768) * std + mean
        self.params_infer_code = {
            "spk_emb": rand_spk,
            "temperature": .3,
            "top_P": 0.7,
            "top_K": 20,
            "prompt": "[speed_5]"
        }

    def setRefineTextConf(self , oralConf = "[oral_0]" , laughConf = "[laugh_0]" , breakConf = "[break_0]"):
        self.params_refine_text = {"prompt": f"{oralConf}{laughConf}{breakConf}"}

    def setInferCode(self , temperature = 0.3 , top_P = 0.7 , top_K = 20 , speed = "[speed_5]"):
        self.params_infer_code["temperature"] = temperature
        self.params_infer_code["top_P"] = top_P
        self.params_infer_code["top_K"] = top_K
        self.params_infer_code["prompt"] = speed

    def generateSound(self , texts , savePath = "output/" , filePrefix = "output"):
        wavs = self.chat.infer(texts , use_decoder = True , params_refine_text = self.params_refine_text , params_infer_code = self.params_infer_code)
        wavFilePath = []
        for (index, wave) in enumerate(wavs):
            soundfile.write(f"{savePath}{filePrefix}{index}.wav" , wave[0] , 24000)
            wavFilePath.append(f"{savePath}{filePrefix}{index}.wav")
        return wavFilePath

if __name__ == "__main__":
    chUtil = ChatTTSUtil()
    chUtil.setInferCode(0.8 , 0.7 , 20 , speed = "[speed_3]")
    chUtil.generateSound(texts)
