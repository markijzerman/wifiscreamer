import boto3
import subprocess
from pyssml.PySSML import PySSML
s = PySSML()
session = boto3.Session(profile_name='default')
polly = session.client('polly')

# USE POLLY
# Alle documentatie nodig: http://docs.aws.amazon.com/polly/latest/dg/supported-ssml.html
# http://docs.aws.amazon.com/polly/latest/dg/voicelist.html
# <speak><prosody rate="x-slow">Hallo <prosody pitch="+80%">Adriaan.</prosody></prosody><amazon:effect name="whispered">Ik heb een beetje binnensmond gekotst van geluk zonet.</amazon:effect><prosody pitch="+80%"><prosody rate="x-slow">doe mij maar een hele <break time="0.1s"/> dikke <break time="0.1s"/> <prosody pitch="-80%">HEMA-worst.</prosody></prosody></prosody></speak>

good_attributes = {'rate': 'x-slow', 'pitch': 'low', 'volume': 'soft'}
bad_attribute = {'rate': 'slow', 'pitcher': 'high', 'volume': 'loud'}
bad_attribute2 = {'rate': {}, 'pitch': 'high', 'volume': 'loud'}
bad_value = {'rate': 'slow', 'pitch': 'Frank', 'volume': 'loud'}


s.prosody(good_attributes, 'helicopter')
s.say('add something')
s.prosody(good_attributes, 'another thing')


spoken_text = polly.synthesize_speech(Text=s.ssml(), 
OutputFormat ='mp3', 
VoiceId='Joey', 
TextType='ssml')

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

# PLAY MP3
subprocess.Popen(['mpg123', '-q', 'output.mp3']).wait()