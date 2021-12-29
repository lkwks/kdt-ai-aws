### AWS EC2를 활용하여 이 코드를 배포하는 법

1. EC2에서 딥러닝을 제공하는 AMI 인스턴스를 새로 만든다.

- 만들 때 포트번호 5000번이고 모든 호스트의 접속을 허용하는(0.0.0.0) TCP를 추가해야 함.


2. 터미널로 인스턴스에 접속 후, 가상환경 실행 - 깃허브 클론 - 라이브러리 설치 - 서버 실행 명령어를 차례대로 입력한다.

```
conda activate pytorch_p37
git clone https://github.com/lkwks/kdt-ai-aws
cd kdt-ai-aws
pip install -r requirements.txt
python app.py
```

- requirements.txt 설치할 때 transformers, scikit-learn이 설치가 안될 수 있음. 이 경우 conda update 명령어를 입력해 업데이트를 해야.

3. 다음과 같은 형식의 .json 파일을 /predict URI에 POST method로 서버에 전송한다. (HTTP URI: /predict)

```json
{"text": ["...", "..."],
 "use_fast": false}
```
