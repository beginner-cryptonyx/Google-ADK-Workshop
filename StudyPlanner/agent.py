from google.adk.agents import Agent, ParallelAgent, SequentialAgent, LoopAgent
from .subagents import (
    PlanningAgent,
    CoordinatorAgent,
    TopicAgent,
    PracticeAgent,
    ScheduleAgent,
    StudyPlanWriter,
    ReviewAgent)


starting_pipeline = SequentialAgent(
    name="starting_pipeline",
    sub_agents=[CoordinatorAgent, PlanningAgent],
)


planning = ParallelAgent(
    name="planning",
    sub_agents=[TopicAgent, PracticeAgent, ScheduleAgent],
)

ending_pipeline = LoopAgent(
    name="ending_pipeline",
    sub_agents=[StudyPlanWriter, ReviewAgent],
    max_iterations=2
)

full_workflow = SequentialAgent(
    name="full_workflow",
    sub_agents=[starting_pipeline, planning, ending_pipeline],
)
root_agent = Agent(
    model='gemini-3.5-flash-lite',
    name='root_agent',
    description='This is the root agent for the study planner application. It coordinates the entire workflow of creating a study plan for students based on their requests and requirements.',
    instruction="""
        You are the root agent for the study planner application. Your responsibilities are to coordinate the entire workflow of creating a study plan for students based on their requests and requirements.
        
        You MUST call the following agents in sequence:
            1. starting_pipeline - to receive the student's request and prepare the requirements for creating the study plan
            2. planning - to start the three independent analysis tasks in parallel
            3. ending_pipeline - to finalize the study plan and review it with the student
            
        You should ensure that the workflow is executed in the correct order and that all necessary information is collected and processed at each step.
        Always call the next agent in the sequence after the current agent has completed its task.
        Never answer specialist questions yourself, always delegate to the appropriate agent.
        
        At the end of the workflow, you should provide a detailed study plan and any recommendations for the student.
        
        Every sub-agent should be called with the relevant information collected from the previous agents in the workflow, without execptions.
    """,
    sub_agents=[full_workflow],
)
