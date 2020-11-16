# EDA

Okay! So, our Pandas Profile returned that displacement and # of Cylinders contained a shocking 40 missing values. There is a reason I didn't remove rows containing null values, and that is that this dataset contains electric and hydrogen powered vehicles. Logically, these engines might not report the same way as a gasoline, diesel, or hybrid vehicle. Printing all rows where Displacement == Null shows us that yes, this is in fact the case!

![Numbers](https://github.com/data301-2020-winter1/course-project-solo_6023/blob/main/images/chrome_2020-11-15_15-37-32.png?raw=true)


Because of this, we don't want to remove these rows, as it would remove interesting data!

Something else of note is that our MPG is recoreded as categorical. This is interesting, and looking at our data we can see that hybrid vehicles have their MPG recorded in the form "Gas Only MPG/Hybrid MPG" which means that this is NOT a single integer! For ease of manipulation, I'm going to go with the first of these values, and then store it back into the MPG categories, and then convert all the rows to integers.

Thankfully, it seems our data doesn't contain any outliers. I did remove duplicate values BEFORE the analysis, because I knew that would get flagged due to sloppy data processing when I imported the data. I removed values from the data I didn't need but forgot that some of that data produced differences between models that otherwise had none. For some reason, Pandas "drop_duplicates" function didn't seem to work inside my function chain, so it is preformed in this document. I will save the cleaned and edited CSV to the processed folder!

