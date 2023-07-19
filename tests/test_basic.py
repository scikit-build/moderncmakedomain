import pytest

@pytest.mark.parametrize("parallel", [0, 1, 2])
@pytest.mark.sphinx(
    "html",
    freshenv=True,
    confoverrides={"html_baseurl": "https://example.org/docs/", "language": "en"},
)
def test_simple_html(app, status, warning, parallel):
    app.warningiserror = True
    app.parallel = parallel
    app.build()
    local_pth = app.outdir / "local.html"
    external_pth = app.outdir / "external.html"

    with open(str(local_pth), encoding="utf-8") as f:
        local = f.read()

    with open(str(external_pth), encoding="utf-8") as f:
        external = f.read()

    print(local)
    assert 'href="#variable:MYVAR"' in local
    assert 'id="variable:MYVAR"' in local



