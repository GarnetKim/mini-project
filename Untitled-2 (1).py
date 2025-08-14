import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
# QLabel: 문제 표시
# QLineEdit: 사용자 입력
# QPushButton + Signal & Slot: 클릭 시 답 체크
# QMessageBox: 정답/오답 알림
from datetime import datetime

# 문제 리스트
problems = [
    {"question": "세상에서 가장 빠른 닭은?", "answer": "후다닥"},
    {"question": "병아리가 가장 잘 먹는 약은?", "answer": "삐약"},
    {"question": "왕이 넘어지면?", "answer": "킹콩"},
    {"question": "왕이 외출할 때 타는 차?", "answer": "킹카"},
    {"question": "7 * 8 = ?", "answer": "56"} 
    {"question":"물(H₂O)의 끓는점은 1기압에서 몇 도인가?","choices":["90℃","95℃","100℃","110℃"],"answer_index":2,"explanation":"표준기압에서 물은 100℃에서 끓습니다."},
    {"question":"지구가 태양을 한 바퀴 도는 데 걸리는 시간은?","choices":["약 24시간","약 7일","약 365일","약 12개월"],"answer_index":2,"explanation":"평균 약 365.24일입니다."},
    {"question":"우리 몸에서 가장 큰 기관(organ)은?","choices":["간","폐","심장","피부"],"answer_index":3,"explanation":"피부가 인체 최대 기관입니다."},
    {"question":"식물이 광합성에 필요한 기체는?","choices":["산소","질소","헬륨","이산화탄소"],"answer_index":3,"explanation":"이산화탄소와 물로 포도당과 산소를 만듭니다."},
    {"question":"삼각형의 내각의 합은?","choices":["90°","180°","270°","360°"],"answer_index":1,"explanation":"삼각형의 내각의 합은 항상 180°입니다."},
    {"question":"1바이트(Byte)는 몇 비트(bit)?","choices":["4","8","16","32"],"answer_index":1,"explanation":"1바이트=8비트입니다."},
    {"question":"HTTP는 어떤 계층의 프로토콜일까?","choices":["물리","데이터링크","네트워크","애플리케이션"],"answer_index":3,"explanation":"웹 통신의 애플리케이션 계층 프로토콜입니다."},
    {"question":"파이썬에서 리스트를 만드는 기호는?","choices":["()","{}","[]","<>"],"answer_index":2,"explanation":"대괄호 []가 리스트 리터럴입니다."},
    {"question":"대한민국의 수도는?","choices":["부산","인천","서울","대전"],"answer_index":2,"explanation":"대한민국의 수도는 서울입니다."},
    {"question":"한글을 창제한 왕은?","choices":["태조","세조","세종","성종"],"answer_index":2,"explanation":"세종대왕이 훈민정음을 창제했습니다."},
    {"question":"태양은 어떤 천체로 분류될까?","choices":["행성","위성","소행성","항성"],"answer_index":3,"explanation":"태양은 스스로 빛을 내는 항성입니다."},
    {"question":"대기 중 가장 많은 기체는?","choices":["산소","아르곤","이산화탄소","질소"],"answer_index":3,"explanation":"지구 대기의 약 78%는 질소입니다."},
    {"question":"원주율 π에 가장 가까운 값은?","choices":["2.17","3.14","3.41","3.2"],"answer_index":1,"explanation":"보통 3.14로 근사합니다."},
    {"question":"전기 회로에서 전구들을 직렬로 연결하면?","choices":["모든 전구에 같은 전압, 전류는 분배","같은 전류가 흐르고 전압은 분배됨","전압과 전류 모두 동일","전부 밝기가 동일하지 않음"],"answer_index":1,"explanation":"직렬에서는 전류가 동일하고 전압이 분배됩니다."},
    {"question":"SSD에 대한 설명으로 옳은 것은?","choices":["자기디스크 사용","반도체 메모리 사용","테이프 사용","광디스크 사용"],"answer_index":1,"explanation":"SSD는 반도체 플래시 메모리를 사용합니다."},
    {"question":"빛의 속도(진공)는 대략?","choices":["3×10^6 m/s","3×10^7 m/s","3×10^8 m/s","3×10^9 m/s"],"answer_index":2,"explanation":"약 3×10^8 m/s입니다."},
    {"question":"계절이 생기는 주된 이유는?","choices":["태양의 크기 변화","지구와 태양 거리 변화","태양의 자전","지구 자전축의 기울기"],"answer_index":3,"explanation":"자전축 약 23.5° 기울기 때문에 계절이 생깁니다."},
    {"question":"컴퓨터에서 키보드는 어떤 장치?","choices":["출력","보조기억","입력","연산"],"answer_index":2,"explanation":"키보드는 대표적인 입력 장치입니다."},
    {"question":"‘안돼/안 돼’ 중 명령·금지 의미로 맞는 것은?","choices":["안 돼","안돼"],"answer_index":0,"explanation":"‘안(부사)+돼(되다의 활용)’는 띄어 씁니다."},
    {"question":"우리 은하의 영어 명칭은?","choices":["Andromeda","Milky Way","Triangulum","Whirlpool"],"answer_index":1,"explanation":"우리 은하는 Milky Way Galaxy라고 합니다."}
]  
]

score = 0
current_index = 0

def check_answer():
    global score, current_index
    user_answer = answer_input.text().strip()
    
    if user_answer == problems[current_index]["answer"]:
        QMessageBox.information(window, "결과", "정답! 🎉")
        score += 1
    else:
        QMessageBox.warning(window, "결과", f"틀렸습니다 😢 정답: {problems[current_index]['answer']}")
    
    current_index += 1
    if current_index < len(problems):
        problem_label.setText(problems[current_index]["question"])
        answer_input.clear()
    else:
        QMessageBox.information(window, "퀴즈 종료", f"퀴즈가 끝났습니다! 점수: {score}/{len(problems)}")
        save_score()  # 점수 파일 저장
        window.close()

def save_score():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 날짜와 시간
    with open("scores.txt", "a") as f:
        f.write(f"[{now}] 점수: {score}/{len(problems)}\n")
        
# 앱과 최상위 창 만들기
app = QApplication(sys.argv) # PyQt 앱 엔진(이벤트 루프)을 한 번만 만드는 줄
window = QWidget() # 최상위 창
window.setWindowTitle("퀴즈 프로그램")
window.setGeometry(300, 300, 400, 200) # x, y, 가로, 세로

# 위젯(라벨/입력/버튼) 배치
problem_label = QLabel(problems[current_index]["question"], window) # 텍스트 표시 위젯
problem_label.move(20, 20) # 창 내부 좌표(왼쪽 위 모서리)

answer_input = QLineEdit(window) # 한 줄 입력
answer_input.move(20, 60) # 좌표 지정
answer_input.resize(200, 30) # 크기를 직접 지정

submit_button = QPushButton("제출", window) # 클릭 가능한 버튼
submit_button.move(240, 60)
submit_button.clicked.connect(check_answer) # 시그널-슬롯 연결: 버튼 클릭

# 화면 표시 + 이벤트 루프
window.show() # 창을 화면에 나타내는 호출
sys.exit(app.exec_()) # 종료








