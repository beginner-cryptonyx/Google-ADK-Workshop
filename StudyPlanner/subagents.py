from google.adk.agents import Agent

CoordinatorAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='CoordinatorAgent',
)

PlanningAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='PlanningAgent',
)


TopicAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='TopicAgent',
)

PracticeAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="PracticeAgent",
)

ScheduleAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="ScheduleAgent",
)




StudyPlanWriter = Agent(
    model="gemini-3.5-flash-lite",
    name="StudyPlanWriter",
)

ReviewAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="ReviewAgent",
)



