# OpenCV Course

A hands-on journey through OpenCV fundamentals — each session builds on the last, moving from reading raw visual data to manipulating and creating it from scratch. Every session directory contains the session's code along with a dedicated README covering not just *what* the code does, but the underlying philosophy behind it.

## Mini-Projects

* [Face Detection](./_15_face_detection/README.md)

## 📚 Sessions

### [Session 1 — Reading Images & Videos](./01_reading/README.md)
The starting point of any computer vision pipeline: getting visual data into your program. Covers reading static images with `imread()` and streaming video frame-by-frame with `VideoCapture`, along with the core idea that an image is just a NumPy array underneath.

### [Session 2 — Rescaling & Resolution](./02_rescale/README.md)
Tackles the practical problem of oversized media. Covers two distinct approaches — rescaling frames after capture vs. changing resolution at the source — plus the geometry of scale factors and defensive checks for invalid frames.

### [Session 3 — Drawing on Images](./03_draw/README.md)
Shifts from reading images to creating them. Covers building a blank canvas from scratch and drawing on it two ways: direct array slicing vs. OpenCV's built-in shape functions (rectangles, circles, lines, text), along with OpenCV's BGR color convention.


## 🎯 Purpose

This repository serves as a personal learning log for an OpenCV course — every script is preserved as written during the course, and each README documents the reasoning and mental models behind the code, not just a restatement of what it does.