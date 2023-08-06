import pandas as pd
from rake_nltk import Rake
import re

# Load CSV to pandas DF
df = pd.read_csv('archive\Scraped_Car_Review_tesla.csv')

def clean_text(text): # Clean the Reviews of punctuations, non-ASCII chars, extra space, and set to lowercase
    # Convert to Lowercase
    text = text.lower()
    # Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Remove punctuations
    text = re.sub(r'[^\w\s]', ' ', text)
    # Remove extra space
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_top_phrases(review, max_phrases=10): # NLP RAKE library to rank top phrases
    r = Rake()
    r.extract_keywords_from_text(review)
    phrases = r.get_ranked_phrases()
    return ' '.join(phrases[:max_phrases]) 

def extract_vehicle_title(row):
    # The dataset presents itself as [Year] [Make] [Model] [Model_subdata](e.g Model 3) [Car_Type] [Trim]
    # Apply New Columns to df

    parts = row['Vehicle_Title'].split()

    # Extract Year to New Column
    row['Vehicle_Year'] = parts[0]

    # Extract Make to New Column
    row['Vehicle_Make'] = parts[1]

    # Extract Model
    row['Vehicle_Model'] = f"{parts[2]} {parts[3]}"

    # Extract Car Type
    row['Vehicle_CarType'] = parts[4]

    # Extract Trim
    row['Vehicle_Trim'] = " ".join(parts[5:])

    # Return the newly modified dataframe that includes all of the new columns
    return row

# Clean the text
df['Review'] = df['Review'].apply(clean_text)
# Use RAKE to extract top phrases from the reviews
df['Review Top 10 Phrases'] = df['Review'].apply(extract_top_phrases)

# Remove the "on" and hours:minutes under Review_Date Column
df['Review_Date'] = df['Review_Date'].str.split().str[1]
# Split the Data in Vehicle_Title to their respective components
# Axis applies the function row-wise 
df = df.apply(extract_vehicle_title, axis=1)

# Use RAKE once more on the results for a Summary Dataframe
"""
results = []
groups = df.groupby(['Vehicle_Year', 'Vehicle_Model'])
for (year, model), group in groups:
    aggregated_review = ' '.join(group['Review'].to_list())
    avg_rating = group['Rating'].mean()

    top_phrases = extract_top_phrases(aggregated_review, 10)

    results.append({
        'Year': year,
        'Model': model,
        'Average Rating': avg_rating,
        'Top Phrases': ' '.join(top_phrases)
    })

summary_df = pd.DataFrame(results)"""


# Save the results to a new excel sheet
df[['Review_Date', 'Vehicle_Year', 'Vehicle_Make', 'Vehicle_Model', 'Vehicle_CarType', 'Vehicle_Trim', 'Rating', 'Review Top 10 Phrases']].to_excel("processed_reviews_Tesla.xlsx", index=False)
#summary_df.to_excel("summary_reviews_Tesla.xlsx", index=False)