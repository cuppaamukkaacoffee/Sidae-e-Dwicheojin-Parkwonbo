# /auth/login/

POST:

- body에 'username', 'password' -> JWT 반환(유효 30분)

  
# /auth/register/

POST:

- body에 'username', 'password' -> 회원생성



# /scan/query/

  

POST:

- header Authorization 항목에 'Token \<JWT>'

- body에

  - 'username' (필수, Token 소유주와 일치해야함),

  - 'target': 타켓 서비스 주소,

  - 'sub_path': 세부 도메인,

  - 'vulnerability': 취약점'

    > 'SQL Injection', 'XSS', 'Open Redirect', 'Windows Directory Traversal', 'Linux Directory Traversal', LFI Check', 'RFI Check', 'RCE Linux Check', 'SSTI Check'

  - 'result_string': 스캔 결과 'vulnerable/benign'

  - 'with_headers': 참일 시 헤더까지 포함한 결과 응답

  - 'targets_only': 유저가 스캔한 타겟들 일람(username 필수)

  - 'urls_only': 타겟 하위 url들 일람(username, target 필수)

-> 결과 JSON 목록

  # ws://\<주소>:8000/ws/scan/

- 웹소켓 전용

- 연결후 data에 JSON
 
  - 'token': 'Token \<JWT>'

  - 'target': 타겟 서비스 주소,

  - 'fuzz': 취약점 스캔 여부 'True/False'

-> 서브 도메인 목록, 전체 결과 JSON 목록
  

# Todo

  

- WebSocket/ASGI 패치 :white_check_mark:

- 스캔 모듈 추가

- 스캔 요청/응답 헤더 모델 추가 :white_check_mark:

  - 응답 바디 처리

- UnicodeError 대응 개선

- ClientSession 다수 사용 :white_check_mark:

- 크롤링 읍답 속도 향상 :white_check_mark:
