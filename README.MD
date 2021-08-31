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


scrap_profile(twitter_username="microsoft",output="csv",browser="firefox",tweets_count=10,filename="microsoft",directory="/home/user/Downloads")


```

Output:
<br>
<table class="table table-bordered table-hover table-condensed">
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
<tr>
<td>1430928787823374336</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">68</td>
<td align="right">321</td>
<td align="right">3287</td>
<td>False</td>
<td> </td>
<td>2021-08-26T16:23:03+00:00</td>
<td>The Art        The Artist</td>
<td>[]</td>
<td>[]</td>
<td>[&#39;https://pbs.twimg.com/media/E9uuJHMXMAw38W3?format=jpg&amp;name=360x360&#39;, &#39;https://pbs.twimg.com/media/E9uuJepWQAM3cYS?format=jpg&amp;name=360x360&#39;]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430928787823374336</td>
<td> </td>
</tr>
<tr>
<td>1430646543376289793</td>
<td>satyanadella</td>
<td>Satya Nadella</td>
<td>https://twitter.com/satyanadella/photo</td>
<td align="right">113</td>
<td align="right">605</td>
<td align="right">3385</td>
<td>True</td>
<td>https://twitter.com/satyanadella/status/1430646543376289793</td>
<td>2021-08-25T21:41:30+00:00</td>
<td>Thank you <br/>@POTUS<br/> for convening a critical conversation on cybersecurity. Microsoft will invest $20 billion to advance our security solutions over the next 5 years, $150 million to help US government agencies upgrade protections, and expand our cybersecurity training partnerships.</td>
<td>[]</td>
<td>[&#39;POTUS&#39;]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/satyanadella/status/1430646543376289793</td>
<td> </td>
</tr>
<tr>
<td>1430658746666078214</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">13</td>
<td align="right">39</td>
<td align="right">153</td>
<td>False</td>
<td> </td>
<td>2021-08-25T22:30:00+00:00</td>
<td>What does a more equitable future with technology look like, and will it include everyone? <br/><br/>Scholars discuss how race and tech affect one another in this series from Microsoft Research: https://msft.it/6008nhd8p</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430658746666078214</td>
<td>https://www.microsoft.com/en-us/research/blog/lecture-series-aims-to-help-spur-dialogue-around-race-and-technology/?ocid=FY22_soc_omc_br_tw_Lecture_series</td>
</tr>
<tr>
<td>1430636863132520457</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">23</td>
<td align="right">50</td>
<td align="right">460</td>
<td>False</td>
<td> </td>
<td>2021-08-25T21:03:02+00:00</td>
<td>Coming soon to Microsoft 365:</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430636863132520457</td>
<td>https://t.co/NW4eIBwgFd?amp=1</td>
</tr>
<tr>
<td>1430636860909527050</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">45</td>
<td align="right">139</td>
<td align="right">1847</td>
<td>False</td>
<td> </td>
<td>2021-08-25T21:03:02+00:00</td>
<td>Sharing a little love in your feed, courtesy of our redesigned red heart emoji.</td>
<td>[]</td>
<td>[]</td>
<td>[&#39;https://pbs.twimg.com/media/E9qko6GWEAQ2i-R?format=jpg&amp;name=360x360&#39;, &#39;https://pbs.twimg.com/media/E9qkpHfXMAcA-oM?format=jpg&amp;name=360x360&#39;]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430636860909527050</td>
<td> </td>
</tr>
<tr>
<td>1430518133341708289</td>
<td>SpecialOlympics</td>
<td>Special Olympics</td>
<td>https://twitter.com/SpecialOlympics/photo</td>
<td align="right">3</td>
<td align="right">32</td>
<td align="right">96</td>
<td>True</td>
<td>https://twitter.com/SpecialOlympics/status/1430518133341708289</td>
<td>2021-08-25T13:11:15+00:00</td>
<td>Thank you <br/>@DBLTAPesports<br/> for featuring September&#39;s first-ever <br/>@SpecialOlympics<br/> #GamingForInclusion event in partnership with <br/>@Microsoft</td>
<td>[&#39;GamingForInclusion&#39;]</td>
<td>[&#39;DBLTAPesports&#39;, &#39;SpecialOlympics&#39;, &#39;Microsoft&#39;]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/SpecialOlympics/status/1430518133341708289</td>
<td>https://t.co/KC7EtQx2G8?amp=1</td>
</tr>
<tr>
<td>1430608919127285760</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">389</td>
<td align="right">944</td>
<td align="right">6217</td>
<td>False</td>
<td> </td>
<td>2021-08-25T19:12:00+00:00</td>
<td>CTRL CCCCCCCCCCCCCCCCCCC<br/><br/>CTRL V</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430608919127285760</td>
<td> </td>
</tr>
<tr>
<td>1430590803441852417</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">3</td>
<td align="right">28</td>
<td align="right">136</td>
<td>False</td>
<td> </td>
<td>2021-08-25T18:00:01+00:00</td>
<td>Here&#39;s where to find us: https://msft.it/6003nhjZF </td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Microsoft/status/1430590803441852417</td>
<td>https://news.microsoft.com/europe/features/cigarette-butts-are-poisoning-shoreline-animals-this-beach-rover-may-help-clean-all-that-up/?ocid=FY22_soc_omc_br_tw_Beach_botFS</td>
</tr>
<tr>
<td>1430588315477192708</td>
<td>Microsoft</td>
<td>Microsoft</td>
<td>https://twitter.com/Microsoft/photo</td>
<td align="right">54</td>
<td align="right">70</td>
<td align="right">642</td>
<td>False</td>
<td> </td>
<td>2021-08-25T17:50:08+00:00</td>
<td>We&#39;re using Microsoft Flight simulator to fly us to different places around the world. <br/><br/>Any guesses on where we are? </td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[&#39;https://video.twimg.com/tweet_video/E9p4d5WWUAgv7Mz.mp4&#39;]</td>
<td>https://twitter.com/Microsoft/status/1430588315477192708</td>
<td> </td>
</tr>
</tbody></table>