# main.py
# 요구사항:
# - mission_computer_main.log 전체 출력
# - 예외 처리 (파일 없음, 디코딩 오류 등)
# - 콤마(,) 기준으로 날짜/시간과 메시지를 분리해 List로 변환 및 출력
# - 리스트를 시간 역순(사전식 역순)으로 정렬하여 출력
# - 정렬된 리스트를 Dict로 변환
# - Dict를 mission_computer_main.json(UTF-8, JSON)으로 저장

LOG_PATH = "dataFile/mission_computer_main.log"
JSON_PATH = "dataFile/mission_computer_main.json"

# 1. 파일 읽기
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f: # open으로 파일 열어 만든 객체를 f라는 변수에 저장함
        return f.read()


# 2. 리스트 변환
def to_list(log_text: str):
    lines = log_text.splitlines() # 줄바꿈 기준으로 잘라서 return, list형태로
    records = []
    for line in lines[1:]:  # 첫 줄은 헤더라 스킵
        parts = line.split(",")
        if len(parts) >= 3:
            ts, _, msg = parts
            records.append([ts.strip(), msg.strip()])
    return records


# 3. 리스트 정렬 (시간 역순)
def sort_list(records):
    return sorted(records, key=lambda x: x[0], reverse=True) 
    # lambda: 기준 [0]이니까 첫번쨰 원소를 기준으로 둬라. 복합자료형(리스트)이라서 필요함
    # reverse=True니까 내림차순


# 4. 딕셔너리 변환
def to_dict(records):
    return {ts: msg for ts, msg in records}


# 5. JSON 저장 (직접 문자열 생성)
def save_json(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n")
        items = []
        for ts, msg in data.items():
            ts_safe = ts.replace('"', '\\"')
            msg_safe = msg.replace('"', '\\"')
            items.append(f'  "{ts_safe}": "{msg_safe}"')
        f.write(",\n".join(items))
        f.write("\n}")


def main():
    try:
        # 1. 파일 읽기
        text = read_file(LOG_PATH)
        print("=== [원본 로그 전체 내용] ===")
        print(text.rstrip())

        # 2. 리스트 변환
        records = to_list(text)
        print("\n=== [리스트 [timestamp, message]] ===")
        for rec in records:  # 한 줄씩 출력
            print(rec)

        # 3. 정렬
        records_sorted = sort_list(records)
        print("\n=== [시간 역순 정렬 리스트] ===")
        for rec in records_sorted:  # 한 줄씩 출력
            print(rec)

        # 4. 딕셔너리 변환
        data_dict = to_dict(records_sorted)

        # 5. JSON 저장
        save_json(data_dict, JSON_PATH)
        print(f'\n✅ JSON 저장 완료: "{JSON_PATH}"')

    except FileNotFoundError:
        print(f'❌ 파일을 찾을 수 없습니다: "{LOG_PATH}"')
    except UnicodeDecodeError:
        print(f'❌ 디코딩 오류 발생. 파일 인코딩 확인 필요: "{LOG_PATH}"')
    except Exception as e:
        print(f"❌ 기타 오류: {e}")


if __name__ == "__main__":
    main()
