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

  - 'scan_session_id': 개별 스캔 세션 id,

  - 'sub_path': 세부 도메인,

  - 'vulnerability': 취약점'

    > 'SQL Injection', 'XSS', 'Open Redirect', 'Windows Directory Traversal', 'Linux Directory Traversal', 'LFI Check', 'RFI Check', 'RCE Linux Check', 'RCE PHP Check', 'SSTI Check'

  - 'result_string': 스캔 결과 'vulnerable/benign'
  
  - 'with_headers': 참일시 스캔 HTTP 요청/응답 헤더까지 응답에 담아줌
  
  - 'targets_only': 참일시 스캔 세션들만 응답
  
  - 'urls_only': 특정 타겟 하위 url들만 응답

-> 결과 JSON 목록

  # ws://\<주소>:8000/ws/scan/

- 웹소켓 전용

- 연결후 data에 JSON
 
  - 'token': 'Token \<JWT>'

  - 'target': 타겟 서비스 주소,

  - 'url_fuzz': url 상 취약점 스캔 여부 'True/False'

  - 'traversal_check': 'path traversal' 취약점 스캔 여부 'True/False'

  - 'form_fuzz': 페이지 form 취약점 스캔 여부 'True/False'

-> 서브 도메인 목록, 전체 결과 JSON 목록
  



# Todo

  

- WebSocket/ASGI 패치 :white_check_mark:

- 스캔 모듈 추가

- 스캔 요청/응답 헤더 모델 추가 :white_check_mark:

  - 응답 바디 처리

- UnicodeError 대응 개선

- ClientSession 다수 사용 :white_check_mark:

- 크롤링 읍답 속도 향상 :white_check_mark:

---

# /netscan/target/

POST:

- header Authorization 항목에 'Token \<JWT>'

- body에

  - 'username': Token 소유주와 일치해야함 (필수)

  - 'target': 타켓 서비스 주소 (필수, 복수 가능)  
  ex) 'http://testhtml5.vulnweb.com/, http://testphp.vulnweb.com/'  
    'http://domain/' 형식 지켜야됨, ','으로 타겟 구분

  - 'timestamp': 스캔한 날짜 (필수x)  
  ex) 2021-03-19  
-> 결과 JSON 목록

# /netscan/result/

POST:

- header Authorization 항목에 'Token \<JWT>'

- body에

  - 'username': Token 소유주와 일치해야함 (필수)

  - 'scan_session_id' (필수)
  
  -> {"ips": JSON 리스트, "ports": JSON 리스트, "whois": JSON, "robot": JSON}  
  
  netscan 시, whois_flag, robot_flag를 설정하지 않아,  
  
  scan_session_id에 해당하는 whois, robot이 없을 경우 빈 JSON 보내줌  

 # ws://\<주소>:8000/ws/netscan/

- 웹소켓 전용

- 연결후 data에 JSON
 
  - 'token': 'Token \<JWT>'

  - 'target': 타겟 서비스 주소,

  - 'port_range': 스캔할 포트 넘버 (ex. '1-443,65535') 빈 문자열일 시, 0-65535
  
  - 'rate' : 스캔 속도 pps (string으로 보낼 것) 빈 문자열일 시, 100
  
  - 'whois_flag' : true, false
  
  - 'robot_flag' : true, false

-> ip address 목록, port scan, whois, robot 목록

# Network Scan Todo


- 관리자 권한 여부 (runserver를 관리자 권한으로 실행 고려) :white_check_mark:

- Nmap full Scan 시, Nmap 자체의 성능으로 인한 시간 지연 (masscan 도입 고려) :white_check_mark:

- half mode scan, Xmas scan, Null scan 등 다양한 옵션 추가

- whois를 이용한 정보 수집 :white_check_mark

- robots.txt 정보 수집 :white_check_mark
