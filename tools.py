from crewai_tools import tool

from scrap import Scrap

@tool("Scrap News URLs")
def scrap():
    """
    뉴스 페이지에 접근하여 뉴스 상세 정보를 스크래핑 해오는 함수
    1회 호출으로 모든 카테고리와 필요한 뉴스의 정보를 스크래핑하여 csv 형식으로 저장 후 반환합니다.
    """
    scrap_result = Scrap().scrap()
    return scrap_result
