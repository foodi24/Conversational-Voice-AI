from RealtimeTTS import TextToAudioStream, SystemEngine


def main():
    print("Starting TTS...")

    engine = SystemEngine()
    stream = TextToAudioStream(engine)

    text = "Hello! This is a test of Realtime Text to Speech."

    print("Speaking...")
    stream.feed(text)
    stream.play()

    print("TTS test finished.")


if __name__ == "__main__":
    main()