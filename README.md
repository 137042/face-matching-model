# face-matching-model
- 구글에서 특정 동물 사진을 수집 
- 유저가 업로드한 사진과 가장 흡사한 동물 예측
- teaching machine을 활용
- streamlit을 활용한 웹페이지
- https://share.streamlit.io/gimseonjin/streamlit_kumoh/main/main.py
## model test

<img width="960" alt="tm_test" src="https://user-images.githubusercontent.com/75469383/154939850-30bfa402-09aa-43d3-9652-8f1135106245.png">

## ngrok test

<img width="960" alt="ngrok_test" src="https://user-images.githubusercontent.com/75469383/154940036-f052ac8f-c4a7-41b1-86a2-743ba1a7acaf.png">




<div align="center">
    <br/>
    <h1>Application</h1>
    <p>Official social application developed by Kumoh42.com Operation team.</p><br/>
    <img src="https://forthebadge.com/images/badges/built-with-love.svg">
    <img src="https://forthebadge.com/images/badges/fo-real.svg">
    <br/>
    <br/>
    master<br/>
    <img src="https://semaphoreci.com/api/v1/foryou8033j/kumohtime_v2/branches/master/badge.svg">
    <br/>
    <br/>
</div>

#### Development
<pre class="highlight highlight-html">
Based on <a href="">Flutter</a> SDK with Dart Language
</pre>

#### Requirement
```
Flutter SDK : >=2.1.0 <3.0.0
Android Dev : Android Studio or Visual Studio Code
iOS Dev : Android Studio or XCode or Visual Studio Code
```

#### Build Setup
<pre class="highlight highlight-html">
ENG : <a href="https://flutter.dev/docs/get-started/install">https://flutter.dev/docs/get-started/install</a>
KOR : <a href="https://flutter-ko.dev/docs/get-started/install">https://flutter-ko.dev/docs/get-started/install</a>
</pre>

#### Branch Management
```bash

#Branch naming rules
master
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