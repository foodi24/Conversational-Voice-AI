from RealtimeSTT import AudioToTextRecorder


def main():
    print("Starting microphone...")
    print("Speak something.")

    recorder = AudioToTextRecorder()

    while True:
        text = recorder.text()
        print("You said:", text)


if __name__ == "__main__":
    main()