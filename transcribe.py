import speech_recognition as sr
import os
import random
from os import path
from pydub import AudioSegment
import librosa
import soundfile as sf
import pandas as pd
from random import randrange
# convert mp3 file to wav
#sound = AudioSegment.from_mp3("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs/audio1_WAVs/audio1_0a49a4094fb8e024VE7L3751Z_30.mp3")
#sound.export("transcript.wav", format="wav")
audio1_directory = "/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs/audio3_WAVs_short"
filenames_1 = os.listdir(audio1_directory)


script_1 = []
for file in filenames_1:
        x,_ = librosa.load(audio1_directory + "/" + file, sr=16000)
        sf.write('tmp.wav', x, 16000)

        # transcribe audio file
        AUDIO_FILE = "tmp.wav"
        print("collected")
        # use the audio file as the audio source
        r = sr.Recognizer()
        print("recognized")
        with sr.AudioFile(AUDIO_FILE) as source:
                print("start")
                audio = r.record(source)  # read the entire audio file
                try:
                        script_1.append(r.recognize_google(audio))
                        print("Transcription: " + r.recognize_google(audio))
                except:
                        script_1.append("error")
                        print("error")


df_1 = pd.DataFrame()
df_1["File_Name"] = filenames_1
df_1["Transcript"] = script_1

audio2_directory = "/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs/audio4_WAVs_short"
filenames_2 = os.listdir(audio2_directory)
script_2 = []
for file in filenames_2:
        x,_ = librosa.load(audio2_directory + "/" + file, sr=16000)
        sf.write('tmp.wav', x, 16000)

        # transcribe audio file
        AUDIO_FILE = "tmp.wav"
        print("collected")
        # use the audio file as the audio source
        r = sr.Recognizer()
        print("recognized")
        with sr.AudioFile(AUDIO_FILE) as source:
                print("start")
                audio = r.record(source)  # read the entire audio file
                try:
                        script_2.append(r.recognize_google(audio))
                        print("Transcription: " + r.recognize_google(audio))
                except:
                        script_2.append("error")
                        print("error")

df_2 = pd.DataFrame()
df_2["File_Name"] = filenames_2
df_2["Transcript"] = script_2

df_1.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts_short.csv")
df_2.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio4_scripts_short.csv")
