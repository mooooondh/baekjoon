<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">2839번 - </span><span id="problem_title">설탕 배달</span>
				<span class="label-success problem-label"></span><span class="label-primary problem-label"></span><span class="label-default problem-label"></span><span class="label-purple problem-label"></span>				
		</div>
<div id="problem-body">
			<div class="col-md-12">
				<section id="description" class="problem-section">
				<div class="headline">
				<h2>문제</h2>
				</div>
				<div id="problem_description" class="problem-text">
				<p>상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.</p>
<p>상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.</p>
<p>상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.</p>
				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)</p>
					</div>
					</section>
				</div>
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.</p>
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
						<pre class="sampledata" id="sample-input-1">18
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
						<pre class="sampledata" id="sample-output-1">4
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
						<pre class="sampledata" id="sample-input-2">4
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
						<pre class="sampledata" id="sample-output-2">-1
</pre>
						</section>
					</div>
									</div>
				</div>
								<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput3">
						<div class="headline">
						<h2>예제 입력 3
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-3">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-3">6
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput3">
						<div class="headline">
						<h2>예제 출력 3
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-3">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-3">2
</pre>
						</section>
					</div>
									</div>
				</div>
								<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput4">
						<div class="headline">
						<h2>예제 입력 4
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-4">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-4">9
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput4">
						<div class="headline">
						<h2>예제 출력 4
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-4">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-4">3
</pre>
						</section>
					</div>
									</div>
				</div>
								<div class="col-md-12">
				<div class="row">
					<div class="col-md-6">
						<section id="sampleinput5">
						<div class="headline">
						<h2>예제 입력 5
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-input-5">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-input-5">11
</pre>
						</section>
					</div>
					<div class="col-md-6">
						<section id="sampleoutput5">
						<div class="headline">
						<h2>예제 출력 5
							<button type="button" class="btn btn-link copy-button" style="padding: 0px;" data-clipboard-target="#sample-output-5">복사</button>
						</h2>
						</div>
						<pre class="sampledata" id="sample-output-5">3
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
							<div style="display: none;">
				</div>
								</div>
