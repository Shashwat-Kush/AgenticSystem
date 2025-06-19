import wikipedia

class WikipediaTool:
    def __init__(self,language:str="en"):
        self.language = language
        wikipedia.set_lang(language)

    def run(self, query:str,sentences:int=4)->str:
        try:
            summary = wikipedia.summary(query, sentences=sentences)
            return summary
        except wikipedia.DisambiguationError as e:
            return wikipedia.summary(e.options[0], sentences=sentences)
        except wikipedia.PageError:
            return f"No page found for '{query}' in {self.language} Wikipedia."