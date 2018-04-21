#!/usr/bin/python3
from wit import Wit

client = Wit("YVOLR6LO6WZBEVFZX47XTMT4DIDZD7BS")
resp = None
with open('test.wav', 'rb') as f:
  resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
print('Yay, got Wit.ai response: ' + str(resp))
