KNOWLEDGE_INDEX_NAME = "knowledge"
KNOWLEDGE_INDEX_SETTINGS = {
    "settings": {
        "refresh_interval": "1s",
        "analysis": {
            "filter": {
                "english_stop": {"type": "stop", "stopwords": "_english_"},
                "english_stemmer": {"type": "stemmer", "language": "english"},
                "english_possessive_stemmer": {"type": "stemmer", "language": "possessive_english"},
                "russian_stop": {"type": "stop", "stopwords": "_russian_"},
                "russian_stemmer": {"type": "stemmer", "language": "russian"},
                "custom_stopwords": {
                    "type": "stop",
                    "stopwords": "а,без,более,бы,был,была,были,было,быть,в,вам,вас,весь,во,вот,все,всего,всех,вы,где,да,даже,для,до,его,ее,если,есть,еще,же,за,здесь,и,из,или,им,их,к,как,ко,когда,кто,ли,либо,мне,может,мы,на,надо,наш,не,него,нее,нет,ни,них,но,ну,о,об,однако,он,она,они,оно,от,очень,по,под,при,с,со,так,также,такой,там,те,тем,то,того,тоже,той,только,том,ты,у,уже,хотя,чего,чей,чем,что,чтобы,чье,чья,эта,эти,это,я,a,an,and,are,as,at,be,but,by,for,if,in,into,is,it,no,not,of,on,or,such,that,the,their,then,there,these,they,this,to,was,will,with",  # noqa: E501
                },
            },
            "analyzer": {
                "ru_en": {
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "english_stop",
                        "english_stemmer",
                        "english_possessive_stemmer",
                        "russian_stop",
                        "russian_stemmer",
                        "custom_stopwords",
                    ],
                }
            },
        },
    },
    "mappings": {
        "dynamic": "strict",
        "properties": {
            # ID сообщения
            "id": {"type": "keyword"},
            # ID  автора сообщения
            "author_id": {"type": "long"},
            # Имя автора сообщения
            "author_first_name": {"type": "keyword"},
            # Фамилия автора сообщения
            "author_last_name": {"type": "keyword"},
            # Логин автора сообщения
            "author_login": {"type": "keyword"},
            # ID канала куда опубликовали сообщение
            "published_channel_id": {"type": "long"},
            # ID опубликованного в канале сообщения
            "published_message_id": {"type": "long"},
            # ID текст сообщения
            "text": {"type": "text", "analyzer": "ru_en"},
            # Теги сообщения TODO: пока что не используется никак
            "tags": {"type": "text", "analyzer": "ru_en"},
            # Время публикации сообщения
            "timestamp": {"type": "date", "format": "date_optional_time||epoch_millis"},
        },
    },
}
