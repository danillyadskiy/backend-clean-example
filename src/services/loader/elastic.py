from typing import Any, Dict, List

from elasticsearch import Elasticsearch


class ElasticSearchLoader:
    def __init__(self, connection: Elasticsearch) -> None:
        self.connection = connection

    def create_mapping(self, index_name: str, body: Dict[str, Any]) -> None:
        if not self.connection.indices.exists(index_name):
            self.connection.indices.create(index=index_name, body=body)

    def delete_index(self, index_name: str) -> None:
        if self.connection.indices.exists(index_name):
            self.connection.indices.delete(index_name)

    def upload_index_data(self, data: List[Dict[str, str]]) -> Dict[str, Any]:
        return self.connection.bulk(body=data, request_timeout=3600)
