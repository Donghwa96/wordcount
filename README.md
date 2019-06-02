<h2>구현 의도</h2>

- 멋사 WordCount 강의를 듣는 도중에 자소서의 글자 수 제한이 생각이 났다. 생각이 난 이유는 모르겠지만 WordCount는 단어를 뽑을 수 있어서 자소서를 작성할때 중복되는 단어들을 조심하기 위해 자소서 내용 중 사용 빈도가 높은 1~5위 단어를 보여주고(sorted, slicing) len함수와 replace함수를 이용해 공백포함, 공백제외 글자를 나타낼 수 있는 서비스를 구현하고 싶었다.

<h2>오류 내용</h2>

- 사용빈도가 높은 단어를 보여주고 싶었는데 먼저 정렬을 한 다음 reverse를 하는 게 목적이였는데 자료형이 딕셔너리여서 해당 함수를 이해하는데 애를 먹었다. 찾아보니 간단했다. 그리고 이유는 모르겠는데 장고에 템플릿 css 적용부분에서 빨리 먹히지 않았다. 그래서 안 먹혔다고 생각한 나머지 나중에 해보니 되는 경우가 마지막에 종종 있었다.

<h2>간단한 소감</h2>

- 장고로 많은 삽질을 하다보니 어떤 때는 단순히 MTV 모델을 타자치기 연습용으로 사용했던 적이 있었는데 이번 강의를 통해 많이 정리가 되었다. 지금 까지 5개 정도의 project를 만들었지만 내 스스로 views.py에서 함수를 만들어 render함수를 이해한 적이 이번 처음이다. 이제는 블로그다!

<h2>참고 사이트</h2>

-http://codingdojang.com/scode/634?orderby=&langby=python#answer-filter-area
(sorted와 slicing에 대해서 많은 생각을 가졌음)

<h2>ScreenShots</h2>

![](wordcount1.png)
![](wordcount2.png)
![](wordcount3.png)
![](wordcount4.png)
![](wordcount5.png)