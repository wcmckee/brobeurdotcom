<html><body><p>I've continued to work on my image script, this time focusing more into creating rectangle and text.


I really want to create a television show in a game format. Doing the whole black bars the top and bottom of the screen really excites me. Text and color is also up there.



I added a creation of rectangle to the script - one at the top, and another at the bottom.



[prettify=python]



from PIL import ImageDraw

draw.rectangle([(0, 0), (1920, 150)], fill='black')

draw = ImageDraw.Draw(lightFilz)

draw.rectangle([(0, 500), (1920, 1080)], fill='black')

[/prettify]



I have also added text.



[prettify=python]



import ImageFont, ImageDraw



import random

cRan = random.randint(1,30)

draw = ImageDraw.Draw(lightFilz)

# use a truetype font

font = ImageFont.truetype("cs.ttf", 24)

draw.text((100, 200), "a film by William Mckee", fill=(49,cRan,2),font=font)

draw.text((400, 300), 'Suburb Nightmare: Mist City', fill =(49,3,cRan),font=font)

draw.text((600, 400), 'sound by blah blah', fill=(cRan,3,2), font=font)

[/prettify]



Here's some results:



<a href="/wp-content/uploads/2013/12/street0303.jpg"><img class="alignnone size-large wp-image-602" alt="street0303" src="/wp-content/uploads/2013/12/street0303-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0390.jpg"><img class="alignnone size-large wp-image-603" alt="street0390" src="/wp-content/uploads/2013/12/street0390-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0425.jpg"><img class="alignnone size-large wp-image-604" alt="street0425" src="/wp-content/uploads/2013/12/street0425-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0682.jpg"><img class="alignnone size-large wp-image-605" alt="street0682" src="/wp-content/uploads/2013/12/street0682-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0736.jpg"><img class="alignnone size-large wp-image-606" alt="street0736" src="/wp-content/uploads/2013/12/street0736-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0845.jpg"><img class="alignnone size-large wp-image-607" alt="street0845" src="/wp-content/uploads/2013/12/street0845-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street0853.jpg"><img class="alignnone size-large wp-image-608" alt="street0853" src="/wp-content/uploads/2013/12/street0853-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street1360.jpg"><img class="alignnone size-large wp-image-609" alt="street1360" src="/wp-content/uploads/2013/12/street1360-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street1984.jpg"><img class="alignnone size-large wp-image-610" alt="street1984" src="/wp-content/uploads/2013/12/street1984-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street2537.jpg"><img class="alignnone size-large wp-image-611" alt="street2537" src="/wp-content/uploads/2013/12/street2537-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street2891.jpg"><img class="alignnone size-large wp-image-612" alt="street2891" src="/wp-content/uploads/2013/12/street2891-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street2895.jpg"><img class="alignnone size-large wp-image-613" alt="street2895" src="/wp-content/uploads/2013/12/street2895-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street2965.jpg"><img class="alignnone size-large wp-image-614" alt="street2965" src="/wp-content/uploads/2013/12/street2965-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street3204.jpg"><img class="alignnone size-large wp-image-615" alt="street3204" src="/wp-content/uploads/2013/12/street3204-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street3844.jpg"><img class="alignnone size-large wp-image-616" alt="street3844" src="/wp-content/uploads/2013/12/street3844-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street3941.jpg"><img class="alignnone size-large wp-image-617" alt="street3941" src="/wp-content/uploads/2013/12/street3941-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street4825.jpg"><img class="alignnone size-large wp-image-618" alt="street4825" src="/wp-content/uploads/2013/12/street4825-1024x576.jpg" width="1024" height="576"></a> <a href="/wp-content/uploads/2013/12/street4871.jpg"><img class="alignnone size-large wp-image-619" alt="street4871" src="/wp-content/uploads/2013/12/street4871-1024x576.jpg" width="1024" height="576"></a></p></body></html>