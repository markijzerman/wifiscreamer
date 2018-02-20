import boto3
import subprocess
from pyssml.PySSML import PySSML
from pyssml.AmazonSpeech import AmazonSpeech

s = PySSML()
session = boto3.Session(profile_name='default')
polly = session.client('polly')

# USE POLLY
# Alle documentatie nodig: http://docs.aws.amazon.com/polly/latest/dg/supported-ssml.html
# http://docs.aws.amazon.com/polly/latest/dg/voicelist.html
# <speak><prosody rate="x-slow">Hallo <prosody pitch="+80%">Adriaan.</prosody></prosody><amazon:effect name="whispered">Ik heb een beetje binnensmond gekotst van geluk zonet.</amazon:effect><prosody pitch="+80%"><prosody rate="x-slow">doe mij maar een hele <break time="0.1s"/> dikke <break time="0.1s"/> <prosody pitch="-80%">HEMA-worst.</prosody></prosody></prosody></speak>
# <speak> Zeb is een hele <amazon:effect name="whispered">fijne jongeman.</amazon:effect></speak>


good_attributes = {'rate': 'x-slow', 'pitch': 'low', 'volume': 'soft'}
bad_attribute = {'rate': 'slow', 'pitcher': 'high', 'volume': 'loud'}
bad_attribute2 = {'rate': {}, 'pitch': 'high', 'volume': 'loud'}
bad_value = {'rate': 'slow', 'pitch': 'Frank', 'volume': 'loud'}

s = AmazonSpeech()

s.sentence('Zeb is een hele')
s.whisper('fijne jongeman.')
s.spell_slowly('Zeb', '500ms')
s.whisper('Ik kom zachtjes een beetje in mijn broekje.')
s.prosody(good_attributes, 'Zebje.')

testNormal = '<speak>The pitch and timbre of a persons voice are connected in human speech. <amazon:effect vocal-tract-length="-15%"> If you are going to reduce the vocal tract length, </amazon:effect><amazon:effect vocal-tract-length="-15%"> <prosody pitch="+20%"> you might consider increasing the pitch, too. </prosody></amazon:effect> <amazon:effect vocal-tract-length="+15%"> If you choose to lengthen the vocal tract, </amazon:effect> <amazon:effect vocal-tract-length="+15%"> <prosody pitch="-10%"> you might also want to lower the pitch. </prosody></amazon:effect></speak>'

# spoken_text = polly.synthesize_speech(Text=testNormal, 
# OutputFormat ='mp3', 
# VoiceId='Ruben', 
# TextType='ssml')

spoken_text = s.ssml()

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

# PLAY MP3
subprocess.Popen(['mpg123', '-q', 'output.mp3']).wait()