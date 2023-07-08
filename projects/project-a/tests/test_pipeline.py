def test_pipeline_run(capsys):
    from src.pipeline import Pipeline

    pipeline = Pipeline()
    pipeline.run()

    actual = capsys.readouterr().out
    expected = "Running pipeline A\n"

    assert actual == expected
