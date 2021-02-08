# /login/
GET:
- body에 'username', 'password' -> 회원생성
POST:
- body에 'username', 'password' -> JWT 반환(유효 30분)

# /scan/

GET: 
- header Authorization 항목에 'Token \<JWT>'
- body에
	- 'username',
	- 'target': 타켓 서비스 주소, 
	- 'sub_path': 세부 도메인,
	- 'vulnerability': 취약점'
		> 'SQL Injection', 'XSS', 'Open Redirect', 'Windows Directory Traversal', 'Linux Directory Traversal', LFI Check', 'RFI Check', 'RCE Linux Check', 'SSTI Check'
	- 'result_string': 스캔 결과 'vulnerable/benign'

-> 결과 JSON 목록

POST:
- header Authorization 항목에 'Token \<JWT>'
- body에
	- 'target': 타겟 서비스 주소,
	- 'fuzz': 취약점 스캔 여부 'True/False'

-> 스캔 결과 전체 JSON 목록 (응답에 시간 소요, Websocket 사용 필요)
 

# Todo

- WebSocket/ASGI 패치
- 스캔 모듈 추가
- 스캔 요청/응답 헤더 모델 추가