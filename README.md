# Safest-Route-Prediction-in-Urban-Areas
This is the big data project by Gabriel Maliakal (gtm2122) and Anubha Bhargava (ab3955). 


First run em1.py This will download the latest crime alerts from emails given by spotcrime.com
Then run csvread.py This will add all the coordinates in a single file

After that run GMM.py This will form a gaussian mixture model of four clusters. The mean, variance and weight will be stored in GMM.txt

Finally run check.py this will get the waypoint coordinates.

Finally run plot_route.html and enter the coordinates of origin and destination, the "safest route" will be plot along with walking directions.

