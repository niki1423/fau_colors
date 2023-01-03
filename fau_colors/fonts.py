from pathlib import Path

from matplotlib import font_manager


def register_fausans_font():
    """Register the FAU Sans font.

    This function tries to register the FAU Sans font by scanning the common font directories.
    If the font is not found, it will throw an error.

    After successful registration, the font can be used in matplotlib by setting the following rcParams:
    >>> import matplotlib.pyplot as plt
    >>> plt.rcParams['font.family'] = 'sans-serif'
    >>> plt.rcParams['font.sans-serif'] = 'FAUSans Office'


    Raises
    ------
    FileNotFoundError
        If the font file is not found.

    """
    possible_paths = [
        Path("/Library/Fonts/FAUSansOffice-Regular.ttf"),  # macOS
        Path("/usr/share/fonts/truetype/fausans/FAUSansOffice-Regular.ttf"),  # Linux
        Path("C:/Windows/Fonts/FAUSansOffice-Regular.ttf"),  # Windows
    ]
    for path in possible_paths:
        if path.exists():
            font_manager.fontManager.addfont(path)
            print("Successfully registered FAU Sans font.")
            return

    raise FileNotFoundError(
        "Could not find 'FAUSansOffice-Regular.ttf' on your system. Please install it manually and try again."
    )
