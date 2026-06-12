# Before running the sample
# pip install azure-ai-projects>=2.0.0
    
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os
my_endpoint = os.environ.get("AZURE_FOUNDRY_ENDPOINT", "YOUR_ENDPOINT_HERE")"
    
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
         input=[
            {
                "role": "system",
                "content": """Tu es un agent spécialisé dans l'histoire de l'informatique.
        Tu as accès à une recherche web pour trouver des informations récentes.
        Tu réponds de manière précise, pédagogique et passionnée sur :
        - L'histoire des ordinateurs et des technologies
        - Les pionniers de l'informatique
        - Les machines vintage et leur impact
        - L'évolution des langages de programmation
        Réponds toujours en français."""
            },
            {"role": "user", "content": user_prompt}
        ],
         extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    )
    
    print(f"\nAgent Response: {response.output_text}")