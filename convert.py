import os
from fontTools.ttLib import TTFont

# 원본 파일명과 변환될 파일명 매핑
files = {
    "웰컴체OTF Regular.otf": "WelcomeOTF-Regular.woff2",
    "웰컴체OTF Bold.otf":    "WelcomeOTF-Bold.woff2"
}

for input_name, output_name in files.items():
    if os.path.exists(input_name):
        try:
            font = TTFont(input_name)
            font.flavor = 'woff2'
            font.save(output_name)
            print(f"변환 성공: {output_name}")
        except Exception as e:
            print(f"변환 실패 ({input_name}): {e}")
    else:
        print(f"파일 없음: {input_name}")