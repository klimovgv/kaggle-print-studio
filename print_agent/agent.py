import os
from google.adk.agents.llm_agent import Agent
from google.adk.agents import LlmAgent, Agent
from google.adk.models.google_llm import Gemini
from google.genai import types
from print_agent.tools.register_logo_file import register_logo_file
from print_agent.prompts import FINALIZER_PROMPT, LOGO_GENERATOR_PROMPT, ROOT_AGENT_PROMPT

retry_config=types.HttpRetryOptions(
    attempts=3,  # Maximum retry attempts
    exp_base=5,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

finalizer_agent = Agent(
    name='finalizer_agent',
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    description="Finalizes the print merchandise design brief for client presentation.",
    instruction=FINALIZER_PROMPT,
    tools=[],
)

logo_generator_agent = Agent(
    name='logo_generator_agent',
    model=Gemini(
        model="gemini-2.5-flash-image-preview",
        retry_options=retry_config
    ),
    description="Generates a logo based on client description.",
    instruction=LOGO_GENERATOR_PROMPT,
    output_key="generated_logo",
)

root_agent = LlmAgent(
    name="root_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    sub_agents=[finalizer_agent, logo_generator_agent],
    description="Root agent orchestrating the print merchandise design consultation and finalization.",
    instruction=ROOT_AGENT_PROMPT,
    output_key="user_requirements",
    tools=[register_logo_file],
)

# # Step 2: Set up Session Management
# # InMemorySessionService stores conversations in RAM (temporary)
# session_service = InMemorySessionService()

# # Step 3: Create the Runner
# runner = Runner(agent=consultant_coordinator, app_name="Print Studio Runner", session_service=session_service)


print("✅ root_agent created.")
