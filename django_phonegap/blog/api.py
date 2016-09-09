from django.contrib.auth import get_user_model

from tastypie.models import ApiKey
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.resources import ModelResource
from tastypie.exceptions import BadRequest
from tastypie.validation import FormValidation, Validation

from django_phonegap.corsresource import CorsResourceBase
from .models import Posting
from .forms import PostingForm
import json

User = get_user_model()


class PostingValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        for key, value in bundle.data.items():
            if not isinstance(value, basestring):
                continue

            if key == "url":
                if not 'youtube.com' in value: #or "vimeo.com" in value :
                    print value
                    print "Bad Request"
                    errors[key] = 'Sumitted Need To Be YOUTUBE URL.'

        return errors


class PostingResource(CorsResourceBase,ModelResource):
    class Meta:
        queryset = Posting.objects.all()
        fields = ["user", "title", "url", "id"]
        allowed_method = ['get', "post"]
        resource_name = 'posting'
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()
        validation = PostingValidation()

    def get_object_list(self, request):
        return super(PostingResource, self).get_object_list(request).filter(user=request.user)

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle

"""
    def obj_create(self, bundle, request=None, **kwargs):
        bundle = super(PostingResource, self).obj_create(bundle, kwargs)
        try:
            bundle.obj.user = bundle.request.user
            bundle.obj.title = bundle.data.get('title')
            bundle.obj.url = bundle.data.get("url")
            bundle.obj.save()
        except:
            raise BadRequest("Some error with your data")
        return bundle
"""

#curl -v -X POST -d '{"title": "hello there", "url": ="https://www.youtube.com/watch?v=3cS964_AlMY"}' -H "Authorization: ApiKey galaxy:7d18024c1b6e42c0134f09bed774ed8da47f6975" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/


#galaxy
#7d18024c1b6e42c0134f09bed774ed8da47f6975
#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey galaxy:7d18024c1b6e42c0134f09bed774ed8da47f6975" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/

#star
#72c64eebc15bd67b20fa9d7211e223169c727ecf
#curl -v -X POST -d '{"post": "hello there"}' -H "Authorization: ApiKey star:72c64eebc15bd67b20fa9d7211e223169c727ecf" -H "Content-Type: application/json" http://127.0.0.1:8000/api/v1/posting/






#star
#

#    def dehydrate(self, bundle):
#        username = bundle.data.get('username')
#        user = User.objects.get(username=username)
#        bundle.data['api_key'] = ApiKey.objects.get_or_create(user=user)[0].key
#        return bundle
