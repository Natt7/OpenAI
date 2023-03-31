import os
import openai
openai.organization = "org-CqtFT4zC7wcv5AX32AXdtPuK"
openai.api_key = os.getenv("OPENAI_API_KEY")
models = openai.Model.list()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Create a list of 8 questions for my interview with a public cloud architect"},
        {"role": "assistant", "content": "1. What inspired you to become a public cloud architect, and what do you enjoy most about your job?\n2. How do you design and implement scalable and resilient cloud solutions that support millions of users and data points in real-time?\n3. What cloud computing technologies and tools do you use to optimize resource allocation, automate deployment, and streamline management for cost-effectiveness and performance?\n4. How do you address security risks, compliance requirements, and data privacy regulations in a cloud environment while facilitating accessibility and collaboration for multiple stakeholders?\n5. How do you stay current on evolving cloud technologies and trends, and how do you incorporate emerging best practices and innovations into your projects?\n6. Can you share an example of a particularly challenging project you have worked on as a cloud architect, and how you overcame any obstacles to achieve success?\n7. How do you collaborate with cross-functional teams and vendors to ensure smooth implementation and integration of cloud solutions, and what leadership skills are essential for effective communication, delegation, and problem-solving?\n8. What advice would you give to someone aspiring to become a public cloud architect, and what qualities and capabilities do you think are essential for success in this field?"},
        {"role": "user", "content": "if I answer the question, can i pass the interview?"}
    ]
)

print(completion)