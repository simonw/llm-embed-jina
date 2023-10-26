import llm


def test_jina_embed_small():
    model = llm.get_embedding_model("jina-embeddings-v2-small-en")
    floats = model.embed("hello world")
    assert len(floats) == 512
    assert all(isinstance(f, float) for f in floats)
