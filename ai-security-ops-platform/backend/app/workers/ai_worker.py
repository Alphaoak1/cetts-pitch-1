import redis
import rq
from app.core.config import settings

redis_conn = redis.from_url(settings.REDIS_URL)
queue = rq.Queue("ai-queue", connection=redis_conn)

def transcribe_job(audio_path: str, incident_id: str):
    # Placeholder: call Whisper + LLM
    # In real impl, use faster-whisper and a lightweight LLM
    return {"incident_id": incident_id, "transcript": "Mock transcript"}