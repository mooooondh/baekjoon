<div class="col-md-12">
			<div class="page-header">
				<h1><span class="printable">5585번 - </span><span id="problem_title">거스름돈</span>
				<span class="label-primary problem-label">출처</span><span class="label-default problem-label">다국어</span><span class="label-purple problem-label">분류</span>				<div class="btn-group pull-right problem-button">
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
				<p>타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.</p>

<p>예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.</p>

<p style="text-align:center"><img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/5585/1.png" style="height:126px; width:250px"></p>

				</div>
				</section>
			</div>
										<div class="col-md-12">
					<section id="input" class="problem-section">
					<div class="headline">
					<h2>입력</h2>
					</div>
					<div id="problem_input" class="problem-text">
					<p>입력은 한줄로 이루어져있고, 타로가 지불할 돈(1&nbsp;이상 1000미만의 정수)&nbsp;1개가&nbsp;쓰여져있다.</p>

					</div>
					</section>
				</div>
	
				<div class="col-md-12">
					<section id="output" class="problem-section">
					<div class="headline">
					<h2>출력</h2>
					</div>
					<div id="problem_output" class="problem-text">
					<p>제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.</p>

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
						<pre class="sampledata" id="sample-input-1">380
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
				<section id="hint" style="display: none;" class="problem-section">
				<div class="headline">
				<h2>힌트</h2>
				</div>
				<div id="problem_hint" class="problem-text">
				
				</div>
				</section>
			</div>
							<div style="display: none;">
					<div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjU1ODUiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWFjNzBcdWMyYTRcdWI5ODRcdWIzYzgiLCJkZXNjcmlwdGlvbiI6IjxwPlx1ZDBjMFx1Yjg1Y1x1YjI5NCBcdWM3OTBcdWM4ZmMgSk9JXHVjN2ExXHVkNjU0XHVjODEwXHVjNWQwXHVjMTFjIFx1YmIzY1x1YWM3NFx1Yzc0NCBcdWMwYjBcdWIyZTQuIEpPSVx1YzdhMVx1ZDY1NFx1YzgxMFx1YzVkMFx1YjI5NCBcdWM3OTRcdWIzYzhcdWM3M2NcdWI4NWMgNTAwXHVjNWQ0LCAxMDBcdWM1ZDQsIDUwXHVjNWQ0LCAxMFx1YzVkNCwgNVx1YzVkNCwgMVx1YzVkNFx1Yzc3NCBcdWNkYTlcdWJkODRcdWQ3ODggXHVjNzg4XHVhY2UwLCBcdWM1YjhcdWM4MWNcdWIwOTggXHVhYzcwXHVjMmE0XHViOTg0XHViM2M4IFx1YWMxY1x1YzIxOFx1YWMwMCBcdWFjMDBcdWM3YTUgXHVjODAxXHVhYzhjIFx1Yzc5NFx1YjNjOFx1Yzc0NCBcdWM5MDBcdWIyZTQuIFx1ZDBjMFx1Yjg1Y1x1YWMwMCBKT0lcdWM3YTFcdWQ2NTRcdWM4MTBcdWM1ZDBcdWMxMWMgXHViYjNjXHVhYzc0XHVjNzQ0IFx1YzBhY1x1YWNlMCBcdWNlNzRcdWM2YjRcdWQxMzBcdWM1ZDBcdWMxMWMgMTAwMFx1YzVkNCBcdWM5YzBcdWQzZDBcdWI5N2MgXHVkNTVjXHVjN2E1IFx1YjBjOFx1Yzc0NCBcdWI1NGMsIFx1YmMxYlx1Yzc0NCBcdWM3OTRcdWIzYzhcdWM1ZDAgXHVkM2VjXHVkNTY4XHViNDFjIFx1Yzc5NFx1YjNjOFx1Yzc1OCBcdWFjMWNcdWMyMThcdWI5N2MgXHVhZDZjXHVkNTU4XHViMjk0IFx1ZDUwNFx1Yjg1Y1x1YWRmOFx1YjdhOFx1Yzc0NCBcdWM3OTFcdWMxMzFcdWQ1NThcdWMyZGNcdWM2MjQuPFwvcD5cclxuXHJcbjxwPlx1YzYwOFx1Yjk3YyBcdWI0ZTRcdWM1YjQgXHVjNzg1XHViODI1XHViNDFjIFx1YzYwODFcdWM3NTggXHVhY2JkXHVjNmIwXHVjNWQwXHViMjk0IFx1YzU0NFx1Yjc5OCBcdWFkZjhcdWI5YmNcdWM1ZDBcdWMxMWMgXHVjYzk4XHViN2ZjIDRcdWFjMWNcdWI5N2MgXHVjZDljXHViODI1XHVkNTc0XHVjNTdjIFx1ZDU1Y1x1YjJlNC48XC9wPlxyXG5cclxuPHAgc3R5bGU9XCJ0ZXh0LWFsaWduOmNlbnRlclwiPjxpbWcgc3JjPVwiaHR0cHM6XC9cL29ubGluZWp1ZGdlaW1hZ2VzLnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL3Byb2JsZW1cLzU1ODVcLzEucG5nXCIgc3R5bGU9XCJoZWlnaHQ6MTI2cHg7IHdpZHRoOjI1MHB4XCIgXC8+PFwvcD5cclxuIiwiaW5wdXQiOiI8cD5cdWM3ODVcdWI4MjVcdWM3NDAgXHVkNTVjXHVjOTA0XHViODVjIFx1Yzc3NFx1YjhlOFx1YzViNFx1YzgzOFx1Yzc4OFx1YWNlMCwgXHVkMGMwXHViODVjXHVhYzAwIFx1YzljMFx1YmQ4OFx1ZDU2MCBcdWIzYzgoMSZuYnNwO1x1Yzc3NFx1YzBjMSAxMDAwXHViYmY4XHViOWNjXHVjNzU4IFx1YzgxNVx1YzIxOCkmbmJzcDsxXHVhYzFjXHVhYzAwJm5ic3A7XHVjNGYwXHVjNWVjXHVjODM4XHVjNzg4XHViMmU0LjxcL3A+XHJcbiIsIm91dHB1dCI6IjxwPlx1YzgxY1x1Y2Q5Y1x1ZDU2MCBcdWNkOWNcdWI4MjUgXHVkMzBjXHVjNzdjXHVjNzQwIDFcdWQ1ODlcdWM3M2NcdWI4NWNcdWI5Y2MgXHViNDE4XHVjNWI0IFx1Yzc4OFx1YjJlNC4gXHVjNzk0XHViM2M4XHVjNWQwIFx1ZDNlY1x1ZDU2OFx1YjQxYyBcdWI5ZTRcdWMyMThcdWI5N2MgXHVjZDljXHViODI1XHVkNTU4XHVjMmRjXHVjNjI0LjxcL3A+XHJcbiIsImhpbnQiOiIiLCJvcmlnaW5hbCI6IjAiLCJwcm9ibGVtX2xhbmdfY29kZSI6Ilx1ZDU1Y1x1YWQ2ZFx1YzViNCJ9LHsicHJvYmxlbV9pZCI6IjU1ODUiLCJwcm9ibGVtX2xhbmciOiIyIiwidGl0bGUiOiJcdTMwNGFcdTMwNjRcdTMwOGEiLCJkZXNjcmlwdGlvbiI6IjxwPlx1NTkyYVx1OTBjZVx1NTQxYlx1MzA2Zlx1MzA4OFx1MzA0ZkpPSVx1OTZkMVx1OGNhOFx1NWU5N1x1MzA2N1x1OGNiN1x1MzA0NFx1NzI2OVx1MzA5Mlx1MzA1OVx1MzA4Ylx1ZmYwZSBKT0lcdTk2ZDFcdThjYThcdTVlOTdcdTMwNmJcdTMwNmZcdTc4NmNcdThjYThcdTMwNmY1MDBcdTUxODZcdWZmMGMxMDBcdTUxODZcdWZmMGM1MFx1NTE4Nlx1ZmYwYzEwXHU1MTg2XHVmZjBjNVx1NTE4Nlx1ZmYwYzFcdTUxODZcdTMwNGNcdTUzNDFcdTUyMDZcdTMwNmFcdTY1NzBcdTMwNjBcdTMwNTFcdTMwNDJcdTMwOGFcdWZmMGNcdTMwNDRcdTMwNjRcdTMwODJcdTY3MDBcdTMwODJcdTY3OWFcdTY1NzBcdTMwNGNcdTVjMTFcdTMwNmFcdTMwNGZcdTMwNmFcdTMwOGJcdTMwODhcdTMwNDZcdTMwNmFcdTMwNGFcdTMwNjRcdTMwOGFcdTMwNmVcdTY1MmZcdTYyNTVcdTMwNDRcdTY1YjlcdTMwOTJcdTMwNTlcdTMwOGJcdWZmMGUgXHU1OTJhXHU5MGNlXHU1NDFiXHUzMDRjSk9JXHU5NmQxXHU4Y2E4XHU1ZTk3XHUzMDY3XHU4Y2I3XHUzMDQ0XHU3MjY5XHUzMDkyXHUzMDU3XHUzMDY2XHUzMGVjXHUzMGI4XHUzMDY3MTAwMFx1NTE4Nlx1NjcyZFx1MzA5MjFcdTY3OWFcdTUxZmFcdTMwNTdcdTMwNWZcdTY2NDJcdWZmMGNcdTMwODJcdTMwODlcdTMwNDZcdTMwNGFcdTMwNjRcdTMwOGFcdTMwNmJcdTU0MmJcdTMwN2VcdTMwOGNcdTMwOGJcdTc4NmNcdThjYThcdTMwNmVcdTY3OWFcdTY1NzBcdTMwOTJcdTZjNDJcdTMwODFcdTMwOGJcdTMwZDdcdTMwZWRcdTMwYjBcdTMwZTlcdTMwZTBcdTMwOTJcdTRmNWNcdTYyMTBcdTMwNWJcdTMwODhcdWZmMGU8XC9wPlxyXG5cclxuPHA+XHU0ZjhiXHUzMDQ4XHUzMDcwXHU1MTY1XHU1MjliXHU0ZjhiMVx1MzA2ZVx1NTgzNFx1NTQwOFx1MzA2Zlx1NGUwYlx1MzA2ZVx1NTZmM1x1MzA2Ylx1NzkzYVx1MzA1OVx1MzA4OFx1MzA0Nlx1MzA2Ylx1ZmYwYzRcdTMwOTJcdTUxZmFcdTUyOWJcdTMwNTdcdTMwNmFcdTMwNTFcdTMwOGNcdTMwNzBcdTMwNmFcdTMwODlcdTMwNmFcdTMwNDRcdWZmMGU8XC9wPlxyXG5cclxuPHAgc3R5bGU9XCJ0ZXh0LWFsaWduOiBjZW50ZXI7XCI+PGltZyBhbHQ9XCJcIiBzcmM9XCJodHRwczpcL1wvb25saW5lanVkZ2VpbWFnZXMuczMtYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvcHJvYmxlbVwvNTU4NVwvMS5wbmdcIiBzdHlsZT1cImhlaWdodDoyNTJweDsgd2lkdGg6NTAwcHhcIiBcLz48XC9wPlxyXG4iLCJpbnB1dCI6IjxwPlx1NTE2NVx1NTI5Ylx1MzA2ZjFcdTg4NGNcdTMwNGJcdTMwODlcdTMwNmFcdTMwOGFcdWZmMGNcdTU5MmFcdTkwY2VcdTU0MWJcdTMwNGNcdTY1MmZcdTYyNTVcdTMwNDZcdTkxZDFcdTk4NGRcdWZmMDgxXHU0ZWU1XHU0ZTBhMTAwMFx1NjcyYVx1NmU4MFx1MzA2ZVx1NjU3NFx1NjU3MFx1ZmYwOVx1MzA0YzFcdTMwNjRcdTMwNjBcdTMwNTFcdTY2ZjhcdTMwNGJcdTMwOGNcdTMwNjZcdTMwNDRcdTMwOGJcdWZmMGU8XC9wPlxyXG5cclxuIiwib3V0cHV0IjoiPHA+XHU2M2QwXHU1MWZhXHUzMDU5XHUzMDhiXHU1MWZhXHU1MjliXHUzMGQ1XHUzMGExXHUzMGE0XHUzMGViXHUzMDZmMVx1ODg0Y1x1MzA2ZVx1MzA3Zlx1MzA2N1x1MzA0Mlx1MzA4Ylx1ZmYwZSBcdTMwNGFcdTMwNjRcdTMwOGFcdTMwNmJcdTU0MmJcdTMwN2VcdTMwOGNcdTMwOGJcdTc4NmNcdThjYThcdTMwNmVcdTY3OWFcdTY1NzBcdTMwOTJcdTUxZmFcdTUyOWJcdTMwNWJcdTMwODhcdWZmMGU8XC9wPlxyXG5cclxuIiwiaGludCI6IiIsIm9yaWdpbmFsIjoiMSIsInByb2JsZW1fbGFuZ19jb2RlIjoiXHVjNzdjXHViY2Y4XHVjNWI0In1d</div>
				</div>
								</div>