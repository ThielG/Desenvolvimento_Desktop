import sqlite3
import sys
from datetime import datetime

from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QTableWidget, QAbstractItemView, \
    QPushButton, QLabel, QLineEdit, QWidget, QMessageBox, QTableWidgetItem


class EstoqueApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Controle de estoque')
        self.setWindowIcon(QtGui.QIcon('brown-box.png'))
        self.setGeometry(100, 100, 800, 400)

        self.conn = sqlite3.connect('estoque.db')
        self.cursor = self.conn.cursor()
        self.id_produto = None

        self.criar_tabela()

        layout_principal = QHBoxLayout()
        layout_esquerda = QVBoxLayout()
        layout_direita = QVBoxLayout()
        layout_botoes = QHBoxLayout()

        self.tbl_produtos = QTableWidget()
        self.tbl_produtos.verticalHeader().setVisible(False)
        self.tbl_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)

        layout_direita.addWidget(self.tbl_produtos)

        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_remover = QPushButton('Remover')
        self.btn_editar = QPushButton('Editar')

        layout_botoes.addWidget(self.btn_editar)
        layout_botoes.addWidget(self.btn_remover)

        self.lbl_nome = QLabel('Nome do produto')
        self.txt_nome = QLineEdit()
        self.lbl_preco = QLabel('Preço do produto')
        self.txt_preco = QLineEdit()
        self.lbl_quantidade = QLabel('Quantidade em estoque')
        self.txt_quantidade = QLineEdit()
        self.lbl_data = QLabel('Data de validade')
        self.txt_data = QLineEdit()
        self.lbl_categoria = QLabel('Categoria')
        self.txt_categoria = QLineEdit()
        self.lbl_fornecedor = QLabel('Fornecedor')
        self.txt_fornecedor = QLineEdit()

        layout_esquerda.addWidget(self.lbl_nome)
        layout_esquerda.addWidget(self.txt_nome)
        layout_esquerda.addWidget(self.lbl_preco)
        layout_esquerda.addWidget(self.txt_preco)
        layout_esquerda.addWidget(self.lbl_quantidade)
        layout_esquerda.addWidget(self.txt_quantidade)
        layout_esquerda.addWidget(self.lbl_data)
        layout_esquerda.addWidget(self.txt_data)
        layout_esquerda.addWidget(self.lbl_categoria)
        layout_esquerda.addWidget(self.txt_categoria)
        layout_esquerda.addWidget(self.lbl_fornecedor)
        layout_esquerda.addWidget(self.txt_fornecedor)
        layout_esquerda.addWidget(self.btn_cadastrar)
        layout_esquerda.addLayout(layout_botoes)

        layout_principal.addLayout(layout_esquerda)
        layout_principal.addLayout(layout_direita)

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

        self.btn_cadastrar.clicked.connect(self.inserir_produtos)
        self.btn_editar.clicked.connect(self.editar_produtos)
        self.btn_remover.clicked.connect(self.remover_produto)

        self.carregar_lista()

    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            preco REAL NOT NULL, 
                            quantidade INTEGER NOT NULL,
                            data_validade TEXT,
                            categoria TEXT,
                            fornecedor TEXT)''')

        self.conn.commit()

    def inserir_produtos(self):
        if self.validar_data() and self.validar_preco() and self.validar_quantidade() and self.validar_nome():
            if self.btn_cadastrar.text() == 'Cadastrar':
                try:
                    self.cursor.execute("INSERT INTO produtos (nome, preco, quantidade, data_validade, categoria, "
                                        "fornecedor) VALUES (?, ?, ?, ?, ?, ?)", (self.txt_nome.text(),
                                                                                  self.txt_preco.text(),
                                                                                  self.txt_quantidade.text(),
                                                                                  self.txt_data.text(),
                                                                                  self.txt_categoria.text(),
                                                                                  self.txt_fornecedor.text()))
                    self.conn.commit()
                    QMessageBox.information(self, 'Cadastro de produto', 'Produto cadastrado com sucesso!')
                    self.limpar_campos()
                    self.carregar_lista()

                except Exception as e:
                    print(e)
            else:
                try:
                    self.cursor.execute("UPDATE produtos SET nome = ?, preco = ?, quantidade = ?, data_validade = ?,"
                                        "categoria = ?, fornecedor = ? WHERE id = ?", (self.txt_nome.text(),
                                                                                      float(self.txt_preco.text()),
                                                                                      int(self.txt_quantidade.text()),
                                                                                      self.txt_data.text(),
                                                                                      self.txt_categoria.text(),
                                                                                      self.txt_fornecedor.text(),
                                                                                      self.id_produto))
                    self.conn.commit()
                    QMessageBox.information(self, 'Cadastro de produto', 'Produto atualizado com sucesso!')
                except sqlite3.Error as e:
                    QMessageBox.warning(self, 'Alerta', f'Não foi possivel atualizar o item. \nErro: {e}.')

                self.carregar_lista()
                self.limpar_campos()
                self.btn_cadastrar.setText('Cadastrar')
                self.btn_editar.setText('Editar')

    def remover_produto(self):
        item_atual = self.tbl_produtos.currentItem()

        if item_atual:
            self.id_produto = int(self.tbl_produtos.item(item_atual.row(), 0).text())
            resposta = QMessageBox.question(self, 'Confirmação', 'Deseja remover o pproduto?', QMessageBox.Yes |
                                            QMessageBox.No)
            if resposta == QMessageBox.Yes:
                self.cursor.execute("DELETE FROM produtos WHERE id = ?", (self.id_produto,))
                self.conn.commit()
                self.carregar_lista()
                self.limpar_campos()

        else:
            QMessageBox.warning(self, 'Alerta', 'Selecione um item a ser removido.')

    def editar_produtos(self):
        id_produto = None
        item_atual = self.tbl_produtos.currentItem()
        if self.btn_editar.text() == 'Editar':
            if item_atual:
                self.id_produto = int(self.tbl_produtos.item(item_atual.row(), 0).text())
                self.txt_nome.setText(self.tbl_produtos.item(item_atual.row(), 1).text())
                self.txt_preco.setText(self.tbl_produtos.item(item_atual.row(), 2).text())
                self.txt_quantidade.setText(self.tbl_produtos.item(item_atual.row(), 3).text())
                self.txt_data.setText(self.tbl_produtos.item(item_atual.row(), 4).text())
                self.txt_categoria.setText(self.tbl_produtos.item(item_atual.row(), 5).text())
                self.txt_fornecedor.setText(self.tbl_produtos.item(item_atual.row(), 6).text())
                self.btn_cadastrar.setText('Atualizar')
                self.btn_editar.setText('Cancelar')
            else:
                QMessageBox.warning(self, 'Aviso', 'Selecione um produto para editar.')
        else:
            self.limpar_campos()
            self.btn_cadastrar.setText('Cadastrar')
            self.btn_editar.setText('Editar')
            self.tbl_produtos.clearSelection()

    def carregar_lista(self):
        self.tbl_produtos.clear()
        self.cursor.execute('SELECT * FROM produtos')
        produtos = self.cursor.fetchall()
        colunas = ['ID', 'Nome', 'Preço', 'Quantidade', 'Validade', 'Categoria', 'Forncedor']
        self.tbl_produtos.setColumnCount(len(colunas))
        self.tbl_produtos.setHorizontalHeaderLabels(colunas)
        self.tbl_produtos.resizeColumnToContents(0)
        self.tbl_produtos.setRowCount(len(produtos))

        for linha, produto in enumerate(produtos):
            for coluna, valor in enumerate(produto):
                item = QTableWidgetItem(str(valor))
                self.tbl_produtos.setItem(linha, coluna, item)

        self.tbl_produtos.resizeColumnToContents(0)

    def limpar_campos(self):
        self.txt_nome.clear(),
        self.txt_preco.clear(),
        self.txt_quantidade.clear(),
        self.txt_data.clear(),
        self.txt_categoria.clear(),
        self.txt_fornecedor.clear()

    def validar_data(self):
        try:
            datetime.strptime(self.txt_data.text(), '%d/%m/%Y')
            return True

        except:
            QMessageBox.warning(self, 'Aviso', 'Data de validade fora do padrão dd/mm/aaaa.')
            return False

    def validar_preco(self):
        try:
            float(self.txt_preco.text())
            return True

        except:
            QMessageBox.warning(self, 'Aviso', 'Valor inserido no campo "preço" está incorreto.')
            return False

    def validar_quantidade(self):
        try:
            int(self.txt_quantidade.text())
            return True

        except:
            QMessageBox.warning(self, 'Aviso', 'Valor inserido no campo "quantidade" não é um número real.')
            return False

    def validar_nome(self):
        if self.txt_nome.text() != '':
            return True

        else:
            QMessageBox.warning(self, 'Aviso', 'O campo "nome" deve estar preenchido.')
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EstoqueApp()
    window.show()
    sys.exit(app.exec())
