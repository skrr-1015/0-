import os
import shutil
import random
from pathlib import Path

# 원본 데이터 경로 (압축 푼 TrashNet 폴더 경로를 여기에 넣어)
SRC_DIR = r"C:\Users\dnwls\OneDrive\바탕 화면\Garbage classification\Garbage classification"

# YOLO용 새 경로
DST_DIR = "datasets/recycle"

# 클래스 매핑 (YOLO용 인덱스)
classes = {
    "cardboard": 0,
    "glass": 1,
    "metal": 2,
    "paper": 3,
    "plastic": 4,
    "trash": 5
}

# 새 폴더 구조 생성
for split in ["train", "val"]:
    os.makedirs(f"{DST_DIR}/images/{split}", exist_ok=True)
    os.makedirs(f"{DST_DIR}/labels/{split}", exist_ok=True)

# 각 클래스별 처리
for cls, idx in classes.items():
    img_dir = Path(SRC_DIR) / cls
    imgs = list(img_dir.glob("*.jpg"))
    random.shuffle(imgs)

    split_idx = int(len(imgs) * 0.8)  # 80% train
    train_imgs, val_imgs = imgs[:split_idx], imgs[split_idx:]

    # train 이동
    for img in train_imgs:
        shutil.copy(img, f"{DST_DIR}/images/train/{img.name}")
        with open(f"{DST_DIR}/labels/train/{img.stem}.txt", "w") as f:
            f.write(f"{idx} 0.5 0.5 1 1\n")

    # val 이동
    for img in val_imgs:
        shutil.copy(img, f"{DST_DIR}/images/val/{img.name}")
        with open(f"{DST_DIR}/labels/val/{img.stem}.txt", "w") as f:
            f.write(f"{idx} 0.5 0.5 1 1\n")

print("✅ 데이터셋 정리가 완료되었습니다!")