# Session 1 — Reading Images & Videos

## Overview

This session covers the most fundamental operation in any computer vision pipeline: getting visual data *into* your program. Before you can transform, analyze, or detect anything, OpenCV needs to read pixels from a file (or a camera stream) into a data structure you can work with. This session covers two entry points — static images and video files — because they share the same underlying logic but differ in one key way: an image is a single frame, while a video is a *sequence* of frames read in a loop.

## Files

- `read_image.py` — reads and displays a small image and a larger image
- `read_video.py` — reads and displays a video file frame by frame

## Core Philosophy

**An image, to OpenCV, is just a NumPy array.** `cv.imread()` doesn't return some special "image object" — it returns a multi-dimensional array of pixel values (height × width × color channels). This matters because it means everything you learn later about slicing, masking, and manipulating NumPy arrays applies directly to images. There's no hidden magic; reading an image is just loading numbers into memory.

**A video is not fundamentally different from an image — it's a loop of images.** `cv.VideoCapture` doesn't hand you the whole video at once. It gives you a *source* you repeatedly `.read()` from, one frame at a time, inside a `while True` loop. Each frame is read, displayed, and discarded before the next one is fetched. This streaming approach is what allows OpenCV to handle video without loading the entire file into memory — a deliberate and necessary design choice, since videos can be far too large to hold in RAM all at once.

**Displaying is separate from reading.** `cv.imshow()` just draws whatever array you give it into a window — it has no idea whether that array came from a photo, a video frame, or a live webcam. This separation (read → process → display) is a pattern that carries through the entire OpenCV workflow, and it's worth internalizing early.

**`cv.waitKey()` is what keeps windows alive.** OpenCV's window system needs the program to actively "wait" and listen for keyboard input; without it, windows would flash and disappear instantly. `cv.waitKey(0)` waits forever for a single keypress (good for static images), while `cv.waitKey(20)` inside a loop waits only 20ms per iteration — just long enough to check for a key press before moving to the next frame, which is what makes video playback feel continuous rather than frozen on each frame.

**Errors are expected, not exceptional.** Two failure modes show up immediately in this session, and both are worth understanding rather than fearing:
- An `Assertion -215` error on `imread`/`VideoCapture` almost always means the file path is wrong — OpenCV read `None` and choked trying to process it.
- The same error at the *end* of a video loop just means the frames ran out — `capture.read()` returned `False` and there was nothing left to show.

Neither of these is really a "crash" in the traditional sense — they're OpenCV telling you it received empty data. Learning to read these errors as *path problems* or *end-of-stream signals*, rather than mysterious bugs, is a big part of getting comfortable with the library.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Images = NumPy arrays | Enables all future array-based manipulation |
| Video = loop of frames | Keeps memory usage manageable for large files |
| `waitKey()` | Controls both window persistence and playback speed |
| `0` / `1` in `VideoCapture` | Same function reads files *or* live webcam feeds |
| Assertion -215 | Almost always a bad path or an exhausted video stream |

