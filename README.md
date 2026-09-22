# reddit-popularity-analysis

This project was developed as part of my Diploma Thesis at the University of Patras and focuses on the analysis of the popularity of Computer Science topics on Reddit.

The study combines quantitative data analysis with Large Language Models (LLMs) to investigate trends, compare different areas of Computer Science, analyse discussions, and study how interest in specific topics evolves over time.

Objectives

The main objectives of the project are:

* Collect and organize Reddit data from selected Computer Science-related subreddits.
* Preprocess and filter the collected data.
* Quantitatively analyse the popularity of Computer Science topics.
* Compare technologies, programming languages, academic fields and professional directions.
* Analyse the evolution of topics over time.
* Use Large Language Models for topic analysis and comment summarization.
* Develop an automated Reddit bot for collecting, analysing and publishing statistics.
* Automate the bot's execution using GitHub Actions.

## Key Features

### Reddit Data Collection

Data is collected programmatically through the Reddit API, including posts, comments and relevant metadata.

### Data Analysis

The project uses statistical analysis and data visualization to investigate the popularity of different Computer Science topics.

The analysis includes comparisons such as:

* Programming languages
* Backend vs Frontend Development
* Software Engineering vs Data Science
* DevOps vs Cyber Security
* Data Structures vs Machine Learning
* Machine Learning vs Deep Learning
* Data Scientist vs Data Analyst
* SQL vs Excel
* Natural Language Processing vs Computer Vision

### LLM-based Analysis

Large Language Models are used to support the analysis of unstructured Reddit discussions.

The project includes:

* Comment summarization
* Topic analysis
* Thematic grouping
* Prompt-based analysis
* Interpretation of large volumes of textual data

### Automated Reddit Bot

An automated Reddit bot was developed to collect and analyse recent posts, generate statistics and publish experimental content.

The bot is executed automatically using GitHub Actions.

## Technologies

* Python
* Reddit API
* PRAW
* OpenAI API
* Pandas
* Matplotlib
* Large Language Models (LLMs)
* GitHub Actions
* CSV

## Project Structure

```text
reddit-popularity-analysis/
│
├── src/              # Source code
├── notebooks/        # Data analysis notebooks
├── results/          # Generated results and visualizations
├── .github/
│   └── workflows/    # GitHub Actions workflows
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Methodology

The project follows a pipeline consisting of:

1. Reddit data collection
2. Data preprocessing
3. Statistical analysis
4. Data visualization
5. Topic analysis
6. LLM-based summarization
7. Automated Reddit bot execution

## Results

The analysis revealed differences in the popularity of traditional and emerging areas of Computer Science and identified changes in community interest over time.

The study also explored the use of LLMs as supporting tools for analysing and summarizing large volumes of unstructured Reddit discussions.

## Thesis

This project is based on my Diploma Thesis:

**"Popularity Analysis of Computer Science Topics on Reddit Using Data Analysis and Large Language Models (LLMs)"**

University of Patras — Department of Computer Engineering and Informatics
June 2026

## Author

**Konstantinos Papageorgiou**

Computer Engineering and Informatics Graduate
University of Patras
