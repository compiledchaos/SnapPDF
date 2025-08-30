import types

def test_start_triggers_click_and_capture(monkeypatch, tmp_path):
    # Lazy import inside test to ensure monkeypatches take effect in module namespace
    from app.utils import start as start_mod

    calls = {
        "auto_click": [],
        "capture_screen": [],
        "pg_click": [],
        "sleep": [],
    }

    def fake_auto_click(click_method, key):
        calls["auto_click"].append((click_method, key))

    def fake_capture_screen(path, region=None):
        calls["capture_screen"].append((str(path), tuple(region) if region else None))

    def fake_pg_click(**kwargs):
        calls["pg_click"].append(kwargs)

    def fake_sleep(seconds):
        calls["sleep"].append(seconds)

    # Patch dependencies in the start module namespace
    monkeypatch.setattr(start_mod, "auto_click", fake_auto_click)
    monkeypatch.setattr(start_mod, "capture_screen", fake_capture_screen)
    monkeypatch.setattr(start_mod, "time", types.SimpleNamespace(sleep=fake_sleep))
    monkeypatch.setattr(start_mod, "pg", types.SimpleNamespace(click=fake_pg_click))

    output_dir = tmp_path / "captures"

    # Inputs
    num_clicks = 3
    click_method = "Key"  # as used by the app
    key = "right"
    region = (100, 200, 300, 400)  # x, y, w, h
    interval = 0.1

    start_mod.start(
        num_clicks=num_clicks,
        click_method=click_method,
        key=key,
        region=region,
        interval=interval,
        output_folder=str(output_dir),
    )

    # It should click once at region center before loop
    assert calls["pg_click"], "Expected an initial center click when region is provided"
    center_click = calls["pg_click"][0]
    assert center_click["x"] == region[0] + region[2] // 2
    assert center_click["y"] == region[1] + region[3] // 2

    # The loop should run num_clicks times
    assert len(calls["auto_click"]) == num_clicks
    assert len(calls["capture_screen"]) == num_clicks
    assert len(calls["sleep"]) == num_clicks

    # Validate parameters passed through
    for ac in calls["auto_click"]:
        assert ac == (click_method, key)

    for idx, (path, used_region) in enumerate(calls["capture_screen"], start=1):
        assert path.endswith(f"screenshot_{idx}.png")
        assert used_region == region
