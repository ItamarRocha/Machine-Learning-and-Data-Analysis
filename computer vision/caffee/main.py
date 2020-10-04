import argparse
import cv2

prototxt = "deploy.prototxt.txt"
model = "res10_300x300_ssd_iter_140000.caffemodel"

_input = "imgs/gonzalo.jpeg"

net = cv2.dnn.readNetFromCaffe(prototxt, model)

image = cv2.imread(_input)