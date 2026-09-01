# ML Model Evaluation Cheat Sheet

Building a model is the easy part. The real question is: **how do you know if it's actually any good?**

That's what this cheat sheet is about. Every metric here is just a different way of measuring "how wrong (or right) was the model?" — the trick is that "wrong" means something different depending on what you're predicting.

```
What am I predicting?
        │
        ├── A category (spam/not spam)     → Classification metrics
        ├── A number (price, temperature)  → Regression metrics
        ├── A group (no right answer given) → Clustering metrics
        └── A ranked list (top 10 products) → Ranking metrics
```

# Classification Metrics

Classification means sorting things into buckets — Yes/No, Cat/Dog/Bird, Spam/Not Spam.

Before anything else, meet the **Confusion Matrix**. It sounds intimidating, but it's just a scoreboard of 4 outcomes. Picture a smoke detector in a kitchen:

| | There really IS a fire | There is NO fire |
| --- | --- | --- |
| **Alarm rings** | Caught it! ✅ | False alarm ❌ (burnt toast set it off) |
| **Alarm stays silent** | Missed it ❌ (dangerous!) | Correctly quiet ✅ |

That's the whole matrix: two ways to be right, two ways to be wrong. Every metric below is just a different way of counting these four boxes, so once this table makes sense, the rest of this section is easy.

(Textbooks call these four boxes **True Positive, False Positive, False Negative, True Negative** — you'll see those names in code and documentation, so it's worth knowing them, but "caught it / false alarm / missed it / correctly quiet" is what they actually mean.)

| Metric | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **Accuracy** | Out of every guess the model made, how many were correct? | A multiple-choice test score: correct answers divided by total questions. Simple, but misleading if one answer choice is rare — more on that below. |
| **Precision** | When the model raises the alarm, how often is it actually right? | Think of a friend who's always texting "THIS IS URGENT!!" You quickly learn how much to trust that text. If they're only right 2 times out of 10, you start ignoring them — that's low precision. If they're right 9 times out of 10, you drop everything when they text — that's high precision. Precision only judges the alarms that were actually raised; it doesn't care about emergencies your friend never mentioned. |
| **Recall** | Out of every real emergency that existed, how many did the model actually catch? | Now flip it around: think of a lifeguard watching a beach. Recall asks: of everyone who actually got into trouble in the water, how many did the lifeguard notice and rescue? A lifeguard with low recall misses swimmers in danger — even if every rescue they *do* make is a real one (high precision). You want a lifeguard with high recall, even if it means a few unnecessary trips into the water. |
| **Precision vs. Recall, side by side** | Why can't a model just be good at both? | A spam filter that deletes *anything* remotely suspicious will catch almost every spam email (high recall) but will also trash real emails from your professor (low precision). A spam filter that only deletes emails it's 100% sure about will never touch a real email (high precision) but will let a lot of spam through (low recall). Tightening one almost always loosens the other. |
| **F1 Score** | One overall score that keeps the model from gaming either Precision or Recall alone. | Like judging a movie on both acting AND story — a movie with amazing acting but a terrible plot still isn't a great movie. F1 refuses to give a high score unless a model is reasonably good at *both* precision and recall; it won't let one great number hide one terrible number. |
| **Specificity** | Of everyone who was actually fine, how many did the model correctly leave alone? | Back to the lifeguard: specificity asks, of all the swimmers who were never actually in danger, how many did the lifeguard correctly *not* bother? A lifeguard who blows the whistle on every single swimmer "just in case" has terrible specificity — technically high recall, but exhausting and useless. |
| **ROC-AUC** | If you compared a random true "Yes" case against a random true "No" case, how often would the model correctly say the "Yes" one looks more like a "Yes"? | Picture a pile of cat photos and dog photos mixed together, and the model gives every photo a "dogginess score" from 0 to 1. Pull one random dog photo and one random cat photo — how often does the dog photo score higher? Do that many times and average it: that's ROC-AUC. A score of 1.0 means the model always ranks dogs above cats; 0.5 means it's basically flipping a coin. |
| **PR-AUC** | Same idea as ROC-AUC, but zoomed in on how well the model finds the *rare* cases. | Searching for a few needles hidden in a giant haystack. You don't care how well the model identified all the hay (there's tons of it, that's easy) — you care whether it found the needles without grabbing fistfuls of hay by mistake. This matters a lot for things like fraud or disease detection, where the "Yes" cases are rare. |
| **Log Loss** | How much should the model be punished for being confidently wrong? | Two weather forecasters both predict rain wrongly. Forecaster A said "40% chance of rain" — a reasonable hedge. Forecaster B said "99% chance of rain, guaranteed" — and it was sunny all day. Log Loss punishes Forecaster B far more severely than Forecaster A, because being *confidently* wrong is worse than being *cautiously* wrong. Lower Log Loss is better; zero means perfect. |
| **Matthews Correlation Coefficient (MCC)** | A single fair score that still works even when one bucket is much rarer than the other. | Imagine a class where 95 students pass and only 5 fail. A "model" that predicts everyone passes looks great on Accuracy (95%) but is actually useless — it never caught a single failing student. MCC won't be fooled by this trick; it only scores well if the model is actually doing something smart with *both* groups. Ranges from -1 (always wrong) to +1 (always right), with 0 meaning "no better than a random guess." |

**Rule of thumb:** Precision and Recall almost always trade off against each other. F1 is the go-to when you need one number that keeps both honest.

# Regression Metrics

Regression means predicting a number — a price, a temperature, tomorrow's sales. Now "wrong" doesn't mean "wrong bucket," it means "how far off was the number?"

| Metric | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **MAE (Mean Absolute Error)** | On average, how far off is each prediction, ignoring whether it was too high or too low? | Think of a dartboard. MAE is the average distance every dart landed from the bullseye — it doesn't matter if the dart landed above, below, left, or right, just how far away it was. |
| **MSE (Mean Squared Error)** | Same idea, but big mistakes get punished much harder than small ones. | Missing your bus by 1 minute is a minor annoyance. Missing it by 30 minutes ruins your whole afternoon. MSE deliberately exaggerates the cost of big misses — a 30-minute miss counts for way more than 30 times a 1-minute miss — which pushes the model to avoid huge blunders even if it means slightly worse performance on the easy cases. |
| **RMSE (Root Mean Squared Error)** | The same "big mistakes matter more" idea as MSE, but converted back into normal, human-readable units. | If MSE is measured in "dollars squared" (which means nothing to a person), RMSE takes the square root and gives you back plain dollars — same dartboard idea as MAE, just with extra weight put on the wildest throws. |
| **R² (R-Squared)** | How much better is this model than the laziest possible guess — just predicting the average every time? | Imagine guessing everyone's weight in a room. The laziest approach: assume everyone weighs the average weight. R² measures how much better your model does than that lazy guess, as a percentage. R² = 100% means the model predicts perfectly. R² = 0% means all that effort produced a model no better than just guessing the average. A negative R² means the model is somehow worse than the laziest possible guess — a red flag. |
| **Adjusted R²** | The same idea as R², but it deducts points for throwing in extra features that don't really help. | R² is easy to fool — like padding an essay with extra paragraphs just to make it look more thorough, even though they add nothing. Adjusted R² is the stricter grader who takes off points for that kind of padding, rewarding a model only when extra information actually earns its keep. |
| **MAPE (Mean Absolute Percentage Error)** | The same idea as MAE, but expressed as a percentage so misses of different sizes can be compared fairly. | Being off by $10 on a $20 phone case is a disaster (50% off). Being off by $10 on a $30,000 car is basically nothing (0.03% off). Raw dollar errors can't tell these apart, but MAPE can, because it looks at the error relative to the size of the true value. |

**Rule of thumb:** Use RMSE when big mistakes should be treated as extra costly (predicting how much weight a bridge can hold). Use MAE when every mistake should count the same regardless of size (predicting delivery time in minutes).

# Clustering Metrics

Clustering is different: there's no answer key to grade against, because nobody told the model which group each item "should" belong to. So instead of checking "was it right," these metrics check "did it form sensible, tightly-knit groups?"

| Metric | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **Silhouette Score** | For each item, is it comfortably inside its own group, or awkwardly sitting closer to a different group? | Picture a party where everyone naturally splits into friend circles. A high silhouette score means everyone is clearly standing with their own circle. A low or negative score means some people are standing closer to a *different* circle than their own — a sign the model grouped them wrong. Ranges from -1 to +1; higher is better. |
| **Inertia** (used in the "Elbow Method") | How tightly packed together are the members within each group? | How close together is each friend circle standing — huddled up in a tight cluster, or spread out loosely across the room? Lower inertia means tighter, more cohesive groups. This is plotted against the number of groups chosen to find the "elbow" — the point past which adding more groups stops helping much. |
| **Davies-Bouldin Index** | How much does each group resemble the group that looks most similar to it? | At a dog show, you don't just want each breed's group to look "different on average" — you want it to be clearly distinguishable from the *one breed it's most easily confused with*. Lower values mean the groups stay distinct even from their closest look-alikes. |
| **Adjusted Rand Index (ARI)** | If you already know the "correct" groups from some other source, how well did the model's grouping match reality? | Imagine you made a wedding seating chart, and later compare it to the chart the couple actually wanted. ARI scores how well the two charts line up — while being smart enough not to give credit for matches that could've happened purely by chance. |

# Ranking / Recommendation Metrics

Used whenever a model outputs an ordered list instead of a single answer — think search results or "recommended for you" rows.

| Metric | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **Precision@K** | Of the top K items the model showed, how many were actually good? | Netflix recommends 10 shows on your homepage. Precision@10 asks: of those 10, how many did you actually end up enjoying? |
| **Recall@K** | Of every show in the whole catalog you'd genuinely enjoy, how many did the top-K list manage to surface? | Out of every movie in Netflix's entire library that you would love, how many actually showed up in your top-10 recommendations? A list can have great precision but terrible recall if it only ever recommends the same 3 obvious hits. |
| **MAP (Mean Average Precision)** | Does the model put the *good* results near the top, not just somewhere in the list? | A search engine that puts the right webpage as result #1 deserves more credit than one that buries the same correct page at result #47 — even though technically, both "found" it. MAP rewards getting good results to the top. |
| **NDCG (Normalized Discounted Cumulative Gain)** | Same idea as MAP, but it also understands that not all "good" results are equally good. | On Google, a perfect answer at position 1 is worth more than a decent-but-not-great answer at position 1 — and both beat that same result buried on page 3. NDCG accounts for these shades of "how good," not just "good or bad." |

# Time-Series Forecasting Metrics

Forecasting the future (like tomorrow's sales) mostly reuses the regression metrics above (MAE, RMSE, MAPE), plus one specialist:

| Metric | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **SMAPE (Symmetric MAPE)** | A fairer version of MAPE that doesn't unfairly punish one type of mistake more than the other. | Regular MAPE can behave strangely when the true value is very close to zero (like dividing a small mistake by an even smaller number, making the percentage explode). SMAPE fixes this so a scale works fairly whether you're weighing a feather or a bowling ball. |

# Core Concepts Behind Every Metric

| Concept | What it's really asking | Everyday analogy |
| --- | --- | --- |
| **Overfitting** | Did the model memorize the training data instead of learning the general pattern? | A student who memorizes last year's exact exam questions and answers word-for-word. They ace a repeat of last year's exam, but bomb this year's exam because the questions changed even slightly. The model looks brilliant on data it has already seen, and falls apart on anything new. |
| **Underfitting** | Is the model too simple to notice what's actually going on in the data? | A student who barely opened the textbook and just answers "C" for every multiple-choice question. It doesn't matter what the exam looks like — the result is bad either way, because there was never any real learning happening. |
| **Bias vs. Variance** | Is the model consistently wrong in the same direction, or wildly inconsistent from one dataset to the next? | Two archers. Archer A always hits two inches to the left of the bullseye, every single time — consistent, but consistently off (this is bias). Archer B's arrows land all over the target, sometimes near the bullseye, sometimes nowhere close — unpredictable (this is variance). The best model is like an archer who is both consistent AND centered on the bullseye. |
| **Train/Test Split** | How do you check if a model actually learned, instead of just memorized? | Study from a textbook (the training data), then take a final exam with different questions that test the same concepts (the test data). If you only ever quiz yourself using the exact homework questions, you'll never know if you actually understood the material. |
| **Cross-Validation** | How do you avoid getting a lucky (or unlucky) score from just one test? | Instead of judging a chef based on a single dish for a single judge, have them cook 5 different dishes, each tasted by a different judge, then average all 5 scores. Much harder to get a fluke result that way. This is exactly what "k-fold cross-validation" means — split the data into k parts, test on each part once, and average. |
| **Baseline Model** | Before celebrating a model's score, is it even better than the dumbest possible guess? | Before praising a weather forecaster's accuracy, check whether they even beat the laziest forecast of all: "tomorrow will be like today." If a fancy model can't beat this kind of simple baseline, it isn't actually adding any value. |

# Which Metric Should I Actually Use?

```
What kind of problem?
        │
        ├── Classification
        │        │
        │        ├── Roughly equal group sizes            → Accuracy, F1
        │        ├── One group is rare (fraud, disease)    → Precision, Recall, PR-AUC
        │        └── Comparing models overall               → ROC-AUC
        │
        ├── Regression
        │        │
        │        ├── Big mistakes should be extra costly    → RMSE
        │        ├── Every mistake should count equally      → MAE
        │        └── Want a "% improvement over guessing"    → R²
        │
        ├── Clustering → Silhouette Score
        │
        └── Recommendations / Search → Precision@K, NDCG
```

**One rule worth memorizing:** never trust Accuracy alone when one group is rare.

Example: if 99% of transactions are NOT fraud, a lazy model that predicts "not fraud" every single time still scores 99% accuracy — while catching exactly zero fraud cases. Always pair Accuracy with Precision and Recall (or skip Accuracy entirely) whenever one outcome is much rarer than the other.
