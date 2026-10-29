from moviepy import VideoFileClip

clip = VideoFileClip("stereo_comparison_eth3d.mp4")
clip.write_videofile(
    "stereo_comparison_eth3d_fixed.mp4",
    codec="libx264",
    audio_codec="aac",
    ffmpeg_params=[
        "-pix_fmt", "yuv420p",
        "-profile:v", "main",
        "-crf", "18",
        "-preset", "medium",
        "-movflags", "+faststart"
    ]
)
clip.close()