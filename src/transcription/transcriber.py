#!/usr/bin/env python3
# transcriber.py

"""
Transcriber Module

Description:
Handles the transcription of audio files using OpenAI's Whisper API, 
including preliminary checks for file validity and acceptable duration.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.3
"""

import openai
import json
from pathlib import Path
from pydub import AudioSegment
from utils.helpers import start_logging

def transcribe_audio(
    file_path: Path, api_key: str, language: str = None, 
    output_file: Path = None, debug: bool = False
) -> None:
    """
    Transcribes an audio file if it meets the required conditions.

    This function checks if the file exists, validates its duration,
    and calls OpenAI's Whisper API to perform transcription.

    Args:
        file_path (Path): Path to the audio file to transcribe.
        api_key (str): OpenAI API key for authentication.
        language (str, optional): Language code for transcription.
        output_file (Path, optional): Path to save the transcription output in JSON format.
        debug (bool, optional): Enables detailed logging if True.
    """
    start_logging(debug)
    openai.api_key = api_key

    # Check if the file exists
    if not file_path.is_file():
        print(f"\n❌ Error: The specified file does not exist: {file_path}\n")
        return

    # Load and check audio duration before processing
    try:
        audio = AudioSegment.from_file(file_path)
        duration_in_minutes = len(audio) / (1000 * 60)
    except Exception as e:
        print(f"\n❌ Error loading audio file: {e}\n")
        return

    # Early exit if the file is too long
    if duration_in_minutes > 15:
        print("\n⚠️ Error: File too large, duration exceeds 15 minutes.\n")
        return

    print("\n⏳ Sending the file to OpenAI API for transcription...\n")

    with open(file_path, "rb") as audio_file:
        try:
            # Setting up transcription parameters
            transcription_params = {
                "model": "whisper-1",
                "file": audio_file,
                "response_format": "json"
            }
            if language:
                transcription_params["language"] = language

            # Call OpenAI API to transcribe
            transcription = openai.Audio.transcribe(**transcription_params)

            # Check if transcription response is valid
            if isinstance(transcription, dict) and "text" in transcription:
                transcription_text = transcription["text"]

                # Save transcription to output file if specified
                if output_file:
                    with output_file.open("w", encoding="utf-8") as f:
                        json.dump(transcription, f, ensure_ascii=False, indent=4)
                    print(f"\n✅ Transcription saved to file: {output_file}\n")
                else:
                    print("\n--- Transcription Successful ---\n")
                    print("📝 Transcribed Text:\n")
                    print(transcription_text)
                    print("\n--- End of Transcription ---\n")
            else:
                print(f"\n⚠️ Unexpected API response: {transcription}\n")

        except Exception as e:
            print(f"\n❌ Error during transcription: {e}\n")
