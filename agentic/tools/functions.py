functions = [
  {
    "name": "search",
    "description": "Search the web for a query and return top snippets.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {"type":"string","description":"Search terms"},
        "num_results":{"type":"integer","description":"How many snippets"}
      },
      "required":["query"]
    }
  },
  {
    "name": "wikipedia",
    "description": "Fetch a short summary from Wikipedia for a given topic.",
    "parameters": {
      "type": "object",
      "properties": {
        "topic":{"type":"string","description":"Page title or topic"},
        "sentences":{"type":"integer","description":"Number of sentences"}
      },
      "required":["topic"]
    }
  },
  # add new tools here as you build them...
]