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
    <li><a href="#profileOutput">Keys of the output data</a></li>
    </ul>
    <li><a href="#keyword">Scraping tweets using keywords</a>
    <ul>
    <li><a href="#keywordJson">In JSON format</a></li>
    <li><a href="#keywordCSV">In CSV format</a></li>
    <li><a href="#keywordOutput">Keys of the output data</a></li>
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

<h3 id="profile">To scrap profile's tweets:</h3>
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
from twitter_scraper_selenium import scrap_profile


scrap_profile(twitter_username="microsoft",output="csv",browser="firefox",tweets_count=10,filename="microsoft",directory="/home/user/Downloads")


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
<h3 id="keyword">To scrap tweets using keywords:</h3>

<div>
<p id="keywordJson">In JSON format:</p>

```python
from twitter_scraper_selenium import scrap_keyword
#scrap 10 posts by searching keyword "india" from date 30th August till date 31st August
india = scrap_keyword(keyword="india", browser="firefox",
                      tweets_count=10, until="2021-08-31", since="2021-08-30")
print(india)

```
Output:
```javascript
{
  "1432493306152243200": {
    "tweet_id": "1432493306152243200",
    "username": "TOICitiesNews",
    "name": "TOI Cities",
    "profile_picture": "https://twitter.com/TOICitiesNews/photo",
    "replies": 0,
    "retweets": 0,
    "likes": 0,
    "is_retweet": false,
    "posted_time": "2021-08-30T23:59:53+00:00",
    "content": "Paralympians rake in medals, India Inc showers them with rewards",
    "hashtags": [],
    "mentions": [],
    "images": [],
    "videos": [],
    "tweet_url": "https://twitter.com/TOICitiesNews/status/1432493306152243200",
    "link": "https://t.co/odmappLovL?amp=1"
  },...
}
```
</div>
<br>
<hr>
<div id="keywordCSV">
<p>In CSV format:</p>

```python
from twitter_scraper_selenium import scrap_keyword

scrap_keyword(keyword="india", browser="firefox",
                      tweets_count=10, until="2021-08-31", since="2021-08-30",output="csv",filename="india")
```
<br>
Output:
<table class="table table-bordered table-hover table-condensed" style="line-height: 14px;overflow:hidden;white-space: nowrap">
<thead><tr><th title="Field #1">tweet_id</th>
<th title="Field #2">username</th>
<th title="Field #3">name</th>
<th title="Field #4">profile_picture</th>
<th title="Field #5">replies</th>
<th title="Field #6">retweets</th>
<th title="Field #7">likes</th>
<th title="Field #8">is_retweet</th>
<th title="Field #9">posted_time</th>
<th title="Field #10">content</th>
<th title="Field #11">hashtags</th>
<th title="Field #12">mentions</th>
<th title="Field #13">images</th>
<th title="Field #14">videos</th>
<th title="Field #15">tweet_url</th>
<th title="Field #16">link</th>
</tr></thead>
<tbody><tr>
<td>1432493328822464515</td>
<td>SUDEBBI88994521</td>
<td>S.B# #INDIACalcutta</td>
<td>https://twitter.com/SUDEBBI88994521/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>True</td>
<td>2021-08-30T23:59:58+00:00</td>
<td>Lovely</td>
<td>[]</td>
<td>[]</td>
<td>[&#39;https://pbs.twimg.com/media/E98efytVcAYs1ug?format=jpg&amp;name=small&#39;]</td>
<td>[]</td>
<td>https://twitter.com/SUDEBBI88994521/status/1432493328822464515</td>
<td> </td>
</tr>
<tr>
<td>1432493306152243200</td>
<td>TOICitiesNews</td>
<td>TOI Cities</td>
<td>https://twitter.com/TOICitiesNews/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>False</td>
<td>2021-08-30T23:59:53+00:00</td>
<td>Paralympians rake in medals, India Inc showers them with rewards</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/TOICitiesNews/status/1432493306152243200</td>
<td>https://t.co/odmappLovL?amp=1</td>
</tr>
<tr>
<td>1432493299026309120</td>
<td>IndieBombDotCom</td>
<td>SCULPT STAR, India, PA-C</td>
<td>https://twitter.com/IndieBombDotCom/photo</td>
<td>0</td>
<td align="right">1</td>
<td align="right">0</td>
<td>True</td>
<td>2021-08-30T23:59:51+00:00</td>
<td>Why didn’t I think of this?!</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/IndieBombDotCom/status/1432493299026309120</td>
<td> </td>
</tr>
<tr>
<td>1432493290323075075</td>
<td>aryavansh108</td>
<td>V N ARYA</td>
<td>https://twitter.com/aryavansh108/photo</td>
<td>1</td>
<td align="right">0</td>
<td align="right">0</td>
<td>False</td>
<td>2021-08-30T23:59:49+00:00</td>
<td>The madness of a futile war.<br/><br/>The Yanks after 20 years did little.<br/><br/>Sabre rattling will make India poorer.<br/><br/>Protect our porous borders 1st.</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/aryavansh108/status/1432493290323075075</td>
<td> </td>
</tr>
<tr>
<td>1432493284853645315</td>
<td>surensinghsahni</td>
<td>suren singh sahni</td>
<td>https://twitter.com/surensinghsahni/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>False</td>
<td>2021-08-30T23:59:48+00:00</td>
<td>Statistics are not reliable in India and not all Covid sufferers were tested</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/surensinghsahni/status/1432493284853645315</td>
<td> </td>
</tr>
<tr>
<td>1432493271054381061</td>
<td>INDBureaucracy</td>
<td>Indian Bureaucracy</td>
<td>https://twitter.com/INDBureaucracy/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">1</td>
<td>False</td>
<td>2021-08-30T23:59:44+00:00</td>
<td>Justice Pamidighantam Sri Narasimha appointed as Judge- Supreme Court of India - https://indianbureaucracy.com/justice-pamidighantam-sri-narasimha-appointed-as-judge-supreme-court-of-india/…</td>
<td>[]</td>
<td>[]</td>
<td>[&#39;https://pbs.twimg.com/media/E-E9Ce4VIAIEeLh?format=jpg&amp;name=360x360&#39;]</td>
<td>[]</td>
<td>https://twitter.com/INDBureaucracy/status/1432493271054381061</td>
<td> </td>
</tr>
<tr>
<td>1432493269150310401</td>
<td>KajalBanait2</td>
<td>Kajal Banait</td>
<td>https://twitter.com/KajalBanait2/photo</td>
<td>0</td>
<td align="right">4</td>
<td align="right">6</td>
<td>False</td>
<td>2021-08-30T23:59:44+00:00</td>
<td>Saint Rampal ji maharaj is Tatvdarshi guru who is present in Haryana, India.</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/KajalBanait2/status/1432493269150310401</td>
<td> </td>
</tr>
<tr>
<td>1432493262728740865</td>
<td>While_NEWS</td>
<td>While NEWS</td>
<td>https://twitter.com/While_NEWS/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>False</td>
<td>2021-08-30T23:59:42+00:00</td>
<td>Oppose co-ed policy: Jamiat to non-Muslims | India News – Times of India</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/While_NEWS/status/1432493262728740865</td>
<td>https://t.co/bUDgK8uq4h?amp=1</td>
</tr>
<tr>
<td>1432493262447816704</td>
<td>Adda4N</td>
<td>Adda4News</td>
<td>https://twitter.com/Adda4N/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>False</td>
<td>2021-08-30T23:59:42+00:00</td>
<td>realme: Realme Pad with MediaTek chipset, 4GB RAM could start shortly - Times of India</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/Adda4N/status/1432493262447816704</td>
<td>https://t.co/1fnKHQTIoa?amp=1</td>
</tr>
<tr>
<td>1432493245519613952</td>
<td>india_guache</td>
<td>𝗞 𝗔 𝗟 𝗜</td>
<td>https://twitter.com/india_guache/photo</td>
<td>0</td>
<td align="right">0</td>
<td align="right">0</td>
<td>True</td>
<td>2021-08-30T23:59:38+00:00</td>
<td>Que gonorrea, re si, confirmo JAJAJAJAJAJA</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>[]</td>
<td>https://twitter.com/india_guache/status/1432493245519613952</td>
<td> </td>
</tr>
</tbody></table>

</div>
<br>
<hr>
<div id="keywordOutput">
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