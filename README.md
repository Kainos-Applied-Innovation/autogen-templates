# Autogen Templates
Guide for how to create your own Autogen agents. Check the Microsoft repo for the latest updates.

# Setup
To get started:
1. Navigate to the project's root directory in the Terminal
2. Install all the required plugins:
```bash
pip install -r requirements.txt
```
3. Rename the `.env.example` file to `.env`
3. Setup your OpenAI config, using the `.env` file
4. Run the following command to get started:
```bash
python3 code_reviewer_template.py
```
5. Once you're happy with the response from the agents and no more changes are needed, reply with "exit"