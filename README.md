**PROGRAMA DO ATOS V1.0**
acts of program v1.0


**Sobre o que se trata:**

Esse programa em Python trata a geração de códigos .xml para a utilização da _High Level Architecture_ (HLA). 
Ele recebe como entrada um arquivo de texto e entrega como saida sum documento .xml

**Como utilizar:**

Será nescessário fazer as devidas istalações da bibliotéca cog. Nessa versão do programa utiliza a versão de cog para Python3.9.
Aqui está um [Link](https://cog.readthedocs.io/en/latest/index.html#installation) direto para o tutorial de configuração da bibliotéca cog.

O programa possui requisições a serem cumpridas para o devido funcionamento.   
Você deverá rodar esse programa em uma pasta que possui um arquivo nomeado por **federation.txt**
_nota: você pode configurar isso dentro do código caso queira alterar_

O arquivo federation.txt deve cumprir as seguintes especificações:
**Aruqivo federation.txt**

Start>federationName,typeFederetion;  
name,Sharing,x y z, IsAbstrac;  
atr>name, DataType, Ownership, UpdateRate, Transportation;  
atr>name, DataType, Ownership, UpdateRate, Transportation;  
... _inserir quantas vezes for nescessário para seu arquivo .xml_  
int>name, Sharing, dimensions, transportation;  
par>name, dataType;  
... _inserir quantas vezes for nescessário para seu arquivo .xml_\n

Esse arquivo txt é composto por palavras chaves de depurtação e _strings_ que serão inseridas no arquivo .xml.

-  **Strart** refere a geração do cabeçalho do arquivo .xml
-  **atr** refere a geração dos atributos de seu federado
-  **int** refere a geração das interações de seu federado
- **par** refere a geração de parâmetros de seu federado

Um federado por conter _n_ atributos(atr>), interações(int>) e parâmetros(par>)
_observações_:
- Um parâmetro sempre deve vir em seguida de uma interação.
- atente-se ao inserir os dados em ordem e em quantidades condizentes à demostrada acima.

Um exemplo de texto gerador foi adicionado a esse repositório.

**Contato**
Qualquer sugestão de adição ou alteração entre em contato através do email arruda.atos@gmail.com



