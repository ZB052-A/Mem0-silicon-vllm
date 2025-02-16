import os
from typing import Optional

from openai import OpenAI

from mem0.configs.embeddings.base import BaseEmbedderConfig
from mem0.embeddings.base import EmbeddingBase


class SiliconCloudEmbedding(EmbeddingBase):
    def __init__(self, config: Optional[BaseEmbedderConfig] = None):
        super().__init__(config)

        self.config.model = self.config.model or "BAAI/bge-m3"
        self.config.embedding_dims = self.config.embedding_dims or 1024

        # Custom base URL without API Key requirement
        self.client = OpenAI(
            api_key="",
            base_url="https://api.siliconflow.cn/v1",
        )

    def embed(self, text):
        """
        Get the embedding for the given text using OpenAI.

        Args:
            text (str): The text to embed.

        Returns:
            list: The embedding vector.
        """
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input=[text], model=self.config.model).data[0].embedding