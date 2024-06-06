# Multi-Agent AI Project

This repository contains the code for the Multi-Agent AI project. The project aims to develop and implement multi-agent systems to solve complex problems collaboratively.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Multi-Agent AI project explores the capabilities and interactions of multiple AI agents working together. These agents can communicate, cooperate, and compete to achieve goals more efficiently than a single agent.

## Features

- Multi-agent communication
- Cooperative problem-solving
- Competitive scenarios
- Scalable architecture

## Installation

To install and set up the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/ELFAHIM96/multi_agent_AI.git
    cd multi_agent_AI
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the project, use the following command:

```sh
python main.py
```

# Building a Powerful Multi-Agent Workflow with CrewAI and Groq

## Installation and Importing Libraries

To get started, you need to install the required libraries:

```bash
!pip install --q crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29 langchain_groq
```
### Defining LLM Model (Llama3–70B)

To define your LLM model (Llama3–70B), use the following code snippet:

```python
llm = ChatGroq(temperature=0,
               model_name="llama3-70b-8192",
               api_key='<YOUR_GROQ_API_KEY>')
```




