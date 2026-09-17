from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def listen(seconds=5):

    print("Listening...")

    recording = sd.rec(
        int(seconds * 16000),
        samplerate=16000,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_path = temp_file.name

    temp_file.close()

    write(
        temp_path,
        16000,
        recording
    )
    
    segments, info = model.transcribe(
        temp_path,
        language="en"   
    )

    text = " ".join(
        segment.text
        for segment in segments
    )

    os.remove(temp_path)

    return text.strip().lower()