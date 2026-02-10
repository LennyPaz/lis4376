# Assignment 3: Data Analysis, Shaping and Visualization

**Developer:** Lenny Paz

**Course:** LIS4376 - Artificial Intelligence Applications

## Assignment 3 Requirements

*Two Parts:*

1. Development: Backward-engineer the helper video using Python
2. README.md file with screenshots and Jupyter Notebook link

---

## Files

| File | Description |
|------|-------------|
| [a3.ipynb](a3.ipynb) | Main assignment notebook - comprehensive data analysis and visualization |
| mortality_cleaned.pkl | Cleaned mortality data from Assignment 2 |
| mortality_prepped.pkl | Prepared mortality data with additional columns |
| mortality_wide.pkl | Wide-format mortality data (pivot) |
| mortality_wide.xlsx | Excel export of wide-format data |

## Assignment Overview

This assignment demonstrates comprehensive data analysis, shaping, and visualization techniques using pandas. The notebook is organized into 12 sections:

1. **Environment & Imports** - Setup and configuration
2. **Data Loading** - Reading cleaned data from Assignment 2
3. **Initial Data Inspection** - Examining DataFrame structure
4. **Sorting Data** - Various sorting operations
5. **Statistical Functions** - Mean, max, count operations
6. **Quantiles & Cumulative Sum** - Percentile and cumulative analysis
7. **Column Arithmetic** - Creating derived columns (Mean, MeanCentered)
8. **Data Modification & File Operations** - String manipulation and file I/O
9. **Indexing** - Single and multi-index operations
10. **Pivot & Melt** - Reshaping between wide and long formats
11. **Grouped Data & Aggregates** - GroupBy operations with multiple aggregation functions
12. **Visualization** - Comprehensive plotting (line, box, bar, pie, scatter, subplots)

## Data Analysis Workflow

The notebook follows a five-step data science workflow:

1. **Get** - Load cleaned mortality data
2. **Clean** - Verify data quality
3. **Prepare** - Sort, transform, and reshape data
4. **Analyze** - Apply statistical functions and aggregations
5. **Display/Visualize** - Create multiple chart types

## Key Techniques Demonstrated

### Data Manipulation
- DataFrame sorting (single and multiple columns)
- Index management (set_index, reset_index, multi-index)
- Column arithmetic and mean centering
- String value replacement (zero-filling age groups)

### Statistical Analysis
- Descriptive statistics (mean, median, max, count)
- Quantile analysis (10%, 50%, 90%)
- Cumulative sum calculations
- GroupBy aggregations (single and multiple functions)

### Data Reshaping
- **Pivot (Wide Format):** Transform long data to wide format with years as index and age groups as columns
- **Melt (Long Format):** Convert wide data back to long format for specific analysis
- Excel and pickle file operations

### Visualization Types
- Line plots (time series)
- Box plots (distribution analysis)
- Bar charts (vertical and horizontal)
- Pie charts (proportional data)
- Scatter plots (relationship analysis)
- Subplots (2x2 layout for comparative analysis)

## Screenshots

### Environment Setup
![Environment Setup](img/01_environment.png)

### Data Loading & Inspection
![Data Loading](img/02_data_loading.png)

### Sorting Operations
![Sorting Data](img/03_sorting.png)

### Statistical Functions
![Statistical Functions](img/04_statistics.png)

### Quantiles & Cumulative Sum
![Quantiles](img/05_quantiles.png)

### Column Arithmetic
![Column Arithmetic](img/06_column_arithmetic.png)

### Data Modification
![Data Modification](img/07_data_modification.png)

### Indexing Operations
![Indexing](img/08_indexing.png)

### Pivot Operations (Wide Format)
![Pivot Wide](img/09_pivot_wide.png)

### Excel File Operations
![Excel Operations](img/10_excel_operations.png)

### Melt Operations (Long Format)
![Melt Long](img/11_melt_long.png)

### Grouped Data & Aggregates
![GroupBy Aggregates](img/12_groupby.png)

### Visualization - Line Plots
![Line Plots](img/13_line_plots.png)

### Visualization - Box Plots
![Box Plots](img/14_box_plots.png)

### Visualization - Bar Charts
![Bar Charts](img/15_bar_charts.png)

### Visualization - Pie Chart
![Pie Chart](img/16_pie_chart.png)

### Visualization - Subplots
![Subplots](img/17_subplots.png)

### Visualization - Scatter Plot
![Scatter Plot](img/18_scatter_plot.png)

---

## Notes

- **Important:** Before uploading the .ipynb file, use Kernel menu to:
  - Restart & Clear Output
  - Restart & Run All
- Excel file (mortality_wide.xlsx) must be saved and read using .xlsx format (cells 34-35)
- Visualization section demonstrates multiple chart types for comprehensive data presentation

## Helper Video

[Assignment 3 Helper Video (no audio)](http://qcitr.com/vids/lis4376_5377_A3.mp4)
