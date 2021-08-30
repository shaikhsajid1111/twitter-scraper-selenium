<h1> Twitter scraper selenium </h1>
<p> Python package to scrap twitter's front-end easily with selenium </p>

<!--TABLE of contents-->
<h2> Table of Contents </h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
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
    <ul>
    <li><a href="#profile">Scraping profile's tweets</a>
    <ul>
    <li><a href="#profileJson">In JSON format</a></li>
    <li><a href="#profileCSV">In CSV format</a></li>
    <li><a href="">Keys of the output data</a></li>
    </ul>
    <li><a href="">Scraping tweets using keywords</a>
    <ul>
    <li><a href="">In JSON format</a></li>
    <li><a href="">In CSV format</a></li>
    <li><a href="">Keys of the output data</a></li>
    </ul>
    </li>
    <li><a href="">Using scraper with proxy</a>
    <ul>
    <li><a>Unauthenticated Proxy</a></li>
    <li><a>Authenticated Proxy</a></li>
    </ul>
    </li>
    </li>
    </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!--TABLE of contents //-->

<h2 id="Prerequisites">Prerequisites </h2>
<li> Internet Connection </li>
<li> Python 3.6+ </li>
<li> Chrome or Firefox browser installed on your machine </li>
<hr>
<h2 id="Installation"> Installation </h2>
<h3 id="sourceInstallation">Installing from the source</h3>
<p>Download the source code or clone it with:<p>

```
git clone https://github.com/shaikhsajid1111/twitter_scraper_selenium
```

<p>Open terminal inside the downloaded folder:</p>

<br>

```
 python3 setup.py install
```

<h3 id="pypiInstallation">
Installing with <a href="https://pypi.org">PyPI</a>
</h3>

<code>pip3 install twitter-scraper-selenium</code>
<hr>
<h2 id="Usage">
Usage</h2>

<h3>To scrap profile's tweets:</h3>
<p id="profileJson">In JSON format:</p>

```python
from twitter_scraper_selenium import scrap_profile

microsoft = scrap_profile(twitter_username="microsoft",output="json",browser="firefox",posts_count=10)
print(microsoft)
```
Output:
```javascript
{
  "1430938749840629773": {
    "post_id": "1430938749840629773",
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
<p id="profileCSV">In CSV format:</p>

```python
from twitter_scraper_selenium import scrap_profile

twitter_username = "microsoft"
browser = "firefox" #chrome can also be used
output_format = "csv"
tweets_count = 10 #number of tweets to scrap
filename = "microsoft_output"
directory_to_save_csv = "/home/user/Downloads"

scrap_profile(twitter_username=twitter_username,output=output_format,browser=browser,tweets_count=tweets_count,filename=filename,directory=directory_to_save_csv)

```

Output:
<br>
<a href="https://ibb.co/rt7KK1J"><img src="https://i.ibb.co/z5nWW0w/MS-SS.jpg" alt="MS-SS" border="0"></a>