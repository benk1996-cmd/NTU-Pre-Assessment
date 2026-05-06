prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt_b

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): Prompt_b clearly defines the role, task etc which make it easier for the AI to understand what is expected.
# Your answer (Reason 2): Prompt_b also breaks the tasks into 3 neat steps which reduces the chance of missing out any part of the request.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: Prompt_a uses a more conversational and natural tone which can help the AI to understand the real world situation better.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer: Included contextual details from prompt_a such as making the tone and language easily understandable for a CEO audience.

new_prompt_b = """
Role: You are a data analyst helping a retail marketing manager prepare findings
for a CEO presentation next Friday. The summary must be clear, concise, and free
of technical jargon.
Task: Analyse customer survey feedback data collected over a 3-month campaign.
Data: 500 responses containing age group, product purchased, satisfaction rating
(1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes and complaints from the written comments.
3. Summarise all findings in a short executive summary paragraph suitable for a CEO.
Constraints: Avoid technical language. Keep the summary to 1 short paragraph.
"""