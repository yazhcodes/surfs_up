# OVERVIEW

This project is about analyzing Oahu's annual temperature and precipitation data, sourced from nine weather stations, to determine whether it has ideal weather conditions to support a Surf and Icecream Shop business. This Challenge in particular is a deep dive into the June and December statistics, to test Oahu's year round sustainability.

# RESULTS

* There are **1700 recordings** available for June month which is _11% more_ than Decemeber's data. So we begin the analysis with an understanding that it IS possible June's stats could be a bit more accurate than December's.
* The **average temperature** of June and December is recorded as _74.9° and 71.04°_ respectively. December being colder than June does not come as a surprise, and this also proves that our analysis is infact going on the right track.
* The **standard deviation** of December is _3.74_ which is slightly higher than June's standard deviation of _3.25_. It's no biggie though!
* The **minimum recorded temperatures** of June and December are far apart at _64° and 56°_, however the **maximum recorded temperatures** turned out much closer than we anticipated at _85° and 83°_ respectively.

<p align='center'>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Jun_Temp.png" width="160" height="300"></img>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Dec_Temp.png" width="200" height="300"></img>
</p>

# SUMMARY

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December.

* The _**outcome of Temperature analysis is quite reassuring**_ to our client who is nervous and excited to open up his Surf and Icecream shop in Oahu. However, our report would be half cooked if we solely relied on temperature and did not include more parameters that are readily available to us. Let's take a deeper dive.
* **Additional Analysis 1:** Including Precipitation
  *  The average recorded precipitation for June and December is 0.13 and 0.21 respectively and 75% of the data fall below 0.12 and 0.15. Although the maximum precipitation is 4.43 and 6.42, we may rest assured that the rainy days are rare in Oahu and it would not be a major deal breaker!

<p align='center'>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Jun_Temp_Prcp.png" width="330" height="300"></img>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Dec_Temp_Prcp.png" width="380" height="300"></img>
</p>

* **Additional Analysis 2:** Station wise averages
  * Finally before submitting our report, it is better to check the station wise averages to rule out any suspiciously high or low recordings. The below chart clarifies any doubt because the average temperatures and precipitation recorded by each station is higher or lower than the overall averages only by a few units which is not daringly significant enough to pull the plug on our client's dream.

<p align='center'>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Jun_Station_Avgs.png" width="400" height="340"></img>
  <img src="https://github.com/yazhcodes/surfs_up/blob/main/Resources/Images/Dec_Station_Avgs.png" width="460" height="340"></img>
</p>
