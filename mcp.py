import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True 
	print("say something mate ")
	audio = r.listen(source)
try:
	print("the audio file countains : " + r.recognize_google(audio))

except sr.unknownValueError:
	print("google speech Recognition could not understand audio")

except sr.RequestError as e:
		print("could not request results from google speech Recogition services; {0} ".format(e))				