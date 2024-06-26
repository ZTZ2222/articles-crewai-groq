from textwrap import dedent
from crewai import Task

from agents import ArticleAgents


class ArticleTasks:

    @staticmethod
    def plan():
        return Task(
            description=dedent("""
                1. Prioritize the latest trends, key players, 
                and noteworthy news on {topic}.\n
                2. Identify the target audience, considering 
                their interests and pain points.\n
                3. Develop a detailed content outline including 
                an introduction, key points, and a call to action.\n
                4. Include SEO keywords and relevant data or sources.
                """),
            expected_output=dedent("""
                A comprehensive content plan document 
                with an outline, audience analysis, 
                SEO keywords, and resources.
                """),
            agent=ArticleAgents.get_planner(),
        )

    @staticmethod
    def write():
        return Task(
            description=dedent("""
                1. Use the content plan to craft a compelling 
                blog post on {topic}.\n
                2. Incorporate SEO keywords naturally.\n
                3. Sections/Subtitles are properly named 
                in an engaging manner.\n
                4. Ensure the post is structured with an 
                engaging introduction, insightful body, 
                and a summarizing conclusion.\n
                5. Proofread for grammatical errors and 
                alignment with the brand's voice.\n
                """),
            expected_output=dedent("""
                A well-written blog post 
                in markdown format, ready for publication, 
                each section should have 2 or 3 paragraphs.
                """),
            agent=ArticleAgents.get_writer(),
        )

    @staticmethod
    def edit():
        return Task(
            description=dedent("""
                Proofread the given blog post for 
                grammatical errors and 
                alignment with the brand's voice.
                """),
            expected_output=dedent("""
                A well-written blog post in markdown format, 
                ready for publication, 
                each section should have 2 or 3 paragraphs.
                """),
            agent=ArticleAgents.get_editor(),
        )
