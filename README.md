# Website Translator
 This Project contains all the websites converted from English to Hindi from the base url - www.classcentral.com.

#**Scraping** :

For this project first I tried using HTTrack to scrape the website,
but it's throwing an error I am able to scrape some other websites using
HTTrack but not this one, and I tried other scraping apps but most 
of them failed, I think that it's the website which is not allowing 
to scrape. Finally I found an app called "Webcopy" which scraped most 
of the data but it doesn't have the feature to include javascript.
It's the only option available so I proceeded.
When I scraped for 1 level deep as instructed I found more than 300 html 
files and it took me 7 hours to scrape all the files using Cyotek Webcopy.

#**Language Translation :**

After the scraping is done I wrote the code in Python Language, 
I used the "Beautifulsoup" library to extract html code from the files 
and identify the "text" in each of them.
Then I used "googletrans" library to translate all the text from English
to Hindi. 
Finally, I replaced the translated Hindi text in every html file.
Since it is a python module and should translate each tag's text one by
one it took 12 hours on an "i5" Laptop with SSD installed.

#**Problem Faced:**

As I mentioned above, since the Webcopy app didn't have the feature to
scrape javascript, all the images are blurred in the final website.
Except that all other features are working fine. 

#**To make it faster :**

According to my knowledge, if we try to scrape other website, HTTrack would
work well and does the work in less time. It would even include all the pictures
without making them blur.
To make the Translation faster we can take an account in Google Cloud Api
and avail the paid service to translate bulk data faster. 

Within the given time, I could do this much, Hoping to hear your feedback.
I explained everything because I need you to know what process I followed.
Thank you for your time.
