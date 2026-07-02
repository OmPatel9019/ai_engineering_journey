from dotenv import load_dotenv
from groq import Groq
import os
import time

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

#Agent
class FirstAgent:
    def __init__(self, goal):
        #goal = user input
        self.goal = goal
    
    #step-1 Reasoning
    def reason(self):
        print("[Agent]Understands the goal..")
        prompt = f"""
        User Goal: {self.goal}
        Identify the user skills.
        Return only the skills
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    #setp-2 Planning
    def plan(self, skills):
        print("[Agent]Planning the goal..")
        prompt = f"""
        Goal: {self.goal}
        Skills: {skills}
        Arrange the skills in best order to learn
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    #step-3 Execution
    def execute(self, plan):
        print("[Agent]Executing the goal..")
        prompt = f"""
        Goal: {self.goal}
        Learning Plan: {plan}
        Create a detail 90-day roadmap
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    #Run agent
    def run(self):
        skills=self.reason()
        time.sleep(1)

        plan=self.plan(skills)
        time.sleep(1)

        roadmap=self.execute(plan)
        
        print("\n" + "*" * 50)
        print("Final Roadmap")
        print("*" *50)
        print(roadmap)

goal =input("Enter you goal:")
agent=FirstAgent(goal)
agent.run()