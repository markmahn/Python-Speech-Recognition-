import speech_recognition as sr

recognizer = sr.Recognizer()

while (True):
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Recording ...")
        recorded_audio = None
        try:
            recorded_audio = recognizer.listen(source, timeout=10)
            print("Done recording")
        except Exception as ex:
            print("Sound of silence ...")


    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio,
                language="nl-NL"
            )

        print("You said: {}".format(text))
        if("{}".format(text) == 'exit'):
            print('exiting ...')
            break

    except Exception as ex:
        print("")

