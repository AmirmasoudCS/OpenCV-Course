# Face Recognition Pipeline Using OpenCV LBPH

<div align="center">
    <img src="assets/results/validate/Paul_McCartney/pm29.jpg"/>
</div>

## Overview

<div align="center">
    <img src="assets/graphical_abstract/face_recognition_graphical_abstract.png">
</div>

A face recognition pipeline built with **OpenCV** that identifies known individuals from detected face regions.

This project extends the previous **Face Detection** pipeline by adding an identity recognition stage.

While face detection answers:

> "Is there a face in this image, and where is it?"

face recognition answers:

> "Whose face is this?"

The system uses:

- **Haar Cascade Classifier** for face detection
- **LBPH (Local Binary Patterns Histograms)** for face recognition

---

## Task Description

The system:

1. Loads a dataset containing images of known individuals.
2. Detects faces using Haar Cascade.
3. Crops detected face regions.
4. Trains an LBPH face recognizer.
5. Loads the trained recognition model.
6. Processes validation images.
7. Predicts the identity of each detected face.
8. Saves annotated results with predicted labels.

**Pipeline modes:**

- **Training Mode** — detects faces from training images and creates an LBPH model.
- **Validation Mode** — evaluates the trained model on unseen images and saves recognition results.

---

## Implementation Overview

Built with:

- **Python**
- **OpenCV**
- **NumPy**
- **LBPH Face Recognizer**
- **Haar Cascade Face Detector**

The pipeline is divided into separate modules:

```text
Training Images
       │
       ▼
Haar Cascade Detector
       │
       ▼
Face Cropping
       │
       ▼
LBPH Training
       │
       ▼
face_trained.yaml
       │
       ▼
Validation Images
       │
       ▼
Haar Cascade Detector
       │
       ▼
Face Recognition
       │
       ▼
Annotated Output Images
```

Each component is separated into independent modules to keep responsibilities clear.

---

## Recognition Algorithm Overview

### 1. Face Detection

The first stage uses the same Haar Cascade detector from the previous project.

For each image:

1. Load the image.
2. Convert it to grayscale.
3. Detect face regions using:

```python
detectMultiScale()
```

4. Extract detected face regions.

---

### 2. Face Recognition Using LBPH

The extracted face regions are passed to an OpenCV LBPH recognizer.

LBPH works by:

1. Comparing local binary patterns around each pixel.
2. Creating histograms describing local texture information.
3. Comparing the histogram of an unknown face with the trained examples.
4. Returning the closest matching identity.

The recognizer outputs:

```python
label, distance = face_recognizer.predict(face)
```

where:

- `label` → predicted person index
- `distance` → similarity distance

Lower distance means a closer match.

> Note: Despite OpenCV naming this value "confidence", it is actually a distance score. Higher values indicate worse matches.

---

## Project Structure

```text
📁 _16_face_recognition
├── 📁 assets
│   ├── 📁 images
│   │   ├── 📁 train
│   │   └── 📁 validate
│   └── 📁 results
│       ├── 📁 train
│       └── 📁 validate
├── 📁 config
│   ├── 🐍 constants.py
│   ├── 📄 face_trained.yaml
│   ├── 📄 features.npy
│   ├── 📄 labels.npy
│   └── 🐍 paths.py
├── 🐍 loader.py
├── 🐍 main.py
├── 📘 README.md
├── 🐍 recognize.py
├── 🐍 saver.py
└── 🐍 train.py
```

---

## Running the Project

Install dependencies:

```bash
pip install -r face_recognition_requirements.txt
```

Run:

```bash
python main.py
```

During execution, the user can choose whether to regenerate training data:

```text
Overwrite the train results?
(0) No
(1) Yes
```

Selecting:

```text
1
```

will:

- detect faces from training images
- regenerate cropped face samples
- retrain the LBPH model

Selecting:

```text
0
```

will:

- load existing cropped face samples
- reuse the previous training results

Then to run recognition:

```bash
python recognize.py
```

and the results of recognition are saved.

---

# Dataset

The dataset consists of images of all four members of **The Beatles**:

- George Harrison
- John Lennon
- Paul McCartney
- Ringo Starr

Each person contains:

- **28 total images**
- **20 training images**
- **8 validation images**

The validation images are completely separated from the training set to evaluate generalization.

---

# Training Configuration

Training process:

```text
20 images/person

        ↓

Face detection

        ↓

Face crop extraction

        ↓

LBPH training

        ↓

face_trained.yaml
```

The trained model is saved and reused during validation.

---

# Validation Results

## Overall Performance

The recognizer was evaluated on:

```
4 people × 8 validation images = 32 total images
```

The system correctly identified:

```
13 / 32 images
```

resulting in an overall accuracy of:

```
40.6%
```

Performance varied significantly between individuals:

| Person | Correct Predictions | Total Images | Accuracy |
|---|---:|---:|---:|
| George Harrison | 4 | 8 | 50.0% |
| John Lennon | 5 | 8 | 62.5% |
| Paul McCartney | 3 | 8 | 37.5% |
| Ringo Starr | 1 | 8 | 12.5% |
| **Overall** | **13** | **32** | **40.6%** |

---

# Successful Recognitions

The recognizer performed best when:

- faces were frontal
- lighting conditions were similar to training images
- facial features were clearly visible

Examples:

<table align="center">
<tr>

<td align="center">
<img src="assets/results/validate/Ringo_Starr/rs22.jpg" width="250"><br>
<sub><em>Correct recognition example</em></sub>
</td>

<td align="center">
<img src="assets/results/validate/John_Lennon/jl9.jpg" width="250"><br>
<sub><em>Correct recognition example</em></sub>
</td>

<td align="center">
<img src="assets/results/validate/George_Harrison/gh9.jpg" width="250"><br>
<sub><em>Correct recognition example</em></sub>
</td>

</tr>
</table>

---

# Misclassification Analysis

The main challenge was distinguishing between visually similar individuals.

Observed confusion patterns:

| Actual Person | Predicted As |
|---|---|
| George Harrison | John Lennon, Paul McCartney |
| John Lennon | George Harrison, Ringo Starr |
| Paul McCartney | George Harrison |
| Ringo Starr | George Harrison |

Paul McCartney was especially difficult for the model, frequently being classified as George Harrison.

These errors occur because LBPH relies on local texture patterns rather than high-level facial representations. Similar hairstyles, facial hair, lighting, and image quality can produce similar feature patterns.

---

# Interesting Failure Cases

## 1. Unknown Person Classified as a Known Identity

One interesting case occurred when images containing **Yoko Ono** were processed.

Although she was not included in the training dataset, the recognizer classified her as:

```
George Harrison
```

Example:

<table>
    <tr>
        <td align="center">
            <img src="assets/results/validate/John_Lennon/jl21.jpg" width="400">
        </td>
        <td align="center">
            <img src="assets/results/validate/John_Lennon/jl28.jpg" width="400">
        </td>
    </tr>
</table>

<em>Unknown person incorrectly classified as George Harrison.</em>

This happens because LBPH is a **closed-set classifier**.

It assumes that every detected face belongs to one of the known classes.

Therefore, instead of returning:

```
Unknown
```

it returns the closest available match.

---

## 2. False Face Detection Propagating Into Recognition

The recognition pipeline depends on the accuracy of the Haar Cascade detector.

If the detector incorrectly identifies a non-face region, LBPH will still attempt recognition.

Example:

<div align="center">
<img src="assets/results/validate/George_Harrison/gh18.jpg" width="400">
</div>

<em>A non-face region incorrectly detected and classified.</em>

Since LBPH has no understanding of what a face is, it cannot reject these detections.

> I guess this is happened because in training face, there were parts of clothings and jewelry cropped as the faces and thus the model trained on them thinks they are an actual person!

---

## 3. Occlusion and Face Detection Failure

In one Ringo Starr validation image, the detector failed to locate the face.

Possible causes:

- smoke partially covering the face
- mouth position changing facial appearance
- reduced visibility of important facial regions

Example:

<div align="center">
<img src="assets/results/validate/Ringo_Starr/rs16.jpg" width="400">
</div>

<em>Face detection failure due to partial occlusion.</em>

Because no face was detected, the recognition stage was never executed.

---

# Limitations

The current pipeline has several limitations:

- Small training dataset
- Sensitive to lighting changes
- Sensitive to pose variations
- Cannot reliably recognize unseen individuals
- LBPH depends heavily on image texture
- False detections from Haar Cascade affect recognition accuracy
- No true "unknown person" rejection mechanism

---

# Future Improvements

Possible improvements:

- Replace Haar Cascade with a deep learning face detector
- Replace LBPH with modern face embeddings:
  - FaceNet
  - ArcFace
  - DeepFace
- Add unknown-person detection using distance thresholds
- Increase training dataset size
- Apply face alignment before recognition
- Benchmark classical methods against deep learning approaches

---

# Conclusion

This project demonstrates a complete classical computer vision face recognition pipeline using OpenCV.

While Haar Cascade and LBPH provide a lightweight solution with minimal computational requirements, the results show their limitations when handling real-world variations.

The system successfully recognized several validation images but struggled with visually similar individuals, unknown faces, and occlusions.

These limitations highlight why modern face recognition systems rely on deep learning-based feature extraction methods, which provide more robust identity representations across different poses, lighting conditions, and environments.