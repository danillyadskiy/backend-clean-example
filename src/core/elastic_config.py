import json

from elasticsearch import AsyncElasticsearch

from core.config import ROOT_DIR, SETTINGS

es_client = AsyncElasticsearch(hosts=[SETTINGS.elastic_host])

KNOWLEDGE_INDEX_NAME = "knowledge"
TEST_INDEX_NAME = "test"

KNOWLEDGE_INDEX_SETTINGS = json.load(open(f"{ROOT_DIR}/resources/elastic/knowledge_index_settings.json"))
TEST_INDEX_SETTINGS = json.load(open(f"{ROOT_DIR}/resources/elastic/test_index_settings.json"))
