from serpapi import GoogleSearch
from typing import List, Dict, Any

class SearchTool:
    def __init__(self, api_key: str):
        self.api_key = "963fd114fb94363c15fa1f2dfb215932b418bbc8e4d325c0bb8c96c8c751717b"

    def run(self, query: str, num_results: int = 3) -> str:
        # 1) Compose the full params dict
        params = {
            "q": query,
            "num": num_results,
            "api_key": self.api_key,
        }
        # 2) Instantiate a new GoogleSearch with those params
        search = GoogleSearch(params)
        # 3) Call get_dict() with no arguments
        data = search.get_dict()
        # print(data)

        # 4) Extract the top-N snippets
        snippets = []
        for item in data.get("organic_results", []):
            snippet = item.get("snippet") or item.get("title")
            snippets.append(snippet)
            if len(snippets) >= num_results:
                break

        return "\n".join(snippets)
    

