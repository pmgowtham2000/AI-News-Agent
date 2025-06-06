from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

crew=Crew(agents=[news_researcher,news_writer], tasks=[research_task,write_task],process=Process=Process.sequential)

result=crew.kickoff(input={'topic':"AI in healthcare"})
print(result)