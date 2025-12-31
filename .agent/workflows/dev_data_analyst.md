---
description: 데이터 분석의 전 과정(질의 정의 -> EDA -> 심층 분석 -> 리포팅)을 체계적으로 가이드하는 워크플로우입니다.
---

# Data Analyst Workflow

Python 생태계(Jupyter, Pandas, Seaborn)를 활용하여 데이터에서 인사이트를 도출하는 전문 분석 워크플로우입니다. OSEMN 방법론을 따릅니다.

### 1단계: 분석 환경 및 목표 정의 (Environment & Goal)
1.  **Notebook Setup**: `docs/analysis/` 또는 `notebooks/` 경로에 새로운 Jupyter Notebook(`01_EDA_[주제].ipynb`)을 생성합니다.
2.  **Objective**: 첫 번째 셀에 마크다운으로 해결하고자 하는 질문(Question)을 정의합니다.
3.  **Library Loading**: 필수 라이브러리(`pandas`, `matplotlib`, `seaborn`)를 임포트하고 한글 폰트 설정을 완료합니다.

### 2단계: 데이터 적재 및 전처리 (Obtain & Scrub)
1.  **Data Loading**: `pd.read_csv()` 등으로 데이터를 로드하고 `df.head()`로 확인합니다.
2.  **Sanity Check**: `df.info()`, `df.describe()`로 결측치(Null)와 이상치를 식별합니다.
3.  **Cleaning**: 결측치 처리(삭제/대체) 및 데이터 타입 변환 코드를 작성합니다.

### 3단계: 탐색적 데이터 분석 (Explore - EDA)
1.  **Univariate Analysis**: 개별 변수의 분포를 히스토그램(`sns.histplot`)으로 확인합니다.
2.  **Bivariate Analysis**: 변수 간의 관계를 산점도(`sns.scatterplot`)나 상관계수(`df.corr()`, Heatmap)로 파악합니다.
3.  **Insight Logging**: 발견된 특징이나 특이점을 마크다운 셀에 즉시 기록합니다.

### 4단계: 머신러닝/딥러닝 모델링 (Model & Optimize)
단순 분석을 넘어 예측 모델을 구축하는 단계입니다. (필요시 수행)

1.  **Preprocessing**: 모델링을 위한 인코딩(Encoding)과 스케일링(Scaling)을 적용합니다.
2.  **Split & Validation**: `train_test_split` 및 `K-Fold` 교차 검증으로 신뢰성 있는 평가 환경을 만듭니다.
3.  **Baseline Model**: 가장 간단한 모델(예: Logistic Regression)로 기준점(Baseline)을 잡습니다.
4.  **Advanced Modeling**: Random Forest, XGBoost, Deep Learning 등 고도화된 모델을 실험하고 Hyperparameter Tuning을 수행합니다.

### 5단계: 해석 및 리포팅 (Interpret & Report)
분석과 모델링 결과를 비즈니스 언어로 번역합니다.

1.  **Interpretation**: 모델의 예측 원인(Feature Importance, SHAP)을 분석하고, 오답(Error Analysis)을 파고듭니다.
2.  **Visualization**: 최종 주장을 뒷받침할 결정적인 시각화 차트(Key Chart)를 정리합니다.
3.  **Action Item**: "그래서 무엇을 해야 하는가?"에 대한 구체적인 실행 계획을 제안합니다.
