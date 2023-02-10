"""
	Requires the following OS packages:
		- zbar (ran with 'zbarimg' command)
"""

from __future__ import annotations

import subprocess
# import sys
import os

import cv2
import time

from PIL import Image


defaultImagePath = "qrCode.png"


def readQRCode(imagePath: str) -> str | None:
	"""
		Reads the QR code in the image at the given path.
		Returns the contents of the QR code.
		Returns None if the QR code could not be read.

		Only works if there is 1 or 0 QR codes in the image.
	"""
	try:
		output = subprocess.check_output(
			["zbarimg", imagePath],
			stderr=subprocess.STDOUT # hides output of zbarimg
		)

		stringOutput = output.decode("utf-8").strip()

		firstLine = stringOutput.split("\n")[0].strip()
		parts = firstLine.split(":")
		linkParts = parts[1:]
		return "".join(linkParts)

	except subprocess.CalledProcessError:
		return None



if __name__ == '__main__':
	# args = sys.argv[1:]

	# for arg in args:
	# 	qrCode = readQRCode(arg)
	# 	print(f"QR Code in {arg}: {qrCode}")


	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		print("Can't open camera.")
		quit()
	else:
		print("Opened camera.")

	time.sleep(1)


	start = time.time()

	while True:
		ret, frame = cap.read()

		if not ret:
			print("Can't receive frame.")
			break


		fps = 1 / (time.time() - start)
		start = time.time()

		print(f"FPS: {fps:.2f}")

		cv2.imshow("Camera Feed", frame)

		img = Image.fromarray(frame)
		img.save(defaultImagePath)

		qrCode = readQRCode(defaultImagePath)

		if qrCode is not None:
			print(f"QR Code: {qrCode}")
		else:
			print("No QR code found.")

		if cv2.waitKey(1) == ord('q'):
			break

	if os.path.exists(defaultImagePath):
		os.remove(defaultImagePath)

	cap.release()
	cv2.destroyAllWindows()
