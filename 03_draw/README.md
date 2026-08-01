# Session 3 — Drawing on Images

## Overview

This session moves from *reading* visual data to *creating* it. Instead of loading a photo or video, we start from a blank canvas — a NumPy array of zeros — and build it up manually: painting regions, drawing shapes, and writing text. This is a deliberate shift in mental model: once you understand an image is just an array, drawing on it stops being a mysterious "graphics" operation and becomes an exercise in directly manipulating pixel values, sometimes through raw indexing and sometimes through OpenCV's drawing functions.

## Files

- `draw.py` — interactive menu-driven script to paint, draw shapes, and write text on a blank image

## Core Philosophy

**A blank image is not "nothing" — it's a fully-formed array of zeros.** `np.zeros((500, 500, 3), dtype='uint8')` isn't a placeholder or an empty canvas in the abstract sense; it's already a complete, valid image where every pixel happens to be black. This reinforces the array-based mental model from Session 1: there's no special "empty" state in OpenCV, only arrays with particular values, and black is just the value zero across all channels.

**There are two fundamentally different ways to "draw," and the code deliberately shows both.** `paint_image()` and `paint_portion()` work by direct array slicing — reaching in and overwriting pixel values (`image[:] = [...]` or `image[y1:y2, x1:x2] = [...]`) without calling any drawing function at all. `draw_rectangle()`, `draw_circle()`, and `draw_line()`, by contrast, delegate to OpenCV's built-in drawing functions. The first approach is really just NumPy manipulation wearing an OpenCV hat; the second is OpenCV doing genuine geometric rasterization (working out which pixels fall inside a circle or along a line). Recognizing which category a given operation falls into clarifies what's actually happening under the hood versus what's a convenience wrapper.

**Color in OpenCV is BGR, not RGB — and this needs to become muscle memory early.** Every color tuple in this code is ordered blue-green-red, the reverse of what most other imaging tools use. This isn't a stylistic quirk; it's a historical artifact of OpenCV's origins, and forgetting it is one of the most common sources of "why is my red image showing up blue" bugs. Hardcoding the BGR order explicitly in each function, as this code does, is a reasonable way to stay deliberate about it while still learning.

**Thickness carries a dual meaning: outline width, or "fill" as a special case.** Passing a positive integer draws a border of that width; passing `-1` doesn't mean "invalid" — in OpenCV's convention it's a specific instruction to fill the shape entirely. This is a small API detail, but it's the kind of thing worth understanding as a deliberate convention rather than a magic number, since it shows up repeatedly across `rectangle`, `circle`, and other drawing functions.

**Validating input at the boundary keeps the drawing functions themselves simple.** Notice that `draw_rectangle()`, `draw_circle()`, etc. contain almost no error handling — all the bounds-checking, type-checking, and re-prompting happens in `main()`, before the functions are ever called. This is an intentional separation of concerns: the drawing functions assume they're given valid, sane input, and the messier job of interrogating the user and enforcing constraints (coordinates within canvas bounds, `finish > start`, valid color names) is isolated to one place. This tends to make the "business logic" functions easier to read, test, and reuse elsewhere.

**A menu-driven `main()` is a scaffold for experimentation, not production code.** The heavy use of `input()` and `eval()` here is appropriate for an exploratory learning script where you want to try different shapes and coordinates without editing code each time — but it's worth noting `eval()` on raw user input is something to be cautious about outside a personal learning sandbox, since it will execute arbitrary Python. In this context it's a fine shortcut for parsing tuples like `(x, y)`; in a real application, `ast.literal_eval` or manual parsing would be the safer choice.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| `np.zeros()` as a starting canvas | An image is just an array — "blank" is a value, not an absence |
| Slicing (`image[:]=`) vs. `cv.rectangle`/`cv.circle`/`cv.line` | Direct array manipulation vs. OpenCV's geometric rasterization |
| BGR channel order | A recurring OpenCV convention, not RGB — easy to trip on |
| `thickness = -1` | Convention for "filled shape," not an error value |
| Validation isolated in `main()` | Keeps drawing functions simple and assumption-driven |
| `eval()` for parsing tuples | Convenient for a learning sandbox, risky in production code |