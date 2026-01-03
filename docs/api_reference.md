# API Reference

## Authentication API
사용자 인증 및 세션 관리를 위한 API입니다.

### POST /auth/login
사용자 로그인을 처리하고 세션을 생성합니다.

**Request (Form Data):**
- `email` (str, required): 사용자 이메일
- `password` (str, required): 비밀번호
- `remember_me` (bool, optional): 로그인 유지 여부

**Response:**
- **Success (302)**: 메인 페이지(`/`) 또는 이전 페이지로 리다이렉트.
- **Error (200)**: 로그인 페이지를 다시 렌더링하며 에러 메시지 표시.

---

### POST /auth/register
신규 사용자를 등록합니다.

**Request (Form Data):**
- `email` (str, required): 사용자 이메일 (Unique)
- `username` (str, required): 사용자 이름 (Unique)
- `password` (str, required): 비밀번호
- `confirm_password` (str, required): 비밀번호 확인

**Response:**
- **Success (302)**: 로그인 페이지(`/auth/login`)로 리다이렉트.
- **Error (200)**: 회원가입 페이지를 다시 렌더링하며 에러 메시지 표시.

---

### GET /auth/logout
현재 세션을 종료하고 로그아웃합니다.

**Response:**
- **Success (302)**: 메인 페이지(`/`)로 리다이렉트.

---

## Data API
대시보드 차트 및 테이블 렌더링을 위한 데이터 API입니다.
현재는 Mock Data를 반환합니다.

### POST /district
자치구별 변동률 데이터를 반환합니다 (Bar Chart용).

**Request:**
- `Content-Type: application/json` (Optional params for filtering)

**Response (200 OK):**
```json
{
  "status": "success",
  "data": [
    {"name": "Gangnam", "value": 12.5},
    {"name": "Seocho", "value": 10.2},
    ...
  ]
}
```

### POST /building
건물 용도별 평균 가격 데이터를 반환합니다 (Area Chart용).

**Request:**
- `Content-Type: application/json`

**Response (200 OK):**
```json
{
  "status": "success",
  "data": [
    {"date": "2023-01", "apartment": 50000, "commercial": 30000},
    {"date": "2023-02", "apartment": 51000, "commercial": 29000},
    ...
  ]
}
```

### POST /predict/location
위치별 예측 상세 데이터를 반환합니다 (Table용).

**Request:**
- `Content-Type: application/json`

**Response (200 OK):**
```json
{
  "status": "success",
  "data": [
    {"location": "Yeoksam-dong", "current_price": 100, "predicted_price": 110, "change": "+10%"},
    ...
  ]
}
```
