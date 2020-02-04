from ..core.renderers import demoJSONRenderer


class NoticeJSONRenderer(demoJSONRenderer):
    object_label = "notifications"
    pagination_object_label = "notice"
    pagination_count_label = "notice_count"
