# Safest-Route-Prediction-in-Urban-Areas

This code is for the Advanced Big Data Analytics Course at Columbia University. The following scripts are designed to help the user find the safest walking route in New York City. It is designed for those who are unfamiliar with NYC or uncomfortable walking in the city at night. The project displays the safest walking route on a map and provides the directions to the user. This project was designed using NYC historical crime data and a constantly updating police news feed from spotcrime.com.

The algorithm works as follows:
1. The user enters the origin and destination.
2. Load the historical crime datasets and spotcrime.com data.
3. Get a circle around the origin and destination to limit the data to that area.
4. Gathers all locations of the stores open for 24 hours within the area using the Yelp API.
5. Use Gaussian Mixture Modelling to fit the crime locations between the origin and destination.
6. Use the mixed Gaussian Multivariate Distribution on the locations of the 24 hour shops to find the safest walking path.
7. Use these locations as waypoints to plot the route in Google Maps and provide walking directions.
8. Plot the crime data using a visualization plot on Google.

To run the script:
1. Run em1.py. This will download the latest crime alerts from spotcrime.com.
2. Run csvread.py. This will create a file of all the crime coordinates.
3. Run GMM.py. This will form a Gaussian Mixture Model of four clusters. The mean, variance and weight will be stored within the file GMM.txt.
4. Run check.py to get the waypoint coordinates of the path.
5. Lastly, run plot_route.html and enter the coordinates of the origin and destination. This will plot the safest route along with walking directions.

This project was created by:
* Gabriel Maliakal
* Anubha Bhargava
