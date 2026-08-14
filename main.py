from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine
from langchain_ollama import ChatOllama


def main():
    print("Starting VoiceAI...")

    # Speech-to-Text
    recorder = AudioToTextRecorder()

    # Text-to-Speech
    engine = SystemEngine()
    stream = TextToAudioStream(engine)

    # Language Model
    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    print("VoiceAI is ready!")
    print("Speak something...")

    while True:
        try:
            # Listen to the user
            text = recorder.text()

            if not text.strip():
                continue

            print("You said:", text)

            # Send the text to Llama
            response = llm.invoke(text)
            answer = response.content

            print("AI:", answer)

            # Speak the response
            stream.feed(answer)
            stream.play()

            print("\nSpeak something else...")

        except KeyboardInterrupt:
            print("\nVoiceAI stopped.")
            break


if __name__ == "__main__":
    main()