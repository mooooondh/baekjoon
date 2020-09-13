<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">2839번 - </span><span id="problem_title">설탕 배달</span>
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
					<div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjI4MzkiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWMxMjRcdWQwZDUgXHViYzMwXHViMmVjIiwiZGVzY3JpcHRpb24iOiI8cD5cdWMwYzFcdWFkZmNcdWM3NzRcdWIyOTQgXHVjNjk0XHVjOTk4IFx1YzEyNFx1ZDBkNVx1YWNmNVx1YzdhNVx1YzVkMFx1YzExYyBcdWMxMjRcdWQwZDVcdWM3NDQgXHViYzMwXHViMmVjXHVkNTU4XHVhY2UwIFx1Yzc4OFx1YjJlNC4gXHVjMGMxXHVhZGZjXHVjNzc0XHViMjk0IFx1YzljMFx1YWUwOCBcdWMwYWNcdWQwZDVcdWFjMDBcdWFjOGNcdWM1ZDAgXHVjMTI0XHVkMGQ1XHVjNzQ0IFx1YzgxNVx1ZDY1NVx1ZDU1OFx1YWM4YyBOXHVkMGFjXHViODVjXHVhZGY4XHViN2E4XHVjNzQ0IFx1YmMzMFx1YjJlY1x1ZDU3NFx1YzU3YyBcdWQ1NWNcdWIyZTQuIFx1YzEyNFx1ZDBkNVx1YWNmNVx1YzdhNVx1YzVkMFx1YzExYyBcdWI5Y2NcdWI0ZGNcdWIyOTQgXHVjMTI0XHVkMGQ1XHVjNzQwIFx1YmQwOVx1YzljMFx1YzVkMCBcdWIyZjRcdWFjYThcdWM4MzggXHVjNzg4XHViMmU0LiBcdWJkMDlcdWM5YzBcdWIyOTQgM1x1ZDBhY1x1Yjg1Y1x1YWRmOFx1YjdhOCBcdWJkMDlcdWM5YzBcdWM2NDAgNVx1ZDBhY1x1Yjg1Y1x1YWRmOFx1YjdhOCBcdWJkMDlcdWM5YzBcdWFjMDAgXHVjNzg4XHViMmU0LjxcL3A+XHJcblxyXG48cD5cdWMwYzFcdWFkZmNcdWM3NzRcdWIyOTQgXHVhZGMwXHVjYzJlXHVhZTMwIFx1YjU0Y1x1YmIzOFx1YzVkMCwgXHVjZDVjXHViMzAwXHVkNTVjIFx1YzgwMVx1Yzc0MCBcdWJkMDlcdWM5YzBcdWI5N2MgXHViNGU0XHVhY2UwIFx1YWMwMFx1YjgyNFx1YWNlMCBcdWQ1NWNcdWIyZTQuIFx1YzYwOFx1Yjk3YyBcdWI0ZTRcdWM1YjQsIDE4XHVkMGFjXHViODVjXHVhZGY4XHViN2E4IFx1YzEyNFx1ZDBkNVx1Yzc0NCBcdWJjMzBcdWIyZWNcdWQ1NzRcdWM1N2MgXHVkNTYwIFx1YjU0YywgM1x1ZDBhY1x1Yjg1Y1x1YWRmOFx1YjdhOCBcdWJkMDlcdWM5YzAgNlx1YWMxY1x1Yjk3YyBcdWFjMDBcdWM4MzhcdWFjMDBcdWIzYzQgXHViNDE4XHVjOWMwXHViOWNjLCA1XHVkMGFjXHViODVjXHVhZGY4XHViN2E4IDNcdWFjMWNcdWM2NDAgM1x1ZDBhY1x1Yjg1Y1x1YWRmOFx1YjdhOCAxXHVhYzFjXHViOTdjIFx1YmMzMFx1YjJlY1x1ZDU1OFx1YmE3NCwgXHViMzU0IFx1YzgwMVx1Yzc0MCBcdWFjMWNcdWMyMThcdWM3NTggXHViZDA5XHVjOWMwXHViOTdjIFx1YmMzMFx1YjJlY1x1ZDU2MCBcdWMyMTggXHVjNzg4XHViMmU0LjxcL3A+XHJcblxyXG48cD5cdWMwYzFcdWFkZmNcdWM3NzRcdWFjMDAgXHVjMTI0XHVkMGQ1XHVjNzQ0IFx1YzgxNVx1ZDY1NVx1ZDU1OFx1YWM4YyBOXHVkMGFjXHViODVjXHVhZGY4XHViN2E4IFx1YmMzMFx1YjJlY1x1ZDU3NFx1YzU3YyBcdWQ1NjAgXHViNTRjLCBcdWJkMDlcdWM5YzAgXHViYTg3IFx1YWMxY1x1Yjk3YyBcdWFjMDBcdWM4MzhcdWFjMDBcdWJhNzQgXHViNDE4XHViMjk0XHVjOWMwIFx1YWRmOCBcdWMyMThcdWI5N2MgXHVhZDZjXHVkNTU4XHViMjk0IFx1ZDUwNFx1Yjg1Y1x1YWRmOFx1YjdhOFx1Yzc0NCBcdWM3OTFcdWMxMzFcdWQ1NThcdWMyZGNcdWM2MjQuPFwvcD5cclxuIiwiaW5wdXQiOiI8cD5cdWNjYWJcdWM5ZjggXHVjOTA0XHVjNWQwIE5cdWM3NzQgXHVjOGZjXHVjNWI0XHVjOWM0XHViMmU0LiAoMyAmbGU7IE4gJmxlOyA1MDAwKTxcL3A+XHJcbiIsIm91dHB1dCI6IjxwPlx1YzBjMVx1YWRmY1x1Yzc3NFx1YWMwMCBcdWJjMzBcdWIyZWNcdWQ1NThcdWIyOTQgXHViZDA5XHVjOWMwXHVjNzU4IFx1Y2Q1Y1x1YzE4YyBcdWFjMWNcdWMyMThcdWI5N2MgXHVjZDljXHViODI1XHVkNTVjXHViMmU0LiBcdWI5Y2NcdWM1N2QsIFx1YzgxNVx1ZDY1NVx1ZDU1OFx1YWM4YyBOXHVkMGFjXHViODVjXHVhZGY4XHViN2E4XHVjNzQ0IFx1YjljY1x1YjRlNCBcdWMyMTggXHVjNWM2XHViMmU0XHViYTc0IC0xXHVjNzQ0IFx1Y2Q5Y1x1YjgyNVx1ZDU1Y1x1YjJlNC48XC9wPlxyXG4iLCJoaW50IjoiIiwib3JpZ2luYWwiOiIwIiwicHJvYmxlbV9sYW5nX2NvZGUiOiJcdWQ1NWNcdWFkNmRcdWM1YjQifSx7InByb2JsZW1faWQiOiIyODM5IiwicHJvYmxlbV9sYW5nIjoiMSIsInRpdGxlIjoiXHUwMTYwRVx1MDEwNkVSIiwiZGVzY3JpcHRpb24iOiI8cD5NaXJrbyB3b3JrcyBpbiBhIHN1Z2FyIGZhY3RvcnkgYXMgYSBkZWxpdmVyeSBib3kuIEhlIGhhcyBqdXN0IHJlY2VpdmVkIGFuIG9yZGVyOiBoZSBoYXMgdG8gZGVsaXZlciBleGFjdGx5IE4ga2lsb2dyYW1zIG9mIHN1Z2FyIHRvIGEgY2FuZHkgc3RvcmUgb24gdGhlIEFkcmlhdGljIGNvYXN0LiBNaXJrbyBjYW4gdXNlIHR3byB0eXBlcyBvZiBwYWNrYWdlcywgdGhlIG9uZXMgdGhhdCBjb250YWluIDMga2lsb2dyYW1zLCBhbmQgdGhlIG9uZXMgd2l0aCA1IGtpbG9ncmFtcyBvZiBzdWdhci48XC9wPlxyXG5cclxuPHA+TWlya28gd291bGQgbGlrZSB0byB0YWtlIGFzIGZldyBwYWNrYWdlcyBhcyBwb3NzaWJsZS4gRm9yIGV4YW1wbGUsIGlmIGhlIGhhcyB0byBkZWxpdmVyIDE4IGtpbG9ncmFtcyBvZiBzdWdhciwgaGUgY291bGQgdXNlIHNpeCAzLWtpbG9ncmFtIHBhY2thZ2VzLiBCdXQsIGl0IHdvdWxkIGJlIGJldHRlciB0byB1c2UgdGhyZWUgNS1raWxvZ3JhbSBwYWNrYWdlcywgYW5kIG9uZSAzLWtpbG9ncmFtIHBhY2thZ2UsIHJlc3VsdGluZyBpbiB0aGUgdG90YWwgb2YgZm91ciBwYWNrYWdlcy48XC9wPlxyXG5cclxuPHA+SGVscCBNaXJrbyBieSBmaW5kaW5nIHRoZSBtaW5pbXVtIG51bWJlciBvZiBwYWNrYWdlcyByZXF1aXJlZCB0byB0cmFuc3BvcnQgZXhhY3RseSBOIGtpbG9ncmFtcyBvZiBzdWdhci48XC9wPlxyXG4iLCJpbnB1dCI6IjxwPlRoZSBmaXJzdCBhbmQgb25seSBsaW5lIG9mIGlucHV0IGNvbnRhaW5zIG9uZSBpbnRlZ2VyIE4gKDMgJmxlOyBOICZsZTsgNTAwMCkuPFwvcD5cclxuIiwib3V0cHV0IjoiPHA+VGhlIGZpcnN0IGFuZCBvbmx5IGxpbmUgb2Ygb3V0cHV0IHNob3VsZCBjb250YWluIHRoZSBtaW5pbXVtIG51bWJlciBvZiBwYWNrYWdlcyBNaXJrbyBoYXMgdG8gdXNlLiBJZiBpdCBpcyBpbXBvc3NpYmxlIHRvIGRlbGl2ZXIgZXhhY3RseSBOIGtpbG9ncmFtcywgb3V0cHV0IC0xLjxcL3A+XHJcbiIsImhpbnQiOiIiLCJvcmlnaW5hbCI6IjEiLCJwcm9ibGVtX2xhbmdfY29kZSI6Ilx1YzYwMVx1YzViNCJ9XQ==</div>
				</div>
								</div>
