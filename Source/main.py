# main.py
import csv
import json

def main():
    log_file = "dataFile/mission_computer_main.log"
    json_file = "dataFile/mission_computer_main.json"

    # 로그 파일 읽기 + 전체 출력 (예외 처리)
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[오류] 로그 파일 '{log_file}'을 찾을 수 없습니다.")
        return
    except UnicodeDecodeError:
        print(f"[오류] 로그 파일 '{log_file}' 디코딩 실패 (UTF-8 아님)")
        return
    except Exception:
        print(f"[오류] 로그 파일 '{log_file}'을 읽는 중 예기치 못한 문제가 발생했습니다.")
        return 

    print("====== [원본 로그 파일 전체 내용] ======")
    print(content.strip())
    print("=====================================\n")

    # log 파일 내용 토대로 [timestamp, message] 리스트 변환
    entries = []
    with open(log_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = row.get("timestamp", "").strip() # 시간
            msg = row.get("message", "").strip() # 메시지
            entries.append([ts, msg])

    print("====== [리스트 객체 출력: [날짜/시간, 메시지]] ======")
    for e in entries:
        print(e)
    print("===============================================\n")

    # 시간 역순(최신→과거) 사전식 정렬
    # 현재 로그 포맷(YYYY-MM-DD HH:MM:SS)은 문자열 역순 정렬과 시간 역순이 일치함
    sorted_entries = sorted(entries, key=lambda x: x[0], reverse=True)

    print("====== [시간 역순 정렬 리스트 출력] ======")
    for e in sorted_entries:
        print(e)
    print("=====================================\n")

    # Dict 변환: {timestamp: message or [messages...]}
    dict_obj = {}
    for ts, msg in sorted_entries:
        if ts in dict_obj:
            if isinstance(dict_obj[ts], list):
                dict_obj[ts].append(msg)
            else:
                dict_obj[ts] = [dict_obj[ts], msg]
        else:
            dict_obj[ts] = msg

    # JSON 저장 (UTF-8, pretty)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dict_obj, f, ensure_ascii=False, indent=2)

    print(f"완료: 변환된 Dict 객체를 '{json_file}'에 저장했습니다.")

if __name__ == "__main__":
    main()