# Session 11 — Masking

## Overview

This session is the direct payoff of Session 10's bitwise operations. Masking uses a binary image — the mask — to select exactly which pixels of a real photo should survive and which should be discarded, without ever touching the pixel values of the original image directly. Instead of manually slicing rectangular regions (as in Session 4's cropping), a mask can be *any shape*, giving far more precise control over which part of an image to isolate.

## Core Philosophy

**A mask is nothing more than the binary image from Session 10, now applied to a real photo instead of two abstract shapes.** `blank` is created the same way as before — a single-channel array of zeros — and a shape is drawn onto it the same way. Nothing new is introduced conceptually here; the mask is still just an on/off map. What's new is what it's paired with: instead of combining two synthetic shapes, this mask is used to filter a real, multi-channel color image.

**The mask's dimensions must match the image's spatial dimensions, but not its channel count — and that distinction matters.** `blank` is built from `image.shape[:2]`, deliberately slicing off the channel dimension so the mask is `(height, width)` while the image is `(height, width, 3)`. This isn't an inconsistency — a mask doesn't need color, it only needs to answer "keep or discard" for each spatial location, and that answer applies identically across all three of the image's color channels at once.

**`cv.bitwise_and(image, image, mask=mask)` is a slightly unusual-looking call, and understanding why reveals how masking actually works under the hood.** Passing the *same* image as both arguments might look redundant — ANDing anything with itself just returns itself — but the real logic lives in the `mask` keyword argument. The mask acts as an additional filter on *where* the AND operation is even allowed to write a result: at every pixel where the mask is 255, the output is `image AND image` (i.e., the original pixel, unchanged); at every pixel where the mask is 0, the output is forced to 0 (black), regardless of what AND would otherwise compute. In other words, the mask isn't participating in the bitwise logic between two images — it's acting as a stencil that decides which pixels get through at all.

**Masking succeeds where cropping (Session 4) is too rigid, because a mask can be any shape a bitwise operation can produce.** Cropping can only ever select a rectangle, because array slicing is inherently rectangular. A mask, by contrast, can be a circle (as here), or — per the code's closing comment — a more complex shape built by combining circles and rectangles with the same AND/OR operators from Session 10. This is the real reason masking exists as its own technique rather than being redundant with cropping: it decouples "the region I care about" from "the shape a NumPy slice is capable of expressing."

**Because masking discards pixels rather than removing them structurally, the output image keeps its original dimensions.** Unlike cropping, which produces a smaller image, a masked image is exactly the same size as the input — the excluded region is simply blacked out rather than removed. This is a meaningful tradeoff: masking preserves the original image's coordinate system (useful if you need to later overlay or compare against the unmasked original), at the cost of the output still technically containing "empty" black space rather than being a tight, minimal region.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Mask = same binary image concept as Session 10 | No new primitive — just applied to a real photo instead of synthetic shapes |
| Mask shape = image's `[:2]`, not full shape | A mask needs only spatial coverage, applied uniformly across all color channels |
| `bitwise_and(image, image, mask=mask)` | The mask acts as a stencil deciding *where* pixels pass through, not as a second operand |
| Masking vs. cropping | Masks can take any shape; cropping is limited to rectangles by array slicing |
| Masked output keeps original dimensions | Excluded regions are blacked out, not removed — unlike a crop |