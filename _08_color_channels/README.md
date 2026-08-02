# Session 8 — Color Channels

## Overview

This session pulls apart the assumption, quietly relied on since Session 1, that a color image is one indivisible thing. In reality, a BGR image is three separate grayscale images stacked together — one per channel — and this session makes that literal by splitting an image into its Blue, Green, and Red components, inspecting each one individually, and merging them back together.

## Files

- `color_channels.py` — splits an image into B/G/R channels, visualizes each in isolation, and reconstructs the original by merging them

## Core Philosophy

**A color image is three grayscale images that happen to be interleaved.** `cv.split(image)` returns `b`, `g`, `r` as three separate single-channel arrays — and critically, each one *is* a grayscale image, not a "blue-tinted" or "colored" one. This is the central realization of the session: color isn't some indivisible property of a pixel, it's the *combination* of three independent intensity measurements, and OpenCV represents it exactly that way under the hood.

**Displaying a channel as grayscale, rather than as a color, is what actually reveals its meaning.** When `b`, `g`, and `r` are shown directly with `cv.imshow()`, they render in grayscale — and the comment in the code spells out why that's the correct and informative way to view them: brightness in that grayscale image directly encodes *how much* of that color is present at each pixel, not what color it looks like. A bright area in the "Blue Channels" window means "lots of blue here," not "this is blue." Viewing channels this way turns an abstract idea (channel intensity) into something you can literally see varying across the image.

**Reconstructing a single-color image (`blue_image`, `green_image`, `red_image`) requires putting the *other two* channels back — just filled with zeros.** This is a subtle but important detail: `cv.merge([b, blank, blank])` doesn't produce "the blue channel as an image," it produces a full 3-channel BGR image where the green and red channels are entirely absent (zero). This is necessary because `cv.imshow()` (and BGR images generally) expect three channels — there's no such thing as displaying "pure blue" without a channel structure to display it in. The blank channels aren't a workaround, they're a structural requirement of what a color image *is*.

**Shape tells you the channel count, and it's worth reading deliberately.** The code prints `image.shape` (which includes a third dimension — the channel count) against `b.shape`, `g.shape`, `r.shape` (which don't have one at all). This isn't incidental — it's direct evidence of the split having actually happened: a full-color image is `(height, width, 3)`, while an individual channel is just `(height, width)`, a genuinely two-dimensional array indistinguishable in structure from any other single-channel grayscale image. Checking `.shape` is a fast, reliable way to confirm what kind of image you're holding at any point in a pipeline.

**Merging is the exact inverse of splitting, and recombining the *unmodified* channels proves the operation is lossless.** `cv.merge([b, g, r])` at the end reconstructs an image identical to the original — a natural "does this actually work" sanity check. This matters beyond just being a nice demonstration: it establishes that split/merge is a completely reversible operation, which means channels can be freely extracted, individually modified (boosting one, zeroing another, swapping order), and merged back — a technique that becomes genuinely useful for tasks like color-based masking or channel-specific adjustments in later work.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| `cv.split()` | A BGR image is really three separate grayscale images stacked together |
| Channel brightness = color intensity | Not "what color," but "how much of that color" at each pixel |
| Blank channels in `cv.merge()` | Required structurally — there's no way to display "pure blue" without 3 channels |
| `.shape` with vs. without a 3rd dimension | Fast, reliable way to tell a full-color image from a single channel |
| `cv.merge()` reverses `cv.split()` | Confirms the operation is lossless — channels can be split, edited, and recombined |