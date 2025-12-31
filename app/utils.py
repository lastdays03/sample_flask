from flask import jsonify


def success_response(data, message=None, code=200):
    """표준 성공 응답 래퍼.

    성공적인 API 요청에 대해 일관된 JSON 응답 포맷을 생성합니다.

    Args:
        data (dict | list): 응답에 포함할 데이터 페이로드.
        message (str, optional): 성공 메시지. 기본값은 None.
        code (int, optional): HTTP 상태 코드. 기본값은 200.

    Returns:
        tuple[Response, int]: JSON 응답 객체와 상태 코드의 튜플.
    """
    response_body = {"status": "success", "data": data, "message": message}
    return jsonify(response_body), code


def error_response(message, code=400, payload=None):
    """표준 에러 응답 래퍼.

    실패한 API 요청에 대해 일관된 JSON 응답 포맷을 생성합니다.

    Args:
        message (str): 에러 설명 메시지.
        code (int, optional): HTTP 상태 코드. 기본값은 400.
        payload (dict, optional): 상세 에러 정보나 추가 데이터. 기본값은 None.

    Returns:
        tuple[Response, int]: JSON 응답 객체와 상태 코드의 튜플.
    """
    response_body = {"status": "error", "message": message, "payload": payload}
    return jsonify(response_body), code
