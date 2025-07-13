# Explanations of each subpart
## Part A
* As per the requirements given, aimed to create a visual representation of the worker logs and important events like crashes, overlaps and failures, we plotted the Grunt-style graphs

## Part B and C
* We check if the last event of a particular job is 4 or less ms ago. If yes, then it is a duplicate.
* The reason we pick 4ms is because a large fraction of the events occur 5ms after the previous

