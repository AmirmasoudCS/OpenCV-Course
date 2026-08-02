# Session 6 — Contours

## Overview

This session moves from detecting *where* intensity changes sharply (edges, from Session 4) to identifying *shapes* — continuous boundaries that outline objects. Contours are one of the first genuinely structural pieces of information OpenCV can extract from an image: rather than a scattered map of edge pixels, a contour is a connected curve, which opens the door to counting objects, measuring their size, or approximating their shape. This session explores two different paths to get there — via Canny edges, and via simple thresholding — and compares them side by side.

## Files

- `main.py` — menu-driven entry point comparing the two contour-finding approaches
- `find_contours.py` — wraps `cv.findContours()` to extract contours and hierarchy from a binary image
- `threshold.py` — binarizes a grayscale image using a fixed threshold

## Core Philosophy

**Contours are not the same thing as edges, even though they're closely related and often interchangeable in practice.** The comment at the top of `main.py` makes this distinction explicit: edges are a raw signal about where pixel intensity changes sharply, while contours are the result of tracing *continuous* boundaries out of that (or similar) information. In practice, running Canny before contour detection works well because the edges are already thin and well-defined — but conceptually, `cv.findContours()` doesn't care how its binary input was produced, only that foreground and background are cleanly separated.

**`cv.findContours()` fundamentally needs a binary image — everything upstream exists to produce one.** Whether that binary image comes from Canny edge detection (choice 1) or from `cv.threshold()` (choice 2), the underlying requirement is the same: pixels need to be cleanly split into "belongs to a shape" (typically white/255) versus "background" (black/0). This is why both paths in `main.py` funnel toward a binarization step before contours are ever extracted — contour-finding isn't a general-purpose image analysis tool, it's specifically a boundary-tracer over black-and-white input.

**Thresholding is a simpler, more direct way to binarize an image than the blur-then-Canny pipeline.** `cv.threshold()` makes one blunt decision per pixel: is it above or below a cutoff value? Everything below becomes black, everything above becomes white. This sacrifices the nuance of true edge detection (which considers gradients and connects weaker edges to strong ones) in exchange for simplicity and speed — and it works well specifically when there's strong contrast between the object and its background, which is why it's presented here as a genuine alternative to Canny rather than a lesser version of it.

**Contours come as a structured, two-part result: the shapes themselves, and how they relate to each other.** `cv.findContours()` returns both `contours` (a list of point arrays, each describing one boundary) and `hierarchies` (describing nesting — which contours are "inside" others, like a hole in a donut shape). This session doesn't yet do anything with the hierarchy, but its presence in the return signature is worth noting: contour detection isn't just "find the shapes," it's also "understand how they're nested," which becomes essential once an image has overlapping or nested objects.

**Drawing contours onto a blank canvas, rather than the original image, isolates the result for inspection.** `cv.drawContours(blank, contours, -1, (0, 0, 255), 2)` draws onto a freshly created black array the same size as the original — not onto the photo itself. This is a deliberate choice that echoes Session 3: it lets you evaluate *only* what was detected, without the original image's colors and detail making it harder to judge whether the contour-finding actually worked well. The `-1` index means "draw all contours," reusing the same "-1 as a special convention" pattern seen with fill thickness back in Session 3.

**The contour count is a quick, informal sanity check — and a good habit to keep.** Printing `len(contours)` before visualizing anything gives an immediate signal about whether the parameters (threshold value, Canny thresholds) are in a reasonable range. An unexpectedly huge number of contours usually means noise is being picked up as tiny false boundaries; an unexpectedly small number suggests the threshold is too aggressive and merging distinct objects together. This kind of numeric sanity check before visual inspection is a useful habit whenever a pipeline has tunable parameters.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Contours ≠ edges | Contours are continuous, connected boundaries — a step beyond raw edge pixels |
| `findContours()` needs binary input | Both Canny and thresholding exist here purely to produce that binary image |
| Thresholding vs. Canny | A blunt cutoff vs. gradient-aware detection — simpler but less nuanced |
| `contours` + `hierarchies` | Shapes themselves, plus how they're nested relative to each other |
| Drawing on a blank canvas | Isolates the detection result for clean visual evaluation |
| `len(contours)` as a sanity check | Quick numeric signal for whether parameters are reasonably tuned |