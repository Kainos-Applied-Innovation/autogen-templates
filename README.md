# 🔮 Autogen Templates
Guide for how to create your own Autogen agents. Check the [Microsoft repo](https://github.com/microsoft/autogen/tree/main) for the latest updates.


## 📝 Note

Microsoft's Research team is making rapid progress with this new open source tool and are regularly adding features.

As a result, this repo may become a little out-of-date over time as they continue to make changes. If you encounter any errors, you should check their GitHub repo first.

You should also consider ugrading to their latest version of Autogen, as they add new capabilities.

The following instructions are for 🍎 Mac users, but there should be a lot of similarity for Windows users.



## 🎬 Before you get started

You should have Python installed on your Mac. Then download this repo.

You should also decide what model you want to use. This can be changed later, but if you want to use:


### Azure OpenAI (recommended)
1. Open the Azure portal
2. Create a new Azure OpenAI resource, if you haven't made one already
3. Open the Azure OpenAI Playground
4. Deploy a GPT model and give it a name (you'll use this name later). I recommend starting with the GPT-3.5-turbo model
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


### OpenAI platform (not recommended)

You can also create a key within the OpenAI platform and access the GPT models that way.

For security reasons, especially with company data, it's not recommended.



## 💻 Setup

To get started:
1. Open the Finder app on your Mac
2. Find where you've downloaded this repo
3. Right click on the folder and click on "New Terminal at Tab"
4. The terminal window will open for that folder
5. Install all the required plugins:
```bash
pip install -r requirements.txt
```
6. Make sure that the `.env` file has been set up, using the steps in the previous section
7. Run the following command to get started:
```bash
python3 code_reviewer_template.py
```
8. Once you're happy with the response from the agents and no more changes are needed, reply with "exit". If you need to, you can use the `CONTROL KEY + C` on Mac to immediately stop the process



## 💡 Examples

Below are ideas on how you could use Autogen agents to help you:

- Code review agents
    - Check code for bugs, security, performance issues and suggest improvements
- Feedback and improvement loop
    - Check text for errors and suggest improvements
    - Add those improvements to the original text
    - E.g. text, emails, social media posts
- Generate a GOV.UK error message for a situation where ...
    - Should follow the WCAG 2.1 accessibility guidelines
    - Messages should be concise and easily understood
- Brainstorming sessions
    - Would likely require a bit more prompting, since you'll want to avoid the generic answers from GPT
    - You could collaborate with several bots and iterate on ideas, since we can have a human-in-the-loop
- Generate alt text for an image that features ...
    - Do not start with "Image of"



## ⚠️ General Advice

The Generative AI industry is changing rapidly and new tools are being released every week. 

You should check the Generative AI page on Sharepoint for the latest advice and best practices.



## 💬 Prompt Advice

To write good prompts, we need to use the model's training dataset to our advantage. Remember that these LLMs have been trained on thousands of books, online posts, Wikipedia articles etc.

### Autogen Roles
When you're creating a Role for an Autogen agent, you should:
- Include the agent's name
    - This might help with agent selection
- Describe what the agent should and shouldn't do
- Outline any output you want to get back
- Consider adding a sentence at the end, which tells the agent what other bot it should talk to
    - e.g. For the Recommendation bot, it's told to "Collaborate with the Summariser" bot and will then write a summary based on the Recommendation bot's message

### Make the model "listen" to you

If you're finding that the model does not do what you want, despite explicitly telling it in the prompt, then you can try a few things:
- Write your important command in all caps
    - e.g. "DO NOT INCLUDE ANY JSON IN YOUR RESPONSE"
    - Research shows that models respond better to this, since they interpret it as though you are shouting
    - This makes sense, since people would normally write like this in books and online posts - which is what the model was trained on
- Write your important command at the end of the prompt
    - LLMs have issues with attention. Sometimes text in a section will throw them off-course and lead to weird results
    - Putting it at the end means they're more likely to do it



## 📞 Feedback

We're making regular improvements to the templates and are keen to hear your feedback.

Feel free to drop us a message if you have any:
- suggestions on what can be improved
- spotted a bug that needs fixed
- ideas on templates that could be useful
- ... or anything else that comes to mind



## 🔨 Contributors
Liam McCormick - development