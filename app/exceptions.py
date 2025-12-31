class CoreException(Exception):
    """모든 애플리케이션 관련 에러의 기본 예외 클래스입니다.

    Args:
        message (str): 에러 메시지.
        code (str, optional): 에러 코드. 기본값은 "INTERNAL_ERROR".
        payload (dict, optional): 추가 에러 정보. 기본값은 None.
    """

    def __init__(self, message, code="INTERNAL_ERROR", payload=None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.payload = payload


class BusinessException(CoreException):
    """비즈니스 로직 에러 발생 시 사용하는 예외입니다.
    
    사용자에게 노출될 수 있는 논리적 오류를 나타냅니다.
    """

    def __init__(self, message, code="BUSINESS_ERROR", payload=None):
        super().__init__(message, code, payload)


class SystemException(CoreException):
    """시스템 에러 발생 시 사용하는 예외입니다.
    
    인프라 문제나 예상치 못한 시스템 오류를 나타냅니다.
    """

    def __init__(self, message, code="SYSTEM_ERROR", payload=None):
        super().__init__(message, code, payload)

