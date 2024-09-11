from crewai import Task
from pydantic import BaseModel
from typing import List


class Tasks:

    def new_scraping(self, agent):
        return Task(
            description="""
                - 뉴스 페이지에 접근하여 뉴스 상세 정보를 스크래핑 해옵니다
                - 뉴스의 정보를 스크래핑하여 csv 형식으로 저장합니다.
            """,
            agent=agent,
            expected_output="웹에서 스크래핑 해온 정보를 csv로 저장",
            output_file="raw_news.csv",

        )

    def news_filtering(self, agent):
        return Task(
            description="""
                - 중요성을 판단할 기준은 다음과 같습니다:
                    1. 사회적 영향력: 얼마나 많은 사람들에게 영향을 미칠 가능성이 있는가?
                    2. 시의성: 현재의 시점에서 얼마나 중요한가?
                    3. 심각성: 다루는 이슈가 얼마나 심각한가?
                    4. 관련성: 대출이라는 주제에 얼마나 관련성이 있는가? 
                - 특히 관련성을 가장 주의깊게 봐야하며, 대출과 전혀 관련이 없는 뉴스의 경우 중요도가 없다고 판단합니다.
                
                단계별로 다음을 수행합니다.
                1. 웹에서 뉴스를 스크래핑 해옵니다.
                1. 뉴스의 중요성을 판단하고 중요도가 높은 10개 이내의 뉴스만 남깁니다.
                2. 대출 시장에 긍정적/부정적 영향을 미칠지 분석 후 POSITIVE / NEGATIVE를 구분하고 그 이유를 적습니다. 
                3. 각 뉴스의 내용을 요약한 후 앞서 분석한 결과와 합쳐서 출력합니다.
            """,
            agent=agent,
            expected_output="중요 뉴스 별 요약과 해당 뉴스의 대출 시장 영향도를 분석한 보고서를 출력",
            output_file="filtered_news.md",
        )
