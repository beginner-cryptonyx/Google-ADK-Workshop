from google.adk.agents import Agent


# Parallel Agents

TopicAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='TopicAgent',
    instruction="""
        You are the topic agent, your responsibilies are to identify and analyze the topics to be covered for the exam.
        
        For each topic, you should provide the following information:
        1. Priority - High / Medium / Low
        2. Difficulty Level - Easy / Medium / Hard
        3. Recommended Study focus
        """
)

PracticeAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="PracticeAgent",
    instruction="""
        You are the practice agent, your responsibilies are to determine how much practice should be done for each topic.
        
        For each practice item, you should provide the following information:
        1. Number of practice questions
        2. Type of practice questions - eg: Concept Questions, Coding Problems, Mixed Practice, Mock Tests, etc.
        """
)

ScheduleAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="ScheduleAgent",
    instruction="""
        You are the schedule agent, your responsibilies are to create a study schedule based on the following information:
        1. Remaining days until the exam (eg: 30 days)
        2. Available time for study (eg: 2 hours per day)
        3. Topics to be covered
        
        For each topic, you should provide the following information:
        1. Number of days allocated for each topic
        2. Time of day for study - Morning / Afternoon / Evening
        3. Breaks and rest days
        
        Overall, you should produce a day-wise schedule and incude revison and practice along side new topics. The schedule should be realistic and achievable, and should take into account the student's current level of understanding and available time for study.
        """
)


# First sequntial
PlanningAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='PlanningAgent',
    instruction="""
        Prepare the requirements for creating the study plan and start the three independent analysis tasks.
        
        You will call the following agents in parallel:
        1. TopicAgent - to identify the topics to be covered
        2. PracticeAgent - to identify the practice questions and exercises
        3. ScheduleAgent - to create a study schedule based on the available time and exam
        
    """,
    
)

CoordinatorAgent = Agent(
    model='gemini-3.5-flash-lite',
    name='CoordinatorAgent',
    instruction="""
        You are the cordinator, your responsibilies are to receive the students request, and pass it to the planning workflow.
        
        You should Identify the following information:
        1. Subject
        2. Exam Date - and the days remaining until the exam
        3. Topics to be covered
        4. Current level of understanding of the student
        5. Available time for study
    """,
    
)







StudyPlanWriter = Agent(
    model="gemini-3.5-flash-lite",
    name="StudyPlanWriter",
)

ReviewAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="ReviewAgent",
)



