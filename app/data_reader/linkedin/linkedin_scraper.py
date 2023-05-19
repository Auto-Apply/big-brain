from app.scraper import Scraper
from app.data_reader.linkedin.constants import (
    LINKEDIN_SEARCH_URL_BASE,
    LINKEDIN_SEARCH_URL_TIME,
    LINKEDIN_SEARCH_URL_LOCATION,
    LINKEDIN_SEARCH_URL_KEYWORDS,
    LINKEDIN_SEARCH_URL_GEOID,
)
import os


class linkedin_scraper(Scraper):
    def construct_search_url(
        self,
        recency_seconds: str,
        geo_id: str,
        location: str,
        keywords: str = "",
    ) -> str:
        if len(keywords) == 0:
            keywords = self.get_keywords_from_file()
        return (
            LINKEDIN_SEARCH_URL_BASE
            + LINKEDIN_SEARCH_URL_TIME
            + recency_seconds
            + LINKEDIN_SEARCH_URL_LOCATION
            + location
            + LINKEDIN_SEARCH_URL_GEOID
            + geo_id
            + LINKEDIN_SEARCH_URL_KEYWORDS
            + keywords
        )

    def get_keywords_from_file(self, file: str = "linkedin.query") -> str:
        try:
            path = os.path.abspath(f"../../../data/{file}")
            with open(path, "r") as f:
                content = f.readlines()
                content = [x.strip() for x in content]
                search_filter = " ".join(content)
                return search_filter
        except Exception as e:
            print(f"Exception in linkedin_scraper class: {e}")
            return ""

    def __init__(self) -> None:
        print("poo")
