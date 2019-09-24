# research-summer2019

Since it was my first research opportinity ever, I decided to try it out for May-Aug period during Summer 2019.

Basically, my responsibilities and my activities included:
- Analyzed 12GB+ large datasets obtained from government websites, Twitter API, and other sources in JSON format using
Python, R, and other tools for law and media related research publications, such as the one sent to 22nd ACM Conference
on Computer-Supported Cooperative Work and Social Computing
- Applied complex mathematical solutions, such as statistical analysis (MS Excel), network analysis (NetworkX in Python),
and topic modelling (Mallet in Java) to provide data models for professors from universities in Canada and the US
- Led a small group of researchers to guide through Python programming language and API structure for the research

More specifically, I was mainly working on Twitter API data, since the goal of the research was to find out patterns and interesting nuances about the usage of emojis in White Nationalist Communication on Twitter. This is why I took all of raw data (12+ GB of raw Twitter API .json files) that other researches in Canada collected on their servers.

One of the examples of such file:

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/json-example1.jpg">
</p>

Or, a bit prettier than the previous one:

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/json-example2.jpg">
</p>

As you can see, there is a lot of emojis, so I wrote an ugly (but working) Python script, that goes through each hashtag (files with user data were separated by hashtag, i.e. ideological twitter movements, such as white supremacy, anti-white, etc). The script extracts all the emojis using regex, and then composes a .csv or .xlsx .json, depending on the need, table with most frequent emojis, separated by stance and ideology.

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/emoji-json.jpg">
</p>

Then I did this:

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/emoji-clouds.jpg">
</p>

The next thing was my network analysis, which wasn't very successful due to the fact that I had a computer with Windows 7 installed on it.

What I did with my previously parsed Twitter data, is that I took all the emojis from each tweet, and then composed a file of all permutations of the emojis across all tweets. The edge looked like this: ('🧕', '🤔', 1). The first and second are supposed to be the emojis considered, and the third is the number, which represented the weight of the edge (or frequency, in my case).

The unicode characters and Windows fonts were not properly configured on that machine. Therefore, the screenshots of my emoji network are a bit ugly.

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet1.jpg">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet2.jpg">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet3.jpg">
</p>


