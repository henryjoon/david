CSV_PATH = "mars_base/Mars_Base_Inventory_List.csv"
OUT_PATH = "mars_base/Mars_Base_Inventory_danger.csv"

# 1. 파일 읽기
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f: # open으로 파일 열어 만든 객체를 f라는 변수에 저장함
        return f.read()


# 2. 리스트 변환
def to_list(csv_text: str):
    lines = csv_text.splitlines() # 줄바꿈 기준으로 잘라서 return, list형태로
    records = []
    for line in lines[1:]:  # 첫 줄은 헤더라 스킵
        parts = line.split(",")
        if len(parts) >= 5:
            subs, wgt, g, stn, Flam = parts
            records.append([subs.strip(), wgt.strip(), g.strip(), stn.strip(), Flam.strip()])
    return records


# 3. 리스트 정렬 (시간 역순)
def sort_list(records):
    return sorted(records, key=lambda x: x[4], reverse=True) 
    # lambda: 기준 [0]이니까 첫번쨰 원소를 기준으로 둬라. 복합자료형(리스트)이라서 필요함
    # reverse=True니까 내림차순

# 6. 인화성 지수 0.7이상 필터링
def filtering_Flam(lst):
    filtered_lst = []
    for val in lst:
        if float(val[4]) >= 0.7:
            filtered_lst.append(val)
    return filtered_lst
        

# 5. csv 저장 (직접 문자열 생성)
def save_file(data: list, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write("Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability\n")
        for val in data:
            for x in val:
                f.write(x)
                f.write(",")
            f.write("\n")


def main():
    try:
        # 1. 파일 읽기
        text = read_file(CSV_PATH)
        print("=== [원본 csv 파일 전체 내용] ===")
        print(text.rstrip())

        # 2. 리스트 변환
        records = to_list(text)
        print("\n=== [리스트] ===")
        for rec in records:  # 한 줄씩 출력
            print(rec)

        # 3. 정렬
        records_sorted = sort_list(records)
        print("\n=== [인화성 지수 내림차순 정렬 리스트] ===")
        for rec in records_sorted:  # 한 줄씩 출력
            print(rec)
            
        # 4. 필터링
        record_filtered = filtering_Flam(records_sorted)
        print("\n=== [인화성 0.7 이상 리스트] ===")
        for rec_fil in record_filtered:
            print(rec_fil)

        # 5. csv 저장
        save_file(record_filtered, OUT_PATH)
        print(f'\n✅ CSV 저장 완료: "{OUT_PATH}"')

    except FileNotFoundError:
        print(f'❌ 파일을 찾을 수 없습니다: "{CSV_PATH}"')
    except UnicodeDecodeError:
        print(f'❌ 디코딩 오류 발생. 파일 인코딩 확인 필요: "{CSV_PATH}"')
    except Exception as e:
        print(f"❌ 기타 오류: {e}")


if __name__ == "__main__":
    main()
