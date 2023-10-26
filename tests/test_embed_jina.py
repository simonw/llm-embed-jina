from click.testing import CliRunner
from llm.cli import cli
import llm


def test_jina_embed_small():
    model = llm.get_embedding_model("jina-embeddings-v2-small-en")
    floats = model.embed("hello world")
    assert len(floats) == 512
    assert all(isinstance(f, float) for f in floats)


def test_jina_embed_long_string():
    model = llm.get_embedding_model("jina-embeddings-v2-small-en")
    outputs = list(model.embed_multi(["a" * 9000, "two"]))
    for floats in outputs:
        assert len(floats) == 512


def test_jina_embed_multi(tmpdir):
    db_path = str(tmpdir / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "embed-multi",
            "-m",
            "jina-embeddings-v2-small-en",
            "test",
            "-",
            "-d",
            db_path,
        ],
        input='[{"id": "a", "text": "abc"}]',
        catch_exceptions=False,
    )
    assert result.exit_code == 0
