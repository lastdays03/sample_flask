import pytest
from app.exceptions import CoreException, BusinessException, SystemException


def test_core_exception_structure():
    """CoreException 구조 테스트.
    
    메시지와 코드가 예외 객체에 올바르게 저장되는지 확인합니다.
    """
    with pytest.raises(CoreException) as excinfo:
        raise CoreException("Generic Error", code="GENERIC_ERROR")

    assert str(excinfo.value) == "Generic Error"
    assert excinfo.value.message == "Generic Error"
    assert excinfo.value.code == "GENERIC_ERROR"


def test_business_exception():
    """BusinessException 기본값 테스트.
    
    BusinessException 발생 시 기본 에러 코드(BUSINESS_ERROR)가 설정되고,
    CoreException의 인스턴스인지 확인합니다.
    """
    with pytest.raises(BusinessException) as excinfo:
        raise BusinessException("Invalid Input")

    assert excinfo.value.code == "BUSINESS_ERROR"
    assert isinstance(excinfo.value, CoreException)


def test_system_exception():
    """SystemException 기본값 테스트.
    
    SystemException 발생 시 기본 에러 코드(SYSTEM_ERROR)가 설정되고,
    CoreException의 인스턴스인지 확인합니다.
    """
    with pytest.raises(SystemException) as excinfo:
        raise SystemException("DB Down")


    assert excinfo.value.code == "SYSTEM_ERROR"
    assert isinstance(excinfo.value, CoreException)
