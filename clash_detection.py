import sys
import json
import logging
import ifcclash 
from ifcclash import ClashSettings, Clasher

## python -m ifcclash input.json -o output.json

# 충돌 감지 설정 초기화
settings = ClashSettings()
settings.output = "output.json"  # 결과 파일 경로
settings.logger = logging.getLogger("Clash")
settings.logger.setLevel(logging.DEBUG)

# 로깅 핸들러 추가
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
settings.logger.addHandler(handler)

# Clasher 객체 생성
ifc_clasher = Clasher(settings)

# 충돌 세트 로드
input_file = "input.json"  # JSON 파일 경로
with open(input_file, "r") as clash_sets_file:
    ifc_clasher.clash_sets = json.loads(clash_sets_file.read())

# 충돌 감지 실행
ifc_clasher.clash()

# 결과를 JSON 파일로 내보내기
ifc_clasher.export()
