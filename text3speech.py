from deepgram import    (
                        DeepgramClient,
                        SpeakOptions,
                        )
import os
from dotenv import load_dotenv

# Charge les variables d'environnement du fichier .env
load_dotenv()
api_deepgram = os.getenv("CLEF_API_DEEPGRAM")


filename = "./audios/system.wav"

def text2speech(text):
    try:
        SPEAK_OPTIONS = {"text": text}
        deepgram = DeepgramClient(api_key=api_deepgram)
 
        options = SpeakOptions(
            model="aura-angus-en",
            encoding="linear16",
            sample_rate=48000,
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    text2speech(" ")
