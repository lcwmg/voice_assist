import speech_recognition as sr
import pyttsx3
import time

# 初始化语音识别器和文本到语音引擎
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# 函数：监听用户的语音命令
def listen():
    with sr.Microphone() as source:
        print("正在听...")
        recognizer.adjust_for_ambient_noise(source)  # 调整噪音
        audio = recognizer.listen(source)

    try:
        print("正在识别...")
        command = recognizer.recognize_google(audio, language='zh-CN').lower()
        print("您说：", command)
        return command
    except sr.UnknownValueError:
        print("抱歉，我没有听清楚。")
        return ""

# 函数：回应用户的语音
def speak(response):
    engine.say(response)
    engine.runAndWait()

# 函数：打开家电设备
def turn_on_appliance(appliance):
    # 发送命令以打开设备的代码
    print(f"正在打开 {appliance}...")
    speak(f"正在打开{appliance}...")

# 函数：调度关机命令
def schedule_shutdown(minutes):
    print(f"将在 {minutes} 分钟后关机...")
    speak(f"将在{minutes}分钟后关机...")
    time.sleep(minutes * 60)  # 将分钟转换为秒
    print("正在关机...")
    speak("正在关机...")

# 主函数：执行语音助手
def main():
    while True:
        command = listen()
        if "你好" in command:
            speak("你好！有什么可以帮您的吗？")
        elif "打开" in command:
            appliance = command.split("打开")[1].strip()
            turn_on_appliance(appliance)
        elif "定时关机" in command:
            minutes = int(command.split("定时关机")[1].strip())
            schedule_shutdown(minutes)
        elif "再见" in command:
            speak("再见！")
            break
        else:
            speak("抱歉，我不明白您说的是什么。")

if __name__ == "__main__":
    main()