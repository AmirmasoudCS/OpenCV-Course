# Session 13 — Thresholding

## Overview

Thresholding made a brief appearance back in Session 6 as a means to an end — a way to produce binary input for contour detection. This session gives it full attention as a topic in its own right, comparing simple (manual) thresholding against adaptive (computed) thresholding, and examining why a single global threshold value is often not good enough.

## Core Philosophy

**Thresholding is a decision rule applied identically to every pixel: is it above or below a cutoff?** The comment at the top of the file states the rule plainly — below threshold becomes black, at or above becomes white (or the chosen maximum value). What makes this session more than a repeat of Session 6 is the focus on *how that cutoff gets decided*, comparing a version where the human picks it versus a version where the algorithm computes it locally.

**`cv.THRESH_BINARY_INV` reveals that "binary" doesn't dictate *which* value means foreground — that's a separate choice layered on top.** Running the exact same threshold value through `cv.THRESH_BINARY` and `cv.THRESH_BINARY_INV` produces two images that are pixel-for-pixel opposites of each other. This matters because "binary" only guarantees two possible values — it says nothing about which one represents the object of interest versus the background. Depending on whether the subject is lighter or darker than its surroundings, the inverted version may actually be the more useful one for downstream steps like contour detection, where you generally want the shape you care about to be the white (255) region.

**Simple thresholding's core weakness is baked into its name: the threshold has to be chosen manually, and one number rarely fits an entire image.** A single global cutoff assumes the whole image has fairly uniform lighting — but real photos often have brighter and darker regions from shadows, uneven lighting, or gradients. A threshold tuned to work well in one area of the image may badly misclassify pixels in another area that's naturally darker or brighter, even if those pixels are conceptually part of the same "foreground" object.

**Adaptive thresholding's key idea is to stop asking "what's the one best threshold for this whole image" and instead ask "what's the best threshold for this specific neighborhood."** `cv.adaptiveThreshold()` computes a *different* threshold for each pixel, based only on the pixels around it (the size of that neighborhood is `block_size`). This directly addresses simple thresholding's weakness: a region that's locally dark can still have its own locally-appropriate cutoff, rather than being judged against a threshold that was really only calibrated for a different, brighter part of the image.

**The `method` parameter is really answering "how should the local threshold be computed," and mean is just the simplest option.** `cv.ADAPTIVE_THRESH_MEAN_C` computes each pixel's local threshold as the unweighted mean of its neighborhood (sized by `block_size`) — echoing the same "simple average" logic seen with `cv.blur()` back in Session 9. The code's closing note about a Gaussian-weighted alternative existing (`ADAPTIVE_THRESH_GAUSSIAN_C`) is a direct parallel to the averaging-vs-Gaussian-blur relationship from that session: the mean-based version treats every neighboring pixel equally, while a Gaussian-based version would weight closer pixels more heavily when computing the local threshold.

**The `c` parameter is a manual fine-tuning knob layered on top of an otherwise automatic process — a reminder that "adaptive" doesn't mean "parameter-free."** Even though the whole point of adaptive thresholding is to avoid hand-picking a single global cutoff, `c` still lets you nudge the *computed* threshold up or down slightly. This is worth noting because it tempers the idea that adaptive thresholding fully removes manual tuning from the picture — it shifts the tuning problem from "pick the right absolute threshold" to "pick the right neighborhood size and adjustment," which is usually easier, but not eliminated entirely.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Thresholding = a per-pixel binary decision | Reduces an image to two values based on a cutoff rule |
| `THRESH_BINARY` vs `THRESH_BINARY_INV` | Same cutoff, opposite polarity — "binary" doesn't decide which value is foreground |
| Simple thresholding's weakness | One global cutoff struggles with images that have uneven lighting |
| Adaptive thresholding's core idea | Compute a local threshold per neighborhood instead of one global value |
| `ADAPTIVE_THRESH_MEAN_C` | Local average as the threshold — same logic as Session 9's simple blur averaging |
| `c` parameter | Adaptive thresholding still has tuning knobs — it's not fully automatic |