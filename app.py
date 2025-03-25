from flask import Flask, render_template, request, send_file
import torch
import os
import sys
import torchaudio
from pathlib import Path

# Add CSM to Python path
sys.path.append(str(Path(__file__).parent / 'csm'))

from generator import load_csm_1b

app = Flask(__name__)

# Initialize the CSM model
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print("Loading CSM model...")
generator = load_csm_1b(device=device)
print("Model loaded successfully!")

# Create output directory if it doesn't exist
os.makedirs('static/audio', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    
    try:
        # Generate audio using CSM
        audio = generator.generate(
            text=text,
            speaker=0,
            context=[],
            max_audio_length_ms=10_000,
        )
        
        # Save the audio file
        output_path = os.path.join('static', 'audio', 'output.wav')
        torchaudio.save(output_path, audio.unsqueeze(0).cpu(), generator.sample_rate)
        
        return {
            'status': 'success',
            'audio_url': '/static/audio/output.wav'
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run(debug=True)