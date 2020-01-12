from demo.apps.core.renderers import demoJSONRenderer


class ArticleJSONRenderer(demoJSONRenderer):
    object_label = 'article'
    pagination_object_label = 'articles'
    pagination_count_label = 'articlesCount'


class CommentJSONRenderer(demoJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
