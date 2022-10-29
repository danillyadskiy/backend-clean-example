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
            "author_first_name": {"type": "text", "analyzer": "ru_en"},
            # Фамилия автора сообщения
            "author_last_name": {"type": "text", "analyzer": "ru_en"},
            # Логин автора сообщения
            "author_login": {"type": "text", "analyzer": "ru_en"},
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
