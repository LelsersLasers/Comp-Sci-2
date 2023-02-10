"""
	Requires the following OS packages:
		- zbar (ran with 'zbarimg' command)
"""

from __future__ import annotations

import subprocess
import os

import cv2
import time

from PIL import Image


defaultImagePath = "qrCode.png"


def readQRCode(imagePath: str) -> list[str] | None:
    """
    Reads the QR code in the image at the given path.
    Returns the contents of the QR code.
    Returns None if the QR code could not be read.
    """
    try:
        output = subprocess.check_output(
            ["zbarimg", imagePath],
            stderr=subprocess.STDOUT  # hides output of zbarimg
        )

        stringOutput = output.decode("utf-8").strip()

        outputs: list[str] = []

        lines = stringOutput.split("\n")
        for line in lines:
            line = line.strip()
            parts = line.split(":")
            linkParts = parts[1:]
            fullLink = "".join(linkParts)
            if len(fullLink) > 0:
                outputs.append(fullLink)

        return outputs

    except subprocess.CalledProcessError:
        return None


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Can't open camera.")
        quit()
    else:
        print("Opened camera.")

    time.sleep(1)

    start = time.time()
    delta = 1.0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame.")
            break

        delta = time.time() - start
        fps = 1 / delta
        start = time.time()

        print(f"\nFPS: {fps:.2f}\tDelta: {(delta * 1000):.2f} ms")

        cv2.imshow("Camera Feed", frame)

        # Takes 60-70 ms --------------------------------------------------------------#
        img = Image.fromarray(frame)
        img.save(defaultImagePath)
        # ------------------------------------------------------------------------------#

        qrCode = readQRCode(defaultImagePath)

        if qrCode is not None:
            print(f"QR Code(s): {qrCode}")
        else:
            print("No QR code found.")

        if cv2.waitKey(1) == ord("q"):
            break

    if os.path.exists(defaultImagePath):
        os.remove(defaultImagePath)

    cap.release()
    cv2.destroyAllWindows()
