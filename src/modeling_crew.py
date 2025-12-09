from crewai import Agent, Task, Crew, Process
from src.tools import code_execution_tool

class ModelingCrew:
    def __init__(self, llm):
        self.llm = llm

    def run(self, dataset_path, task_desc):
        # agents
        
        analyst = Agent(
            role='Data Analyst',
            goal='Load data and check for issues.',
            backstory='You allow the engineer to do their job by ensuring data is loadable.',
            tools=[code_execution_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        engineer = Agent(
            role='ML Engineer',
            goal='Train a model and REPORT METRICS.',
            backstory='You write code to train models. You MUST print the Accuracy and F1 Score.',
            tools=[code_execution_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

        writer = Agent(
            role='Technical Writer',
            goal='Summarize the technical findings.',
            backstory='You read the output from the engineer and write a Model Card.',
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
        
        #in autocrew, these role, goal, tools will be auto assigned according to the tasks through JSON. 
        #User will only provide the high level task description. But here we define them manually.
        #same for tasks and mrm crew
        #number of task could be different as well in Auto CreW.

        # tasks
        
        task1 = Task(
            description=f"Write and execute Python code to load '{dataset_path}'. Print df.shape and df.info().",
            expected_output="Data summary.",
            agent=analyst
        )

        task2 = Task(
            description=f"Write and execute Python code to load '{dataset_path}' (DO NOT generate fake data). "
                        f"Handle missing values if any. Train a Random Forest for: {task_desc}. "
                        f"Print 'Accuracy' and 'F1 Score'.",
            expected_output="Metrics printed to stdout.",
            agent=engineer,
            context=[task1]
        )

        task3 = Task(
            description="Write a short Model Card based on the metrics found in the previous task.",
            expected_output="Text Model Card.",
            agent=writer,
            context=[task2]
        )

        # crew
        crew = Crew(
            agents=[analyst, engineer, writer],
            tasks=[task1, task2, task3],
            process=Process.sequential,
            memory=False, #to fix openai embedding error as we dont want to spend money on memory here
            verbose=True,
            tracing=True
            
        )

        return crew.kickoff()