import random
from datetime import date
from flask import session

class Toolbox:
    def __init__(self, item, img, description, service):
        self.item = item
        self.img = img
        self.description = description
        self.service = service


python = Toolbox(item="Python", img="pyhon-con", description="#", service="backend")

backend_toolbox = [python]




class Project:
    def __init__(self, title, subtitle, description, date, link, url_for, link_title, tags, image, alt="Project image", blank=False):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.link = link
        self.url_for = url_for
        self.link_title = link_title
        self.tags = tags
        self.image = image
        self.alt = alt
        self.blank = blank

data_science_tags = ["Data analysis", "Machine learning","Predictive modeling","Big data","Data visualization","Statistical analysis","Natural language processing (NLP)","Deep learning","Artificial intelligence (AI)","Data mining","Business intelligence","Time series analysis","Regression analysis","Cluster analysis","Decision trees","Random forests","Neural networks","Dimensionality reduction","Feature selection","Anomaly detection"]

front_end_tags = ["User Interface (UI) Design", "User Experience (UX) Design","Web Design","Responsive Design","HTML","CSS","JavaScript","jQuery","Bootstrap","Material Design","Typography","Color Theory","Layout Design","Grid Systems","Mobile Design","Accessibility","Cross-browser Compatibility","Performance Optimization","Web Standards","Visual Design"]

back_end_tags = ["Server-side programming languages (e.g. Python, Java, Ruby, Node.js)","Web frameworks (e.g. Django, Flask, Ruby on Rails, Express.js)","Database management systems (e.g. SQL, NoSQL)","APIs (Application Programming Interfaces)","REST (Representational State Transfer) API design","Authentication and Authorization","Web Security (e.g. HTTPS, SSL, TLS)","Caching (e.g. Redis, Memcached)","DevOps (e.g. Continuous Integration, Continuous Deployment)","Cloud Services (e.g. Amazon Web Services, Google Cloud Platform)","Microservices","Message Queuing","Load Balancing","Scalability","Performance Optimization","Serverless Architecture","Content Management Systems (e.g. WordPress, Drupal)","Version Control (e.g. Git, SVN)","Debugging and Testing","Software Architecture and Design Patterns"]




tip_redistribution_proj = Project("Examining the Effectiveness of Tip Redistributing in the Casino Industry", "A Data-Driven Approach Revisiting The Impact of Current Tipping Practices", "This case study examines the mandatory tip sharing practices among Blackjack and Craps dealers at Ameristar Casino.", "January 2023", link=None, url_for='projects.tip_redistribution', link_title="View Case Study", image="static/images/projects/tip_redistribution.png", alt="Tip Redistribution Image", tags=["Case Study", "Data Analysis", "ChartJS", "Business intelligence"])

periodic_table_proj = Project("Interactive Periodic Table of Elements", "subtitle tbd", "Description tbd", "January 2023", link=None, url_for='projects.periodic_table', link_title="Go To Table", image="static/images/projects/periodic_table.png", alt="Periodic Table Image", tags=["Interactive", "UI", "UX", "Database Management"])

gamblers_fallacy_proj = Project("The Gambler's Fallacy", "When the Past Fools You into Thinking You Can Predict the Future", "The gambler's fallacy is the mistaken belief that past events in a random process influence future outcomes, despite the probabilities being independent of each other.", date="2022", link="https://github.com/ZSturman/Gamblers-Fallacy--Roulette", url_for=None, link_title="Repository", image="static/images/projects/gamblers_fallacy.png", alt="Gambler's Fallacy Image", tags=["Python", "Simulation"], blank=True)

productivity_app_proj = Project("Productivity App", "subtitle", "Crafting intelligent solutions through programming and data", date="2022", link="https://github.com/ZSturman/Flask-Productivity-App", url_for=None, link_title="Repository", image="static/images/projects/productivity_app.png", alt="Productivity Image", tags=["Flask", "SQL", "NGINX"], blank=True)





project5 = Project(title="Fictional Heros and Villians Battle", subtitle="subtitle", description="Randomly select or choose for yourself characters to battle against each other and see who wins from all the fictional universes", date="2023", link="#", url_for=None, link_title="link title", image="img", tags=["Temp"])

project6 = Project(title="Financial Dashboard", subtitle="subtitle", description="description", date="2022", link="#", url_for=None, link_title="link title", image="img", tags=["Temp"])

project7 = Project(title="Deeptime Dashboard", subtitle="subtitle", description="description", date="2022", link="#", url_for=None, link_title="link title", image="img", tags=["Temp"])

project8 = Project(title="Streamlit Test", subtitle="subtitle", description="description", date="2022", link="https://zsturman-streamlit-test-myapp-vnqhbk.streamlit.app/", url_for=None, link_title="Streamlit Test", image="img", tags=["Temp"], blank=True)

project9 = Project(title="Title", subtitle="subtitle", description="description", date="2022", link="#", url_for=None, link_title="link title", image="img", tags=["Temp"])

projects_list = [tip_redistribution_proj, periodic_table_proj, gamblers_fallacy_proj, productivity_app_proj]





class Review:
    def __init__(self, review, name, business):
        self.review = review
        self.name = name
        self.business = business
        img_name = name.replace(" ","_").lower()
        self.img = "../static/images/reviews/"+img_name+".jpeg"

review1 = Review("As a Python beginner, I appreciated Zachary's patience and clear explanations. Zachary helped me understand complex concepts and execute a successful project.", "Frew Arega", "Freelancer")
review2 = Review("Working with Zachary on our data visualization project was a pleasure. The final product exceeded our expectations and was delivered on time.", "Shawn Victor", "Ameristar Casino")
review5 = Review("The data visualizations created by Zachary for our team were outstanding. They were not only visually appealing but also effectively conveyed the key insights.", "John McDonald", "The Knife Grinder")
review6 = Review("I was pleased with Zachary's professionalism throughout our data analysis project. Communication was prompt and results were delivered as promised.", "Joshua Temple", "Independence Phone Co.")
review7 = Review("I was impressed by Zachary's expertise in data cleaning and analysis. The results were presented in an organized and easy-to-understand way.", "Corey Monsdeoca", "Sheriff Mo")
review8 = Review("Working with Zachary on our data analysis project was a seamless experience. Zachary was able to turn our raw data into meaningful insights with ease.", "Crystal Lor", "Alaskan Bar Tokes")

reviews_list = [review1, review2, review5, review6, review7, review8]

email_body_list = "Hi Zachary,%0D%0A%0D%0A I am interested in learning more about your services and would appreciate it if you could share with me more information on the projects you've worked on, your rates, and availability.%0D%0A%0D%0A Thank you for your time and I look forward to hearing back from you soon."

mailing_list_txt_list= ["Unlock the secrets to better data-driven decisions with exclusive insights and analysis", "Sign up now for personalized tips delivered straight to your inbox", "Join Zachary's community of data science enthusiasts and receive the latest news, tutorials, and case studies in your inbox", "Be the first to know the latest breakthroughs in data science - sign up for Zachary's newsletter now"]

email_subject_line = 'Request for Data Science/ Data Analysis Information'

call_to_action_list = ["Discover what I can do", "Collaborate with me", "Let's start a project", "Explore my portfolio", "Find out how I can help", "Let's create something great", "See my work in action", "Let's work together"]


today = date.today()


def portfolio_context_processor(config):
    dev_test = config.DEV_TEST
    dev_status = config.DEV_STATUS
    mailing_list_txt = random.choice(mailing_list_txt_list)
    call_to_action_txt = random.choice(call_to_action_list)
    current_date = today.strftime("%B %d, %Y")
    subscribed = session.get('subscribed', False)
    return {'dev_test': dev_test, 'dev_status':dev_status, 'mailing_list_txt':mailing_list_txt, 'email_body_list':email_body_list, 'email_subject_line':email_subject_line, 'call_to_action_txt':call_to_action_txt, 'reviews_list':reviews_list, 'projects_list':projects_list, "current_date":current_date, "subscribed":subscribed, "backend_toolbox":backend_toolbox}