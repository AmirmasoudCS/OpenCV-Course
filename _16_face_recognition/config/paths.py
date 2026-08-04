from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"
IMAGES = ASSETS / "images"
TRAIN = IMAGES / "train"
VALIDATE = IMAGES / "validate"
RESULTS = ASSETS / "results"
RESULTS_TRAIN = RESULTS / "train"
RESULTS_VALIDATE = RESULTS / "validate"
CONFIG = ROOT / 'config'

GEORGE_HARRISON_TRAIN = TRAIN / "George_Harrison"
JOHN_LENNON_TRAIN = TRAIN / "John_Lennon"
PAUL_MCCARTENY_TRAIN = TRAIN / "Paul_McCartney"
RINGO_STARR_TRAIN = TRAIN / "Ringo_Starr"

GEORGE_HARRISON_VALIDATE = VALIDATE / "George_Harrison"
JOHN_LENNON_VALIDATE = VALIDATE / "John_Lennon"
PAUL_MCCARTENY_VALIDATE = VALIDATE / "Paul_McCartney"
RINGO_STARR_VALIDATE = VALIDATE / "Ringo_Starr"