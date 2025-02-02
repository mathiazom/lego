from django.conf import settings
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from lego.apps.companies.models import Company
from lego.apps.email.models import EmailList
from lego.apps.meetings.models import Meeting
from lego.apps.notifications.models import Announcement
from lego.apps.permissions.constants import CREATE, LIST
from lego.apps.polls.models import Poll
from lego.apps.quotes.models import Quote
from lego.apps.surveys.models import Survey
from lego.apps.users.models import AbakusGroup, Penalty, User


class SiteMetaViewSet(viewsets.ViewSet):

    permission_classes = [permissions.AllowAny]

    def list(self, request):
        user = request.user
        site_meta = settings.SITE

        # Allow non-logged in users to see these as well:
        allow_anonymous_entities = ["events", "articles", "joblistings", "galleries"]

        # Whereas these require that a user has keyword permissions:
        permission_entities = {
            "companies": (Company, LIST),
            "meetings": (Meeting, LIST),
            "polls": (Poll, LIST),
            "quotes": (Quote, LIST),
            "interest_groups": (AbakusGroup, LIST),
            # Admin:
            "bdb": (Company, CREATE),
            "announcements": (Announcement, CREATE),
            "penalties": (Penalty, CREATE),
            "surveys": (Survey, CREATE),
            "groups": (AbakusGroup, CREATE),
            "email": (EmailList, CREATE),
            "users": (User, CREATE),
        }

        is_allowed = {entity: True for entity in allow_anonymous_entities}
        for entity, (model, permission) in permission_entities.items():
            is_allowed[entity] = user.has_perm(permission, model)

        return Response({"site": site_meta, "is_allowed": is_allowed})
