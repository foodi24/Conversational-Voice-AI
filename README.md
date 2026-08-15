# 🎙️ VoiceAI — Speech-to-Text, LLM, and Text-to-Speech

## 📌 Project Overview

This project implements a **VoiceAI assistant** that receives audio input from a microphone, converts the speech into text, sends the text to a Large Language Model (LLM) to generate a response, and finally converts the generated response back into audio.

The project was developed to fulfill the following requirements:

1. 🎤 Convert audio input into text.
2. 🧠 Generate a response using an LLM.
3. 🔊 Convert the generated response into audio.
4. 📂 Upload the project files to GitHub with an explanation of the implementation steps.

---

## ⚙️ How the System Works

The VoiceAI system follows this pipeline:

**🎤 Microphone Input**
↓
**📝 Speech-to-Text (RealtimeSTT)**
↓
**🧠 Large Language Model (Ollama + Llama 3.2)**
↓
**💬 Generated Text Response**
↓
**🔊 Text-to-Speech (RealtimeTTS)**
↓
**🔈 Audio Output**

The user speaks into the microphone, the speech is converted into text, the text is processed by the LLM, and the response is spoken aloud by the computer.

---

## 🛠️ Technologies Used

### Python

The main programming language used to develop the project.

### RealtimeSTT

Used to capture audio from the microphone and convert spoken language into text.

### Ollama

Used to run the LLM locally.

### Llama 3.2

The language model used to generate responses to the user's speech.

### LangChain

Used to communicate with the Ollama model through `ChatOllama`.

### RealtimeTTS

Used to convert the LLM's text response into spoken audio.

### FFmpeg

Required by the audio-processing components of the project.

---

## 📁 Project Structure

```text
VoiceAI/
│
├── main.py
├── test_stt.py
├── test_tts.py
├── test_llm.py
└── README.md
```

### File Description

| File          | Description                                           |
| ------------- | ----------------------------------------------------- |
| `main.py`     | Main VoiceAI application connecting STT, LLM, and TTS |
| `test_stt.py` | Tests microphone input and speech-to-text             |
| `test_tts.py` | Tests text-to-speech output                           |
| `test_llm.py` | Tests the Llama 3.2 LLM through Ollama                |
| `README.md`   | Project documentation and implementation steps        |

---

# 🚀 Installation and Setup

## 1. Install Python

Install Python 3 on the computer and make sure Python is available from the Command Prompt.

Verify the installation:

```cmd
python --version
```

---

## 2. Create the Project Folder

Create a folder for the project, for example:

```text
VoiceAI
```

Open Command Prompt inside the project folder.

---

## 3. Create a Virtual Environment

Create a Python virtual environment:

```cmd
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

After activation, `(venv)` should appear at the beginning of the Command Prompt.

---

## 4. Install the Required Python Packages

Install the required packages:

```cmd
pip install RealtimeSTT RealtimeTTS langchain-ollama pydub
```

These packages provide the speech recognition, speech synthesis, LLM integration, and audio processing functionality required by the project.

---

# 🎵 5. Install FFmpeg

FFmpeg is required for audio processing.

After installing FFmpeg, verify that Windows can find it:

```cmd
where ffmpeg
```

The project was tested with FFmpeg located at:

```text
C:\ffmpeg\bin\ffmpeg.exe
```

Then verify the installation:

```cmd
ffmpeg -version
```

If the FFmpeg version information appears, FFmpeg is installed correctly.

---

# 🧠 6. Install and Set Up Ollama

Ollama is used to run the LLM locally.

After installing Ollama, download the Llama 3.2 model:

```cmd
ollama pull llama3.2
```

The model can then be used by the Python application through `ChatOllama`.

---

# 🧪 Testing the Individual Components

Before running the complete VoiceAI system, each component was tested separately.

## 🎤 Speech-to-Text Test

Run:

```cmd
python test_stt.py
```

The program starts the microphone and waits for speech.

Example:

```text
Starting microphone...
Speak something.
You said: Hello, this is a test.
```

This confirms that the microphone and speech-to-text system are working correctly.

---

## 🔊 Text-to-Speech Test

Run:

```cmd
python test_tts.py
```

The computer should speak the generated test sentence.

Example output:

```text
Starting TTS...
Speaking...
TTS test finished.
```

This confirms that the text-to-speech system is working correctly.

---

## 🧠 LLM Test

Run:

```cmd
python test_llm.py
```

The program sends a test prompt to Llama 3.2 through Ollama and displays the generated response.

This confirms that the LLM is correctly installed and accessible from Python.

---

# ▶️ Running the Complete VoiceAI System

After successfully testing the individual components, run:

```cmd
python main.py
```

The program displays:

```text
Starting VoiceAI...
VoiceAI is ready!
Speak something...
```

The user can then speak into the microphone.

For example:

```text
You said: Hello.
AI: Hello! How can I assist you today?
```

The AI response is then converted into audio and spoken by the computer.

The user can continue speaking and interacting with the VoiceAI system.

---

# 🔄 Complete Processing Flow

The complete process can be summarized as:

### Step 1 — Audio Input

The user speaks through the microphone.

### Step 2 — Speech-to-Text

`RealtimeSTT` captures the speech and converts it into text.

Example:

```text
Audio: "How are you?"
↓
Text: "How are you?"
```

### Step 3 — LLM Processing

The text is sent to Llama 3.2 through Ollama.

Example:

```text
User: How are you?
↓
Llama 3.2:
"I'm just a language model, so I don't have feelings..."
```

### Step 4 — Text-to-Speech

The generated response is passed to `RealtimeTTS`.

The response is converted into audio and played through the computer's speakers.

### Step 5 — Continuous Interaction

The system returns to the microphone and waits for the next user input.

---

# 💻 Main Program

The `main.py` file combines all three required components:

* `AudioToTextRecorder` for speech recognition
* `ChatOllama` for LLM processing
* `TextToAudioStream` and `SystemEngine` for speech output

This allows the three separate technologies to work together as one VoiceAI application.

---

# ✅ Task Requirements

| Requirement                      | Implementation           | Status      |
| -------------------------------- | ------------------------ | ----------- |
| Convert audio input to text      | RealtimeSTT              | ✅ Completed |
| Generate a response using an LLM | Ollama + Llama 3.2       | ✅ Completed |
| Convert the response to audio    | RealtimeTTS              | ✅ Completed |
| Upload files to GitHub           | Project files and README | ✅ Completed |
| Explain the implementation steps | This README              | ✅ Completed |

---

# 🧪 Final Test Result

The complete system was successfully tested.

Example interaction:

```text
User: Hello.

VoiceAI:
Hello! How can I assist you today?
```

Another test:

```text
User: How are you?

VoiceAI:
I'm just a language model, so I don't have feelings or emotions like humans do.
However, I'm functioning properly and ready to assist you with any questions or tasks you may have!
```

The responses were successfully generated by the LLM and spoken through the computer's speakers.

---

# 📌 Notes

* An active microphone is required for speech input.
* Speakers or headphones are required for audio output.
* Ollama must be installed and the `llama3.2` model must be available.
* FFmpeg must be installed and accessible from the system PATH.
* The Python virtual environment should be activated before running the project.
* The `venv` folder should **not** be uploaded to GitHub because it contains the local Python environment and can be recreated using the installation instructions.

---

# 🎯 Conclusion

This project successfully demonstrates a complete **voice-based AI interaction pipeline**.

The system takes human speech as input, converts it into text, processes the text using a locally running LLM, and converts the generated response back into speech.

Therefore, all three core requirements of the task have been successfully implemented:

**🎤 Speech → 📝 Text → 🧠 LLM → 💬 Response → 🔊 Speech**

---

## 🎥 Project Demonstration

A video demonstration of the completed VoiceAI system:

▶️ (https://youtu.be/XnZxjbWPfZ4)

---

## 👨‍💻 Author

**Fahad**

**Cybersecurity Student**
