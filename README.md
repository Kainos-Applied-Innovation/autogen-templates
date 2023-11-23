# 🔮 Autogen Templates
Guide for how to create your own Autogen agents. Check the Microsoft repo for the latest updates.


## 📝 Note

Microsoft's Research team is making rapid progress with this new open source tool and are regularly adding features.

As a result, this repo may become a little out-of-date over time as they continue to make changes. If you encounter any errors, you should check their GitHub repo first.

You should also consider ugrading to their latest version of Autogen, as they add new capabilities.



## 🎬 Before you get started

You should decide what model you want to use. This can be changed later, but if you want to use:

### Azure OpenAI (recommended)
1. Open the Azure portal
2. Create a new Azure OpenAI resource, if you haven't made one already
3. Open the Azure OpenAI Playground
4. Deploy a GPT model and give it a name (you'll use this name later). I recommend starting with GPT-3.5-turbo 
5. Note your deployment settings. You'll need your:
- key
- base url 
- API version
- your model's deployment name
> You can find these details by opening the Chat Playground and clicking on "View Code"
6. Within this project's directory, rename the `.env.example` file to `.env`
7. Add your `key` and `base url`
8. Open the `code_reviewer_template.py` file
9. Modify the `config_list` variable. You should add your model's deployment name and the API version


### Open source models
For instructions on this, you can check for tutorials online.



## 💻 Setup

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



## 💡 Examples

Below are ideas on how you could use Autogen agents to help you:

- Code review agents
    - Check code for bugs, security, performance issues and suggest improvements
- Feedback and improvement loop
    - Check text for errors and suggest improvements
    - Add those improvements to the original text
    - E.g. text, emails, social media posts
- Brainstorming sessions
    - Would likely require a bit more prompting, since you'll want to avoid the generic answers from GPT
    - You could collaborate with several bots and iterate on ideas, since we can have a human-in-the-loop



## ⚠️ General Advice

The Generative AI industry is changing rapidly and new tools are being released every week. 

You should check the Generative AI page on Sharepoint for the latest advice and best practices.



## 📞 Feedback

We're making regular improvements to the templates and are keen to hear your feedback.

Feel free to drop us a message if you have any:
- suggestions on what can be improved
- spotted a bug that needs fixed
- ideas on templates that could be useful
- ... or anything else that comes to mind



## 🔨 Contributors
Liam McCormick - development