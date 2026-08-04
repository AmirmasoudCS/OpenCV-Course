# Session 14 — Edge Detection

## Overview

Canny edge detection has been used as a tool since Session 4, but always as a given — a function called without asking what it actually computes internally. This session goes one level deeper, introducing Laplacian and Sobel as two more fundamental gradient-based methods, and situating Canny as something built *on top of* them rather than a separate, unrelated technique.

## Core Philosophy

**An edge is, mathematically, a place where intensity changes rapidly — and every method in this session is really just a different way of measuring that rate of change.** Laplacian and Sobel are both described in the code as computing "gradients," which is the key unifying idea: an edge isn't a special property OpenCV detects by magic, it's simply a large derivative of pixel intensity with respect to position. Once framed this way, the three techniques in this file stop looking like unrelated tools and start looking like variations on the same underlying calculus.

**Laplacian's core technical wrinkle — negative values needing `cv.CV_64F` and `np.absolute()` — exists because gradients are inherently signed, but images aren't.** A transition from black to white and a transition from white to black are, numerically, gradients of opposite sign (positive vs. negative slope) — but a standard image can only store non-negative pixel values (0–255, `uint8`). Computing the Laplacian in a higher-precision floating-point format (`CV_64F`) first *preserves* that sign information during the calculation, and only afterward is the absolute value taken and the result cast back down to `uint8` for display. Skipping this step (computing directly in `uint8`) would silently clip or wrap negative gradient values, corrupting the result — this is a good example of a case where choosing the right intermediate data type isn't a stylistic detail, it's necessary for correctness.

**Sobel splits the same underlying idea — "find the gradient" — into two separate, directional questions.** Rather than one combined gradient computation, `cv.Sobel(..., 1, 0)` and `cv.Sobel(..., 0, 1)` compute the rate of intensity change specifically along the x-axis and specifically along the y-axis, respectively. This distinction matters because real edges aren't only horizontal or only vertical — a diagonal edge, for instance, shows up as a *combination* of both gradients. Looking at `Sobel X` and `Sobel Y` separately shows you edges that are stronger in one direction than the other, which the single, direction-agnostic Laplacian result doesn't expose on its own.

**Combining the two Sobel directions with `bitwise_or` is a reasonable, simple way to merge them into one edge map — but it's worth recognizing it's a specific choice, not the only option.** OR-ing `sobelx` and `sobely` keeps a pixel as an edge if it was detected as an edge in *either* direction, giving a fuller picture of overall edge structure than either direction alone. This mirrors the same logic explored explicitly with shapes in Session 10 — here it's applied to gradient maps instead of geometric shapes, but the underlying "union" reasoning is identical.

**Canny isn't a fourth, independent technique — it's explicitly built using Sobel internally, which reframes everything learned about it in earlier sessions.** The comment in the code states this directly: Canny is a multi-stage algorithm, and one of those stages computes gradients using Sobel. This means the "familiar" `cv.Canny()` call from Sessions 4 and 6 was never a black box unrelated to what's being learned here — it was always doing something conceptually similar to Sobel, plus additional refinement steps (like non-maximum suppression and the dual-threshold hysteresis mentioned back in Session 4) that clean up and connect the raw gradient information into cleaner, thinner edges.

**The code's closing note — that Sobel tends to be favored in more advanced use — hints at a practical tradeoff between raw signal and refined output.** Canny's extra processing stages make it excellent for producing clean, ready-to-use edge maps (which is why it's been the default choice for contour detection in this course so far). But Sobel's raw, less-processed gradient output preserves more low-level directional information that Canny's later stages intentionally discard — information that can be valuable when building custom, more advanced pipelines rather than simply wanting a finished edge map.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Edge = large intensity gradient | Reframes Laplacian, Sobel, and Canny as variations on the same underlying idea |
| `CV_64F` + `np.absolute()` in Laplacian | Preserves signed gradient direction before casting back to displayable `uint8` |
| Sobel X vs. Sobel Y | Directional gradients — needed because edges aren't only horizontal or vertical |
| `bitwise_or(sobelx, sobely)` | Same union logic from Session 10, now applied to gradient maps instead of shapes |
| Canny uses Sobel internally | Not a separate technique — an extension of Sobel with added refinement stages |
| Sobel's raw output vs. Canny's refined output | A tradeoff between preserved detail and ready-to-use cleanliness |