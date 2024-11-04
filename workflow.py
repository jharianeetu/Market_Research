import json
import logging
from agents.research_agent import ResearchAgent  # Ensure this import path is correct based on your project structure
from agents.use_case_agent import generate_use_cases  # Ensure this import path is correct based on your project structure

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_report(industry_info, company_focus, use_cases):
    """
    Generate a structured report combining industry information,
    company focus areas, and generated use cases.
    
    Args:
        industry_info (list): List of industry-related news articles.
        company_focus (dict): Dictionary containing company's focus areas.
        use_cases (list): List of generated use cases.

    Returns:
        dict: The generated report.
    """
    report = {
        "industry_information": industry_info,
        "company_focus": {
            "focus_areas": company_focus['focus_areas'],
            "strategic_products": company_focus['strategic_products']
        },
        "generated_use_cases": use_cases
    }
    return report

def save_report(report, filename='market_research_report.json'):
    """
    Save the generated report as a JSON file.
    
    Args:
        report (dict): The report to save.
        filename (str): The name of the file to save the report to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(report, json_file, indent=4)
        logging.info(f"Market research report saved as '{filename}'.")
    except Exception as e:
        logging.error(f"Error saving report: {e}")

def main():
    # Replace 'your_serpapi_key' with your actual SerpApi key
    serpapi_key = "a58e9e746da9708c5742a4a763930f0ae595f0599c61252665f42b5494957312"
    
    # Initialize the ResearchAgent
    research_agent = ResearchAgent(company_name="Tesla", industry="Automotive", serpapi_key=serpapi_key)
    
    # Fetch industry information
    industry_info = research_agent.search_industry_info()
    logging.info("Industry Information: %s", industry_info)
    
    # Fetch company focus areas
    company_focus = research_agent.get_company_focus()
    logging.info("Company Focus Areas: %s", company_focus)
    
    # Generate use cases
    use_cases = generate_use_cases(company_focus['focus_areas'], company_focus['strategic_products'])
    logging.info("Generated Use Cases: %s", use_cases)
    
    # Generate the report
    report = generate_report(industry_info, company_focus, use_cases)
    
    # Save the report
    save_report(report)

if __name__ == "__main__":
    main()
