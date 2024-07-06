# Mp4SilenceRemover

This Python script removes silent parts from an MP4 video, both video and audio, to create a shorter video containing only the moments with voice. It leverages `ffmpeg` for video processing and `pydub` for audio processing.

## Features
- Extracts audio from the video.
- Detects non-silent audio chunks based on a specified silence threshold and minimum silence length.
- Cuts the video to keep only the non-silent parts.
- Merges the non-silent video chunks into a final output video.

## Requirements
- Python 3.6 or higher
- `ffmpeg` (must be installed and added to your system's PATH)
- Python libraries: `pydub`, `tempfile`

## Installation
1. Install the required Python libraries:
    ```sh
    pip install pydub
    ```

2. Place your input MP4 video in the same directory as the script or specify the full path to the video.

3. Run the script:
    ```sh
    python Mp4SilenceRemover.py
    ```

4. The output video will be saved in the specified output path.

## Parameters
- `input_video_path`: Path to the input MP4 video file.
- `output_video_path`: Path to save the output MP4 video file.
- `silence_thresh`: (Optional) Silence threshold in dBFS. Default is -50 dBFS.
- `min_silence_len`: (Optional) Minimum length of silence in milliseconds. Default is 1000 ms.

## Example
```python
input_video_path = "C:/Python/Scripts/input.mp4"
output_video_path = "C:/Python/Scripts/output.mp4"
remove_silence(input_video_path, output_video_path)
