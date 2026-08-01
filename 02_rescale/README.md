# Session 2 — Rescaling & Resolution

## Overview

This session tackles a practical problem that shows up the moment you work with real-world media: images and videos come in whatever size they were captured or exported at, and that size is rarely convenient. A 4K video frame is overkill for a quick preview window and unnecessarily expensive to process. This session introduces two different ways of controlling size — rescaling existing frames after the fact, and changing the capture resolution at the source — and treats them as two distinct tools for two distinct situations.

## Files

- `rescale_video.py` — interactive script offering both a frame-rescaling approach (for any video file) and a resolution-changing approach (for live webcam)
- `rescale_image.py` — applies the same rescaling helper function to a static image

## Core Philosophy

**Rescaling and changing resolution are not the same operation, even though they look similar.** `rescaleFrame()` takes a frame that has *already been captured* at full size and shrinks it down after the fact — this works uniformly on images, videos, and live streams, because by the time you have a `frame`, it's just an array, and resizing an array doesn't care where it came from. `changeRes()`, on the other hand, reaches into the capture device itself and asks it to *produce* frames at a different resolution to begin with. This only makes sense for live sources (via `capture.set()`) — you can't ask a pre-recorded video file to have been filmed at a different resolution. Keeping this distinction clear is more valuable than either function individually: it's the difference between "shrinking the output" and "changing the input."

**Scale factors compound, they don't add.** A scale of 0.5 doesn't mean "half the size" in the intuitive sense — it means half the *width* and half the *height*, which multiply together into a quarter of the total area. This is a classic trap: if the actual goal is to halve the visible area, the scale factor needs to be `sqrt(0.5)`, not `0.5`. Rescaling is fundamentally a geometric operation, not a linear one, and the code should be read with that in mind.

**A resize function should be source-agnostic.** `rescaleFrame()` is written to accept a raw frame and return a raw frame — it has no idea whether that frame came from `imread()`, a video loop, or a webcam. This is a deliberate design pattern: build small utility functions around the *data* (arrays), not around the *source* of the data, so the same function is reusable everywhere without modification.

**Fail loudly and early, not silently and late.** This session introduces `capture.isOpened()` and explicit checks on `isTrue`/`frame is None` before attempting to use a frame. Rather than letting the program crash deep inside OpenCV with a cryptic assertion error, the code checks assumptions at the boundary — right after reading — and exits with a clear message if those assumptions fail. This is a shift from Session 1's "let the error happen and interpret it after the fact" toward proactively guarding against bad states.

**Interpolation matters even if it's invisible at first glance.** `cv.INTER_AREA` isn't an arbitrary default — it's specifically well-suited to shrinking images, since it computes each new pixel as an area-weighted average of the source pixels, which avoids the aliasing artifacts that simpler methods (like nearest-neighbor) can introduce when downsizing. The choice of interpolation method is a quiet but meaningful decision baked into what looks like a one-line resize call.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| `rescaleFrame()` vs `changeRes()` | Post-hoc resizing (any source) vs. source-level resolution (live only) |
| Scale factors multiply across dimensions | 0.5 scale ≠ half the area — it's a quarter |
| `capture.isOpened()` / frame validity checks | Catch bad state early instead of crashing deep in OpenCV |
| `cv.INTER_AREA` | Appropriate interpolation choice specifically for shrinking images |
| Reusable resize function | Works identically on images, video files, and webcam frames |