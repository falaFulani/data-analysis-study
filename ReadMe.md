# Pandas & Python Coding Exercises - Electric Vehicle Population Dataset

## Beginner Level

### Exercise 1: Data Loading and Inspection
Load the CSV file and perform basic data exploration.

**Tasks:**
1. Load the dataset into a pandas DataFrame
2. Display the first 10 rows
3. Check the shape of the dataset (number of rows and columns)
4. Display column names and their data types
5. Get basic statistical summary of numerical columns

### Exercise 2: Data Selection
Practice selecting specific columns and rows.

**Tasks:**
1. Select only the 'Make', 'Model', and 'Electric Vehicle Type' columns
2. Select rows 20-30 (inclusive)
3. Select all rows where the 'State' is 'WA'
4. Select the 'City' and 'County' columns for the first 50 rows

### Exercise 3: Filtering Data
Apply various filters to extract specific subsets.

**Tasks:**
1. Find all Tesla vehicles
2. Find all Battery Electric Vehicles (BEV) with range > 200 miles
3. Find all vehicles in King County
4. Find vehicles manufactured in 2023 or later
5. Find vehicles that are "Clean Alternative Fuel Vehicle Eligible"

### Exercise 4: Handling Missing Values
Identify and handle missing data.

**Tasks:**
1. Check for null values in each column
2. Calculate the percentage of missing values per column
3. Fill missing 'Electric Utility' values with "Unknown"
4. Drop rows where 'Legislative District' is missing

### Exercise 5: Basic Sorting and Ranking
Sort and rank the data.

**Tasks:**
1. Sort vehicles by Model Year (descending)
2. Sort by Electric Range (highest to lowest)
3. Find top 10 vehicles with highest electric range
4. Sort by Make, then by Model, then by Model Year

---

## Intermediate Level

### Exercise 6: GroupBy Operations
Use groupby to aggregate data.

**Tasks:**
1. Count number of vehicles by Make
2. Find average electric range by Electric Vehicle Type
3. Find maximum electric range by Make
4. Count vehicles by County, sorted by count descending
5. Find the most common Model for each Make

### Exercise 7: Data Transformations
Create new columns and transform existing data.

**Tasks:**
1. Extract the year from the 'Model Year' column (if not already numeric)
2. Create a new column 'Vehicle Age' (current year - model year, assume current year is 2026)
3. Create a categorical column 'Range Category' (Short: <100, Medium: 100-200, Long: 200-300, Extended: 300+)
4. Extract city and state from 'Vehicle Location' (if needed, or just note the format)
5. Create a binary column 'Is_Tesla' (True/False)

### Exercise 8: Multi-condition Filtering
Apply complex filters with multiple conditions.

**Tasks:**
1. Find all BEV vehicles with range > 200 made after 2020
2. Find Tesla vehicles in King or Snohomish counties
3. Find PHEV vehicles with range < 30 that are NOT eligible
4. Find vehicles with range between 200-300 that are eligible
5. Find vehicles made by Tesla, Nissan, or Chevrolet in 2020-2023

### Exercise 9: Statistical Analysis
Calculate various statistics by groups.

**Tasks:**
1. Calculate mean, median, min, max of electric range by Make
2. Find standard deviation of range for each Electric Vehicle Type
3. Identify outliers in electric range (use IQR method)
4. Calculate the percentage of eligible vehicles by Make
5. Create a correlation matrix of numeric columns

### Exercise 10: Pivot Tables and Cross-tabulations
Create pivot tables and crosstabs.

**Tasks:**
1. Create a pivot table showing count of vehicles by Make and Electric Vehicle Type
2. Create a pivot table showing average range by County and Model Year
3. Create a crosstab of eligibility status by Make
4. Create a pivot table showing total vehicles by Legislative District and County

---

## Junior Professional Level

### Exercise 11: Time Series Analysis
Analyze trends over model years.

**Tasks:**
1. Count vehicles by model year and plot the trend
2. Calculate year-over-year growth in electric vehicle adoption
3. Find the most popular Make for each model year
4. Analyze how average electric range has changed over years
5. Predict number of vehicles for 2026 based on historical trend

### Exercise 12: Geospatial Analysis
Work with location data.

**Tasks:**
1. Count vehicles by city and find top 10 cities
2. Create a density analysis of vehicles by county
3. Find which legislative districts have the most EVs
4. Calculate EVs per capita by county (you'd need population data - assume or research separately)
5. Identify clusters of high-range vehicles by location

### Exercise 13: Text Analysis on Make/Model
Analyze text data in vehicle descriptions.

**Tasks:**
1. Find all unique Makes and count them
2. Find most common words in Model names
3. Identify which Makes have the most diverse Model offerings
4. Create a function to standardize Make names (handle typos, variations)
5. Find all vehicles with "LEAF" in the model name and analyze their distribution

### Exercise 14: Performance Optimization
Optimize code for large dataset operations.

**Tasks:**
1. Compare performance of iterrows vs vectorized operations for calculating a new column
2. Use query() method for complex filtering and compare speed with boolean indexing
3. Implement parallel processing for a complex groupby operation
4. Optimize memory usage by converting appropriate columns to categorical
5. Create a function with memoization for repeated calculations

### Exercise 15: Advanced Aggregations
Use advanced pandas aggregation functions.

**Tasks:**
1. Use agg() to get multiple statistics for each group
2. Create custom aggregation functions for grouped data
3. Use transform() to add group-level statistics as new columns
4. Use expanding and rolling windows on model year data
5. Implement weighted averages (by range or year) for various metrics

### Exercise 16: Data Quality and Validation
Implement data quality checks.

**Tasks:**
1. Check for duplicate VINs (first 10 characters) and handle them
2. Validate that electric range is consistent with vehicle type (PHEV should have lower range)
3. Check for invalid model years (future years or too old)
4. Verify that all postal codes match the state (WA should have 98xxx)
5. Create a data quality report with flags for suspicious records

### Exercise 17: Merging and Joining
Work with multiple data sources.

**Tasks:**
1. Create a sample population dataset by county and merge with vehicle counts
2. Join with utility company data (create sample) to analyze utility preferences
3. Merge with legislative district information (create sample) for political analysis
4. Perform fuzzy matching to clean inconsistent city names
5. Create a time-series dataset by merging with external economic indicators

---

## Professional Level

### Exercise 18: Machine Learning Feature Engineering
Prepare data for predictive modeling.

**Tasks:**
1. Create features for predicting electric range: encode Make, County, Model Year
2. Build a feature matrix for classifying vehicle eligibility
3. Perform feature selection using correlation analysis and feature importance
4. Create interaction features between Make and Model Year
5. Build a pipeline for preprocessing new vehicle data

### Exercise 19: Advanced Visualization
Create sophisticated visualizations.

**Tasks:**
1. Create a geographic heatmap of vehicle density by county (requires geopandas)
2. Build an animated bubble chart showing Make popularity over years
3. Create a parallel coordinates plot for numeric features
4. Build a dashboard with 3-4 linked visualizations
5. Create a network graph showing relationships between Makes and Counties

### Exercise 20: Custom Pandas Extensions
Extend pandas with custom functionality.

**Tasks:**
1. Create a custom accessor for EV-specific calculations
2. Implement a custom groupby class for vehicle analysis
3. Create a custom indexer for filtering by range and year
4. Build a custom plotting method for EV distribution
5. Implement a custom dtype for handling VIN numbers

### Exercise 21: Production-Ready Code
Write production-quality analysis code.

**Tasks:**
1. Create a modular Python package with separate modules for loading, cleaning, analysis
2. Write unit tests for critical data transformations
3. Implement logging and error handling throughout
4. Create configuration files for analysis parameters
5. Build a CLI tool that accepts different analysis commands

### Exercise 22: Advanced Analytics
Perform sophisticated analytical tasks.

**Tasks:**
1. Calculate market share trends for top 5 manufacturers over time
2. Build a cohort analysis of vehicles by model year and eligibility
3. Perform survival analysis on vehicle models (how long they stay in production)
4. Calculate the Gini coefficient for range distribution by county
5. Implement change point detection in average range over years

### Exercise 23: Optimization and Scalability
Optimize for performance at scale.

**Tasks:**
1. Implement chunking to process data that doesn't fit in memory
2. Use Dask or Modin to parallelize operations
3. Optimize groupby operations for 10x speed improvement
4. Create materialized views of common aggregations
5. Benchmark different approaches and document findings

### Exercise 24: Real-world Scenario Analysis
Solve complex business problems.

**Tasks:**
1. Identify the best locations for new charging stations based on current EV distribution
2. Predict which counties will have the highest EV growth in next 5 years
3. Analyze the relationship between legislative districts and EV adoption rates
4. Create a scoring system for "EV readiness" by zip code
5. Build a recommendation system for fleet managers choosing vehicles

### Exercise 25: Comprehensive Analysis Project
Complete end-to-end analysis.

**Tasks:**
1. Clean and prepare the full dataset
2. Perform exploratory data analysis with visualizations
3. Identify key trends and patterns in EV adoption
4. Build predictive models for EV eligibility and range
5. Create a final report with executive summary, methodology, findings, and recommendations
6. Package the analysis in a Jupyter notebook with markdown explanations
7. Create interactive visualizations using Plotly or Bokeh
8. Deploy a simple Streamlit app to explore the data

---

*Note: Submit your solutions one exercise at a time for feedback. Some exercises may require additional external data sources or libraries - please ask for clarification if needed.*