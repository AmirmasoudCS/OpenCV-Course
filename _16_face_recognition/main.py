from _16_face_recognition.train import create_train
from _16_face_recognition.saver import save
from _16_face_recognition.loader import load_train

def main():
    overwrite: bool = int(input("Overwrite the train results?\n(0) No    (1) Yes\n"))

    if overwrite:
        features, labels = create_train()
        save(features, labels)

    else:
        features, labels = load_train()

    print(len(features), labels)
        

if __name__ == "__main__":
    main()