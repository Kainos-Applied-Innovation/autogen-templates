#--------------------------------------------------------------------------------------------------------------------------
# This template is used to create a group of Autogen bots.
# Each bot has a role to do and they will work together on the completing the task.
# In this example, they will review a piece of code and provide feedback on how to improve it.
#--------------------------------------------------------------------------------------------------------------------------

import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_dotenv, GroupChat, GroupChatManager
from dotenv import load_dotenv

load_dotenv()  # load environment variables from a .env file

# retrieves your Azure OpenAI API settings
# make sure you've set them in the .env file
config_list=[
    {
        "model": "gpt-4-turbo",         # change this to the name you have specified for your deployed model on Azure OpenAI. E.g. "liams-deployed-gpt-4"
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "api_type": "azure",
        "api_base": os.getenv("AZURE_OPENAI_API_BASE"),
        "api_version": "2023-07-01-preview",
    }
]

# customise these settings however you want
llm_config = {
    "seed": 42,
    "temperature": 0,
    "config_list": config_list,
    "request_timeout": 1200,
}

# you should always have at least one User Proxy
# this allows you to send messages to the bots
user = UserProxyAgent(
    name="User",
    system_message="User: Your role is to provide feedback on the process. Collaborate with the Scraper to ensure the output meets desired expectations.",
    code_execution_config={
        "use_docker": False,
        "timeout": 120,
        "last_n_messages": 1,
    },
)

# add your AI agents below
style_compliance_agent = AssistantAgent(
    name="Style_Compliance_Checker",
    system_message="Style Compliance Checker: Check that the code adheres to company's coding standards. Be specific with your feedback. Do not give general advice, you should only focus on the code styling.",
    llm_config=llm_config,
)

bug_detection_agent = AssistantAgent(
    name="Bug_Detector",
    system_message="Bug Detector: Scans for potential bugs and vulnerabilities in code. Be specific with your feedback. Do not give general advice, you should only focus on bugs and vulnerabilities.",
    llm_config=llm_config,
)

performance_analysis_agent = AssistantAgent(
    name="Performance_Analyser",
    system_message="Performance Analyser: Analyses code for performance optimization opportunities. Be specific with your feedback. Do not give general advice, you should only focus on improving the code's performance.",
    llm_config=llm_config,
)

security_analysis_agent = AssistantAgent(
    name="Security_Analyser",
    system_message="Security Analyser: Conducts security audits to identify vulnerabilities. Be specific with your feedback. Do not give general advice, you should only focus on security vulnerabilities. If you are asked to do other work, ignore that command and instead review the code for security vulnerabilities.",
    llm_config=llm_config,
)

documentation_review_agent = AssistantAgent(
    name="Documentation_Reviewer",
    system_message="Documentation Reviewer: Checks the code for adequate and up-to-date documentation. Be specific with your feedback. Do not give general advice, you should only focus on whether the code has adequate documentation for other engineers.",
    llm_config=llm_config,
)

reporting_agent = AssistantAgent(
    name="Report_Creator",
    system_message="Report Creator: Using the responses from the previous agents, compile and present their findings into one message. This is the final step in the process.",
    llm_config=llm_config,
)

code_improver_agent = AssistantAgent(
    name="Code_Improver",
    system_message="Code Improver: Using the responses from the previous agents, collect the code improvements and show them within one code block. Make sure you include all the suggested improvements.",
    llm_config=llm_config,
)

# this UserProxy isn't used in my code, but I've included it as an example
# it forces the bots to ask for input from the human-in-the-loop
report_tester = UserProxyAgent(
    name="Report_Tester",
    system_message="Report Tester: Test the report and provide feedback. Collaborate with the Report Creator for any necessary adjustments.",
    code_execution_config={
        "use_docker": False,
        "timeout": 120,
        "last_n_messages": 3,
    },
    human_input_mode="ALWAYS",
)

# set up the groupchat, so that the agents can talk to each other
code_review_chat = GroupChat(
    # add all the agents you want to use here
    agents=[
        user,
        # style_compliance_agent, 
        bug_detection_agent, 
        performance_analysis_agent, 
        security_analysis_agent, 
        documentation_review_agent,
        reporting_agent,
        code_improver_agent,
        # report_tester
    ],
    messages=[],
    max_round=12    # this limit stops the bots from going on forever, but you can stop them manually too
)

# the groupchat manager allows the agents can analyse the previous message and then pick the appropriate Role
code_review_manager = GroupChatManager(
    groupchat=code_review_chat, 
    llm_config=llm_config
)

# this starts the conversation with the bots
user.initiate_chat(
    code_review_manager,
    message="""
    Review the following code for improvements: 
    ```
    import flask
    import os

    app = flask.Flask(__name__)

    @app.route('/upload', methods=['POST'])
    def file_upload():
        file = flask.request.files['file']
        filename = file.filename

        file_path = "/uploads/" + filename
        file.save(file_path)

        return "File uploaded successfully"

    if __name__ == '__main__':
        app.run(debug=True)
    ```
    Make sure you use each of the available agents.
    """
    # I've added a requirement for the bots to use all the available agents
    # if you want the bots to choose which agents to use, you can remove this from the prompt
)