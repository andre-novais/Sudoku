class RoubaSudoku():
  def __init__(self, tabela):
    print(tabela)
    self.tabela = tabela
    self.tamanho = 9
    self.numerosPossiveis = [1,2,3,4,5,6,7,8,9]
  def soluciona(self):
    i = 0
    self.prepararDados()
    while i < 500: 
      for indrow in range(self.tamanho):
        for column in range(self.tamanho):
          if type(self.tabela[indrow][column]) == list:
            self.removerImpossiveis(indrow,column)
            self.deduzirPorEliminacao()
      if self.checarResultado():
        print(i)
        for row in self.tabela:
          print(row)
        return
      i += 1
    print(i)
    print(self.tabela)

    return


  def removerImpossiveis(self, indrow,column):
    for j in range(self.tamanho):
      if type(self.tabela[j][column]) == int and self.tabela[j][column] in self.tabela[indrow][column]:
        self.tabela[indrow][column].remove(self.tabela[j][column])
      if type(self.tabela[indrow][j]) == int and self.tabela[indrow][j] in self.tabela[indrow][column]:
        self.tabela[indrow][column].remove(self.tabela[indrow][j])
    for row in range((indrow//3)*3,(indrow//3)*3 + 3):
      for indcolumn in range((column//3)*3,(column//3)*3 + 3):
        if type(self.tabela[row][indcolumn]) == int and self.tabela[row][indcolumn] in self.tabela[indrow][column]:
          self.tabela[indrow][column].remove(self.tabela[row][indcolumn])
    if len(self.tabela[indrow][column])== 1:
      print(f'{indrow+1} row and {column+1} column is {self.tabela[indrow][column]}')
      self.tabela[indrow][column] = self.tabela[indrow][column][0]
    #print(f'{indrow} : {column} can be {self.tabela[indrow][column]}')  
    return

  def checarResultado(self):
    for row in range(self.tamanho):
      for coluna in range(self.tamanho):
        if type(self.tabela[row][coluna]) == list:
          return False
    return True

  def pegaBox(self, indexe):
    return [indexe // 3, indexe // 3 + 1, indexe // 3 + 2]

  def prepararDados(self):
    for row in range(self.tamanho):
      for column in range(self.tamanho):
        if self.tabela[row][column] == '.':
          self.tabela[row][column] = [1,2,3,4,5,6,7,8,9]
    return

  def deduzirPorEliminacao(self):
    for row in range(self.tamanho):
      for number in range(1,10):
        resultado = self.apenasUmaListaRow(row,number)
        if resultado:
          print(f'{resultado[0]+1} row and {resultado[1]+1} column is {number}')
          self.tabela[resultado[0]][resultado[1]] = number
    for coluna in range(self.tamanho):
      for number in range(1,10):
        resultado = self.apenasUmaListaColuna(coluna,number)
        if resultado:
          print(f'{resultado[0]+1} row and {resultado[1]+1} column is {number}')
          self.tabela[resultado[0]][resultado[1]] = number
    boxes = [(3,3),(3,6),(3,9),(6,3),(6,6),(6,9),(9,3),(9,6),(9,9)]
    for box in boxes:
      for number in range(1,10):
        resultado = self.apenasUmaListaBox(box, number)
        if resultado:
          print(f'{resultado[0]+1} row and {resultado[1]+1} column is {number}')
          self.tabela[resultado[0]][resultado[1]] = number
    return
  def apenasUmaListaRow(self, row,number):
    counter = 0
    achada = None
    for coluna in range(self.tamanho):
      if type(self.tabela[row][coluna]) == int and self.tabela[row][coluna] == number:
        return False
      if type(self.tabela[row][coluna]) == list and number in self.tabela[row][coluna]:
        counter += 1
        achada = (row, coluna)
    if counter == 1:
      return achada
    else:
      return False

  def apenasUmaListaColuna(self, coluna,number):
    counter = 0
    achada = None
    for row in range(self.tamanho):
      if type(self.tabela[row][coluna]) == int and self.tabela[row][coluna] == number:
        return False
      if type(self.tabela[row][coluna]) == list and number in self.tabela[row][coluna]:
        counter += 1
        achada = (row, coluna)
    if counter == 1:
      return achada
    else:
      return False

  def apenasUmaListaBox(self,box, number):
    counter = 0
    achada = None
    for row in range(box[0] - 3, box[0]):
      for coluna in range(box[1] - 3, box[1]):
        if type(self.tabela[row][coluna]) == int and self.tabela[row][coluna] == number:
          return False
        if type(self.tabela[row][coluna]) == list and number in self.tabela[row][coluna]:
          counter += 1
          achada = (row, coluna)
    if counter == 1:
      return achada
    else:
      return False
      
      
      
if __name__ == '__main__':
  tabela_easy = [['.',6,'.',2,'.','.','.','.',1],
                 ['.',5,3,9,8,'.',6,'.','.'],
                 [7,'.','.',6,1,3,'.','.','.'],
                 ['.',9,6,3,'.',8,'.','.','.'],
                 [5,'.','.',4,'.',9,'.','.',3],
                 ['.',3,7,5,'.',1,'.',2,8],
                 [6,4,'.','.','.','.',1,5,7],
                 [8,2,'.',7,4,'.','.','.','.'],
                 ['.','.',5,1,'.',6,'.','.','.']]
                 
  tabela_expert = [['.',7,2,5,'.','.','.','.','.'],
                   ['.',3,'.','.','.',4,'.','.','.'],
                   ['.','.','.','.','.',2,'.',1,'.'],
                   ['.','.','.','.','.','.','.','.','.'],
                   ['.','.',4,7,3,'.','.','.','.'],
                   [1,5,7,'.','.','.','.','.','.'],
                   [9,'.',8,'.','.','.',5,'.','.'],
                   ['.','.','.','.','.','.',4,2,'.'],
                   ['.','.','.',9,'.','.',3,7,'.']]
  tabela_hard = [[9,'.','.','.',1,'.','.',7,'.'],]
                 ['.','.','.','.',6,'.','.',2,4],
                 ['.',7,'.',9,'.',8,'.','.','.'],
                 ['.','.',6,'.','.','.','.','.','.'],
                 [2,1,8,'.','.','.','.','.','.'],
                 ['.',5,3,2,'.',4,6,'.','.'],
                 ['.','.','.',5,4,9,'.','.','.'],
                 ['.','.','.','.','.','.',7,'.',2],
                 [5,'.','.','.','.','.','.',8,'.']]
joguinho = RoubaSudoku(tabela_hard)
joguinho.soluciona()               
               
  
