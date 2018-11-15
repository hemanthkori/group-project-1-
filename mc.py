import speech_recognition as sr 

AUDIO_FILE = ("example1.wav")


r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:

	audio = r.record(source)
try:
	print("the audio file countains : " + r.recognize_google(audio))

except sr.unknownValueError:
	print("google speech Recognition could not understand audio")

except sr.RequestError as e:
		print("could not request results from google speech Recogition services; {0} ".format(e))			