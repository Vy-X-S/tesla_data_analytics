# tesla_data_analytics
Data Analytics Project - Clean, Analyze, Visualize, and Interpret datasets to create business action

Data set Sources:
2016 - 2017 Tesla Model S and X Car Sales in Germany and US https://www.kaggle.com/datasets/syedsharjeelahmed/tesla-car-sales
2012 - 2018 Tesla Model S,3,X,Roadster Edmunds Car Reviews https://www.kaggle.com/datasets/ankkur13/edmundsconsumer-car-ratings-and-reviews
(For this analysis, we will be using the "scraped_Car_Review_tesla.csv" for Analysis)

Tools for Analysis
Python RAKE NLTK - Rapid Automatic Keyword Extraction Python library in Natural Language Processing (NLP)
Python re - Python regular expressions
Python Pandas - Dataframes library useful for analytics and handling datasets
Tableau - Data visualization tool to generate charts, dashboards, graphs, and help lead interpretation

Goal / Purpose
Using the dataset, I want to analyze the reviews and trends of car sales to identify potential business opportunities. By using the RAKE algorithm, we may use NLP to rapidly process reviews and find trends. From these trends, I intend to then compare strengths and weaknesses of the current quality of Tesla's products. This reviewer-based analysis may be interpreted in strengths to drive marketing whereas in weaknesses may provide insights to actions for quality improvement. 

Limitations Acknowledgement
Writing this project in 2023 means that the data is at least 5 years old. While the reviewer-based analysis may provide areas of concerns, improvement, or strengths, these may be outdated. A number of weaknesses are also present that may be addressed:
- According to the reviews dataset, I have a limited number of reviews for the Model 3 and therefore lack data for more consistent analysis
- The reviews dataset lacks further information on the user themselves. Ideally, we may also have a profile behind the customer which may have lead to insights on what groups of customer like/dislike about the product(s)
- The author has limited experience for advanced machine learning techniques that may be more efficient 
- In writing the Python code, the code will tend to be written for readability over efficiency. An example is the decision to use df.apply() rather than a dot product algorithm. Vectorization is definitely more efficient, especially when dealing with larger sets of data, but maintainability and readability were prioritized for the intention of education over enigmatic efficiencies. 

Author's Notes
Thank you for taking the time to go through my project and read. I hope to detail my journey and thought processes for this project. As this is an educational project to exercise NLP, I am open to learning how the project may be improved. Thank you :)