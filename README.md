![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Azure](https://img.shields.io/badge/Azure-AI%20Foundry-0078D4?logo=microsoftazure)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-En%20cours-orange)
# 🤖 Agent Historique Informatique — Azure AI Foundry

> Agent IA conversationnel créé avec Microsoft Azure AI Foundry  
> Formation : *Develop your first agent with Microsoft *

---

## 📌 Description

Cet agent répond à des questions sur l'histoire de l'informatique et des ordinateurs vintage. Il tourne en session interactive jusqu'à ce que l'utilisateur tape `quit`.

## 🛠 Stack technique

- Azure AI Foundry (ai.azure.com)
- Python 3.11
- azure-ai-projects 2.2.0
- azure-identity
- Azure CLI
- VS Code

## 🚀 Lancer le projet

### Prérequis
- Python 3.11+
- Azure CLI (`az login` avec un compte Azure actif)
- Un projet Azure AI Foundry avec un agent déployé

### Installation

```bash
git clone https://github.com/TON_USERNAME/mslearn-foundry-agent.git
cd mslearn-foundry-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration
Dans `src/agent.py`, remplace `my_endpoint` par ton endpoint Foundry :
```python
my_endpoint = "https://TON-ENDPOINT.services.ai.azure.com/api/projects/TON-PROJET"
```

### Lancement
```bash
python src/agent.py
``

'''
## Formation suivie

[Sneak Peek: Develop Your First Agent with Microsoft Foundry](https://learn.microsoft.com)

##  Auteure

**katiaaouine2000** 
