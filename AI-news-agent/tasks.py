from tools import tool
from crewai import Task
from agents import newsd_researcher, news_writer

research_task=Task (description=("Identify the next big trend in {topic}. Focus on identifying pros and cons and the overall narratives."
                            "Your final report should clearly articulate the key points,"
                            "its market oppurtunities, and potential risks"),
                            expected_output='A comprehensive 3 paragraphs long report on the latest AI trends',
                            tools=[tool_search],
                            agent=researcher,
                            )

write_task=Task( 
    description=(
        "Compose an insightful article in {topic}. Focus on the latest trends and how it's impacting the industry."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand engaging and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown',
    tools=[tool_search]
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
)