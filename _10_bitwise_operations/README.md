# Session 10 — Bitwise Operations

## Overview

This session introduces bitwise operations — AND, OR, XOR, NOT — applied not to individual bits in the abstract, but to binary *images*, where each pixel is either fully "on" (255) or fully "off" (0). Two shapes, a rectangle and a circle, are drawn onto separate blank canvases and then combined using each operator, making the effect of each one immediately visible as overlapping or excluded regions. This is a foundational building block for masking, which shows up constantly in more advanced image processing.

## Core Philosophy

**A binary image turns every pixel into a boolean, and that's what makes bitwise logic applicable at all.** The comment at the top of the file states this directly: pixels here are either 0 (off) or 1/255 (on), nothing in between. This is a deliberate simplification from the multi-valued grayscale and 3-channel color images used everywhere else in the course — bitwise operators only make intuitive sense once an image has been reduced to this strictly on/off state, since AND/OR/XOR/NOT are fundamentally boolean operations applied pixel-by-pixel across two images of the same shape.

**Drawing shapes here uses a single value instead of a BGR tuple, and that's not a shortcut — it's a consequence of the image only having one channel.** `cv.rectangle(blank.copy(), ..., 255, -1)` passes `255` rather than something like `(0, 0, 255)`, because `blank` is a single-channel array (`np.zeros((400, 400))` with no third dimension), not a 3-channel BGR image. This ties back directly to Session 8's lesson on `.shape` — a single-channel array simply has no BGR structure to address, so a plain intensity value is both correct and the only option.

**AND, OR, and XOR each answer a different question about how two shapes relate spatially.** With the rectangle and circle as two overlapping regions, `bitwise_and` keeps only pixels that are "on" in *both* shapes — visually, this isolates the intersection. `bitwise_or` keeps a pixel if it's "on" in *either* shape — the union, showing the combined footprint of both. `bitwise_xor` keeps a pixel only if it's on in *exactly one* of the two, not both — visually carving out the overlap and leaving only the non-shared regions. Seeing all three side by side on the same two shapes is what makes each operator's logic click: they aren't abstract truth-table exercises, they translate directly into recognizable spatial relationships (intersection, union, symmetric difference).

**NOT is the odd one out because it's unary — it doesn't compare two images, it inverts one.** `cv.bitwise_not()` simply flips every pixel: on becomes off and vice versa. Applied to the rectangle or circle individually, this produces the shape's exact "negative" — everything that *wasn't* part of the shape lights up instead. This is conceptually simpler than AND/OR/XOR precisely because it only needs one input.

**Combining NOT with AND at the end demonstrates that these operators compose, which is exactly what makes them powerful for building masks.** The final line, `cv.bitwise_and(rectangle_not, circle_not)`, isn't a new primitive — it's AND applied to the *results* of two prior NOT operations, producing the region that is outside both shapes simultaneously (equivalent, by De Morgan's law, to the NOT of the union). This is the real payoff of the session: individually, each operator is simple, but chaining them together lets you carve out arbitrarily specific regions of an image — which is precisely the mechanism behind masking, where you isolate exactly the pixels you want to process while excluding everything else.

## Key Takeaways

| Concept | Why it matters |
|---|---|
| Binary image = pixels as booleans | The precondition that makes bitwise logic meaningful on images |
| Single value instead of BGR tuple | A single-channel array has no color structure — just intensity |
| AND / OR / XOR | Intersection, union, and symmetric difference of two shapes, made visible |
| NOT | Unary inversion — the shape's exact negative |
| Composing operators (NOT → AND) | The real power: chaining simple operators to isolate precise regions, the basis of masking |