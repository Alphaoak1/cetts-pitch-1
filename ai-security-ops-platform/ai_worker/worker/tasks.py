import redis
from faster_whisper import WhisperModel

redis_client = redis.from_url("redis://redis:6379/0")
model = WhisperModel("tiny.en", device="cpu", compute_type="int8")

def transcribe_audio(audio_path: str, incident_id: str):
    segments, _ = model.transcribe(audio_path)
    transcript = " ".join(seg.text for seg in segments)
    # TODO: call LLM for summarization
    # Update DB via HTTP call to backend
    import requests
    requests.post(f"http://backend:8000/api/v1/incidents/{incident_id}/transcribe", json={"transcript": transcript})
    return transcript