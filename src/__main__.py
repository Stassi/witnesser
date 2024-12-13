import sys
from .main import main


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src <video_file> [output_directory]")
        sys.exit(1)

    video_file = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "."

    try:
        main(video_file, output_directory)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
