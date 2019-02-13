# Dark Pool Buying
Calculates estimate of dark pool buying index ("DIX") based on publicly available data from the NYSE, NASDAQ, and OTC Reporting Facility ("ORF") exchanges. Concept courtesy of Squeeze Metrics whitepaper here: https://squeezemetrics.com/monitor/download/pdf/short_is_long.pdf?

Dependencies: pandas, numpy, tqdm

2017-2019 YTD data with exponential moving averages shown below. Note that a long downtrend in dark pool buying preceded the February 2018 S&P 500 sell-off. 

![Dark Pool Buying Index](dpi.png)
