from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

loader = WebBaseLoader("https://careers.nike.com/software-engineer-iii-itc/job/R-54332?source=BY_Google_SEM&utm_source=BY_Google_SEM&utm_medium=employer_ad&utm_campaign=TACOE%20APLA_India%20&utm_content=NikeInc")
page_data = loader.load().pop().page_content

llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model="llama-3.3-70b-versatile", 
)

prompt_extract = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTIONS:
    The scraped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containing the following keys:
    'role','experience'.'skills' and 'description'.
    Only return the valid JSON.
    ### VALID JSON (NO PREAMBLE):
    """
)

prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Mohan, BDE at AtliQ. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

chain_email = prompt_email | llm
email = chain_email.invoke({"job_description": str(job), "link_list": links})
print(email.content)

chain_response = prompt_extract | llm
res = chain_response.invoke(input={"page_data": page_data})

json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)

print(json_res)

