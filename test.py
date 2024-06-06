from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

# Set environment variables directly in the script (if not using .env file)
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'crewai-llama3-8b'
os.environ["OPENAI_API_KEY"] = 'NA'  # Assuming no API key is required

# Llama3:8b model configuration
llm = ChatOpenAI(
    model="crewai-llama3-8b",
    base_url=os.environ["OPENAI_API_BASE"]
)

# Math Professor Agent
general_agent = Agent(
  role="Math Professor",
  goal=""" Provide the solution to the students that are asking for mathematical
           questions and give them the answer.""",
  backstory=""" You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
  allow_delegation=False,
  verbose=True,
  llm=llm
)

# Task
task = Task(
    description="what is 3 + 5",
    agent=general_agent,
    expected_output="The expected result is 8."
)

# Crew
crew = Crew(
  agents=[general_agent],
  tasks=[task],
  verbose=2
)

# Execute the task
result = crew.kickoff()

# Print the result
print(result)

