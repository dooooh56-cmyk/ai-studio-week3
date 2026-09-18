import pandas as pd
from pathlib import Path
import openpyxl
pd.set_option("display.width", 180)

# 1. 데이터 로드/인코딩 해결
# pipeline.py가 있는 week03 폴더를 기준으로 CSV 파일을 찾도록 수정
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding='EUC-KR')

# print(df.shape)
# print(df.info())

# 2. 정제/파생 열 생성
df["단가"] = (pd.to_numeric(df["단가"].astype(str).str.replace(",", "", regex=False), errors="coerce").astype("int64"))
df["매출액"] = df["단가"] * df["수량"]
# print(df.head())

# 3. '월'컬럼 추가, groupby 집계
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month
# print(df.head())
# print(df.tail())

#카테고리별 매출 합계
by_cat = df.groupby("카테고리")["매출액"].sum()
# print(by_cat.head())

# 월별 x 카테고리별, 합계와 평균
report = df.groupby(["월", "카테고리"])["매출액"].agg(
  총매출="sum", 평균매출="mean", 거래건수="count"
)
report = report.reset_index()
# print(report)

# 4. Excel 저장, 검증
if not df["매출액"].sum() == report["총매출"].sum():
  print("Error: 원본과 집계표 불일치")
else:
  with pd.ExcelWriter("Monthly_Report.xlsx", engine="openpyxl") as writer:
    report.to_excel(writer, sheet_name="월별카테고리요약", index=False)
    by_cat.reset_index().to_excel(writer, sheet_name="카테고리별합계", index=False)