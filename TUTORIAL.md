# Beyond the Prompt: Building an Autonomous eSIM Deal Hunter with CrewAI

The evolution of AI has moved rapidly from simple chatbots to **Agentic Workflows**. If you are still manually copy-pasting prompts into a web interface to plan your travel, you are missing out on the power of autonomous orchestration. 

In this tutorial, I will show you how to leverage the **CrewAI** framework to build a multi-agent "Research Crew." Our goal is simple but high-value: an AI system that autonomously searches the web, compares roaming eSIM packages based on your destination and trip duration, and returns the best deal with a direct purchase link.

---

### Why CrewAI and UV?
CrewAI isn't just about calling an LLM; it's about **role-playing**. By separating concerns into specialized agents (a Researcher and an Analyst), we reduce "hallucinations" and increase the precision of the output. 

**Pro Tip:** The CrewAI team strongly recommends using **uv** for Python package management. It is significantly faster than pip and handles virtual environments seamlessly, ensuring your agentic projects are reproducible and performant.

### Prerequisites
Before we dive in, ensure you have the following:
*   **Python 3.12 - 3.14** installed.
*   **uv** installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`).
*   An **OpenAI API Key** (for the reasoning "brain").
*   A **Serper.dev API Key**: This is required for real-time web search. You can get one for free (2,500 searches) by signing up at [Serper.dev](https://serper.dev).

---

## Phase 1: Environment Scaffolding
A professional project starts with a solid structure. We will use `uv` to manage our environment and the CrewAI CLI to scaffold the project.

```bash
# Install CrewAI globally or via uv
uv tool install crewai

# Create the project
crewai create crew esim_hunter
```

This creates a structured directory where we separate our **Configurations** (YAML) from our **Logic** (Python).

---

## Phase 2: The Source of Truth (YAML Configuration)
The "magic" of CrewAI is decoupling the agent's persona from the execution code. This allows non-developers to tune the agents without breaking the system.

### 1. Defining the Agents (`agents.yaml`)
We need two distinct personas:
*   **The Researcher**: Navigates the web to find providers like Airalo or Holafly.
*   **The Analyst**: Filters the noise to find the best price-per-GB.

```yaml
researcher:
  role: >
    Specialist Travel Tech Researcher
  goal: >
    Find all available eSIM packages for {location} for a {duration} day trip.
  backstory: >
    You are an expert at navigating travel websites. You focus on finding 
    provider names, data limits, and prices.

analyst:
  role: >
    Senior Value Analyst
  goal: >
    Compare packages and recommend the best value for {location}.
  backstory: >
    You have a keen eye for price-per-GB and network reliability.
```

### 2. Defining the Tasks (`tasks.yaml`)
Tasks link the agents to specific goals and expected outputs.

```yaml
search_task:
  description: >
    Search for eSIM providers in {location} for {duration} days. 
    Capture Provider Name, Price, and direct URL.
  expected_output: >
    A list of at least 5 eSIM package options with pricing and links.
  agent: researcher

analysis_task:
  description: >
    Review the list and pick the best deal for the user.
  expected_output: >
    A final recommendation with a comparison table and a direct purchase link.
  agent: analyst
```

---

## Phase 3: The Orchestration Layer (Python)
Now, we connect these definitions in `crew.py`. We use the `SerperDevTool` to give our researcher "eyes" on the live internet.

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class EsimHunter():
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )

    @task
    def search_task(self) -> Task:
        return Task(config=self.tasks_config['search_task'])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential # Task 1 feeds into Task 2
        )
```

---

## Phase 4: Execution & Kickoff
To run your crew, you simply pass the dynamic variables into the `kickoff` method in your `main.py`.

```python
# main.py
def run():
    inputs = {
        'location': 'Japan',
        'duration': '14'
    }
    EsimHunter().crew().kickoff(inputs=inputs)
```

Run it via the CLI:
```bash
crewai run
```

### Get the Full Source Code
Want to see this project in action without writing a single line of code? I've open-sourced the complete, production-ready solution—including unit tests and the full `uv` configuration—on my GitHub.

👉 **[Download the Code Here](https://github.com/cmarcia/esim_hunter)**

---

### Conclusion: Why This Matters
In under 50 lines of code, we have built a system that:
1.  **Surfs the live web.**
2.  **Analyzes pricing data.**
3.  **Provides a structured recommendation.**

This is the power of **Agentic AI**. We are no longer just asking questions; we are delegating workflows. Whether you're building a travel tool or a corporate research engine, CrewAI provides the industrial-grade framework to make it happen.

**What will you build next with a Crew? Let me know in the comments!**

#AI #GenerativeAI #CrewAI #Python #Automation #TravelTech #AgenticWorkflows
