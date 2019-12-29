import os



# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_webpage.settings')


import django
# Import settings
django.setup()
import random
from blog.models import BlogPost
from faker import Faker
from django.contrib.auth.models import User

fake = Faker()
topics = ['E', 'K', 'M']
k = User.objects.all()


def populate(n=5):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(n):
        fake_text = fake.texts(nb_texts=6, max_nb_chars=1000, ext_word_list=None)
        #fake_creator = random.choice(User)
        #print(fake_creator)
        fake_t_a = random.choice(topics)
        fake_title = fake.texts(nb_texts=1, max_nb_chars=19, ext_word_list=None)
        fake_overview = fake.texts(nb_texts=3, max_nb_chars=50, ext_word_list=None)
        p = BlogPost.objects.get_or_create(text=fake_text, target_age=fake_t_a, title=fake_title, overview=fake_overview, creator=random.choice(k))[0]


if __name__ == "__main__":
    print("populating ...")
    populate(30)
    print("population completed.")

