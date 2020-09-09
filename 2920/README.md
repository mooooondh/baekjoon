<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">2920번 - </span><span id="problem_title">음계</span>
				<span class="label-success problem-label">성공</span><span class="label-primary problem-label">출처</span><span class="label-default problem-label">다국어</span><span class="label-purple problem-label">분류</span>				<div class="btn-group pull-right problem-button">
																										<button class="btn btn-default" type="button" id="favorite_button" data-favorite="0"><span class="glyphicon glyphicon-star-empty" id="favorite_image"></span></button>
																																			<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" href="#" id="lang-select-button">
	
							<span class="lang-select-text">
								한국어
							</span>
							&nbsp;
							<span class="caret"></span>
						</button>
						<ul class="dropdown-menu">
														<li>
								<a href="#" data-language-id="0" class="language-select-link">
									한국어								</a>
							</li>
														<li>
								<a href="#" data-language-id="1" class="language-select-link">
									영어 <span class="label label-default problem-label">원문</span>								</a>
							</li>
													</ul>
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
				<p>다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.</p>

<p>1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.</p>

<p>연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.</p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.</p>

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
						<pre class="sampledata" id="sample-input-1">1 2 3 4 5 6 7 8
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
						<pre class="sampledata" id="sample-output-1">ascending
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
						<pre class="sampledata" id="sample-input-2">8 7 6 5 4 3 2 1
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
						<pre class="sampledata" id="sample-output-2">descending
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
						<pre class="sampledata" id="sample-input-3">8 1 7 2 6 3 5 4
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
						<pre class="sampledata" id="sample-output-3">mixed
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
					<div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjI5MjAiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWM3NGNcdWFjYzQiLCJkZXNjcmlwdGlvbiI6IjxwPlx1YjJlNFx1YzdhNVx1Yzg3MFx1YjI5NCBjIGQgZSBmIGcgYSBiIEMsIFx1Y2QxZCA4XHVhYzFjIFx1Yzc0Y1x1YzczY1x1Yjg1YyBcdWM3NzRcdWI4ZThcdWM1YjRcdWM4MzhcdWM3ODhcdWIyZTQuIFx1Yzc3NCBcdWJiMzhcdWM4MWNcdWM1ZDBcdWMxMWMgOFx1YWMxYyBcdWM3NGNcdWM3NDAgXHViMmU0XHVjNzRjXHVhY2ZjIFx1YWMxOVx1Yzc3NCBcdWMyMmJcdWM3OTBcdWI4NWMgXHViYzE0XHVhZmI4XHVjNWI0IFx1ZDQ1Y1x1ZDYwNFx1ZDU1Y1x1YjJlNC4gY1x1YjI5NCAxXHViODVjLCBkXHViMjk0IDJcdWI4NWMsIC4uLiwgQ1x1Yjk3YyA4XHViODVjIFx1YmMxNFx1YWZiY1x1YjJlNC48XC9wPlxyXG5cclxuPHA+MVx1YmQ4MFx1ZDEzMCA4XHVhZTRjXHVjOWMwIFx1Y2MyOFx1Yjg0MFx1YjMwMFx1Yjg1YyBcdWM1ZjBcdWM4ZmNcdWQ1NWNcdWIyZTRcdWJhNzQgYXNjZW5kaW5nLCA4XHViZDgwXHVkMTMwIDFcdWFlNGNcdWM5YzAgXHVjYzI4XHViODQwXHViMzAwXHViODVjIFx1YzVmMFx1YzhmY1x1ZDU1Y1x1YjJlNFx1YmE3NCBkZXNjZW5kaW5nLCBcdWI0NTggXHViMmU0IFx1YzU0NFx1YjJjOFx1Yjc3Y1x1YmE3NCBtaXhlZCBcdWM3NzRcdWIyZTQuPFwvcD5cclxuXHJcbjxwPlx1YzVmMFx1YzhmY1x1ZDU1YyBcdWMyMWNcdWMxMWNcdWFjMDAgXHVjOGZjXHVjNWI0XHVjODRjXHVjNzQ0IFx1YjU0YywgXHVjNzc0XHVhYzgzXHVjNzc0IGFzY2VuZGluZ1x1Yzc3OFx1YzljMCwgZGVzY2VuZGluZ1x1Yzc3OFx1YzljMCwgXHVjNTQ0XHViMmM4XHViYTc0IG1peGVkXHVjNzc4XHVjOWMwIFx1ZDMxMFx1YmNjNFx1ZDU1OFx1YjI5NCBcdWQ1MDRcdWI4NWNcdWFkZjhcdWI3YThcdWM3NDQgXHVjNzkxXHVjMTMxXHVkNTU4XHVjMmRjXHVjNjI0LjxcL3A+XHJcbiIsImlucHV0IjoiPHA+XHVjY2FiXHVjOWY4IFx1YzkwNFx1YzVkMCA4XHVhYzFjIFx1YzIyYlx1Yzc5MFx1YWMwMCBcdWM4ZmNcdWM1YjRcdWM5YzRcdWIyZTQuIFx1Yzc3NCBcdWMyMmJcdWM3OTBcdWIyOTQgXHViYjM4XHVjODFjIFx1YzEyNFx1YmE4NVx1YzVkMFx1YzExYyBcdWMxMjRcdWJhODVcdWQ1NWMgXHVjNzRjXHVjNzc0XHViYTcwLCAxXHViZDgwXHVkMTMwIDhcdWFlNGNcdWM5YzAgXHVjMjJiXHVjNzkwXHVhYzAwIFx1ZDU1YyBcdWJjODhcdWM1MjkgXHViNGYxXHVjN2E1XHVkNTVjXHViMmU0LjxcL3A+XHJcbiIsIm91dHB1dCI6IjxwPlx1Y2NhYlx1YzlmOCBcdWM5MDRcdWM1ZDAgYXNjZW5kaW5nLCBkZXNjZW5kaW5nLCBtaXhlZCBcdWM5MTEgXHVkNTU4XHViMDk4XHViOTdjIFx1Y2Q5Y1x1YjgyNVx1ZDU1Y1x1YjJlNC48XC9wPlxyXG4iLCJoaW50IjoiIiwib3JpZ2luYWwiOiIwIiwicHJvYmxlbV9sYW5nX2NvZGUiOiJcdWQ1NWNcdWFkNmRcdWM1YjQifSx7InByb2JsZW1faWQiOiIyOTIwIiwicHJvYmxlbV9sYW5nIjoiMSIsInRpdGxlIjoiTk9URSIsImRlc2NyaXB0aW9uIjoiPHA+QyBtYWpvciBzY2FsZSBjb25zaXN0cyBvZiA4IHRvbmVzOiBjIGQgZSBmIGcgYSBiJm5ic3A7Qy4gRm9yIHRoaXMgdGFzayB3ZSBudW1iZXIgdGhlIG5vdGVzIHVzaW5nIG51bWJlcnMgMSB0aHJvdWdoIDguIFRoZSBzY2FsZSBjYW4gYmUgcGxheWVkIGFzY2VuZGluZywgZnJvbSAxIHRvIDgsIGRlc2NlbmRpbmcsIGZyb20gOCB0byAxLCBvciBtaXhlZC4gV3JpdGUgYSBwcm9ncmFtIHRoYXQsIGdpdmVuIHRoZSBzZXF1ZW5jZSBvZiBub3RlcywgZGV0ZXJtaW5lcyB3ZXRoZXIgdGhlIHNjYWxlIHdhcyBwbGF5ZWQgYXNjZW5kaW5nLCBkZXNjZW5kaW5nIG9yIG1peGVkLjxcL3A+XHJcbiIsImlucHV0IjoiPHA+Rmlyc3QgYW5kIG9ubHkgbGluZSBvZiBpbnB1dCB3aWxsIGNvbnRhaW4gOCBpbnRlZ2VycywgZnJvbSAxIHRvIDggaW5jbHVzaXZlLiBFYWNoIGludGVnZXIgd2lsbCBhcHBlYXIgZXhhY3RsZXkgb25jZSBpbiB0aGUgaW5wdXQuPFwvcD5cclxuIiwib3V0cHV0IjoiPHA+SW4gdGhlIGZpcnN0IGFuZCBvbmx5IGxpbmUgb2YgaW5wdXQgcHJpbnQgJnF1b3Q7ZGVzY2VuZGluZyZxdW90OyBpZiB0aGUgc2NhbGUgd2FzIHBsYXllZCBkZXNjZW5kaW5nLCAmcXVvdDthc2NlbmRpbmcmcXVvdDsgaWYgdGhlIHNjYWxlIHdhcyBwbGF5ZWQgYXNjZW5kaW5nIGFuZCAmcXVvdDttaXhlZCZxdW90OyBpZiB0aGUgc2NhbGUgd2FzIHBsYXllZCBtaXhlZC48XC9wPlxyXG4iLCJoaW50IjoiIiwib3JpZ2luYWwiOiIxIiwicHJvYmxlbV9sYW5nX2NvZGUiOiJcdWM2MDFcdWM1YjQifV0=</div>
				</div>
								</div>
