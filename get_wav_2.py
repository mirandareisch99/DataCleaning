import base64, os, sys, csv
import shutil
import pandas as pd
import psycopg2
import json
import re as re


# this function converts the csv file we export from database to audio files (.3gp and .wav)
# file: input csv file path
# a_open: whether the csv file is for open response voice sample

def make_wav():





    gp3s = "audio3_3GPs"
    wav = "audio3_WAVs_new"
    gp3s_2 = "audio4_3GPs"
    wav_2 = "audio4_WAVs_new"
    gp3_audio3_folder = os.path.join("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs", gp3s)
    wav_audio3_folder = os.path.join("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs", wav)
    gp3_audio4_folder = os.path.join("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs", gp3s_2)
    wav_audio4_folder = os.path.join("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/wavs", wav_2)
    if os.path.exists(gp3_audio3_folder):
        shutil.rmtree(gp3_audio3_folder)
    if os.path.exists(wav_audio3_folder):
        shutil.rmtree(wav_audio3_folder)
    if os.path.exists(gp3_audio4_folder):
        shutil.rmtree(gp3_audio4_folder)
    if os.path.exists(wav_audio4_folder):
        shutil.rmtree(wav_audio4_folder)

    os.makedirs(gp3_audio3_folder)
    os.makedirs(wav_audio3_folder)
    os.makedirs(gp3_audio4_folder)
    os.makedirs(wav_audio4_folder)

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=emudata user=qa3ad23 password=cvV-awq-K6L-fdg host=localhost port=5432")
    print("connected")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    audio = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts_short.csv")
    id = audio.sessionid.to_list()
    ids = []
    for i in id:
        x = i.split(".")
        var = x[0]
        ids.append(var)
    cur = conn.cursor()
    # Execute a query
    for ele in ids:
        values = []
        values2 = []
        cur.execute(
            "SELECT DISTINCT json from data where type like %s and source like %s and sessionid like %s ESCAPE '' ",
            ('audio_open3', 'summerDepreST', ele))


        ids = []

        for row in cur:
            if not ('!DOCTYPE' in row[0]):
                audiodataitem = json.loads(row[0])
                try:
                    session = audiodataitem['sessionid']
                    session = session.split('_')[-1]

                    ids.append(session)

                    content = audiodataitem['content']

                    gp3_file = os.path.join(os.getcwd(), gp3_audio3_folder, (session + '.3gp'))

                    wav_file = os.path.join(os.getcwd(), wav_audio3_folder, (session + '.wav'))

                    print(gp3_file)
                    decoded_bytestream = base64.b64decode(content)
                    print()
                    fh = open(wav_file, "wb")
                    fh.write(decoded_bytestream)
                    fh.close()

                    os.chdir("../../../")
                except:
                    continue

        cur.execute(
            "SELECT DISTINCT json from data where type like %s and source like %s and sessionid like %s ESCAPE '' ",
            ('audio_open4', 'summerDepreST', ele))

        ids2 = []
        for row in cur:
            if not ('!DOCTYPE' in row[0]):
                audiodataitem = json.loads(row[0])
                try:
                    session = audiodataitem['sessionid']
                    session = session.split('_')[-1]

                    ids2.append(session)
                    content = audiodataitem['content']

                    gp3_file = os.path.join(os.getcwd(), gp3_audio4_folder, (session + '.3gp'))

                    wav_file = os.path.join(os.getcwd(), wav_audio4_folder, (session + '.wav'))
                    print(gp3_file)
                    decoded_bytestream = base64.b64decode(content)
                    print()
                    fh = open(wav_file, "wb")
                    fh.write(decoded_bytestream)
                    fh.close()

                    os.chdir("../../../")
                except:
                    continue


make_wav()