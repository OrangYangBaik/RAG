import os
import tempfile
from flask_socketio import emit
from vectorDB.chroma_client import get_chroma_client
from vectorDB.embed import load_and_embed
from services import stt_service, llm_service
from llm.prompt import build_prompt
from services.embed_service import LocalNomicEmbeddings

embedding = LocalNomicEmbeddings()
collection = get_chroma_client().get_or_create_collection("product")
load_and_embed(collection)

def register_socket_handlers(socketio):
    @socketio.on('audio')
    def handle_audio(data):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(data)
            audio_path = f.name

        try:
            question = stt_service.transcribe(audio_path)
            #print("Transcribed:", question)

            query_embedding = embedding.embed_query(question)
            results = collection.query(query_embeddings=[query_embedding], n_results=3)
            context = "\n\n".join(results["documents"][0])

            prompt = build_prompt(context, question)
            answer = llm_service.call_llm(prompt)

            #print("Answer:", answer)
            emit('response', {"text": answer})

        finally:
            os.remove(audio_path)
