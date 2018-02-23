from random import randint
import boto3
import os
import subprocess
from pyssml.PySSML import PySSML
from pyssml.AmazonSpeech import AmazonSpeech

from access_points import get_scanner
wifi_scanner = get_scanner()

s = AmazonSpeech()
session = boto3.Session(profile_name='default')
polly = session.client('polly')

# Een zin, woord OF een geluid kunnen triggeren.
# Code roept een functie aan, er wordt een queue gemaakt van dingen om te zeggen...

normal = {'rate': 'medium', 'pitch': 'medium', 'volume': 'medium'}
low_and_slow = {'rate': 'x-slow', 'pitch': 'x-low', 'volume': 'soft'}
fast_and_high = {'rate': 'x-fast', 'pitch': 'x-high', 'volume': 'loud'}
test = {'rate': 'slow', 'pitch': 'low', 'volume': 'loud'}

foundWifiIntro = ['Ik zag net %s voorbij komen.', '%s is een vreemde naam voor een netwerk, denk je ook niet?', 'Wie zijn netwerk %s noemt, is gek.', 'ajajajajaj!... %s. Ik ga nog liever dood dan nog meer netwerken opnoemen.']


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

def findSSIDs():
    foundNetworks = dict((p["ssid"], p) for p in wifi_scanner.get_access_points())
    foundSSIDs = list()
    for i in foundNetworks.keys():
        foundSSIDs.append(i)
    return foundSSIDs

which_sentence = randint(0,(len(foundWifiIntro)-1))

# speakToMe(test, foundWifiIntro[3] % findSSIDs()[randint(0,(len(findSSIDs())-1))])
speakToMe(normal, foundWifiIntro[which_sentence] % findSSIDs()[randint(0,(len(findSSIDs())-1))])