import copy

class RoubaSudoku():
  def __init__(self, tabela):
    print(tabela)
    self.tabela = tabela
    self.tamanho = 9
    self.numerosPossiveis = [1,2,3,4,5,6,7,8,9]
    self.boxes = [(3,3),(3,6),(3,9),(6,3),(6,6),(6,9),(9,3),(9,6),(9,9)]
    self.erroAtivo = False
    self.chutesAtivos = []
  def soluciona(self):
    i = 0
    counterIter = 0
    tabelaInicial = None
    tabelaAvoid = None
    self.prepararDados()
    while i < 500: 
      for indrow in range(self.tamanho):
        for column in range(self.tamanho):
          if type(self.tabela[indrow][column]) == list:
            self.removerImpossiveis(indrow,column)
            self.deduzirPorEliminacao()
      if self.checarErro() or self.inconsiste():
        print(self.checarErro(), self.inconsiste())
        self.erroAtivo = True
      if self.tabela == tabelaInicial and counterIter == 0:
        print('iteração falou')
        tabelaAvoid = copy.deepcopy(self.tabela)
        counterIter += 1
      if self.tabela == tabelaAvoid and counterIter in range(1,6):
        print(f'iteração falhou {counterIter} vezes')
        counterIter += 1
      if (self.tabela == tabelaAvoid and counterIter == 6) or self.erroAtivo:
        counterIter = 0
        self.aplicarChute()
      tabelaInicial = copy.deepcopy(self.tabela)
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
      print(f'only possible for {indrow+1} row and {column+1} column is {self.tabela[indrow][column][0]}')
      self.tabela[indrow][column] = self.tabela[indrow][column][0]
    #print(f'{indrow} : {column} can be {self.tabela[indrow][column]}')  
    return

  def checarResultado(self):
    for row in range(self.tamanho):
      for coluna in range(self.tamanho):
        if type(self.tabela[row][coluna]) == list:
          return False
    return True

  def checarErro(self):
    for row in range(self.tamanho):
      for coluna in range(self.tamanho):
        if type(self.tabela[row][coluna]) == list:
          if len(self.tabela[row][coluna]) == 0:
            return True
    return False

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
          print(f'na linha,{resultado[0]+1} row and {resultado[1]+1} column is {number}')
          self.tabela[resultado[0]][resultado[1]] = number
    for coluna in range(self.tamanho):
      for number in range(1,10):
        resultado = self.apenasUmaListaColuna(coluna,number)
        if resultado:
          print(f'na coluna, {resultado[0]+1} row and {resultado[1]+1} column is {number}')
          self.tabela[resultado[0]][resultado[1]] = number
    for box in self.boxes:
      for number in range(1,10):
        resultado = self.apenasUmaListaBox(box, number)
        if resultado:
          print(f'na caixa {resultado[0]+1} row and {resultado[1]+1} column is {number}')
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
  
  def aplicarChute(self):
    print(f'aplicando chute, erroAtivo = {self.erroAtivo}; chutesAtivos = {len(self.chutesAtivos)}')
    if self.erroAtivo:
      print(f'tentando agora com {self.chutesAtivos[-1][0][0] + 1} row {self.chutesAtivos[-1][0][1] + 1} coluna sendo {self.chutesAtivos[-1][1]}')
      self.tabela = self.chutesAtivos[-1][2]
      self.tabela[self.chutesAtivos[-1][0][0]][self.chutesAtivos[-1][0][1]] = self.chutesAtivos[-1][1]
      self.chutesAtivos.remove(self.chutesAtivos[-1])
      self.erroAtivo = False
      return
    for row in range(self.tamanho):
      for coluna in range(self.tamanho):
        if type(self.tabela[row][coluna]) == list:
          if len(self.tabela[row][coluna]) == 2:
            print(f'celula {row + 1} row {coluna + 1} coluna, valor {self.tabela[row][coluna]} virara {self.tabela[row][coluna][0]}')
            self.chutesAtivos.append(((row,coluna),self.tabela[row][coluna][1],copy.deepcopy(self.tabela)))
            self.tabela[row][coluna] = self.tabela[row][coluna][0]
            self.erroAtivo = False
            return

  def inconsiste(self):
    for linha in self.tabela:
      for number in range(1,10):
        if linha.count(number) > 1:
          print(f'erro devido aos {number} na linha {self.tabela.index(linha) + 1}')
          return True
    for number in range(1,10):
      for coluna in range(9):
        counter = 0
        for linha in range(9):
          if self.tabela[linha][coluna] == number:
            counter += 1
          if counter > 1:
            print(f'erro devido aos {number} na coluna {coluna + 1}')
            return True
    for box in self.boxes:
      for number in range(1,10):
        counter = 0
        for row in range(box[0] - 3, box[0]):
          for coluna in range(box[1] - 3, box[1]):
            if self.tabela[row][coluna] == number:
              counter += 1
        if counter > 1:
          print(f'erro devido aos {number} na caixa {caixa}')
          return True
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
                 
  tabela_expert1 = [['.',7,2,5,'.','.','.','.','.'],
                   ['.',3,'.','.','.',4,'.','.','.'],
                   ['.','.','.','.','.',2,'.',1,'.'],
                   ['.','.','.','.','.','.','.','.','.'],
                   ['.','.',4,7,3,'.','.','.','.'],
                   [1,5,7,'.','.','.','.','.','.'],
                   [9,'.',8,'.','.','.',5,'.','.'],
                   ['.','.','.','.','.','.',4,2,'.'],
                   ['.','.','.',9,'.','.',3,7,'.']]
  tabela_hard = [[9,'.','.','.',1,'.','.',7,'.'],
                 ['.','.','.','.',6,'.','.',2,4],
                 ['.',7,'.',9,'.',8,'.','.','.'],
                 ['.','.',6,'.','.','.','.','.','.'],
                 [2,1,8,'.','.','.','.','.','.'],
                 ['.',5,3,2,'.',4,6,'.','.'],
                 ['.','.','.',5,4,9,'.','.','.'],
                 ['.','.','.','.','.','.',7,'.',2],
                 [5,'.','.','.','.','.','.',8,'.']]

  tabela_expert2 = [['.','.','.','.','.',7,'.','.',3],
                    ['.','.','.',9,1,'.','.','.','.'],
                    [1,'.','.','.','.',3,2,'.',4],
                    ['.',8,'.',1,'.','.','.',7,'.'],
                    ['.','.','.','.','.','.','.',6,'.'],
                    [2,'.','.','.','.',4,'.','.','.'],
                    ['.','.',6,8,'.','.','.','.','.'],
                    ['.',5,'.','.','.','.','.','.',6],
                    ['.',7,3,2,'.','.','.',9,'.']]
  tabela_evil = [[7,'.','.','.','.',6,4,'.','.'],
                 ['.',8,9,'.','.','.','.',5,'.'],
                 [6,'.','.',2,'.','.','.',7,1],
                 ['.','.','.','.',3,'.','.','.','.'],
                 ['.','.',7,8,'.',9,1,'.','.'],
                 ['.','.','.','.',6,'.','.','.','.'],
                 [4,9,'.','.','.',1,'.','.',6],
                 ['.',5,'.','.','.','.',7,3,'.'],
                 ['.','.',8,6,'.','.','.','.',4]]
                  
if __name__ == '__main__':
  joguinho = RoubaSudoku(tabela_hard)
  joguinho.soluciona()               
               
  
