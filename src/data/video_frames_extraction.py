import os
import subprocess

import cv2


def download_video(video_url: str, download_path: str = './video_frames'):
    os.makedirs(download_path, exist_ok=True)
    try:
        subprocess.run([
            'yt-dlp',
            '-o', f'{download_path}/%(title)s.%(ext)s',
            video_url
        ], check=True)
        print(f"Video downloaded successfully to {download_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")


def extract_video_frames(video_file: str, extraction_frequency: int = 30):
    cap = cv2.VideoCapture(video_file)
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save every 30th frame
        if frame_number % extraction_frequency == 0:
            frame_path = os.path.join(os.path.dirname(video_file),
                                      f'frame_{int(frame_number / extraction_frequency)}.jpg')
            cv2.imwrite(frame_path, frame)
            print(f'Extracted frame {frame_number} to {frame_path}')

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()

