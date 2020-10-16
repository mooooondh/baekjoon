문자열 압축
==========================
https://programmers.co.kr/learn/courses/30/lessons/60057


<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>데이터 처리 전문가가 되고 싶은 <strong><q>어피치</q></strong>는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.<br>
간단한 예로 <q>aabbaccc</q>의 경우 <q>2a2ba3c</q>(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, <q>abcabcdede</q>와 같은 문자열은 전혀 압축되지 않습니다. <q>어피치</q>는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.</p>

<p>예를 들어, <q>ababcdcdababcdcd</q>의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 <q>2ab2cd2ab2cd</q>로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 <q>2ababcdcd</q>로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.</p>

<p>다른 예로, <q>abcabcdede</q>와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 <q>abcabc2de</q>가 되지만, 3개 단위로 자른다면 <q>2abcdede</q>가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.</p>

<p>압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.</p>

<h3>제한사항</h3>

<ul>
<li>s의 길이는 1 이상 1,000 이하입니다.</li>
<li>s는 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"aabbaccc"</code></td>
<td>7</td>
</tr>
<tr>
<td><code>"ababcdcdababcdcd"</code></td>
<td>9</td>
</tr>
<tr>
<td><code>"abcabcdede"</code></td>
<td>8</td>
</tr>
<tr>
<td><code>"abcabcabcabcdededededede"</code></td>
<td>14</td>
</tr>
<tr>
<td><code>"xababcdcdababcdcd"</code></td>
<td>17</td>
</tr>
</tbody>
      </table>
<h3>입출력 예에 대한 설명</h3>

<p><strong>입출력 예 #1</strong></p>

<p>문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.</p>

<p><strong>입출력 예 #4</strong></p>

<p>문자열을 2개 단위로 자르면 <q>abcabcabcabc6de</q> 가 됩니다.<br>
문자열을 3개 단위로 자르면 <q>4abcdededededede</q> 가 됩니다.<br>
문자열을 4개 단위로 자르면 <q>abcabcabcabc3dede</q> 가 됩니다.<br>
문자열을 6개 단위로 자를 경우 <q>2abcabc2dedede</q>가 되며, 이때의 길이가 14로 가장 짧습니다.</p>

<p><strong>입출력 예 #5</strong></p>

<p>문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.<br>
따라서 주어진 문자열을 x / ababcdcd  /  ababcdcd 로 자르는 것은 불가능 합니다.<br>
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다. </p>

<hr>

<p><u>혼자 풀기가 막막하다면, 풀이 강의를 들어보세요</u> <a href="https://programmers.co.kr/learn/courses/10336?utm_source=programmers&amp;utm_medium=test_course10336&amp;utm_campaign=course_10336" target="_blank" rel="noopener">(클릭)</a></p>
</div>
    </div>
