<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">2884번 - </span><span id="problem_title">알람 시계</span>
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
				<p>상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.</p>

<p>상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.</p>

<p>이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.</p>

<p>바로 "45분 일찍 알람 설정하기"이다.</p>

<p>이 방법은 단순하다. 원래 설정되어 있는&nbsp;알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.</p>

<p>현재 상근이가 설정한&nbsp;알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.</p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.</p>

<p>입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)</p>

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
						<pre class="sampledata" id="sample-input-1">10 10
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
						<pre class="sampledata" id="sample-output-1">9 25
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
						<pre class="sampledata" id="sample-input-2">0 30
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
						<pre class="sampledata" id="sample-output-2">23 45
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
						<pre class="sampledata" id="sample-input-3">23 40
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
						<pre class="sampledata" id="sample-output-3">22 55
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
					<div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjI4ODQiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWM1NGNcdWI3OGMgXHVjMmRjXHVhY2M0IiwiZGVzY3JpcHRpb24iOiI8cD5cdWMwYzFcdWFkZmNcdWM3NzRcdWIyOTQgXHViOWU0XHVjNzdjIFx1YzU0NFx1Y2U2OCBcdWM1NGNcdWI3OGNcdWM3NDQgXHViNGUzXHVhY2UwIFx1Yzc3Y1x1YzViNFx1YjA5Y1x1YjJlNC4gXHVjNTRjXHViNzhjXHVjNzQ0IFx1YjRlM1x1YWNlMCBcdWJjMTRcdWI4NWMgXHVjNzdjXHVjNWI0XHViMDk4XHViYTc0IFx1YjJlNFx1ZDU4OVx1Yzc3NFx1YWNhMFx1YzljMFx1YjljYywgXHVkNTZkXHVjMGMxIFx1Yzg3MFx1YWUwOFx1YjljYyBcdWIzNTQgXHVjNzkwXHViODI0XHViMjk0IFx1YjljOFx1Yzc0YyBcdWI1NGNcdWJiMzhcdWM1ZDAgXHViOWU0XHVjNzdjIFx1ZDU1OVx1YWQ1MFx1Yjk3YyBcdWM5YzBcdWFjMDFcdWQ1NThcdWFjZTAgXHVjNzg4XHViMmU0LjxcL3A+XHJcblxyXG48cD5cdWMwYzFcdWFkZmNcdWM3NzRcdWIyOTQgXHViYWE4XHViNGUwIFx1YmMyOVx1YmM5NVx1Yzc0NCBcdWIzZDlcdWM2ZDBcdWQ1NzRcdWJjZjRcdWM1NThcdWM5YzBcdWI5Y2MsIFx1Yzg3MFx1YWUwOFx1YjljYyBcdWIzNTQgXHVjNzkwXHViODI0XHViMjk0IFx1YjljOFx1Yzc0Y1x1Yzc0MCBcdWFkZjggXHVjNWI0XHViNWE0IFx1YWM4M1x1YjNjNCBcdWM1YzZcdWM1NjggXHVjMjE4XHVhYzAwIFx1YzVjNlx1YzVjOFx1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVjNzc0XHViN2YwIFx1YzBjMVx1YWRmY1x1Yzc3NFx1Yjk3YyBcdWJkODhcdWMzMGRcdWQ1NThcdWFjOGMgXHViY2Y0XHViMzU4LCBcdWNjM2RcdWM2MDFcdWM3NzRcdWIyOTQgXHVjNzkwXHVjMmUwXHVjNzc0IFx1YzBhY1x1YzZhOVx1ZDU1OFx1YjI5NCBcdWJjMjlcdWJjOTVcdWM3NDQgXHVjZDk0XHVjYzljXHVkNTc0IFx1YzhmY1x1YzVjOFx1YjJlNC48XC9wPlxyXG5cclxuPHA+XHViYzE0XHViODVjICZxdW90OzQ1XHViZDg0IFx1Yzc3Y1x1Y2MwZCBcdWM1NGNcdWI3OGMgXHVjMTI0XHVjODE1XHVkNTU4XHVhZTMwJnF1b3Q7XHVjNzc0XHViMmU0LjxcL3A+XHJcblxyXG48cD5cdWM3NzQgXHViYzI5XHViYzk1XHVjNzQwIFx1YjJlOFx1YzIxY1x1ZDU1OFx1YjJlNC4gXHVjNmQwXHViNzk4IFx1YzEyNFx1YzgxNVx1YjQxOFx1YzViNCBcdWM3ODhcdWIyOTQmbmJzcDtcdWM1NGNcdWI3OGNcdWM3NDQgNDVcdWJkODQgXHVjNTVlXHVjMTFjXHViMjk0IFx1YzJkY1x1YWMwNFx1YzczY1x1Yjg1YyBcdWJjMTRcdWFmYjhcdWIyOTQgXHVhYzgzXHVjNzc0XHViMmU0LiBcdWM1YjRcdWNjMjhcdWQ1M2MgXHVjNTRjXHViNzhjIFx1YzE4Y1x1YjlhY1x1Yjk3YyBcdWI0ZTRcdWM3M2NcdWJhNzQsIFx1YzU0Y1x1Yjc4Y1x1Yzc0NCBcdWIwNDRcdWFjZTAgXHVjODcwXHVhZTA4IFx1YjM1NCBcdWM3OTggXHVhYzgzXHVjNzc0XHVhZTMwIFx1YjU0Y1x1YmIzOFx1Yzc3NFx1YjJlNC4gXHVjNzc0IFx1YmMyOVx1YmM5NVx1Yzc0NCBcdWMwYWNcdWM2YTlcdWQ1NThcdWJhNzQsIFx1YjllNFx1Yzc3YyBcdWM1NDRcdWNlNjggXHViMzU0IFx1YzdhNFx1YjJlNFx1YjI5NCBcdWFlMzBcdWJkODRcdWM3NDQgXHViMjkwXHViMDg0IFx1YzIxOCBcdWM3ODhcdWFjZTAsIFx1ZDU1OVx1YWQ1MFx1YjNjNCBcdWM5YzBcdWFjMDFcdWQ1NThcdWM5YzAgXHVjNTRhXHVhYzhjIFx1YjQxY1x1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVkNjA0XHVjN2FjIFx1YzBjMVx1YWRmY1x1Yzc3NFx1YWMwMCBcdWMxMjRcdWM4MTVcdWQ1NWMmbmJzcDtcdWM1NGNcdWI3OGMgXHVjMmRjXHVhYzAxXHVjNzc0IFx1YzhmY1x1YzViNFx1Yzg0Y1x1Yzc0NCBcdWI1NGMsIFx1Y2MzZFx1YzYwMVx1Yzc3NFx1Yzc1OCBcdWJjMjlcdWJjOTVcdWM3NDQgXHVjMGFjXHVjNmE5XHVkNTVjXHViMmU0XHViYTc0LCBcdWM3NzRcdWI5N2MgXHVjNWI4XHVjODFjXHViODVjIFx1YWNlMFx1Y2NkMFx1YzU3YyBcdWQ1NThcdWIyOTRcdWM5YzAgXHVhZDZjXHVkNTU4XHViMjk0IFx1ZDUwNFx1Yjg1Y1x1YWRmOFx1YjdhOFx1Yzc0NCBcdWM3OTFcdWMxMzFcdWQ1NThcdWMyZGNcdWM2MjQuPFwvcD5cclxuIiwiaW5wdXQiOiI8cD5cdWNjYWJcdWM5ZjggXHVjOTA0XHVjNWQwIFx1YjQ1MCBcdWM4MTVcdWMyMTggSFx1YzY0MCBNXHVjNzc0IFx1YzhmY1x1YzViNFx1YzljNFx1YjJlNC4gKDAgJmxlOyBIICZsZTsgMjMsIDAgJmxlOyBNICZsZTsgNTkpIFx1YWRmOFx1YjlhY1x1YWNlMCBcdWM3NzRcdWFjODNcdWM3NDAgXHVkNjA0XHVjN2FjIFx1YzBjMVx1YWRmY1x1Yzc3NFx1YWMwMCBcdWMxMjRcdWM4MTVcdWQ1NWMgXHViMTkzXHVjNzQwIFx1YzU0Y1x1Yjc4YyBcdWMyZGNcdWFjMDQgSFx1YzJkYyBNXHViZDg0XHVjNzQ0IFx1Yzc1OFx1YmJmOFx1ZDU1Y1x1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVjNzg1XHViODI1IFx1YzJkY1x1YWMwNFx1Yzc0MCAyNFx1YzJkY1x1YWMwNCBcdWQ0NWNcdWQ2MDRcdWM3NDQgXHVjMGFjXHVjNmE5XHVkNTVjXHViMmU0LiAyNFx1YzJkY1x1YWMwNCBcdWQ0NWNcdWQ2MDRcdWM1ZDBcdWMxMWMgXHVkNTU4XHViOGU4XHVjNzU4IFx1YzJkY1x1Yzc5MVx1Yzc0MCAwOjAoXHVjNzkwXHVjODE1KVx1Yzc3NFx1YWNlMCwgXHViMDVkXHVjNzQwIDIzOjU5KFx1YjJlNFx1Yzc0Y1x1YjBhMCBcdWM3OTBcdWM4MTUgMVx1YmQ4NCBcdWM4MDQpXHVjNzc0XHViMmU0LiBcdWMyZGNcdWFjMDRcdWM3NDQgXHViMDk4XHVkMGMwXHViMGJjIFx1YjU0YywgXHViZDg4XHVkNTQ0XHVjNjk0XHVkNTVjIDBcdWM3NDAgXHVjMGFjXHVjNmE5XHVkNTU4XHVjOWMwIFx1YzU0YVx1YjI5NFx1YjJlNC48XC9wPlxyXG4iLCJvdXRwdXQiOiI8cD5cdWNjYWJcdWM5ZjggXHVjOTA0XHVjNWQwIFx1YzBjMVx1YWRmY1x1Yzc3NFx1YWMwMCBcdWNjM2RcdWM2MDFcdWM3NzRcdWM3NTggXHViYzI5XHViYzk1XHVjNzQ0IFx1YzBhY1x1YzZhOVx1ZDU2MCBcdWI1NGMsIFx1YzEyNFx1YzgxNVx1ZDU3NFx1YzU3YyBcdWQ1NThcdWIyOTQgXHVjNTRjXHViNzhjIFx1YzJkY1x1YWMwNFx1Yzc0NCBcdWNkOWNcdWI4MjVcdWQ1NWNcdWIyZTQuIChcdWM3ODVcdWI4MjVcdWFjZmMgXHVhYzE5XHVjNzQwIFx1ZDYxNVx1ZDBkY1x1Yjg1YyBcdWNkOWNcdWI4MjVcdWQ1NThcdWJhNzQgXHViNDFjXHViMmU0Lik8XC9wPlxyXG4iLCJoaW50IjoiIiwib3JpZ2luYWwiOiIwIiwicHJvYmxlbV9sYW5nX2NvZGUiOiJcdWQ1NWNcdWFkNmRcdWM1YjQifSx7InByb2JsZW1faWQiOiIyODg0IiwicHJvYmxlbV9sYW5nIjoiMSIsInRpdGxlIjoiU1BBVkFOQUMiLCJkZXNjcmlwdGlvbiI6IjxwPkV2ZXJ5IHNjaG9vbCBtb3JuaW5nIE1pcmtvIGlzIHdva2VuIHVwIGJ5IHRoZSBzb3VuZCBvZiBoaXMgYWxhcm0gY2xvY2suIFNpbmNlIGhlIGlzIGEgYml0IGZvcmdldGZ1bCwgcXVpdGUgb2Z0ZW4gaGUgbGVhdmVzIHRoZSBhbGFybSBvbiBvbiBTYXR1cmRheSBtb3JuaW5nIHRvby4gVGhhdCYjMzk7cyBub3QgdG9vIGJhZCB0aG91Z2gsIHNpbmNlIGhlIGZlZWxzIGdvb2Qgd2hlbiBoZSByZWFsaXplcyBoZSBkb2VzbiYjMzk7dCBoYXZlIHRvIGdldCB1cCBmcm9tIGhpcyB3YXJtIGFuZCBjb3p5IGJlZC48XC9wPlxyXG5cclxuPHA+SGUgbGlrZXMgdGhhdCBzbyBtdWNoLCB0aGF0IGhlIHdvdWxkIGxpa2UgdG8gZXhwZXJpZW5jZSB0aGF0IG9uIG90aGVyIGRheXMgb2YgdGhlIHdlZWsgdG9vISBIaXMgZnJpZW5kIFNsYXZrbyBvZmZlcmVkIHRoaXMgc2ltcGxlIHNvbHV0aW9uOiBzZXQgaGlzIGFsYXJtIGNsb2NrIDQ1IG1pbnV0ZXMgZWFybHksIGFuZCBoZSBjYW4gZW5qb3kgdGhlIGNvbWZvcnQgb2YgaGlzIGJlZCwgZnVsbHkgYXdha2UsIGZvciA0NSBtaW51dGVzIGVhY2ggZGF5LjxcL3A+XHJcblxyXG48cD5NaXJrbyBkZWNpZGVkIHRvIGhlZWQgaGlzIGFkdmljZSwgaG93ZXZlciBoaXMgYWxhcm0gY2xvY2sgdXNlcyAyNC1ob3VyIG5vdGF0aW9uIGFuZCBoZSBoYXMgaXNzdWVzIHdpdGggYWRqdXN0aW5nIHRoZSB0aW1lLiBIZWxwIE1pcmtvIGFuZCB3cml0ZSBhIHByb2dyYW0gdGhhdCB3aWxsIHRha2Ugb25lIHRpbWUgc3RhbXAsIGluIDI0LWhvdXIgbm90YXRpb24sIGFuZCBwcmludCBvdXQgYSBuZXcgdGltZSBzdGFtcCwgNDUgbWludXRlcyBlYXJsaWVyLCBhbHNvIGluIDI0LWhvdXIgbm90YXRpb24uPFwvcD5cclxuXHJcbjxwPk5vdGU6IGlmIHlvdSBhcmUgdW5mYW1pbGlhciB3aXRoIDI0LWhvdXIgdGltZSBub3RhdGlvbiB5b3Vyc2VsZiwgeW91IG1pZ2h0IGJlIGludGVyZXN0ZWQgdG8ga25vdyBpdCBzdGFydHMgd2l0aCAwOjAwIChtaWRuaWdodCkgYW5kIGVuZHMgd2l0aCAyMzo1OSAob25lIG1pbnV0ZSBiZWZvcmUgbWlkbmlnaHQpLjxcL3A+XHJcbiIsImlucHV0IjoiPHA+VGhlIGZpcnN0IGFuZCBvbmx5IGxpbmUgb2YgaW5wdXQgd2lsbCBjb250YWluIGV4YWN0bHkgdHdvIGludGVnZXJzIEggYW5kIE0gKDAgJmxlOyBIICZsZTsgMjMsIDAgJmxlOyBNICZsZTsgNTkpIHNlcGFyYXRlZCBieSBhIHNpbmdsZSBzcGFjZSwgdGhlIGlucHV0IHRpbWUgaW4gMjQtaG91ciBub3RhdGlvbi4gSCBkZW5vdGVzIGhvdXJzIGFuZCBNIG1pbnV0ZXMuPFwvcD5cclxuIiwib3V0cHV0IjoiPHA+VGhlIGZpcnN0IGFuZCBvbmx5IGxpbmUgb2Ygb3V0cHV0IHNob3VsZCBjb250YWluIGV4YWN0bHkgdHdvIGludGVnZXJzLCB0aGUgdGltZSA0NSBtaW51dGVzIGJlZm9yZSBpbnB1dCB0aW1lLjxcL3A+XHJcbiIsImhpbnQiOiIiLCJvcmlnaW5hbCI6IjEiLCJwcm9ibGVtX2xhbmdfY29kZSI6Ilx1YzYwMVx1YzViNCJ9XQ==</div>
				</div>
								</div>
