from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models

from quiz.get_username import get_username
from quiz.models import Question


class TF_Question(Question):
    user_id = models.CharField(default=get_username(), max_length=100, null=False, blank=False, editable=False)
    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Tick this if the question "
                                              "is true. Leave it blank for"
                                              " false."),
                                  verbose_name=_("Correct"))

    def check_if_correct(self, guess):
        if guess == "True":
            guess_bool = True
        elif guess == "False":
            guess_bool = False
        else:
            return False

        if guess_bool == self.correct:
            return True
        else:
            return False

    def get_answers(self):
        return [{'correct': self.check_if_correct("True"),
                 'content': 'True'},
                {'correct': self.check_if_correct("False"),
                 'content': 'False'}]

    def get_answers_list(self):
        return [(True, True), (False, False)]

    def answer_choice_to_string(self, guess):
        return str(guess)

    class Meta:
        verbose_name = _("True/False Question")
        verbose_name_plural = _("True/False Questions")
        ordering = ['category']