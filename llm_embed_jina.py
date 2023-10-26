import llm
from transformers import AutoModel

MAX_LENGTH = 8192


@llm.hookimpl
def register_embedding_models(register):
    for model_id in (
        "jina-embeddings-v2-small-en",
        "jina-embeddings-v2-base-en",
        "jina-embeddings-v2-large-en",
    ):
        register(JinaEmbeddingModel(model_id))


class JinaEmbeddingModel(llm.EmbeddingModel):
    def __init__(self, model_id):
        self.model_id = model_id
        self._model = None

    def embed_batch(self, texts):
        if self._model is None:
            self._model = AutoModel.from_pretrained(
                "jinaai/{}".format(self.model_id), trust_remote_code=True
            )
        results = self._model.encode([text[:MAX_LENGTH] for text in texts])
        return (list(map(float, result)) for result in results)
