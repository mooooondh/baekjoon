<div class="row">
		<div class="col-md-12">
			<div id="result_log"></div>
		</div>
		<div class="col-md-12">
							<ul class="nav nav-pills no-print problem-menu"><li class="active">
	<a href="/problem/10844">10844번</a>
</li><li><a href="/submit/10844">제출</a></li><li><a href="/problem/status/10844">맞은 사람</a></li><li><a href="/short/status/10844">숏코딩</a></li><li><a href="/problem/history/10844">재채점</a></li><li><a href="/status?from_problem=1&amp;problem_id=10844">채점 현황</a></li><li class="dropdown"><a class="dropdown-toggle" id="drop5" role="button" data-toggle="dropdown" href="#">강의<b class="caret"></b></a><ul id="menu2" class="dropdown-menu" role="menu" aria-labelledby="drop5"><li><a tabindex="-1" href="https://code.plus/course/32">SW 역량 테스트 준비 - 기초</a></li><li><a tabindex="-1" href="https://code.plus/course/41">알고리즘 기초 1/2</a></li><li class="divider"></li><li><a tabindex="-1" href="#" class="lecture-request">강의 요청하기</a></li></ul></li></ul>
					</div>
		<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">10844번 - </span><span id="problem_title">쉬운 계단 수</span>
				<span class="label-purple problem-label">분류</span>				<div class="btn-group pull-right problem-button">
														</div>
				</h1>
									
							</div>
		</div>
		<div class="col-md-12">
			<div class="table-responsive">
				<table class="table" id="problem-info">
				<thead>
				<tr>
									<th style="width:16%;">시간 제한</th>
					<th style="width:16%;">메모리 제한</th>
					<th style="width:17%;">제출</th>
					<th style="width:17%;">정답</th>
					<th style="width:17%;">맞은 사람</th>
					<th style="width:17%;">정답 비율</th>
								</tr>
				</thead>
				<tbody>
				<tr>
				<td>1 초</td>
				<td>256 MB</td>
									<td>72231</td>
					<td>21905</td>
					<td>15728</td>
					<td>28.419%</td>
								</tr>
				</tbody>
				</table>
			</div>
		</div>
		<div id="problem-body">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>45656이란 수를 보자.</p>

<p>이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.</p>

<p>세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.</p>

<p>N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)</p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.</p>

					</div>
					</section>
				</div>
						<div class="col-md-12">
			<section id="limit" style="display:none;" class="problem-section">
			<div class="headline">
			<h2>제한</h2>
			</div>
			<div id="problem_limit" class="problem-text">
						</div>
			</section>
			</div>
																	<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput1">
						<div class="headline">
						<h2>예제 입력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-1">1
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput1">
						<div class="headline">
						<h2>예제 출력 1
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-1">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-1">9
</pre>
						</section>
					</div>
									</div>
				</div>
								<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput2">
						<div class="headline">
						<h2>예제 입력 2
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-2">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-2">2
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput2">
						<div class="headline">
						<h2>예제 출력 2
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-2">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-2">17
</pre>
						</section>
					</div>
									</div>
				</div>
										<div class="col-md-12">
				<section id="hint" style="display: none;" class="problem-section">
				<div class="headline">
				<h2>힌트</h2>
				</div>
				<div id="problem_hint" class="problem-text">
				
				</div>
				</section>
			</div>
								</div>
									<div class="col-md-12"><section id="source"><div class="headline"><h2>출처</h2></div><ul><li>문제를 만든 사람:&nbsp;<a href="/user/baekjoon">baekjoon</a></li></ul></section></div>
																														</div>