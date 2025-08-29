import requests
import os
import wave
from pathlib import Path
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import SpeechService
import time

class CosyVoiceAPIVoiceoverService(SpeechService):
    def __init__(self, api_base="http://localhost:8000", speaker="default", **kwargs):
        super().__init__(**kwargs)  # 会初始化 cache_dir
        self.api_base = api_base
        self.speaker = speaker

    def generate_from_text(self, text: str, **kwargs):
        speaker = kwargs.get("speaker", self.speaker)
        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "cosy2", "speaker": speaker}

        cached_result = self.get_cached_result(input_data, self.cache_dir)
        if cached_result is not None:
            return cached_result
        # 调用 /tts
        resp = requests.post(
            f"{self.api_base}/tts",
            params={"text": text, "speaker": speaker},
            timeout=60
        )
        resp.raise_for_status()
        data = resp.json()

        if "original_audio" not in data or not data["original_audio"]:
            raise RuntimeError("CosyVoice API 没有返回音频文件")
        
        remote_path = data["original_audio"]

        # 下载音频
        dl = requests.get(f"{self.api_base}/download", params={"file": remote_path}, timeout=60)
        dl.raise_for_status()

        # 保存到 cache_dir
        local_filename = f"cosyvoice_{hash(text)}.wav"
        local_path = Path(self.cache_dir) / local_filename
        with open(local_path, "wb") as f:
            f.write(dl.content)


        return {
            "input_text": text,
            "input_data": input_data,
            "original_audio": local_filename
        }

        
