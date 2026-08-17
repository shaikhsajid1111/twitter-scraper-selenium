<h1> Twitter scraper selenium </h1>
<p> Python's package to scrape Twitter's front-end easily with selenium.  </p>


[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT) [![Python >=3.8](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/shaikhsajid1111/facebook_page_scraper/graphs/commit-activity)

<!--TABLE of contents-->
<h2> Table of Contents </h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Installation">Installation</a>
        <ul>
        <li><a href="#sourceInstallation">Installing from source</a></li>
        <li><a href="#pypiInstallation">Installing with PyPI</a></li>
        </ul>
        </li>
      </ul>
    </li>
    <li><a href="#Usage">Usage</a>
    <ul><li><a href="#availableFunction">Available Functions in this package- Summary</a></li></ul>
    <ul><li><a href="#profileDetail">Scraping profile's details</a>
    <ul>
    <li><a href="#profileDetailExample">In JSON Format - Example</a></li>
    <li><a href="#profileDetailArgument">Function Argument</a></li>
    <li><a href="#profileDetailKeys">Keys of the output</a></li>
    </ul>
    </li></ul>
    <!---->
    <ul><li><a href="#xquik-search">Searching X with Xquik</a></li></ul>
    <ul>
    <li><a href="#profile">Scraping profile's tweets</a>
    <ul>
    <li><a href="#profileJson">In JSON format - Example</a></li>
    <li><a href="#profileCSV">In CSV format - Example</a></li>
    <li><a href="#profileArgument">Function Arguments</a></li>
    <li><a href="#profileOutput">Keys of the output data</a></li>
    </ul>
    <li><a href='#to-scrape-user-tweets-with-api'>Scraping user's tweet using API</a></li>
    <ul>
    <li><a href='#to-scrape-user-tweets-with-api'>In JSON format - Example</a></li>
    <li><a href='#users_api_parameter'>Function Arguments</a></li>
    <li><a href='#scrape_user_with_api_args_keys'>Keys of the output</a></li>
    </ul>
    <li><a href="#proxy">Using scraper with proxy</a>
    <ul>
    <li><a href="#unauthenticatedProxy">Unauthenticated Proxy</a></li>
    <li><a href="#authenticatedProxy">Authenticated Proxy</a></li>
    </ul>
    </li>
    </li>
    </ul>
    </li>
    <li><a href="#privacy">Privacy</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---

<h2>⚡ Sponsor</h2>

<h3>
  <strong><a href="https://www.rapidproxy.io/?ref=twsc" rel="nofollow">RapidProxy</a> — Unlock Scalable Web Data for Your Business</strong>
</h3>

<p>
  <a href="https://www.rapidproxy.io/?ref=twsc" rel="nofollow">
    <img src="img/rapidproxy-banner.png" alt="RapidProxy Banner" style="max-width: 100%;">
  </a>
</p>

<p>
  <a href="https://www.rapidproxy.io/?ref=twsc" rel="nofollow">RapidProxy</a> provides high-performance residential proxies for Twitter scraping, Selenium automation, and web data extraction.
</p>

<ul>
  <li><strong>🌐 90M+ IPs</strong> — Massive global pool.</li>
  <li><strong>🔄 Smart Rotation</strong> — Seamless IP switching.</li>
  <li><strong>🛡️ Anti-Block</strong> — Bypass strict anti-bot systems.</li>
  <li><strong>⏳ Non-Expiring Traffic</strong> — Use your data at your own pace.</li>
</ul>

<h3>🎁 Special Offer</h3>
<p>
  <strong><a href="https://www.rapidproxy.io/?ref=twsc" rel="nofollow">Try it free</a></strong> — Plans start from just <strong>$0.65/GB</strong>.<br>
  Use coupon code <code>RAPID10</code> at checkout for <strong>10% off</strong>.
</p>
<hr>
<br>

<p>
  <a href="https://www.rapidproxy.io/?ref=twsc" rel="nofollow">
    <img src="img/swiftproxy-banner.png" alt="RapidProxy Banner" style="max-width: 100%;">
  </a>
</p>

<h3>
  <strong><a href="https://www.swiftproxy.net/?ref=shaikhsajid111" rel="nofollow">Swiftproxy</a> — Reliable Residential Proxies for Scraping & Automation</strong>
</h3>

<p>
  <a href="https://www.swiftproxy.net/?ref=shaikhsajid111" rel="nofollow">Swiftproxy</a> offers dependable residential proxy solutions for web scraping, browser automation, and large-scale data collection projects.
</p>

<ul>
  <li><strong>🌐 90M+ residential IPs</strong> — Global coverage across many regions.</li>
  <li><strong>🔒 HTTP(S) & SOCKS5</strong> — Flexible protocol support for real-world scraping.</li>
  <li><strong>📍 Country, region, and city targeting</strong> — Better geo-targeting control.</li>
  <li><strong>⏳ Non-expiring residential proxy traffic</strong> — Use your proxy data at your own pace.</li>
  <li><strong>🧪 Free trial available</strong> — Test performance before scaling.</li>
</ul>

<h3>🎁 Special Offer</h3>
<p>
  <strong><a href="https://www.swiftproxy.net/?ref=shaikhsajid111" rel="nofollow">Get started with Swiftproxy</a></strong> and use code <code>PROXY90</code> for <strong>10% off</strong>.
</p>

<!--TABLE of contents //-->
<br>
<hr>
<h2 id="Prerequisites">Prerequisites </h2>
<li> Internet Connection </li>
<li> Python 3.6+ </li>
<li> Chrome or Firefox browser installed on your machine </li>
<hr>
<h2 id="Installation"> Installation </h2>
<h3 id="sourceInstallation">Installing from the source</h3>
<p>Download the source code or clone it with:<p>

```
git clone https://github.com/shaikhsajid1111/twitter-scraper-selenium
```

<p>Open terminal inside the downloaded folder:</p>

<br>

```
 python3 setup.py install
```

<h3 id="pypiInstallation">
Installing with <a href="https://pypi.org">PyPI</a>
</h3>

```
pip3 install twitter-scraper-selenium
```

<hr>
<h2 id="Usage">
Usage</h2>
<h3 id="availableFunction">Available Function In this Package - Summary</h3>
<div>
<table>
<thead>
<tr>
<td>Function Name</td>
<td>Function Description</td>
<td>Scraping Method</td>
<td>Scraping Speed</td>
</tr>
</thead>
<tr>
<td><code>scrape_profile()</code></td>
<td>Scrape's Twitter user's profile tweets</td>
<td>Browser Automation</td>
<td>Slow</td>
</tr>
<tr>
<td><code>get_profile_details()</code></td>
<td>Scrape's Twitter user details.</td>
<td>HTTP Request</td>
<td>Fast</td>
</tr>
<tr>
<td><code>scrape_profile_with_api()</code></td>
<td>Scrape's Twitter tweets by twitter profile username. It expects the username of the profile</td>
<td>Browser Automation & HTTP Request</td>
<td>Fast</td>
</tr>
<tr>
<td><code>search_tweets_with_xquik()</code></td>
<td>Search public X posts through the Xquik API.</td>
<td>HTTP Request</td>
<td>Fast</td>
</tr>
</table>
<p>
Note: HTTP Request Method sends the request to Twitter's API directly for scraping data, and Browser Automation visits that page, scroll while collecting the data.</p>
</div>
<br>
<hr>
<h3 id="xquik-search">Search X with Xquik</h3>

<p>
Use the optional Xquik helper for authenticated, read-only X search without
launching Selenium. Create an API key, then store it outside your source code:
</p>

```bash
export XQUIK_API_KEY="<your_api_key>"
```

```python
from twitter_scraper_selenium import search_tweets_with_xquik

page = search_tweets_with_xquik(
    "python #opensource",
    tweets_count=25,
    query_type="Latest",
)

for tweet in page["tweets"]:
    print(tweet["text"])

if page.get("has_next_page"):
    next_page = search_tweets_with_xquik(
        "python #opensource",
        tweets_count=25,
        query_type="Latest",
        cursor=page["next_cursor"],
    )
```

<p>
<code>tweets_count</code> accepts 1 to 200 posts per request.
<code>query_type</code> accepts <code>Latest</code> or <code>Top</code>.
Use <code>since_time</code> and <code>until_time</code> for date bounds.
Pass <code>next_cursor</code> back as <code>cursor</code> to continue.
The helper returns the raw JSON response and raises
<code>XquikApiError</code> for authentication, HTTP, network, or response
errors. See the
<a href="https://docs.xquik.com/api-reference/x/search-tweets">Search Tweets API documentation</a>
for response fields and search operators.
</p>

<p>
Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.
</p>

<hr>
<h3 id="profileDetail">To scrape twitter profile details:</h3>
<div id="profileDetailExample">

```python
from twitter_scraper_selenium import get_profile_details

twitter_username = "TwitterAPI"
filename = "twitter_api_data"
browser = "firefox"
headless = True
get_profile_details(twitter_username=twitter_username, filename=filename, browser=browser, headless=headless)

```
Output:
```js
{
	"id": 6253282,
	"id_str": "6253282",
	"name": "Twitter API",
	"screen_name": "TwitterAPI",
	"location": "San Francisco, CA",
	"profile_location": null,
	"description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
	"url": "https:\/\/t.co\/8IkCzCDr19",
	"entities": {
		"url": {
			"urls": [{
				"url": "https:\/\/t.co\/8IkCzCDr19",
				"expanded_url": "https:\/\/developer.twitter.com",
				"display_url": "developer.twitter.com",
				"indices": [
					0,
					23
				]
			}]
		},
		"description": {
			"urls": []
		}
	},
	"protected": false,
	"followers_count": 6133636,
	"friends_count": 12,
	"listed_count": 12936,
	"created_at": "Wed May 23 06:01:13 +0000 2007",
	"favourites_count": 31,
	"utc_offset": null,
	"time_zone": null,
	"geo_enabled": null,
	"verified": true,
	"statuses_count": 3656,
	"lang": null,
	"contributors_enabled": null,
	"is_translator": null,
	"is_translation_enabled": null,
	"profile_background_color": null,
	"profile_background_image_url": null,
	"profile_background_image_url_https": null,
	"profile_background_tile": null,
	"profile_image_url": null,
	"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/942858479592554497\/BbazLO9L_normal.jpg",
	"profile_banner_url": null,
	"profile_link_color": null,
	"profile_sidebar_border_color": null,
	"profile_sidebar_fill_color": null,
	"profile_text_color": null,
	"profile_use_background_image": null,
	"has_extended_profile": null,
	"default_profile": false,
	"default_profile_image": false,
	"following": null,
	"follow_request_sent": null,
	"notifications": null,
	"translator_type": null
}
```
</div>
<br>
<div id="profileDetailArgument">
<p><code>get_profile_details()</code> arguments:</p>

<table>
    <thead>
        <tr>
            <td>Argument</td>
            <td>Argument Type</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>twitter_username</td>
            <td>String</td>
            <td>Twitter Username</td>
        </tr>
        <tr>
            <td>output_filename</td>
            <td>String</td>
            <td>What should be the filename where output is stored?.</td>
        </tr>
        <tr>
            <td>output_dir</td>
            <td>String</td>
            <td>What directory output file should be saved?</td>
        </tr>
        <tr>
            <td>proxy</td>
            <td>String</td>
            <td>Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port.</td>
        </tr>
    </tbody>
</table>

</div>
<hr>
<br>
<div>
<h4 id="profileDetailKeys">Keys of the output:</p>
Detail of each key can be found <a href="https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user">here</a>.</h4>
</div>
<br>
<hr>
<h3 id="profile">To scrape profile's tweets:</h3>
<p id="profileJson">In JSON format:</p>

```python
from twitter_scraper_selenium import scrape_profile

microsoft = scrape_profile(twitter_username="microsoft",output_format="json",browser="firefox",tweets_count=10)
print(microsoft)
```
Output:
```javascript
{
  "1430938749840629773": {
    "tweet_id": "1430938749840629773",
    "username": "Microsoft",
    "name": "Microsoft",
    "profile_picture": "https://twitter.com/Microsoft/photo",
    "replies": 29,
    "retweets": 58,
    "likes": 453,
    "is_retweet": false,
    "retweet_link": "",
    "posted_time": "2021-08-26T17:02:38+00:00",
    "content": "Easy to use and efficient for all \u2013 Windows 11 is committed to an accessible future.\n\nHere's how it empowers everyone to create, connect, and achieve more: https://msft.it/6009X6tbW ",
    "hashtags": [],
    "mentions": [],
    "images": [],
    "videos": [],
    "tweet_url": "https://twitter.com/Microsoft/status/1430938749840629773",
    "link": "https://blogs.windows.com/windowsexperience/2021/07/01/whats-coming-in-windows-11-accessibility/?ocid=FY22_soc_omc_br_tw_Windows_AC"
  },...
}
```
<hr>
<p id="profileCSV">In CSV format:</p>

```python
from twitter_scraper_selenium import scrape_profile


scrape_profile(twitter_username="microsoft",output_format="csv",browser="firefox",tweets_count=10,filename="microsoft",directory="/home/user/Downloads")


```

Output:
<br>
<table class="table table-bordered table-hover table-condensed" style="line-height: 14px;overflow:hidden;white-space: nowrap">
<thead><tr><th title="Field #1">tweet_id</th>
<th title="Field #2">username</th>
<th title="Field #3">name</th>
<th title="Field #4">profile_picture</th>
<th title="Field #5">replies</th>
<th title="Field #6">retweets</th>
<th title="Field #7">likes</th>
<th title="Field #8">is_retweet</th>
<th title="Field #9">retweet_link</th>
<th title="Field #10">posted_time</th>
<th title="Field #11">content</th>
<th title="Field #12">hashtags</th>
<th title="Field #13">mentions</th>
<th title="Field #14">images</th>
<th title="Field #15">videos</th>
<th title="Field #16">post_url</th>
<th title="Field #17">link</th>
</tr></thead>
<tbody><tr>
<td>1430938749840629773</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">64</td>
<td align="right">75</td>
<td align="right">521</td>
<td>False</td>
<td> </td>
<td>2021-08-26T17:02:38+00:00</td>
<td>Easy to use and efficient for all – Windows 11 is committed to an accessible future.<br/><br/>Here&#39;s how it empowers everyone to create, connect, and achieve more: https://msft.it/6009X6tbW </td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430938749840629773</td>
<td>https://blogs.windows.com/windowsexperience/2021/07/01/whats-coming-in-windows-11-accessibility/?ocid=FY22_soc_omc_br_tw_Windows_AC</td>
</tr>

</tbody>
</table>
<p>...</p>

<br><hr>
<div id="profileArgument">
<p><code>scrape_profile()</code> arguments:</p>

<table>
    <thead>
        <tr>
            <td>Argument</td>
            <td>Argument Type</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>twitter_username</td>
            <td>String</td>
            <td>Twitter username of the account</td>
        </tr>
        <tr>
            <td>browser</td>
            <td>String</td>
            <td>Which browser to use for scraping?, Only 2 are supported Chrome and Firefox. Default is set to Firefox</td>
        </tr>
        <tr>
            <td>proxy</td>
            <td>String</td>
            <td>Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port.</td>
        </tr>
        <tr>
            <td>tweets_count</td>
            <td>Integer</td>
            <td>Number of posts to scrape. Default is 10.</td>
        </tr>
        <tr>
            <td>output_format</td>
            <td>String</td>
            <td>The output format, whether JSON or CSV. Default is JSON.</td>
        </tr>
        <tr>
            <td>filename</td>
            <td>String</td>
            <td>If output parameter is set to CSV, then it is necessary for filename parameter to passed. If not passed then the filename will be same as username passed.</td>
        </tr>
        <tr>
            <td>directory</td>
            <td>String</td>
            <td>If output_format parameter is set to CSV, then it is valid for directory parameter to be passed. If not passed then CSV file will be saved in current working directory.</td>
        </tr>
        <tr>
            <td>headless</td>
            <td>Boolean</td>
            <td>Whether to run crawler headlessly?. Default is <code>True</code></td>
        </tr>
    </tbody>
</table>

</div>
<hr>
<br>
<div id="profileOutput">
<p>Keys of the output</p>

<table>
    <thead>
        <tr>
            <td>Key</td>
            <td>Type</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>tweet_id</td>
            <td>String</td>
            <td>Post Identifier(integer casted inside string)</td>
        </tr>
        <tr>
            <td>username</td>
            <td>String</td>
            <td>Username of the profile</td>
        </tr>
        <tr>
            <td>name</td>
            <td>String</td>
            <td>Name of the profile</td>
        </tr>
        <tr>
            <td>profile_picture</td>
            <td>String</td>
            <td>Profile Picture link</td>
        </tr>
        <tr>
            <td>replies</td>
            <td>Integer</td>
            <td>Number of replies of tweet</td>
        </tr>
        <tr>
            <td>retweets</td>
            <td>Integer</td>
            <td>Number of retweets of tweet</td>
        </tr>
        <tr>
            <td>likes</td>
            <td>Integer</td>
            <td>Number of likes of tweet</td>
        </tr>
        <tr>
            <td>is_retweet</td>
            <td>boolean</td>
            <td>Is the tweet a retweet?</td>
        </tr>
        <tr>
            <td>retweet_link</td>
            <td>String</td>
            <td>If it is retweet, then the retweet link else it'll be empty string</td>
        </tr>
        <tr>
            <td>posted_time</td>
            <td>String</td>
            <td>Time when tweet was posted in ISO 8601 format</td>
        </tr>
        <tr>
            <td>content</td>
            <td>String</td>
            <td>content of tweet as text</td>
        </tr>
        <tr>
            <td>hashtags</td>
            <td>Array</td>
            <td>Hashtags presents in tweet, if they're present in tweet</td>
        </tr>
        <tr>
            <td>mentions</td>
            <td>Array</td>
            <td>Mentions presents in tweet, if they're present in tweet</td>
        </tr>
        <tr>
            <td>images</td>
            <td>Array</td>
            <td>Images links, if they're present in tweet</td>
        </tr>
        <tr>
            <td>videos</td>
            <td>Array</td>
            <td>Videos links, if they're present in tweet</td>
        </tr>
        <tr>
            <td>tweet_url</td>
            <td>String</td>
            <td>URL of the tweet</td>
        </tr>
        <tr>
            <td>link</td>
            <td>String</td>
            <td>If any link is present inside tweet for some external website. </td>
        </tr>
    </tbody>
</table>
</div>
<br>
<hr>
<div id="to-scrape-user-tweets-with-api">

<p>To Scrap profile's tweets with API:</p>

```python
from twitter_scraper_selenium import scrape_profile_with_api

scrape_profile_with_api('elonmusk', output_filename='musk', tweets_count= 100)
```
</div>
<br>
<div id="users_api_parameter">
<p><code>scrape_profile_with_api()</code> Arguments:<p>
<table>
    <thead>
        <tr>
            <td>Argument</td>
            <td>Argument Type</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>username</td>
            <td>String</td>
            <td>Twitter's Profile username</td>
        </tr>
        <tr>
            <td>tweets_count</td>
            <td>Integer</td>
            <td>Number of tweets to scrape.</td>
        </tr>
        <tr>
            <td>output_filename</td>
            <td>String</td>
            <td>What should be the filename where output is stored?.</td>
        </tr>
        <tr>
            <td>output_dir</td>
            <td>String</td>
            <td>What directory output file should be saved?</td>
        </tr>
        <tr>
            <td>proxy</td>
            <td>String</td>
            <td>Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port.</td>
        </tr>
        <tr>
            <td>browser</td>
            <td>String</td>
            <td>Which browser to use for extracting out graphql key. Default is firefox.</td>
        </tr>
        <tr>
            <td>headless</td>
            <td>String</td>
            <td>Whether to run browser in headless mode?</td>
        </tr>
    </tbody>
</table>
</div>
<br>
<div id="scrape_user_with_api_args_keys"> <p>Output:<p>

```js
{
  "1608939190548598784": {
    "tweet_url" : "https://twitter.com/elonmusk/status/1608939190548598784",
    "tweet_details":{
      ...
    },
    "user_details":{
      ...
    }
  }, ...
}
```

</div>
<br>
<hr>
</div>

<h3 id="proxy"> Using scraper with proxy (http proxy) </h3>

<div id="unauthenticatedProxy">
<p>Just pass <code>proxy</code> argument to function.</p>

```python
from twitter_scraper_selenium import scrape_profile

scrape_profile("elonmusk", headless=False, proxy="66.115.38.247:5678", output_format="csv",filename="musk") #In IP:PORT format

```
</div>

<br>
<div id="authenticatedProxy">
<p> Proxy that requires authentication: </p>

```python

from twitter_scraper_selenium import scrape_profile

microsoft_data = scrape_profile(twitter_username="microsoft", browser="chrome", tweets_count=10, output="json",
                      proxy="sajid:pass123@66.115.38.247:5678")  #  username:password@IP:PORT
print(microsoft_data)


```

</div>
<br>
<hr>
<div id="privacy">
<h2>Privacy</h2>

<p>
This scraper only scrapes public data available to unauthenticated user and does not holds the capability to scrape anything private.
</p>
</div>
<br>
<hr>
<div id="license">
<h2>LICENSE</h2>

MIT
</div>
