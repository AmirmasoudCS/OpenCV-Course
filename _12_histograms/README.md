# Session 12 — Histograms

## Overview

This session shifts from *looking at* an image to *counting* it. A histogram doesn't show what an image looks like — it shows how its pixel intensities are distributed: how many pixels are dark, how many are bright, and everything in between. This turns an image into a statistical summary, and this session walks through four variations of that idea — grayscale, masked grayscale, color, and masked color — each building on the last.

## Core Philosophy

**A histogram is a count, not a picture — and `cv.calcHist()`'s parameters exist entirely to define exactly what's being counted.** Every call follows the same shape: which image(s) to read from, which channel to look at, whether to restrict counting to a masked region, how many buckets ("bins") to sort intensity values into, and what range those values span. Understanding this function means understanding that it's answering one question — "for each intensity bucket, how many pixels fall into it?" — and every argument narrows down exactly which pixels and which intensity dimension get counted.

**A grayscale histogram is the simplest case because there's only one channel to ask about.** `cv.calcHist([grey_image], [0], None, [256], [0, 256])` requests channel `0` (the only one that exists) across the full 0–255 range, with no mask (`None`) — meaning every pixel in the entire image contributes. The resulting plot is a direct answer to "how much of this image is dark vs. bright, and in what proportions" — a genuinely useful signal on its own for things like detecting under/overexposed images, independent of any color information.

**Masking a histogram doesn't change *how* the histogram is computed — it changes *which pixels are eligible to be counted at all*.** This is the same masking concept from Session 11, reused for a completely different purpose: rather than masking to visually isolate a region, here the mask restricts `calcHist()`'s attention to only the pixels under the circular mask (`mask=mask`), silently excluding everything else from the count. The histogram shape that results describes the intensity distribution *of that specific region only* — useful for questions like "is this particular area of the image bright or dark," rather than the image as a whole.

**A color histogram isn't one histogram — it's three, computed independently and overlaid.** The loop over `('b', 'g', 'r')` calls `cv.calcHist()` three separate times, once per channel index (`0`, `1`, `2`), because each channel is fundamentally a separate grayscale-like intensity map (a direct callback to Session 8's channel-splitting lesson). There's no single combined "color histogram" — color histograms are, structurally, three grayscale histograms plotted together, one line per channel, letting you compare how much blue, green, and red intensity exists across the image at a glance.

**Combining color and masking in choice 4 demonstrates that these two techniques compose cleanly, because they operate on independent axes of the same function call.** The mask restricts *which pixels* are counted; the channel index restricts *which color dimension* is being measured. Since `calcHist()` accepts both simultaneously, producing a masked *and* color-aware histogram doesn't require new logic — it's simply supplying a mask to the same three-channel loop already used in choice 3. This is a good example of how a well-designed function with independent parameters lets you combine capabilities without any special-casing.

**Fixed y-axis limits (`plt.ylim([0, 5000])` / `[0, 4000])`) are a plotting choice, not a property of the data — and it's worth being aware they were chosen for this specific image.** Because histograms count pixels, their scale depends entirely on the image's resolution and how concentrated its intensities are — a different photo could easily have peaks far above or below these hardcoded limits. These values work here because they were tuned to this particular image; applying this code to a different photo might require adjusting them to avoid a clipped or oddly empty-looking plot.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Histogram = intensity distribution, not an image | Reduces an image to a statistical summary of brightness/color counts |
| `calcHist()`'s parameters | Each argument narrows exactly which pixels and which channel get counted |
| Grayscale histogram | Simplest case — one channel, full image, no mask |
| Masked histogram | Same masking concept as Session 11, repurposed to restrict *counting*, not just display |
| Color histogram = 3 histograms overlaid | One per channel — direct extension of Session 8's channel-splitting idea |
| Masking + color together | The two techniques compose naturally since they act on independent parameters |
| Hardcoded axis limits | Tuned to this specific image — may need adjusting for others |