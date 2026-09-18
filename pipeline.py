import pandas as pd
from pathlib import Path
pd.set_option("display.width", 180)

# 1. 데이터 로드/인코딩 해결
# pipeline.py가 있는 week03 폴더를 기준으로 CSV 파일을 찾도록 수정
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding='EUC-KR')

#print(df.shape)
#print(df.info())

# 2. 정제/파생 열 생성
df["단가"] = (pd.to_numeric(df["단가"].astype(str).str.replace(",", "", regex=False), errors="coerce").astype("int64"))
df["매출액"] = df["단가"] * df["수량"]
print(df.head())