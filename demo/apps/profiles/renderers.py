from demo.apps.core.renderers import demoJSONRenderer


class ProfileJSONRenderer(demoJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
