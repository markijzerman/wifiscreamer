import boto3
import subprocess
session = boto3.Session(profile_name='default')
polly = session.client('polly')

# USE POLLY
# Alle documentatie nodig: http://docs.aws.amazon.com/polly/latest/dg/supported-ssml.html
# <speak><prosody rate="x-slow">Hallo <prosody pitch="+80%">Adriaan.</prosody></prosody><amazon:effect name="whispered">Ik heb een beetje binnensmond gekotst van geluk zonet.</amazon:effect><prosody pitch="+80%"><prosody rate="x-slow">doe mij maar een hele <break time="0.1s"/> dikke <break time="0.1s"/> <prosody pitch="-80%">HEMA-worst.</prosody></prosody></prosody></speak>

text_to_speak = '<speak><prosody rate="x-slow">Hallo <prosody pitch="-80%">jongons.</prosody></prosody><amazon:effect name="whispered">.</amazon:effect><prosody pitch="+80%"><prosody rate="x-slow">doe mij maar een hele <break time="0.1s"/> dikke <break time="0.1s"/> <prosody pitch="-80%">HEMA-worst.</prosody></prosody></prosody></speak>'
spoken_text = polly.synthesize_speech(Text=text_to_speak, 
OutputFormat ='mp3', 
VoiceId='Ruben', 
TextType='ssml')

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

# PLAY MP3
subprocess.Popen(['mpg123', '-q', 'output.mp3']).wait()