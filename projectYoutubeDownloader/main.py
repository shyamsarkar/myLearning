from pytube import YouTube
import os
import subprocess

video_url = 'https://www.youtube.com/watch?v=20GIloOLBQ0&list=PL8p2I9GklV47TMMnPzqnkCtSOS3ebr4O7&index=2&pp=iAQB'

def download_video_and_audio(video_url, output_path, resolution='1080p'):
    # try:
    # Create a YouTube object
    yt = YouTube(video_url)

    print(f"Video Title: {yt.title}")
    print(f"Views: {yt.views:,}")

    # Filter for the video stream (video only, without audio)
    video_stream = yt.streams.filter(res=resolution, mime_type="video/mp4", only_video=True).first()

    # If the specified resolution is not available, get the highest resolution video stream
    if video_stream is None:
        print(f"Resolution {resolution} not available. Downloading highest resolution instead.")
        video_stream = yt.streams.filter(mime_type="video/mp4", only_video=True).order_by("resolution").desc().first()

    print(f"Selected Video Quality: {video_stream.resolution}")
    print(f"Downloading video: {yt.title} ...")
    video_file = video_stream.download(output_path, filename="video.mp4")

    # Download the audio stream (audio only)
    print(f"Downloading audio: {yt.title} ...")
    audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
    audio_file = audio_stream.download(output_path, filename="audio.mp4")

    # Output file where the video and audio will be merged
    final_output = os.path.join(output_path, f"{yt.title}.mp4")

    # Merge video and audio using ffmpeg
    print("Merging video and audio...")
    merge_video_and_audio(video_file, audio_file, final_output)

    print(f"Download and merge completed! File saved as {final_output}")

    # Cleanup - remove the temporary audio and video files
    os.remove(video_file)
    os.remove(audio_file)

    # except Exception as e:
    #     print(f"An error occurred: {e}")

def merge_video_and_audio(video_file, audio_file, output_file):
    # Use ffmpeg to merge the video and audio
    command = [
        'ffmpeg',
        '-i', video_file,  # Input video file
        '-i', audio_file,  # Input audio file
        '-c:v', 'copy',    # Copy the video codec
        '-c:a', 'aac',     # Set the audio codec to AAC
        '-strict', 'experimental',
        output_file        # Output file
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Example usage
if __name__ == "__main__":
    # Output path where the video will be saved (current directory)
    output_path = '.'  # You can specify any folder path

    # You can change the resolution to your desired quality
    preferred_resolution = '1080p'  # Change to your preferred quality (e.g., '2160p' for 4K)

    download_video_and_audio(video_url, output_path, preferred_resolution)
