import speech_recognition as sr
# https://pypi.org/project/SpeechRecognition/
class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self):
        with self.mic as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio, language='zh-CN') # api
            # text = self.recognizer.recognize_sphinx(audio, language='zh-CN') # 本地，需要recognize_sphinx
            # 下载recognize_sphinx的中文语言包
            # https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst 
            # text = self.recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""


    def run(self):
        while True:
            command = self.listen()
            print("用户:"+command)
            if "你好" in command:
                print("系统:你好！")
                break

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()

