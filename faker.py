import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dataAnalytics.settings')

import django
django.setup()
#FAKE POP SCript
import random
from  StudentProfiler.models import Students
# topics=['Search','Social','MarketPlace','News','Games',]
# def add_topic():
#     t=Topics.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
#
# def populate(n=5):
#    for entry in range(n):
#     topic=add_topic()
#
#     webpages=WebPage.objects.get_or_create(topic=topic,name=fakegen.company(),url=fakegen.url())[0]
#     webpages.save()
#     access=AccessRecord.objects.get_or_create(name=webpages,date=fakegen.date())[0]
#     access.save()
# def populate(n=5):
#     for i in range(n):
#         users=Users.objects.get_or_create(firstName=fakegen.first_name(),lastName=fakegen.last_name(),email=fakegen.email())[0]
#
#
#
category=['low','medium','high']


def populate():
    for i in range(60):
        if i<=8:
            s=Students.objects.create(UID="15-"+"CMPN"+"B0"+str(i+1)+"-19",subject="DS",category=random.choice(category))
        else:
            s=Students.objects.create(UID="15-"+"CMPN"+"B"+str(i+1)+"-19",subject="DS",category=random.choice(category))
        s.save()
if __name__=='__main__':
     print('populating')
     populate()
     print('populated')
