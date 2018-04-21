#!/usr/bin/python3
from wit import Wit
import os
import talkey

client = Wit(os.environ['WIT'])

def gettext():
	resp = None
	with open('test.wav', 'rb') as f:
		resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
	return resp

def say(text):
	import json
	from watson_developer_cloud import TextToSpeechV1

	text_to_speech = TextToSpeechV1(
    	username=os.environ['WATSON_USER'],
    	password=os.environ['WATSON_PASS'])

	with open('output.wav','wb') as audio_file:
		audio_file.write( text_to_speech.synthesize(text, accept='audio/wav',voice="en-US_AllisonVoice").content)
	play('output.wav')

def play(filename):
	import wave, sys, pyaudio
	wf = wave.open(filename)
	p = pyaudio.PyAudio()
	chunk = 1024
	stream = p.open(format =
					p.get_format_from_width(wf.getsampwidth()),
					channels = wf.getnchannels(),
					rate = wf.getframerate(),
					output = True)
	data = wf.readframes(chunk)
	while data:
		stream.write(data)
		data = wf.readframes(chunk)

	stream.stop_stream()
	stream.close()
	p.terminate()
