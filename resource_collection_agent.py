import logging
from serpapi import GoogleSearch

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ResourceCollectionAgent:
    def __init__(self, serpapi_key):
        self.serpapi_key = serpapi_key

    def fetch_resources(self, query):
        """
        Fetch resources related to a specific query.
        
        Args:
            query (str): The search query for fetching resources.
            
        Returns:
            list: A list of URLs related to the query.
        """
        params = {
            "engine": "google",
            "q": query,
            "api_key": self.serpapi_key,
            "tbm": "nws"
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            resources = results.get("news_results", [])
            logging.info(f"Fetched resources for query '{query}': {resources}")
            return resources
        except Exception as e:
            logging.error(f"An error occurred while fetching resources: {e}")
            return []

# Example usage
if __name__ == "__main__":
    serpapi_key = "a58e9e746da9708c5742a4a763930f0ae595f0599c61252665f42b5494957312"  # Replace with your actual SerpApi key
    agent = ResourceCollectionAgent(serpapi_key)
    resources = agent.fetch_resources("AI trends in automotive industry")
    print("Fetched Resources:", resources)
