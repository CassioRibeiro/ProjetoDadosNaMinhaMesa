# ProjeroDadosNaMinhaMesa

### Projeto em grupo da formação em Análise de Dados Resilia/Senac

# ProjetoDadosNaMinhaMesa #### Projeto em grupo da formação em Análise de Dados Resilia/Senac. 

* O projeto consiste em realizar um script python que os dados coletados são a Idade, Genero, 4 respotas sobre hábitos pós pandemia, data e hora e convertido em um arquivo csv. A forma como isso será feita fica a critério do nosso squad.

## Tecnologias usadas 
* Python 3.11 🐍 
* Canva

## Falando do código...

* Dois arquivos foram criados, um deles contendo a classe com o método que irá coletar as informações do tema proposto que é Hábitos pós pandemia, no outro o main que irá importar esse arquivo e rodar nosso script.

* Bibliotecas foram usadas no projeto e estão no requirements.

* Uma estrutura de repetição principal foi criada e logo após começa a coleta da idade do entrevistado onde colocamos um tratamento de exceção para evitar erros do usuário. Aqui, conforme solicitado previamente, o programa se encerra após o usuário digitar "00".

* Logo após começa uma série de estruturas de repetição onde o primeiro é pra coletar o genero do entrevistado onde é oferecido um menu de escolha e também usamos tratamento de exceção que será de prache nesse projeto, todos os dados coletados serão tratados para evitar erros de digitação do usuário.

* Uma série de 4 estruturas de repetições se repete onde em cada um deles será feita uma pergunta do tema proposto e coletada a resposta.

* Em seguida usamos a biblioteca datetime para captar a hora e data em tempo real do sistema. Entretanto precisamos formatar tal informação pois a mesma vem no padrão americano e modificamos para o nosso padrão PT/BR

* Na sequencia todos esses dados que foram coletados são colocados numa lista e inseridos numa lista principal onde se torna uma sub-lista.

* Por fim a ultima estrutura de repetição. Aqui iremos perguntar se o usuário quer coletar dados de outro entrevistado ou se deseja encerraro programa. Caso o usuário opte por iniciar outra coleta, a tela é limpa e iniciado novamente o processo de coleta de dados do entrevistados. Se a opção for de encerrar alí a coleta, pegamos a lista principal e trabsformamos em um data frame usando o Pandas, em seguida exportamos esse freme para um arquivo csv que ja está criado apenas com o cabeçalho definido. toda vez que o programa rodar será inserida novas linhas a esse arquivo. Nessa exportação definimos o modo "a" para que seja possível adicionar novas linhas ao arquivo ao invés de subscrever o mesmo, excluimos a indexação e o cabeçalho natural que se cria ao usarmos um data frame, além de usar o padrão brasileiro "utf-8" 

* E por fim apenas uma mensagem final de saudação com o nome do nosso squad e nosso slogam.
