from .extract_audio import extract_audio


def main(video_file: str, output_directory: str = "."):
    extract_audio(video_file, output_directory)
