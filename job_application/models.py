from django.db import models


class ApplicationFormModel(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    date = models.DateField("start date")
    occupation = models.CharField(max_length=80)

    def __str__(self) -> dict:
        applicant = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date": self.date,
            "occupation": self.occupation,
        }
        return applicant
