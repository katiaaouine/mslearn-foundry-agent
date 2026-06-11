# Before running the sample
# pip install azure-ai-projects>=2.0.0
    
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
    
my_endpoint = "https://katiaaouine-5012-resource.services.ai.azure.com/api/projects/katiaaouine-5012"
    
project_client = AIProjectClient(
     endpoint=my_endpoint,
     credential=DefaultAzureCredential(),
)
    
my_agent = "agent-historique"
my_version = "1"
    
openai_client = project_client.get_openai_client()
    
# Iteratively ask for prompts and get responses
while True:
    user_prompt = input("\nEnter your prompt (or type 'quit' to exit): ").strip()
    
    if user_prompt.lower() == "quit":
        print("Exiting agent.")
        break
    
    if not user_prompt:
        print("Please enter a valid prompt.")
        continue
    
    # Reference the agent to get a response
    response = openai_client.responses.create(
         input=[{"role": "user", "content": user_prompt}],
         extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    )
    
    print(f"\nAgent Response: {response.output_text}")