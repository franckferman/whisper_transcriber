#!/usr/bin/env python3
# main.py

"""
Whisper Transcriber CLI Application

Description:
CLI application for transcribing audio files using OpenAI's Whisper API and 
for cleaning temporary files within the project directory.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import typer
from pathlib import Path
from transcription.transcriber import transcribe_audio
from utils.cleaner import clean_project
from utils.helpers import display_loading_dots
import threading

app = typer.Typer()

@app.command(help="Transcribes an audio file using OpenAI's Whisper API.")
def transcribe(
    file: Path = typer.Option(..., "-f", "--file", help="Path to the audio file to transcribe."),
    key: str = typer.Option(..., "-k", "--key", help="OpenAI API key for authentication."),
    language: str = typer.Option(
        None, "-l", "--lang", "--language",
        help="Language for transcription ('fr' for French or 'en' for English)."
    ),
    output: Path = typer.Option(
        None, "-o", "--output", help="Path to save the transcription output in JSON format."
    ),
    debug: bool = typer.Option(
        False, "--debug", help="Enable debug mode with detailed logging."
    )
) -> None:
    """
    Transcribes an audio file with specified language and saves it as JSON if output is provided.

    Args:
        file (Path): Path to the audio file to transcribe.
        key (str): OpenAI API key for authentication.
        language (str): Language for transcription ('fr' for French or 'en' for English).
        output (Path): File path for saving the transcription.
        debug (bool): Enables debug logging if True.
    """
    # Determine the language code for transcription
    language_code = None
    if language:
        if language.lower() in ["fr", "french", "francais", "français"]:
            language_code = "fr"
        elif language.lower() in ["en", "english", "anglais"]:
            language_code = "en"
        else:
            print("Unrecognized language. Use 'fr' for French or 'en' for English.")
            raise typer.Exit()

    # Display loading animation in a separate thread
    loading_active = True
    loading_thread = threading.Thread(target=display_loading_dots, args=(lambda: loading_active,))
    loading_thread.start()

    # Call transcription function
    transcribe_audio(file, key, language_code, output, debug)
    loading_active = False
    loading_thread.join()


@app.command(help="Cleans up temporary files (.pyc, __pycache__, etc.) in the project.")
def clean(
    directory: Path = typer.Argument(
        ".", help="Starting directory for cleaning up unwanted files."
    ),
    enable_logging: bool = typer.Option(
        False, "--log", help="Enable logging for the cleanup process."
    )
) -> None:
    """
    Removes temporary and unwanted files from the project directory.

    This function recursively deletes files such as Python bytecode, cache directories,
    and other temporary files within the specified directory.

    Args:
        directory (Path): The root directory to start cleaning. Defaults to the current directory.
        enable_logging (bool): Enables logging of cleanup actions if True.
    """
    clean_project(directory=directory, enable_logging=enable_logging)


if __name__ == "__main__":
    app()
