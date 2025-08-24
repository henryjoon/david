## 반달곰 커피 홈페이지 (H2 헤더)
참조링크: [https://반달곰커피] [https://반달곰커피]
문구: 오디오 출력 소스코드
코드 블록 (Python):
```python
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
```
<img src="david.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>
