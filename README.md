# Baseball Pitch Identifier

The Baseball Pitch Identifier is a program that uses a machine learning algorithm to predict the type of a pitch given a few input parameters (velocity, spin rate, and horizontal and vertical break). The current build uses the Random Forest Classifier. The dataset contains the average of the aforementioned parameters recorded for a specific pitch type from a specific pitcher in a given year from 2016-2022 and 2023 up to July 26. The data was retrieved from Baseball Savant. This program is useful for determining the type of a pitch when tagging it in Trackman, for people new to reading pitch data, or for anyone who finds the data for a given pitch ambiguous. The program outputs the predicted class probabilities for each pitch type so you can see which pitch types most likely match the input and its ambiguity. 

These scatter plots show the range of the parameter values for each pitch type in a way that is easy to visualize. Note the horizontal break is mirrored for left and right-handed pitchers, as seen in the blue and orange graph. The graphs were generated using seaborn in Python on Kaggle.

![Velocity and Spin Rate](mlbpitchid/veloxspinratenew.PNG?raw=true)
![Horizontal and Vertical](mlbpitchid/vertxhoriznew.PNG?raw=true)
![Horizotal and Vertical: Left and Right Handedness](mlbpitchid/vertxhoriznewrl.PNG?raw=true)

Notes:

On Baseball Savant, horizontal break is positive in the left (<-) direction, and negative to the right (->). Vertical break is negative when the arrow points down, and is usually negative every time.

As the data is from Major League Baseball, the program may not be as accurate at lower levels such as college or high school.
