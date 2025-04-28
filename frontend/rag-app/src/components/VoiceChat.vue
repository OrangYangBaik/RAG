<template>
  <div class="voice-chat">
    <button @click="toggleRecording" class="record-btn">
      {{ isRecording ? '⏹' : '🎤' }}
    </button>

    <div v-if="isRecording" class="recording-indicator">
      🔴 Recording...
    </div>

    <div v-if="response" class="response-box">
      <h3>Response</h3>
      <p>{{ response }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { io } from 'socket.io-client'

const isRecording = ref(false)
const response = ref('')
let mediaRecorder = null
let audioChunks = []
let socket = null

onMounted(() => {
  socket = io('http://localhost:5000')
  socket.on('response', (data) => {
    response.value = data.text
  })
})

const toggleRecording = async () => {
  if (isRecording.value) {
    mediaRecorder.stop()
    isRecording.value = false
    return
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    mediaRecorder = new MediaRecorder(stream)
    audioChunks = []

    mediaRecorder.ondataavailable = (e) => {
      audioChunks.push(e.data)
    }

    mediaRecorder.onstop = async () => {
      const blob = new Blob(audioChunks, { type: 'audio/wav' })
      const arrayBuffer = await blob.arrayBuffer()
      socket.emit('audio', arrayBuffer)
    }

    mediaRecorder.start()
    isRecording.value = true
  } catch (err) {
    console.error('🎤 Microphone access denied or error:', err)
  }
}
</script>

<style scoped>
.voice-chat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding: 2rem;
  background: #1e1e2f;
  border-radius: 16px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
  max-width: 600px;
  margin: 0 auto;
}

.record-btn {
  background: linear-gradient(135deg, #ff416c, #ff4b2b);
  color: white;
  width: 4rem;
  height: 4rem;
  font-size: 1.5rem;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 15px rgba(255, 65, 108, 0.4);
}

.record-btn:hover {
  transform: scale(1.1);
}

.recording-indicator {
  color: #ff6b6b;
  font-size: 1rem;
  font-weight: 500;
  animation: pulse 1.2s infinite;
}

@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

.response-box {
  background: #2c2c3e;
  padding: 1.5rem;
  border-radius: 12px;
  width: 100%;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  color: #ddd;
}

.response-box h3 {
  margin-bottom: 0.5rem;
  color: #ff9f43;
  font-weight: 600;
}

.response-box p {
  line-height: 1.6;
  font-size: 1rem;
  color: #f1f1f1;
}
</style>
