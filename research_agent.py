from serpapi import GoogleSearch
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ResearchAgent:
    def __init__(self, company_name, industry, serpapi_key):
        """
        Initialize the ResearchAgent with the company's name, industry, and SerpApi API key.
        
        Args:
            company_name (str): Name of the company to research.
            industry (str): Industry in which the company operates.
            serpapi_key (str): Your SerpApi API key.
        """
        self.company_name = company_name
        self.industry = industry
        self.serpapi_key = serpapi_key

    def search_industry_info(self):
        """
        Search and retrieve information about the industry using SerpApi.
        
        Returns:
            list: A list of industry-related news articles and links.
        """
        query = f"AI trends in {self.industry} industry"
        params = {
            "engine": "google",
            "q": query,
            "api_key": self.serpapi_key,
            "tbm": "nws"  # 'tbm=nws' tells Google to return news results.
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            news_articles = results.get("news_results", [])
            logging.info("Successfully fetched industry news articles.")
            return news_articles
        except Exception as e:
            logging.error(f"An error occurred while fetching industry info: {e}")
            return []

    def get_company_focus(self):
        """
        Identify the company's key focus areas, such as customer experience, supply chain, etc.
        
        Returns:
            dict: A dictionary containing the company's focus areas and strategic products.
        """
        logging.info("Fetching company focus areas.")

        # Placeholder data. Replace with actual data retrieval logic if possible.
        focus_areas = {
            "focus_areas": ["customer experience", "supply chain", "product innovation"],
            "strategic_products": ["electric vehicles", "autonomous driving technology"]
        }

        logging.info("Successfully retrieved company focus areas.")
        return focus_areas

# Sample usage (this code is for testing purposes and should be placed in main.py):
if __name__ == "__main__":
    # Replace 'your_serpapi_key' with your actual SerpApi key
    serpapi_key = "a58e9e746da9708c5742a4a763930f0ae595f0599c61252665f42b5494957312"  # Replace with your SerpApi key
    research_agent = ResearchAgent(company_name="Tesla", industry="Automotive", serpapi_key=serpapi_key)

    # Fetch and print industry information
    industry_info = research_agent.search_industry_info()
    print("Industry Information:", industry_info)

    # Fetch and print company focus areas
    company_focus = research_agent.get_company_focus()
    print("Company Focus:", company_focus)
