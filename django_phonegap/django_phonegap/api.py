from django.contrib.auth import get_user_model

from tastypie.models import ApiKey
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.resources import ModelResource
from tastypie.exceptions import BadRequest

from django_phonegap.corsresource import CorsResourceBase


User = get_user_model()


class LoginResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ["first_name", "last_name", "username",]
        allowed_method = ['get']
        resource_name = 'login'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()


#"7d18024c1b6e42c0134f09bed774ed8da47f6975"

    def dehydrate(self, bundle):
        username = bundle.data.get('username')
        user = User.objects.get(username=username)
        bundle.data['api_key'] = ApiKey.objects.get_or_create(user=user)[0].key
        return bundle
