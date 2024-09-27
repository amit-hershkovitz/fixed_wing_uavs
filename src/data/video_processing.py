import os
import subprocess

import cv2


def download_video(source: str, destination: str) -> str:
    os.makedirs(destination, exist_ok=True)

    try:
        subprocess.run([
            'yt-dlp',
            '-f', 'bestvideo+bestaudio',
            '--merge-output-format', 'mp4',
            '-o', f'{destination}/temp.%(ext)s',
            source
        ], check=True)
        print(f"Video downloaded successfully to {destination}.")

    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")

    return f'{destination}/temp.mp4'


def extract_video_frames(source_video: str,
                         destination: str,
                         video_id: int,
                         extraction_frequency: int = 30) -> list[str, ...]:

    cap = cv2.VideoCapture(source_video)

    frame_number = 0
    paths = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_number % extraction_frequency == 0:
            frame_path = os.path.join(destination, f'{video_id}_{int(frame_number / extraction_frequency)}.jpg')
            cv2.imwrite(frame_path, frame)
            paths.append(frame_path)
            print(f'Extracted frame {frame_number} to {frame_path}')

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()

    return paths


def reject_frames(paths: list[str, ...]) -> list[str, ...]:
    kept_paths = []

    terminate_rejection_process = False

    for path in paths:
        cv2.namedWindow('Image Candidate', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Image Candidate', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        img = cv2.imread(path)
        cv2.imshow('Image Candidate', img)

        while True:
            key = cv2.waitKey(0)

            if key == ord('k'):
                kept_paths.append(path)
                break
            elif key == ord('d'):
                os.remove(path)
                break
            elif key == ord('q'):
                terminate_rejection_process = True
                break

        if terminate_rejection_process:
            break

    cv2.destroyAllWindows()  # Close all OpenCV windows

    return kept_paths
