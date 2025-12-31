"""
메인 애플리케이션용 목(Mock) 데이터.

이 모듈은 API 응답 테스트 및 프론트엔드 연동을 위한 가상 데이터를 포함합니다.
- DISTRICT_DATA: 자치구별 변동률 데이터
- BUILDING_DATA: 건물 용도별 평균 가격 데이터
- PREDICT_DATA: 위치별 예측 결과 데이터
"""

# 메인 애플리케이션용 목(Mock) 데이터


DISTRICT_DATA = [
    {"district_name": "Gangnam", "total_change_rate": 12.5},
    {"district_name": "Seocho", "total_change_rate": 10.2},
    {"district_name": "Songpa", "total_change_rate": 8.7},
]

BUILDING_DATA = [
    {"building_use": "아파트", "reception_year": "2020", "avg_price_per_sqm": 25000},
    {"building_use": "아파트", "reception_year": "2021", "avg_price_per_sqm": 27000},
    {"building_use": "오피스텔", "reception_year": "2020", "avg_price_per_sqm": 12000},
    {"building_use": "오피스텔", "reception_year": "2021", "avg_price_per_sqm": 13000},
]

PREDICT_DATA = [
    {
        "district_name": "Gangnam",
        "legal_dong_name": "Yeoksam",
        "change_rank": 1,
        "total_change_rate": 15.2,
        "price_per_sqm_format": "35,000,000",
        "transaction_count": 120,
    },
    {
        "district_name": "Seocho",
        "legal_dong_name": "Banpo",
        "change_rank": 2,
        "total_change_rate": 14.1,
        "price_per_sqm_format": "42,000,000",
        "transaction_count": 85,
    },
]

