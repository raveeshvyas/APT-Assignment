# Thought Process

## Approach

## All Statistical Values
We found the statistical values of all the columns as follows

|       | deltaX       | gamma        | omega        | flux         | pulse        | neutronCount  |
|-------|--------------|--------------|--------------|--------------|--------------|---------------|
| mean  | 95.209593    | 95.402143    | 95.016844    | 95.209804    | 95.209737    | 50541.730472  |
| std   | 103.796442   | 103.796594   | 103.797184   | 103.797320   | 103.796308   | 28578.459770  |
| min   | -211.728008  | -211.323966  | -211.882648  | -211.767355  | -211.500164  | 1000.000000   |
| 25%   | 39.445254    | 39.632531    | 39.242162    | 39.438783    | 39.449301    | 25810.000000  |
| 50%   | 114.096853   | 114.286186   | 113.906685   | 114.114242   | 114.092463   | 50604.000000  |
| 75%   | 175.434137   | 175.621276   | 175.241753   | 175.425143   | 175.434474   | 75257.000000  |
| max   | 286.705521   | 286.709571   | 286.513061   | 286.549948   | 286.466974   | 99999.000000  |


## Finding Volume

We started by finding the column corresponding to volume. This is because volume is expected to be an integer because it represents the number of shares traded that day which is a discrete value and it would have much different statistical values (mean, median, min, max, range and standard deviation) than the other columns.

Examining Table (1?), we observe the highly different values of all the statistical measures which significantly makes us determine that the column `neutronCount` corresponds to volume.

## Finding High and Low (bounds for a time unit)

Then we proceeded to calculate the bounds (low and high) from the data. To do this we came up with the idea of taking the minimum and maximum from each row and find the columns which give minimum and maximum for most of the values in the dataset after keeping aside the column for volume (`neutronCount`).

Frequency of each column being the ROW-WISE MAXIMUM:
| Column | Frequency  |
|--------|------------|
| gamma  | 432559     |
| pulse  | 67441      |

(others 0)

Frequency of each column being the ROW-WISE MINIMUM:
| Column | Frequency  |
|--------|------------|
| omega  | 432906     |
| pulse  | 67094      |

(others 0)

From Table (2?), we infer that after keeping aside the column for volume (`neutronCount`) the values in the column `gamma` are the maximum for `<how many>` values which is the highest and thus we can very confidently suggest that `gamma` is indeed the maximum and maps to the actual column `high`.

Similarly, we consolidated the results for all the times each column is the minimum of all the columns for all values as shown in Table (3?) and found that the column `omega` is lowest for most times `<how much>` and thus maps to the actual column `low`.

<\Add Candlestick Analysis>

## Finding Price

Now we were left with three columns: `deltaX`, `flux` and `pulse`.

Assumption: Price could have meant many things (e.g. predicted price for a day, average price, etc.)

However, we observed an anomaly where the values in the `pulse` column occasionally reached both the maximum and minimum extremes, though not very frequently (as shown in Table (4?)). Meanwhile, the other two columns, `deltaX` and `flux`, consistently remained within the bounds defined by `gamma` (= high) and `omega` (= low).

This gave us a huge clue that `pulse` may be the price since it cannot be open or close because both open and close follow the following condition.

$$low <= open <= high$$
$$low <= close <= high$$

This means that price may be the predicted price or some other suitable such quantity. However it can be said with much confidence that `pulse` is not `open / close`. Hence, pulse needs to be `price`.

(make a chart to determine how the price)

## Finding Open and Close

We were now left with only two columns and we had to determine which one is the opening share value (open) and which one is the closing share value (close).

Here we thought of using candlestick diagrams

## Hypothesis 1 (which we later deduce as correct)

<img src="images/hyp_1.png" width=700>
<img src="images/hyp_1_circles.png" width=700>

### Analysing one segment
<img src="images/hyp_1_part_1.png" width=700>

<\write the trend here>

### Analysing another segment
<img src="images/hyp_1_part_2.png" width=700>

<\write the trend here>

## Hypothesis 2 (which we later deduce as incorrect)
<img src="images/hyp_2.png" width=700>
<img src="images/hyp_2_circles.png" width=700>

### Analysing one segment
<img src="images/hyp_2_part_1.png" width=700>

### Analysing another segment
<img src="images/hyp_2_part_2.png" width=700>


######### Add analysis about why this and why not this later

### Challenges (and how we overcame them)
1. It was challenging to find an accurate way to map deltaX and flux to open and close. We overcame this by employing many methods:
   1. A custom self-devised definite sliding window algorithm to find the minimum differences across pairs and compute the most desirable pair (in order).
   2. Using a clever regression model technique.
   3. Candle Stick Analysis


### Confidence 
<columnwise confidence analysis based on some statistics of your choice>

1. Low
2. High
3. Volume
4. price = P(1 | low = conf1 && high = conf2)
5. open -> slope + thresholding / regression model
5. close -> slope + thresholding / regression model

### Summary
Overall, I combined ...................................................... to derive the mapping. I also wrote a ........................... 




WRITE ALL ASSUMPTIONS CLEARLY