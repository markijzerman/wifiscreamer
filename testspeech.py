import boto3
import os
import subprocess
from pyssml.PySSML import PySSML
from pyssml.AmazonSpeech import AmazonSpeech

# s = PySSML()
session = boto3.Session(profile_name='default')
polly = session.client('polly')

# Een zin, woord OF een geluid kunnen triggeren.
# Code roept een functie aan, er wordt een queue gemaakt van dingen om te zeggen...


low_and_slow = {'rate': 'x-slow', 'pitch': 'x-low', 'volume': 'soft'}
fast_and_high = {'rate': 'x-fast', 'pitch': 'x-high', 'volume': 'loud'}

s = AmazonSpeech()

def speakToMe(style, words):
    s.prosody(style, words)
    spoken_text = polly.synthesize_speech(Text=s.ssml(), 
    OutputFormat ='mp3', 
    VoiceId='Lotte', 
    TextType='ssml')
    playSound(spoken_text)

def playSound(spoken_text):
    with open('output.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()
    # PLAY MP3
    subprocess.Popen(['mpg123', '-q', 'output.mp3']).wait()

speakToMe(low_and_slow, 'Zeb Stevens, wat een man is het toch.')