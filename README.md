# 🦋 Butterfly Effect Engine

AI-powered supply chain arbitrage discovery platform combining graph databases, AI agents, and data integration.

## 🎯 Overview

The Butterfly Effect Engine discovers non-obvious arbitrage opportunities in complex supply chains by:
- **Graph Analysis**: Neo4j models supplier networks and relationships
- **AI Reasoning**: LangChain agents analyze patterns and recommend opportunities
- **Data Integration**: Palantir Foundry pipelines ingest real-time market data

## 🚀 Key Features

- **Graph-Based Discovery**: Identify hidden supplier relationships
- **AI-Powered Insights**: Intelligent agents analyze arbitrage potential
- **Real-Time Data**: Live market data integration
- **Scalable Architecture**: Production-ready design

## 🛠️ Tech Stack

- **Database**: Neo4j (Graph Database)
- **AI/ML**: LangChain, OpenAI GPT-4
- **Data Integration**: Palantir Foundry
- **Backend**: Python 3.10, FastAPI
- **Deployment**: Docker, AWS

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/butterfly-effect-engine.git
cd butterfly-effect-engine

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```
## 🎮 Quick Start
from src.agents import ArbitrageAgent
from src.neo4j import SupplyChainGraph

### Initialize graph database
graph = SupplyChainGraph()

### Create AI agent
agent = ArbitrageAgent()

### Discover opportunities
opportunities = agent.discover_arbitrage(graph)
print(opportunities)

## 📊 Project Structure
butterfly-effect-engine/
│
├── src/
│   ├── __init__.py
│   │
│   ├── core/                      # Core data processing modules
│   │   ├── __init__.py
│   │   ├── data_loader.py        # Week 1: Pandas data loading
│   │   ├── financial_transforms.py # Week 1: Financial calculations
│   │   └── graph_builder.py      # Week 1: NetworkX graph construction
│   │
│   ├── neo4j/                     # Graph database models
│   │   ├── __init__.py
│   │   ├── models.py             # Neo4j node/relationship models
│   │   ├── cypher_queries.py     # Week 1: Cypher query functions
│   │   ├── connection.py         # Database connection handler
│   │   └── graph_operations.py   # Graph CRUD operations
│   │
│   ├── langchain/                 # AI agent logic
│   │   ├── __init__.py
│   │   ├── agents.py             # LangChain agent definitions
│   │   ├── chains.py             # Custom chains
│   │   ├── prompts.py            # Prompt templates
│   │   └── tools.py              # Custom LangChain tools
│   │
│   ├── foundry/                   # Data pipeline integration
│   │   ├── __init__.py
│   │   ├── spark_pipeline.py     # Week 1: PySpark processing
│   │   └── transformations.py    # Data transformations
│   │
│   ├── agents/                    # Custom agent implementations
│   │   ├── __init__.py
│   │   ├── arbitrage_agent.py    # Supply chain arbitrage detection
│   │   ├── news_processor.py     # News → Entities extraction
│   │   └── entity_extractor.py   # Entity recognition
│   │
│   └── utils/                     # NEW: Utility functions
│       ├── __init__.py
│       ├── logging_config.py     # Logging setup
│       ├── data_validator.py     # Data validation utilities
│       └── visualization.py      # Plotting/graph visualization
│
├── data/                          # Sample datasets
│   ├── raw/                      # Original downloaded data
│   │   ├── comtrade/            # UN Comtrade trade data
│   │   ├── commodities/         # Yahoo Finance commodity prices
│   │   ├── shipping/            # Shipping/logistics data
│   │   └── news/                # GDELT/NewsAPI data
│   │
│   ├── processed/                # Cleaned/transformed data
│   │   ├── trade_flows.csv
│   │   ├── price_arbitrage.csv
│   │   └── entities.csv
│   │
│   └── sample/                   # Small test datasets
│       └── sample_trade_data.csv
│
├── scripts/                       # Executable scripts
│   ├── setup_environment.sh      # Environment setup script
│   ├── setup_neo4j.py           # Week 1: Neo4j initialization
│   ├── download_data.py         # Data download automation
│   ├── run_pipeline.py          # Week 1 Fri: Execute full pipeline
│   ├── seed_database.py         # Populate Neo4j with sample data
│   │
│   ├── exploration/              # NEW: Exploration scripts (replaces notebooks)
│   │   ├── explore_data.py      # Week 1: Data exploration
│   │   ├── analyze_graph.py     # Week 1: NetworkX exploration
│   │   ├── test_neo4j.py        # Week 1: Cypher query testing
│   │   └── demo_pipeline.py     # Week 1 Fri: Full pipeline demo
│   │
│   └── analysis/                 # NEW: Analysis scripts
│       ├── price_analysis.py    # Commodity price analysis
│       ├── trade_flow_analysis.py # Trade pattern analysis
│       └── arbitrage_detection.py # Arbitrage opportunity finder
│
├── tests/                         # Unit and integration tests
│   ├── __init__.py
│   ├── test_data_loader.py       # Week 1 tests
│   ├── test_financial_transforms.py # Week 1 tests
│   ├── test_graph_builder.py     # Week 1 tests
│   ├── test_neo4j/
│   │   ├── __init__.py
│   │   └── test_cypher_queries.py # Week 1 tests
│   ├── test_agents/
│   │   ├── __init__.py
│   │   └── test_news_processor.py
│   └── test_utils/
│       ├── __init__.py
│       └── test_data_validator.py
│
├── docs/                          # Documentation
│   ├── architecture.md           # System architecture
│   ├── setup.md                  # Setup instructions
│   ├── week1_progress.md         # Week 1 progress tracking
│   ├── graph_concepts.md         # Week 1: Graph theory notes
│   ├── api_references.md         # API documentation
│   └── datasets.md               # Dataset documentation
│
├── config/                        # Configuration files
│   ├── neo4j_config.yaml        # Neo4j connection settings
│   ├── data_sources.yaml        # Data source URLs/APIs
│   ├── pipeline_config.yaml     # Pipeline parameters
│   └── logging_config.yaml      # Logging configuration
│
├── outputs/                       # NEW: Script outputs
│   ├── reports/                 # Generated reports
│   ├── visualizations/          # Generated plots/graphs
│   └── logs/                    # Application logs
│
├── pyproject.toml                # Poetry dependencies
├── poetry.lock                   # Lock file
├── .gitignore                    # Git ignore rules
├── .env.example                  # Environment variables template
├── README.md                     # Project overview
└── LICENSE                       # Project license

## 🧪 Running Tests
pytests tests/

## Demo
[Link to demo video]

## 🤝 ContributingContributions welcome! 
Please read CONTRIBUTING.md first.

## 📝 License
MIT License - see LICENSE file for details.

## 👤 Author
Mychelle Hale
LinkedIn: [your-profile]
Portfolio: [your-website]
Email: your-email@example.com

## 🙏 Acknowledgments
Neo4j for graph database technology
LangChain for AI agent framework
Palantir for data integration platform