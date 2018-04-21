#!/usr/bin/python3
from wit import Wit
import os
import talkey

client = Wit(os.environ['WIT'])

def gettext(filename):
	resp = None
	with open(filename, 'rb') as f:
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

def record():
	import pyaudio
	import wave
	 
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"

	audio = pyaudio.PyAudio()
	
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print ("recording...")
	frames = []
	 
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	print ("finished recording")
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
	 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
