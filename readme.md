Link for dataset: https://www.kaggle.com/datasets/open-source-sports/baseball-databank?resource=download&select=Batting.csv

is it better to use **existing metrics** for player evaluation or **making our own** with some kind of salary prediction?

# Things to do:
## Understanding dataset
- Figuring out which tables do what
- Figuring out which tables contain actually useful info
- Are all tables operating in the same time interval?
- In the tables we care about, understand which features do what

## Salary prediction
- set up functions for predictions with salary prediction baseline and other stuff we make later 
- figure out how to join salary table with other tables containing player statistics
- Use player statistics along with YearID to predict salary with linear regression
- Try another algorithm to predict salary. SVM random forests or something idk

## Sequence prediction
- Try something like ARIMA to predict the next thing for a given feature given the history of that feature only
- Expand that to include a bunch of other features (but still predict one thing)
- Maybe try a RNN to predict the whole next sequence

- What metric do we use... should we care about predicting everything or just key features used in existing metrics. Not sure.

