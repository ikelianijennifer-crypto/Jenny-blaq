import requests
import os
import re

API_KEY = "23ce04e89f4b4d8f4d32e90478e5f54f450ea1d6f26f2e79472da765180353b8"
VOICE_ID = "VU16byTywsWv5JpI8rbc"
OUTPUT_DIR = "/mnt/user-data/outputs"
FINAL_OUTPUT = os.path.join(OUTPUT_DIR, "every-high-priest-audio.mp3")

# Read script and extract text after SCRIPT:
with open("/mnt/user-data/outputs/script-every-high-priest-in-the-bible.md", "r") as f:
    content = f.read()

script_text = content.split("SCRIPT:", 1)[1].strip()

# Clean up markdown italics
script_text = re.sub(r'\*([^*]+)\*', r'\1', script_text)

# Split into chunks of ~4500 characters, breaking at paragraph boundaries
def split_into_chunks(text, max_chars=4500):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current_chunk) + len(para) + 2 > max_chars and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = para
        else:
            current_chunk += "\n\n" + para if current_chunk else para
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks

chunks = split_into_chunks(script_text)
print(f"Script split into {len(chunks)} chunks")

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "audio/mpeg"
}

chunk_files = []
for i, chunk in enumerate(chunks):
    print(f"Generating chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")
    payload = {
        "text": chunk,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        chunk_path = os.path.join(OUTPUT_DIR, f"chunk_{i:03d}.mp3")
        with open(chunk_path, "wb") as f:
            f.write(response.content)
        chunk_files.append(chunk_path)
        print(f"  Chunk {i+1} saved ({len(response.content)} bytes)")
    else:
        print(f"  ERROR on chunk {i+1}: {response.status_code} - {response.text}")
        exit(1)

# Concatenate all MP3 chunks into final file
print(f"\nConcatenating {len(chunk_files)} chunks into final audio...")
with open(FINAL_OUTPUT, "wb") as outfile:
    for chunk_path in chunk_files:
        with open(chunk_path, "rb") as infile:
            outfile.write(infile.read())

# Clean up chunk files
for chunk_path in chunk_files:
    os.remove(chunk_path)

final_size = os.path.getsize(FINAL_OUTPUT)
print(f"\nDone! Final audio: {FINAL_OUTPUT}")
print(f"File size: {final_size / 1024 / 1024:.1f} MB")
