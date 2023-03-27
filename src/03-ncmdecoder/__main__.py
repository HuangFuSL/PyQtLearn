import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QWidget

from .decrypt import process_file


class Main(QWidget):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    default_path = sys.argv[1] if len(sys.argv) > 1 else "."
    main = Main()
    file = QFileDialog.getOpenFileNames(
        main, "Open NCM", default_path, "NCM (*.ncm)"
    )
    path = QFileDialog.getExistingDirectory(main, "Save to", default_path)
    for _ in file[0]:
        process_file(_, path)
    main.close()
