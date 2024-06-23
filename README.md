# README

## Introduction
This repository contains code and resources for automating medical chart documentation using AI. The project aims to streamline the process of medical documentation for doctors by generating structured medical charts from patient transcripts.

## Files
- `main.py`: The main script to run the project.
- `recording_convert.py`: Script to convert audio recordings into text format.
- `text_summary.py`: Script to summarize the transcribed text into a medical chart format.
- `output.txt`: Sample output text of a medical conversation transcript.
- `prompt.txt`: Instructions and prompt format for generating the medical chart documentation.

## Usage

1. **Recording Conversion**:
   - Use the `recording_convert.py` script to convert audio recordings into text format.
   - Command: `python recording_convert.py <input_audio_file>`

2. **Text Summarization**:
   - Use the `text_summary.py` script to summarize the transcribed text into a medical chart format.
   - Command: `python text_summary.py <input_text_file>`

3. **Running the Main Script**:
   - The `main.py` script ties everything together, allowing you to process audio recordings directly and obtain the medical chart documentation.
   - Command: `python main.py <input_audio_file>`

## Example
To convert an audio recording and generate a medical chart, run:
```bash
python main.py path/to/your/audiofile.wav
