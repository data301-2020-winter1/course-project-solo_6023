# Analysis (Post EDA)
---

Cool! Now I've fixed the MPG section of the dataset, and we can move forward with our research questions! I think a few good ones to look at might be:
- What is the distrubution of different fuel type vehicles? aka: How can we visualize how many gasoline vehicles are on the road vs alternatives?
- Is there a correlation between a bigger engine and worse fuel economy? aka: Chart the regression between cylinders/displacement and combined MPG
- Avergage fuel economy by vehicle class? aka: Mean of combined MPG to vehicle type (small car, small truck, i.e) 

Let's see the graph for the first one:

![NumVehicles](https://github.com/data301-2020-winter1/course-project-solo_6023/blob/main/images/chrome_2020-11-15_18-49-37.png?raw=true)

**Interesting!** This honestly suprised me a bit, I would have figured there'd be more SUVs! We do however see that between small SUVs and large SUVs, there are more SUV models in 2020 than small cars, collectively. Let's take a look at the fuel economy of these models and compare them!

![Fuel economy of vehicles by type](https://github.com/data301-2020-winter1/course-project-solo_6023/blob/main/images/chrome_2020-11-15_18-47-09.png?raw=true)

Okay, this is really cool! We can absoultely identify which vehicles on this graph are electic, since the data source calculates an approximate of MPG for electric vehicles which puts them well above 100 MPG. We can see that there is a considerable difference in the average fuel economy of a small SUV versus a standard SUV, which shouldn't be suprising. Larger vehicles *would* use more fuel, that makes sense. Comparing small, midsize, and large cars, we can see the same trend; Larger vehicles use mroe fuel!

To further demonstrate, let's look at a logarithmic relation between fuel economy and engine size (represented as displacement, or, the total volume of the engines cylinders)

![Fuel economy relation to engine size](https://github.com/data301-2020-winter1/course-project-solo_6023/blob/main/images/chrome_2020-11-15_18-46-57.png?raw=true)

Yep! Exactly what we expected to see! This chart does not include electric vehicles or hydrogen vehicles, as neither of those have we would think of as an "engine displacement". To show that we can safely exclude these values from this chart, let's look at a distribution of fuel types.

![Fuel economy relation to engine size](https://github.com/data301-2020-winter1/course-project-solo_6023/blob/main/images/chrome_2020-11-15_18-46-41.png?raw=true)

*Sigh*, for all the progress that's been made, the VAST majority of vehicles are still either gasoline powered or a gasoline/electric hybrid. That said, we can take away the clear message that buying a vehicle bigger than you need is probably a bad choice. The fuel savings in a smaller SUV will not only reduce carbon footprint, but also save you money. As we can see from the first chart, you also have the most choice within the small vehicle space! As someone who personally drives a smaller (albeit old and heavily polluting) SUV, I believe people often buy a vehicle with edge cases in mind, i.e "What if I one time need to transport 7 people? Clearly I need the larger SUV!" rather than what is the objectively better choice. Perhaps making the data more clear would reduce this mentality!
