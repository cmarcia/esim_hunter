# eSIM Hunter: Autonomous Deal Finder

An AI-powered research crew that finds the best roaming eSIM deals for your travels using the [CrewAI](https://crewai.com) framework.

👉 **[Read the Step-by-Step Tutorial](./TUTORIAL.md)**

## Features
- **Autonomous Research**: Searches the web for the latest eSIM packages.
- **Value Analysis**: Compares data limits and prices to find the best ROI.
- **Direct Links**: Provides clickable purchase links in a generated report.

## Setup

### 1. Prerequisites
- [uv](https://github.com/astral-sh/uv) installed.
- OpenAI API Key.
- Serper.dev API Key.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/cmarcia/esim_hunter.git
cd esim_hunter
uv sync
```

### 3. Configuration
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Edit `.env` and add your `OPENAI_API_KEY` and `SERPER_API_KEY`.

## Running the Crew
Execute the following command to start the research process:
```bash
uv run python src/esim_hunter/main.py
```
The final recommendation will be saved to `report.md`.

## Testing
Run unit tests to ensure the crew is correctly configured:
```bash
uv run pytest
```
