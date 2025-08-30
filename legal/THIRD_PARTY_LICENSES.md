Third‑Party Notices
-------------------
This product bundles third‑party components. Their licenses are
reproduced or referenced below. You must comply with their terms in
addition to the Apache License 2.0 that applies to SnapPDF's own code.

- PySide6 / Qt (LGPL‑3.0)
  Copyright (C) The Qt Company Ltd and other contributors
  License: GNU Lesser General Public License v3.0
  https://www.qt.io/     | https://www.qt.io/licensing/
  https://doc.qt.io/qt-6/lgpl.html

- PyAutoGUI (BSD 3‑Clause)
  Copyright (c) 2014, Al Sweigart
  https://github.com/asweigart/pyautogui
  License: BSD 3‑Clause
  https://github.com/asweigart/pyautogui/blob/master/LICENSE.txt

- img2pdf (MIT)
  Copyright (c) 2010-2024 Dirk Holtwick
  https://gitlab.mister-muffin.de/josch/img2pdf
  License: MIT
  https://gitlab.mister-muffin.de/josch/img2pdf/-/blob/master/LICENSE

- keyboard (MIT)
  Copyright (c) Boppreh
  https://github.com/boppreh/keyboard
  License: MIT
  https://github.com/boppreh/keyboard/blob/master/LICENSE.txt

- Pillow (PIL License / HPND variant)
  Copyright (c) 1995-2011 Fredrik Lundh and Contributors
  https://python-pillow.org/
  License: Historical Permission Notice and Disclaimer (HPND)‑like
  https://github.com/python-pillow/Pillow/blob/main/LICENSE

- pytest (MIT) [development/testing]
  Copyright (c) Holger Krekel and others
  https://docs.pytest.org/
  License: MIT
  https://github.com/pytest-dev/pytest/blob/main/LICENSE

LGPL Compliance Note (PySide6/Qt)
---------------------------------
When distributing builds that include Qt/PySide6 libraries:
- Provide the LGPL‑3.0 license text and attribution (as above).
- Do not statically link Qt components; allow users to replace the LGPL
  libraries (typical for Python wheels/dlls included by PyInstaller).
- Provide any modifications to LGPL components under the same license.

If any attribution, link, or license text above is incomplete or out of
date, please open an issue or pull request to update this file.