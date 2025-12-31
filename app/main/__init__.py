from flask import Blueprint, render_template

main = Blueprint("main", __name__)

from app.utils import success_response
from app.main.mock_data import DISTRICT_DATA, BUILDING_DATA, PREDICT_DATA


@main.route("/")
def index():
    """메인 페이지 라우트.
    
    애플리케이션의 홈 페이지를 렌더링합니다.
    
    Returns:
        str: 렌더링된 'main/index.html' 템플릿.
    """
    return render_template("main/index.html")


@main.route("/district", methods=["POST"])
def district_data():
    """자치구별 데이터 API.
    
    Bar Chart 렌더링을 위한 자치구별 변동률 데이터를 반환합니다.
    (현재는 Mock 데이터를 사용)
    
    Returns:
        tuple[Response, int]: JSON 포맷의 자치구 데이터 및 200 상태 코드.
    """
    # Bar Chart용 목(Mock) 데이터
    return success_response(DISTRICT_DATA)


@main.route("/building", methods=["POST"])
def building_data():
    """건물 용도별 데이터 API.
    
    Area Chart 렌더링을 위한 건물 용도별 평균 가격 데이터를 반환합니다.
    (현재는 Mock 데이터를 사용)
    
    Returns:
        tuple[Response, int]: JSON 포맷의 건물 데이터 및 200 상태 코드.
    """
    # Area Chart용 목(Mock) 데이터
    return success_response(BUILDING_DATA)


@main.route("/predict/location", methods=["POST"])
def predict_location():
    """위치별 예측 데이터 API.
    
    테이블 렌더링을 위한 위치별 예측 상세 데이터를 반환합니다.
    (현재는 Mock 데이터를 사용)
    
    Returns:
        tuple[Response, int]: JSON 포맷의 예측 데이터 및 200 상태 코드.
    """
    # 테이블(Table)용 목(Mock) 데이터
    return success_response(PREDICT_DATA)

