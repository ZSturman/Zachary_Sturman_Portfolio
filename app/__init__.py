import random
from flask import Flask, session
from flask_mail import Mail, Message

class Review:
    def __init__(self, review, name, business):
        self.review = review
        self.name = name
        self.business = business
        img_name = name.replace(" ","_").lower()
        self.img = "../static/images/reviews/"+img_name+".jpeg"

review1 = Review("As a Python beginner, I appreciated Zachary's patience and clear explanations. Zachary helped me understand complex concepts and execute a successful project.", "Frew Arega", "Freelancer")
review2 = Review("Working with Zachary on our data visualization project was a pleasure. The final product exceeded our expectations and was delivered on time.", "Shawn Victor", "Ameristar Casino")
review3 = Review("I was impressed by Zachary's skill with Python. The scripts Zachary wrote for our company have saved us a significant amount of time and effort.", "Walter Adams", "Ameristar Casino")
review4 = Review("As a manager, I appreciate Zachary's communication skills and ability to deliver results on time. Zachary is a true asset to any team.", "I'Ayala", "Penn Gaming")
review5 = Review("The data visualizations created by Zachary for our team were outstanding. They were not only visually appealing but also effectively conveyed the key insights.", "John McDonald", "The Knife Grinder")
review6 = Review("I was pleased with Zachary's professionalism throughout our data analysis project. Communication was prompt and results were delivered as promised.", "Joshua Temple", "Independence Phone Co.")
review7 = Review("I was impressed by Zachary's expertise in data cleaning and analysis. The results were presented in an organized and easy-to-understand way.", "Corey Monsdeoca", "Sheriff Mo")
review8 = Review("Working with Zachary on our data analysis project was a seamless experience. Zachary was able to turn our raw data into meaningful insights with ease.", "Crystal Lor", "Alaskan Bar Tokes")

reviews_list = [review1, review2, review3, review4, review5, review6, review7, review8]



call_to_action_list = ["Discover what I can do", "Collaborate with me", "Let's start a project", "Explore my portfolio", "Find out how I can help", "Let's create something great", "See my work in action", "Let's work together"]



email_body_list = "Hi Zachary,%0D%0A%0D%0A I am interested in learning more about your services and would appreciate it if you could share with me more information on the projects you've worked on, your rates, and availability.%0D%0A%0D%0A Thank you for your time and I look forward to hearing back from you soon."

mailing_list_txt_list= ["Unlock the secrets to better data-driven decisions with exclusive insights and analysis", "Sign up now for personalized tips delivered straight to your inbox", "Join Zachary's community of data science enthusiasts and receive the latest news, tutorials, and case studies in your inbox", "Be the first to know the latest breakthroughs in data science - sign up for Zachary's newsletter now"]









def create_app():
    app = Flask(__name__)

    mail = Mail()
    mail.init_app(app)

    from app.errors.handlers import errors
    from app.main.routes import main
    from app.projects.routes import projects
    from app.services.routes import services
    from app.mail.routes import zs_mail
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(services)
    app.register_blueprint(zs_mail)

    @app.context_processor
    def stuff():
        mailing_list_txt = random.choice(mailing_list_txt_list)
        email_subject_line = 'Request for Data Science/ Data Analysis Information'
        email_body = email_body_list
        subscribed = session.get('subscribed', False)
        dev_status = False
        dev_test = False
        return dict(mailing_list_txt = mailing_list_txt, email_subject_line=email_subject_line, email_body=email_body, reviews_list=reviews_list, subscribed=subscribed, dev_status=dev_status, dev_test=dev_test)











    return app