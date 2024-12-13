import sys
from .main import main


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src <video_file>")
        sys.exit(1)

    video_file = sys.argv[1]

    try:
        main(video_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
