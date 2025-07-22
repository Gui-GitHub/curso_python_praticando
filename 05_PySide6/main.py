from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem, QLabel
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from styles import setupTheme

class ToDoMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tarefas")
        self.setMinimumSize(400, 500)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Entrada de nova tarefa
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Digite uma nova tarefa...")
        self.task_input.returnPressed.connect(self.add_task)  # Adiciona ao pressionar Enter

        add_button = QPushButton("Adicionar")
        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)

        # Informação didática sobre edição
        info_label = QLabel("Dica: Dê dois cliques em uma tarefa para editar.")
        main_layout.addWidget(info_label)

        # Lista de tarefas
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.edit_task)  # Edita ao duplo clique

        # Botão para remover tarefa selecionada
        remove_button = QPushButton("Remover Selecionada")
        remove_button.clicked.connect(self.remove_task)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(remove_button)

        # Campo de edição de tarefa (oculto por padrão)
        self.edit_input = QLineEdit()
        self.edit_input.setPlaceholderText("Edite a tarefa e pressione Enter")
        self.edit_input.hide()
        main_layout.addWidget(self.edit_input)
        self.edit_input.returnPressed.connect(self.save_edit)

        self._editing_item = None

    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(item)
            self.task_input.clear()

    def edit_task(self, item):
        self._editing_item = item
        self.edit_input.setText(item.text())
        self.edit_input.show()
        self.edit_input.setFocus()

    def save_edit(self):
        if self._editing_item and self.edit_input.text().strip():
            self._editing_item.setText(self.edit_input.text().strip())
        self.edit_input.hide()
        self._editing_item = None

    def remove_task(self):
        for item in self.task_list.selectedItems():
            self.task_list.takeItem(self.task_list.row(item))

if __name__ == "__main__":
    app = QApplication([])
    setupTheme()
    window = ToDoMainWindow()
    window.show()
    app.exec()
