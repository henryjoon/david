# log_analysis.py

LOG_PATH = "dataFile/mission_computer_main.log"
REPORT_PATH = "Markdown/log_analysis.md"


# 1. 파일 읽기
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# 2. 로그 분석 (사고 원인 추론)
def analyze_log(log_text: str) -> str:
    lines = log_text.splitlines()[1:]  # 첫 줄 헤더 스킵
    report_lines = []

    # 주요 사고 관련 이벤트 탐지
    cause_events = []
    for line in lines:
        parts = line.split(",")
        if len(parts) == 3:
            ts, _, msg = parts
            if "unstable" in msg:
                cause_events.append((ts, msg))
            elif "explosion" in msg:
                cause_events.append((ts, msg))

    # 분석 내용 구성
    report_lines.append("# 사고 원인 분석 보고서\n")
    report_lines.append("## 로그 요약\n")
    report_lines.append("아래는 로그에서 발견된 주요 사고 관련 이벤트입니다:\n")

    for ts, msg in cause_events:
        report_lines.append(f"- **{ts}**: {msg}")

    report_lines.append("\n## 사고 원인 추론\n")
    if len(cause_events) >= 2:
        report_lines.append(
            "로그에 따르면 **산소 탱크 불안정(Oxygen tank unstable)** 상태가 감지된 이후, "
            "**산소 탱크 폭발(Oxygen tank explosion)** 이 발생했습니다.\n"
            "따라서 사고의 직접적인 원인은 **산소 탱크 이상으로 인한 폭발**으로 추론됩니다."
        )
    else:
        report_lines.append(
            "로그 상에 명확한 사고 관련 이벤트가 부족하여 원인을 특정하기 어렵습니다."
        )

    return "\n".join(report_lines)


# 3. 분석 결과를 Markdown 파일로 저장
def save_report(report_text: str, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)


def main():
    try:
        log_text = read_file(LOG_PATH)
        report = analyze_log(log_text)
        save_report(report, REPORT_PATH)
        print(f"✅ 사고 분석 보고서 저장 완료: {REPORT_PATH}")
    except FileNotFoundError:
        print(f"❌ 로그 파일을 찾을 수 없습니다: {LOG_PATH}")
    except UnicodeDecodeError:
        print(f"❌ 디코딩 오류 발생. 파일 인코딩 확인 필요: {LOG_PATH}")
    except Exception as e:
        print(f"❌ 알 수 없는 오류: {e}")


if __name__ == "__main__":
    main()
