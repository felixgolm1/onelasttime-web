import imageio_ffmpeg
import subprocess

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [
    ffmpeg_exe,
    "-i", "assets/img/video elsa.mp4",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-keyint_min", "1",
    "-g", "1",
    "-movflags", "+faststart",
    "-c:a", "copy",
    "assets/img/video_elsa_kf.mp4",
    "-y"
]
print("Running command:", " ".join(cmd))
subprocess.run(cmd, check=True)
