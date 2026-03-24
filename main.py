from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
# Texto original (português)
texto = "Olá eu sou o Theo e estou gerando áudios no python"

# 1. Traduz para inglês e para o espanhol
traduzido = GoogleTranslator(source='pt', target='en').translate(texto)
traduzido2 = GoogleTranslator(source='pt', target='es').translate(texto)

print("Tradução em inglês:", traduzido)
print("Tradução em espanhol:", traduzido2)

# 2. Gera áudio em inglês
tts = gTTS(text=traduzido, lang='en')
tts.save("audio_en.mp3")

# 3. Gera áudio em espanhol
tts = gTTS(text=traduzido2, lang='es')
tts.save("audio_es.mp3")

# 4. Toca o áudio
os.system("start audio_en.mp3")
time.sleep(7)
os.system("start audio_es.mp3")