from tempfile import NamedTemporaryFile
from translate import Translator
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import os
import numpy as np
import pyaudio

texto = input("Texto a ser traduzido: ")
traduzir = input("Deseja traduzir para o inglês? (s/n): ")

if traduzir.lower() == "s":
    translator = Translator(from_lang="pt-br", to_lang="en")
    traduzido = translator.translate(texto)
    print("Texto traduzido:", traduzido)
    tts = gTTS(text=traduzido, lang="en")
else:
    traduzido = texto
    tts = gTTS(text=traduzido, lang="pt-br")

# Salva o arquivo de áudio em um arquivo temporário
with NamedTemporaryFile(suffix=".wav", delete=False) as fp:
    tts.write_to_fp(fp)

# Carrega o arquivo de áudio usando a biblioteca Pydub
audio = AudioSegment.from_wav(fp.name)

# Obtém os dados de áudio como bytes
audio_data = tts.get_bytes()

# Reproduz os dados de áudio usando a biblioteca PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(audio.sample_width),
                channels=audio.channels,
                rate=audio.frame_rate,
                output=True)
stream.write(audio_data)
stream.stop_stream()
stream.close()
p.terminate()

# Remove o arquivo temporário
os.remove(fp.name)


# translator = Translator(to_lang="en")
# translation = translator.translate("Olá mundo!")
# print(translation)


# {"key": "9d42841d7713f7410ab6"}
