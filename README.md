# Whisper Transcriber

**Whisper Transcriber** is a command-line application designed to transcribe audio files using OpenAI's Whisper API. 
It includes features for language selection, logging, and cleanup of temporary files, with built-in checks for file validity and size before processing.

---

## Features
- Transcribe audio files using OpenAI's Whisper API.
- Language selection for transcription (`fr` for French, `en` for English).
- Logging for debugging and tracking transcription activities.
- Automatic cleanup of temporary files such as `.pyc`, `__pycache__`, etc.

---

## Installation

### Prerequisites
1. Clone the repository:
   ```bash
   git clone https://github.com/franckferman/whisper-transcriber.git
   cd whisper-transcriber
   ```
2. Install dependencies with [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```

3. Alternatively, you can use pip:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Transcription
To transcribe an audio file, use the following command:

```bash
poetry run whisper-transcriber transcribe -f <path_to_audio_file> -k <API_KEY> -l <language_code>
```

#### Example
```bash
poetry run whisper-transcriber transcribe -f "audio/sample.mp3" -k "your_openai_api_key" -l "en"
```

#### Options
- `-f`, `--file`: Path to the audio file to transcribe.
- `-k`, `--key`: OpenAI API key for authentication.
- `-l`, `--lang`: Language code for transcription (`fr` or `en`).
- `-o`, `--output`: File path to save the transcription output as JSON.
- `--debug`: Enable debug logging, which creates a log file `transcription.log`.

### Cleanup
To remove temporary files and logs from the project directory:

```bash
poetry run whisper-transcriber clean --log
```

#### Options
- `--log`: Enable logging for the cleanup process.

---

## Development

### Running Tests
To test the transcription and cleanup functions, ensure all necessary dependencies are installed:
```bash
poetry install --with dev
```

Then, run tests using your preferred test runner.

### Formatting
- The project uses `black`, `flake8`, and `mypy` for formatting, linting, and type-checking.
  - Format code with: `black .`
  - Lint code with: `flake8 .`
  - Type-check code with: `mypy .`

---

## License

This project is licensed under the GNU AGPLv3. See the `LICENSE` file for details.
