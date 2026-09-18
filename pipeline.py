import pandas as pd
from pathlib import Path
pd.set_option("display.width", 180)

# pipeline.py가 있는 week03 폴더를 기준으로 CSV 파일을 찾도록 수정
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding='EUC-KR')

print(df.shape)
print(df.info())