from pathlib import Path


def test_download_writes_pdf(monkeypatch, tmp_path):
    from app.utils import download as download_mod

    # Prepare a temporary captures folder with dummy png paths
    captures = tmp_path / "captures"
    captures.mkdir()
    # Create fake image files (empty is fine since we mock img2pdf.convert)
    for i in range(1, 4):
        (captures / f"screenshot_{i}.png").write_bytes(b"PNG")

    # Capture data written to the output file
    converted_args = {"paths": None}

    def fake_convert(paths):
        converted_args["paths"] = list(paths)
        return b"%PDF-1.7\n%...mock...\n%%EOF\n"

    monkeypatch.setattr(download_mod.img2pdf, "convert", fake_convert)

    output_pdf = tmp_path / "output.pdf"

    download_mod.download(captures_folder=captures, output_file=output_pdf)

    # Ensure convert got the expected list of image paths
    assert converted_args["paths"] is not None
    assert all(p.endswith(".png") for p in converted_args["paths"])
    assert len(converted_args["paths"]) == 3

    # Ensure output file exists and contains mock PDF bytes
    assert output_pdf.exists()
    assert output_pdf.read_bytes().startswith(b"%PDF")
