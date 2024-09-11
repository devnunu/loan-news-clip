from crewai import Agent
from crewai_tools import FileReadTool, FileWriterTool
from tools import scrap

file_read_tool = FileReadTool(file_path='article_df.csv')
file_writer_tool = FileWriterTool()


class Agents:

    # def news_researcher(self, llm):
    #     return Agent(
    #         role="뉴스 리서처",
    #         goal="웹에 게시된 뉴스를 스크래핑함",
    #         backstory="""
    #             - 당신은 뉴스 리서처입니다.
    #             - 당신은 한국인이며 한국어로 말하고 생각합니다
    #             - 웹에 게시된 뉴스를 스크래핑해오는 역할을 담당합니다.
    #             """,
    #         verbose=True,
    #         allow_delegation=False,
    #         llm=llm,
    #         tools=[
    #             scrap
    #         ]
    #     )

    def news_filter(self, llm):
        return Agent(
            role="금융 뉴스 분석가",
            goal="무작위 뉴스 중 중요한 금융 뉴스만 추려냄",
            backstory="""
                - 당신은 한국어의 이해력이 매우 높으며 한국어로 말하고 생각하는 한국인입니다. 
                - 당신은 금융 회사에 소속된 금융 전문가이자 금융 분석가 입니다. 
                - 무작위 뉴스 중에서 금융과 관련된 중요한 뉴스만 필터링 합니다.
                - 당신의 진행한 업무가 다른 사람들에게 도움을 줄 수 있기를 바랍니다. 
                """,
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tools=[
                scrap
            ]
        )
