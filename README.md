# manim voiceover接入cosyvoice2
1. 使用conda或venv配置manim环境，安装manim和manim voiceover
2. 按照 https://github.com/lixiang90/CosyVoice2SimpleAPI 的步骤拉取代码，配置CosyVoice2环境，下载模型并配置API
3. 在CosyVoice2环境中启动api，方法是在CosyVoice2SimpleAPI文件夹下使用`python cosy2.py`
4. 把本repo的 `manim_cosy2.py` 放到你想要开始撰写manim代码的文件夹下
5. 参考 `test1.py` 撰写合适的manim voiceover代码
```python
from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService  # Google TTS 示例
from manim_cosy2 import CosyVoiceAPIVoiceoverService

class VoiceoverExample(VoiceoverScene):
    def construct(self):
        # 选择语音合成服务
        self.set_speech_service(CosyVoiceAPIVoiceoverService(speaker="default"))
        # self.set_speech_service(GTTSService(lang="zh"))

        with self.voiceover(text="大家好，这是一个 Manim Voiceover 的示例。") as tracker:
            square = Square()
            self.play(Create(square), run_time=tracker.duration)
```
6. 如有需要，可以在CosyVoice2SimpleAPI项目中添加新的说话人，方法是首先在asset文件夹下添加说话音频样例，再在 `cosy2.py` 修改 `DEFAULT_SPEAKERS` 字典。
7. 使用命令 `python -m manim test1.py VoiceoverExample -p` （`test1.py` 换成你的文件名，`VoiceoverExample` 换成你的类名）生成并预览视频，此时视频含有使用CosyVoice2生成的音频。
