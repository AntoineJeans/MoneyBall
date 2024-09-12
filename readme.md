Link for dataset: https://www.kaggle.com/datasets/open-source-sports/baseball-databank?resource=download&select=Batting.csv



# Questions about the data
- How do we deal with gaps in the years? Should there be a skipped years feature?
- How do we deal with multiple records in the same year for the same player? Should we just add them?
- Should we count AL and NL the same way? Is one easier than the other? it's about half and half
- is it better to use **existing metrics** for player evaluation or **making our own** with some kind of salary prediction?

# interesting datasets:
- https://www.kaggle.com/datasets/open-source-sports/baseball-databank?resource=download&select=Batting.csv
- https://baseballsavant.mlb.com/#
- https://www.covers.com/sport/baseball/mlb/injuries
- https://www.baseball-reference.com/players/f/fingero01.shtml

# Things to do:
## Understanding dataset
- Figuring out which tables do what
- Are all tables operating in the same time interval? - not really, example salaries has earliest 1985
- In the tables we care about, understand which features do what


## Salary prediction
We might want to build a model that can generate a reasonable salary given a player stats. 
- set up classes and functions that will help for development and model evaluation later. Choose a decent error function.
- Use player statistics along with YearID to predict salary with linear regression
- Try another algorithm to predict salary. SVM random forests or something idk

## Metric prediction
- find a decent player evaluation metric and have a model predict it given player history

## Sequence prediction
- instead of predicting player evaluation metric, predict statistics, that will then be used for other stuff (evaluating the metric directly, salary prediction, or just for their own sake)

Is it even called sequence prediction? We don't have one sequence. We have 25k of them. similar projects: weather prediction
We may have common trends between player. is it a good idea to have a model for every player? no.
How much can we actually use autosupervised training? Should you shuffle the autosupervised training data so that data from one player isn't trained sequentially (for example if we do RNN). Should we just jump straight to RNN to expect a working model?

- Use random forest to predict the single next value for number of homeruns in a given year given a bunch of stats from the year prior
- Try something like ARIMA to predict the next thing for a given feature given the history of that feature only
- Expand that to include a bunch of other features (but still predict one thing)
- Maybe try a RNN to predict the whole next sequence

- What metric do we use... should we care about predicting everything or just key features used in existing metrics. Not sure.

## Fall-off detection
Train a sort of classifier that indicates when a player is likely to fall-off next year. This can be done directly on top of metric or sequence prediction, or seperately. The advantage of a classifier might be that we would be able to choose wether we want high recall or precision.
- Add a feature to the dataset that is the res
- Check out past projects with something like a RNN classifier, imitate that shit



