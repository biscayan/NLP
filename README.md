# 포터 스테머 (Porter's stemmer)
Martin F. Porter의 stemming 알고리즘을 이용하여 영어의 어간 추출

<br/>

## 프로젝트 기간
- 대학원 2학기 전산언어학2 수업의 개인과제로 프로젝트를 진행하였습니다.
- 프로젝트 기간 : 2019.11.21 ~ 2019.12.05

<br/>

## 기술 스택
- Python 3.7.3

<br/>

## 스테밍 (Stemming)
- 스테밍은 영어단어에서 접사(affix)를 제거하고 핵심적인 의미를 가지는 어간(stem)을 추출하는 작업입니다.  
- 이번 프로젝트에서는 1980년도에 발표된 Martin F. Porter의 [An algorithm for suffix stripping](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.848.7219&rep=rep1&type=pdf)을 참고하여 스테머를 만들었습니다.  
- 해당 스테머는 스테밍 알고리즘의 1~4단계를 차례대로 적용했으며, 적용된 세부 규칙들은 아래에서 확인할 수 있습니다.  

    <details>
    <summary>1단계 규칙 확인</summary>
    <div markdown="1">

        sses -> ss 
        ies -> i 
        ss -> ss 
        s -> ''
        eed -> e

    </div>
    </details>

    <details>
    <summary>2단계 규칙 확인</summary>
    <div markdown="1">
        
        ational -> ate    
        tional -> tion
        enci -> ence
        anci -> ance
        izer -> ize
        abli -> able
        alli -> al            
        entli -> ent
        eli -> e
        ousli -> ous
        ization -> ize
        ation -> ate
        ator -> ate
        alism -> al
        iveness -> ive
        fulness -> ful
        ousness -> ous
        aliti -> al
        iviti -> ive
        biliti -> ble

    </div>
    </details>

    <details>
    <summary>3단계 규칙 확인</summary>
    <div markdown="1">

            icate -> ic
            ative -> ''
            alize -> al
            ical -> ic
            ful -> ''
            ness -> ''

    </div>
    </details>

    <details>
    <summary>4단계 규칙 확인</summary>
    <div markdown="1">

            al -> ''
            ance -> ''
            ence -> ''
            er -> ''
            ic -> ''
            able -> ''
            ible -> ''
            ant -> ''
            ement -> ''
            ment -> ''
            ent -> ''
            ion -> ''
            ou -> ''
            ism -> ''
            ate -> ''
            iti -> ''
            ous -> ''
            ive -> ''
            ize -> ''

    </div>
    </details>

<br/>

## 스테밍 결과 예시
- 1단계 규칙 적용  

    |단어|스테밍 적용|
    |:---:|:---:|
    |cats|cat| 
    |studies|studi|
    |cars|car|

<br/>

- 2단계 규칙 적용  

    |단어|스테밍 적용|
    |:---:|:---:|
    |relational|relate| 
    |organization|organ|
    |recognizer|recogn|

    <br/>

    cf) 대부분의 단어들이 2단계 규칙 적용 후 다음 단계의 규칙이 적용되어서 2단계 규칙에서 끝나는 단어들은 찾아보기가 힘듭니다.  

<br/>

- 3단계 규칙 적용  

    |단어|스테밍 적용|
    |:---:|:---:|
    |formalize|formal| 
    |crowdedness|crowded|
    |powerful|power|

<br/>

- 4단계 규칙 적용  

    |단어|스테밍 적용|
    |:---:|:---:|
    |activate|activ| 
    |encouragement|encourag|
    |effectiveness|effect|

    <br/>

    cf) effectiveness->effect은 effectiveness->effective 2단계 규칙을 먼저 적용하고, effective->effect 4단계 규칙을 적용한 결과입니다.  

<br/>

## 프로젝트의 한계점 및 후속 프로젝트
- 현재 프로젝트의 스테머는 스테밍 알고리즘의 1~5단계 중에서 4단계까지만 적용하였고 몇몇 규칙들은 빠져있습니다. 따라서 스테밍을 정확하게 하기 위해서 더 많은 규칙을 추가하여 보완할 예정입니다.  
- 스테밍은 형태소 분석에서 많이 사용되지는 하지만, 어간의 일부 철자가 훼손될 수 있으며 사전에 없는 어간을 추출하기도 한다는 단점이 있습니다.  
- 반면에, 레마타이제이션(Lemmatization)은 어간의 철자를 온전히 보존하고 사전에 있는 어간만을 추출한다는 점에서 스테밍보다 뛰어납니다. 따라서 후속 프로젝트에서는 실생활에서 더 유용하게 적용될 수 있는 레마타이제이션을 구현을 해 볼 것입니다.