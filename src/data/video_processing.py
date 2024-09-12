import os
import subprocess

import cv2


def download_video(destination, source):
    os.makedirs(destination, exist_ok=True)

    try:
        subprocess.run([
            'yt-dlp',
            '-o', f'{destination}/%(title)s.%(ext)s',
            source
        ], check=True)
        print(f"Video downloaded successfully to {destination}.")

    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")

    return f'{destination}/%(title)s.%(ext)s'


def extract_video_frames(source_video: str,
                         destination: str,
                         video_id: int,
                         extraction_frequency: int = 30):

    cap = cv2.VideoCapture(source_video)
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_number % extraction_frequency == 0:
            frame_path = os.path.join(destination, f'{video_id}_{int(frame_number / extraction_frequency)}.jpg')
            cv2.imwrite(frame_path, frame)
            print(f'Extracted frame {frame_number} to {frame_path}')

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()
