import os
from dotenv import load_dotenv
from agents import Agents
from task import Tasks
from langchain_ollama.llms import OllamaLLM
from crewai import Crew

load_dotenv()
os.environ["OPEN_API_KEY"] = "NA"

# AI 호출
llm = OllamaLLM(
    model="llama3.1",
)

news_researcher = Agents().news_researcher(llm=llm)
news_filter = Agents().news_filter(llm=llm)

new_scraping_task = Tasks().new_scraping(news_researcher)
news_filtering_task = Tasks().news_filtering(
    news_filter,
    context=[new_scraping_task]
)

crew = Crew(
    tasks=[
        new_scraping_task,
        news_filtering_task
    ],
    agents=[
        news_researcher,
        news_filter
    ],
    verbose=True,
)

result = crew.kickoff()

print(result)
