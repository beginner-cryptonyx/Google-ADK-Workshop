from google.adk.agents import Agent


# Sequntial Agents
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








# Final Agents
StudyPlanWriter = Agent(
    model="gemini-3.5-flash-lite",
    name="StudyPlanWriter",
    instruction="""
        You are the study plan writer, your responsibilies are to create a comprehensive study plan based on the information provided by the other agents:
            1. Topic Agent - to identify the topics to be covered
            2. Practice Agent - to identify the practice questions and exercises
            3. Schedule Agent - to create a study schedule based on the available time and exam
        
        Your job is to combine the information from the other agents and create a comprehensive study plan that includes:
            1. Day-wise schedule for the entire study period
            2. Topics to be covered each day
            3. Practice to complete each day
            4. Revision to be done each day
            5. Mock test or final preparation for the exam
            
        The study plan should be realistic and achievable, and should take into account the student's current level of understanding and available time for study.
    """
)

ReviewAgent = Agent(
    model="gemini-3.5-flash-lite",
    name="ReviewAgent",
    instruction="""
        You are the review agent, your responsibilies are to review the study plan created by the StudyPlanWriter and provide feedback on its effectiveness and feasibility.
        
        You should consider the following factors while reviewing the study plan:
            1. Are all the topics covered in a logical and sequential manner?
            2. Does the plan fit within the available time for study?
            3. Is sufficient time allocated for practice?
            4. Is sufficient time allocated for revision?
            5. Is the final day suitable for a mock test or final preparation for the exam?
            
        Your feedback should be constructive and actionable, and should help improve the overall quality of the study plan.
    """
)



