# tweets-research-py

## Disclaimer
I joined a data science lab my freshman year for 3 months over the summer. The following is just a brief showcase of what I have done and what I have worked with. My experience and my skills are on a completely different at the moment, and I probably wouldn't have done some of the things the way they are presented here.

## What I did
- Analyzed 12GB+ large datasets obtained from government websites, Twitter API, and other sources in JSON format using
Python, R, and other tools for law and media related research publications, such as the one sent to 22nd ACM Conference
on Computer-Supported Cooperative Work and Social Computing
- Applied complex mathematical solutions, such as statistical analysis (MS Excel), network analysis (NetworkX in Python),
and topic modelling (Mallet in Java) to provide data models for professors from universities in Canada and the US
- Led a small group of researchers to guide through Python programming language and API structure for the research

## Other details
More specifically, I was mainly working on Twitter API data, since the goal of the research was to find out patterns and interesting nuances about the usage of emojis in White Nationalist Communication on Twitter. This is why I took all of raw data (12+ GB of raw Twitter API raw dat) that other researches in Canada collected on their servers.

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

Then I created what was called "emoji clouds" for a better representation of frequency and usage of emojis. I tried to create my own Python package for this purpose, however, I ended up using existing software to speed up the process:

<p align="center">
  <img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/emoji-clouds.jpg">
</p>

Finally, I was intending to finish the project my creating emoji networks to represent the complex relationships between various twitter users. I took all the emojis from each tweet, and then composed a file of all permutations of the emojis across all tweets. For the graph to be somewhat successfull, I needed to have edges and weights to the edges for the graph. The edge looked like this: ('🧕', '🤔', 1). The first and second are supposed to be the emojis considered, and the third is the number, which represented the weight of the edge (or frequency, in my case).

The unicode characters and Windows fonts were not properly configured on that machine (I was doing it on a lab machine that had Windows 7 installed). Therefore, the screenshots of my emoji network are a bit ugly.

<table width="100%" border="0">
  <tr>    
  <td><img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet1.png" alt="" align="left" /></td>
  <td><img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet2.png" alt="" align="center" /></td>
  <td><img src="https://github.com/alisnichenko/research-summer2019/blob/master/media/network-snippet3.png" alt="" align="right"/></td>
  </tr>
</table>

I later found out about the possible solution (to make it look somewhat acceptable and readable), which could be just one single `import mplcairo` and it would import specific fonts for the emojis to display properly with `matplotlib` on Windows 7, however it was the end of summer when I found this little trick.


