#!/usr/bin/python3
from wit import Wit
import os

client = Wit(os.environ['WIT'])
resp = None
with open('test.wav', 'rb') as f:
  resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
print('Yay, got Wit.ai response: ' + str(resp))
