import django
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


django.setup()


# with open('universities.json') as f:
#     data = json.load(f)

#     for i in data:
#         print(i)
#         uni = Univeristy.objects.create(name=i['name'], country=i['country'])

#         for j in i['domains']:
#             print(j)
#             domain = Domain.objects.create(university=uni, domain=j)
#             domain.save()


def validate_email(email):
    domain = email.split("@")[1]
    print(domain)

    with open("universities.json") as f:
        data = json.load(f)
    for uni in data:
        if domain in uni["domains"]:
            return {
                "valid": True,
                "university": uni,
            }
    return {"valid": False}


res = validate_email("fa19m2bq040@iub.edu.pk")
print(res)
