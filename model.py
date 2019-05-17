from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document, analyzer, Integer, Text, Index


elastic_search = Elasticsearch(hosts=['localhost'])
second_try = Index('second_try', using=elastic_search)
second_try.delete(ignore=404)
second_try.create()
analyzer = analyzer('simple',
                    tokenizer="standard",
                    filter=["russian_stop", "lowercase", "russian_stemmer"],
                    )


@second_try.document
class NewDocument(Document):
    file_name = Integer()
    title = Text(analyzer=analyzer)
    text = Text(analyzer=analyzer)

    class Index:
        name = 'second_try'
