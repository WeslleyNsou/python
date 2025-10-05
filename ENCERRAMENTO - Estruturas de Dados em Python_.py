import matplotlib.pyplot as plt

#Classe para representar um livro
class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao

  def __str__(self):
    return f"{self.titulo} por {self.autor}, publicado em {self.ano_publicacao}"
  
  #Criando uma lista de livros
biblioteca = []

#Lista para armazenar anos de publicação
ano = []

#Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
  novo_livro = Livro(titulo, autor, ano_publicacao)
  biblioteca.append(novo_livro)
  ano.append(ano_publicacao) #adiciona o ano a lista de anos
  print(f"O livro '{titulo}' foi adicionado à biblioteca.")

#Função para listar todos os livros na bilbioteca
def listar_livros():
  print("Livros na biblioteca:")
  for Livro in biblioteca:
    print(Livro)

#Adicionar alguns livros à biblioteca
adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
adicionar_livro("1984", "George Orwell", 1949)
adicionar_livro("A Revolução dos Bichos", "George Orwell", 1945)

#Listar todos os livros na biblioteca
listar_livros()

#Criar um gráfico de livros por ano
anos = list(set(ano)) #Remove duplicadas dos anos
anos.sort()

#Contagem dos livros dos por ano
contagem_por_ano = [anos.count(ano) for ano in anos]

#Criar um gráfico de linha
plt.plot(anos, contagem_por_ano, marker = 'o', linestyle = '-')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')
plt.xlabel('\nAno de Publicação')
plt.ylabel('\nNúmero de livros')

#Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
  plt.text(anos[i], valor, str(valor), ha = 'center', va = 'bottom')
plt.grid(True)
plt.show()