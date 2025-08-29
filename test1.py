from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService  # Google TTS 示例
from cosy2 import CosyVoiceAPIVoiceoverService

class VoiceoverExample(VoiceoverScene):
    def construct(self):
        # 选择语音合成服务
        self.set_speech_service(CosyVoiceAPIVoiceoverService(speaker="default"))
        # self.set_speech_service(GTTSService(lang="zh"))

        with self.voiceover(text="大家好，这是一个 Manim Voiceover 的示例。") as tracker:
            square = Square()
            self.play(Create(square), run_time=tracker.duration)
