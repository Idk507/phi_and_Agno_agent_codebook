from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 
import os 

os.envrion["GROQ_API_KEY"] = ""

#web_search_agent

web_search_agent = Agent(
    name="Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools =[DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls = True,markdown = True
)

#finance_data_agent
finance_data_agent = Agent(
    name="Finance Data Agent",
    role = "Fetch financial data",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions = ["Always include sources"],
    show_tools_calls = True, markdown = True
)

#multi agent 

multi_ai_agent = Agent(
    team=[web_search_agent,finance_data_agent]
    name="Multi-AI Agent",
    role = "Perform both web search and finance data tasks",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include sources","Use table to display the data"],
    show_tools_calls = True, markdown = True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)