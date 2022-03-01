<div align="center">
    <br/>
    <h1>face matching model</h1>
    <div>유저가 업로드한 사진과 가장 흡사한 동물을 찾아주는 모델</div>
    <div>구글에서 특정 동물 사진을 수집하여 teachable machine 학습</div>
    <div>streamlit을 활용하여 웹페이지 구성</div>
</div>
</br>
</br>
<img width="960" alt="ngrok_test" src="https://user-images.githubusercontent.com/75469383/154940036-f052ac8f-c4a7-41b1-86a2-743ba1a7acaf.png">
<hr>
</br>

#### Development
<pre class="highlight highlight-html">
Based on <a href="">Python</a> with Google Teachable Machine
</pre>

#### Requirement
```
Python : 3.10.1
- numpy : 1.22.2
- keras : 2.8.0
- Pillow : 9.0.1
- streamlit : 1.5.1
- tensorflow : 2.8.0
```
#### How to run
<pre class="highlight highlight-html">
After requirement meeted...
git clone https://github.com/137042/face-matching-model.git
streamlit run main.py

or... just try this!
<a href="https://share.streamlit.io/gimseonjin/streamlit_kumoh/main/main.py">https://share.streamlit.io/gimseonjin/streamlit_kumoh/main/main.py</a>
</pre>

#### Branch Management
```bash

#Branch naming rules
main
항상 보호되는 안정된 브랜치

release/1.2.4
새 버전 준비를 위한 개발 브랜치

bugfix/#42
hotfix/#42
이슈 해결을 위한 브랜치, 이슈 넘버를 기입하여 구분

feature/#notification_list
remove/#weather_header_widget
기능 추가/제거를 위한 브랜치, 기능명을 기입하여 구분

#Contribute method
1. Master 브랜치는 항상 안정된 빌드이자 사용자에게 서비스중인 빌드
2. 프로젝트 관리자가 새 버전 준비시에 release 브랜치 분기
3. 개발자는 이슈, 기능에 따라 release 브랜치에서 분기하여 작업 후 release 브랜치에 Pull request
4. 버전 개발 종료시 관리자는 release 브랜치를 master 브랜치에 병합

```
