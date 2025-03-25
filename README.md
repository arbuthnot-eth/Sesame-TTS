# Sesame TTS

A web application that provides a simple interface for text-to-speech synthesis using Sesame's CSM (Conversational Speech Model).

## Features

- Clean, modern web interface
- Real-time text-to-speech generation
- Built-in audio player for immediate playback
- Responsive design using Tailwind CSS

## Prerequisites

- Python 3.10 or newer
- Access to Meta's Llama 3.2-1B model (requires approval from Meta)
- CUDA-compatible GPU (recommended) or CPU

## Installation

1. Clone the repository:
```bash
git clone https://github.com/arbuthnot-eth/Sesame-TTS.git
cd Sesame-TTS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Log in to Hugging Face (you need access to Meta's Llama model):
```bash
huggingface-cli login
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter your desired text in the input box
2. Click "Generate Speech"
3. Wait for the generation to complete
4. Use the audio player to listen to the generated speech

## Model Information

This application uses:
- CSM (Conversational Speech Model) from Sesame AI Labs
- Meta's Llama 3.2-1B as the backbone
- Mimi audio codes for speech synthesis

## License

This project is licensed under the terms specified by Sesame AI Labs for CSM usage. See their [repository](https://github.com/SesameAILabs/csm) for more details.

## Acknowledgments

- [Sesame AI Labs](https://github.com/SesameAILabs) for the CSM model
- Meta for the Llama model
- Flask for the web framework
- Tailwind CSS for styling