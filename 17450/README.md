<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">17450번 - </span><span id="problem_title">과자 사기</span>
				<span class="label-success problem-label"></span><span class="label-primary problem-label"></span><span class="label-purple problem-label"></span>				<div class="btn-group pull-right problem-button">
																										<button class="btn btn-default" type="button" id="favorite_button" data-favorite="0"><span class="glyphicon glyphicon-star-empty" id="favorite_image"></span></button>
																																						</div>
				</h1>
			</div>
		</div>
<div id="problem-body">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>남서네 집 앞 편의점에는 각각 <code>S</code>, <code>N</code>, <code>U</code>의 이름이 붙은 총 3가지의 과자를 판다. 진열대에는 한 봉지당 가격과 무게가 안내되어 있다. 같은 종류의 과자끼리는 봉지의 무게가 똑같다.</p>
<p>남서는 오늘 과자를 10봉지 사려고 한다. 편의점의 단골인 남서는 할인 쿠폰 하나를 가지고 있는데, 총 구매 금액이 5,000원 이상일 때 500원을 깎아 주는 쿠폰이다. 구매 금액이 5,000원 미만인 경우에는 할인 쿠폰을 쓸 수 없다. 또한 할인을 여러 번 적용할 수는 없다.</p>
<p>남서는 과자를 고를 때 <b>가성비</b>를 중요하게 생각한다. 남서가 생각하는 가성비란, 총 무게를 총 금액으로 나눈 값이다. 남서는 빨리 과자가 먹고 싶기 때문에, 한 종류의 과자만을 10봉지 골라 사 가려고 한다. 또, 다른 물건은 구매하지 않을 생각이다.</p>
<p><b>가성비</b>를 다시 한 번 수학적으로 표현하면 다음과 같다.</p>
<p style="text-align: center;">가성비 = <span style="display: inline-block; position: relative; vertical-align: middle; letter-spacing: 0.001em; text-align: center;"><span style="display: block; padding: 0.1em;">과자 10봉지의 무게의 합</span> <span style="display: none; padding: 0.1em;">/</span> <span style="display: block; padding: 0.1em; border-top: thin solid black;">쿠폰 사용을 고려했을 때 과자 10봉지를 사는 데 필요한 돈</span></span></p>
<p>진열대를 들여다 보던 남서는 신기하게도 세 과자의 가성비가 모두 서로 다르다는 사실을 깨달았다.</p>
<p>남서는 어떤 과자를 사게 될까?</p>
				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>입력은 총 3개의 줄로 이루어지며, 각 줄에는 <code>S</code>, <code>N</code>, <code>U</code>의 순서대로 한 봉지의 가격과 무게가 띄어쓰기를 사이에 두고 주어진다.</p>
<p>모든 입력값은 1&nbsp;이상 1,000&nbsp;이하의 정수이다.</p>
<p>세 종류의 과자의 가성비가 서로 다름이 보장된다.</p>
					</div>
					</section>
				</div>
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫 번째 줄에 가장 가성비가 높은 과자의 이름(<code>S</code> 또는 <code>N</code> 또는 <code>U</code>)을 출력한다.</p>
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
						<pre class="sampledata" id="sample-input-1">8 5
6 6
7 5
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
						<pre class="sampledata" id="sample-output-1">N
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
