# Structured Data Track using Rasa Chatbot

## Overview

The Structured Data Track using Rasa Chatbot project focuses on creating a conversational interface powered by Rasa to interact with and extract information from structured datasets. This project aims to provide an intuitive and user-friendly way to query and manipulate data using natural language through a chatbot.

With the increasing demand for efficient data interaction tools, a chatbot powered by Rasa offers a novel approach to navigating and extracting insights from structured datasets. Users can engage in conversations with the chatbot to retrieve specific information, perform data analysis tasks, and receive relevant insights.

## Features

### 1. Chatbot Interface:

Integrate a chatbot interface powered by Rasa to facilitate natural language conversations for querying and interacting with structured data.

### 2. Data Integration:

Incorporate structured datasets into the chatbot's knowledge base, allowing users to seamlessly query and extract information from the data.

### 3. Natural Language Understanding (NLU):

Implement NLU capabilities using Rasa to accurately interpret user queries and extract relevant entities and intents for effective data interaction.

### 4. Query Processing:

Develop a robust query processing system to handle complex user requests, enabling the chatbot to provide accurate and meaningful responses.

### 5. Data Analysis Commands:

Extend the chatbot's functionality to include commands for basic data analysis tasks, such as aggregations, filtering, and sorting, enhancing the user's ability to derive insights.

### 6. User Feedback Mechanism:

Implement a user feedback mechanism to continuously improve the chatbot's understanding and response accuracy based on user interactions.

### 7. Integration with External Tools:

Explore possibilities for integrating the chatbot with external tools and platforms to enhance its capabilities and provide a comprehensive data interaction experience.

## Technologies Used

- Rasa
- Python
- NLP libraries
- Structured Datasets 
- Flask

## Getting Started

To get started with the Structured Data Track using Rasa Chatbot, follow these steps:

### 1.Creating new env:
 ```bash
   python -m venv bot_env
   bot_env\Scripts\activate
```
### 2. Installing dependencies:
   ```bash
   pip install -r requirement.txt
   ```
### 3. Clone git repo to your system
 ```bash
 git clone https://github.com/b-ashish/personal_bot.git
```
### 4. Now run the app:
```bash
cd personal_bot
python app.py
```
- Currently Chatbot is modified only for given structured data but in modify according to need
- You need to refer user_info/Paymen_details.xlsx to chat with bot if we if structured data is changed then we need to re-train our model

## Usage

- Tracking work if data is realted to time related
- Extact any information from data just by chating with bot
- Modify your data if admin privilege granted no need to use any software 



