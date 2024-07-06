import ffmpeg
from pydub import AudioSegment, silence
import tempfile
import os

def remove_silence(input_video_path, output_video_path, silence_thresh=-30, min_silence_len=500):
    # Extract audio from video
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_audio_path = temp_audio.name
    temp_audio.close()

    ffmpeg.input(input_video_path).output(temp_audio_path).run()

    # Load audio with pydub
    audio = AudioSegment.from_file(temp_audio_path, format="wav")

    # Find non-silent chunks
    non_silent_chunks = silence.detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    # Create temporary directory to store video chunks
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = temp_dir.name

    # Initialize variables to keep track of timestamps
    chunks = []
    for i, chunk in enumerate(non_silent_chunks):
        start, end = chunk
        start /= 1000  # convert to seconds
        end /= 1000    # convert to seconds
        chunks.append((start, end))
        
        # Extract video chunk
        temp_chunk_path = os.path.join(temp_dir_path, f"chunk_{i}.mp4")
        ffmpeg.input(input_video_path, ss=start, to=end).output(temp_chunk_path).run()
    
    # Concatenate video chunks
    with open(f"{temp_dir_path}/filelist.txt", "w") as f:
        for i in range(len(chunks)):
            f.write(f"file 'chunk_{i}.mp4'\n")
    
    ffmpeg.input(f"{temp_dir_path}/filelist.txt", format="concat", safe=0).output(output_video_path, c="copy").run()
    
    # Clean up temporary files
    os.remove(temp_audio_path)
    temp_dir.cleanup()

# Example usage - Update line 6 to adjust volume sensitivity.
input_video_path = "C:/path/to/input.mp4"
output_video_path = "C:/path/to/output.mp4"
remove_silence(input_video_path, output_video_path)
