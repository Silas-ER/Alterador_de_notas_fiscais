
 <h1 align="center"> Programa para alterar notas fiscais em banco de dados MS-SQL </h1>
  


  Programa desenvolvido enquanto estou estagiando, com intuito de acessar uma base de dados de **MS-SQL** para alterar dados de uma tabela vinculada ao ERP utilizado na empresa. 


  <br>
  
 
  O proposito do programa se deu a partir da problematica que o ERP ao importar notas do sistema anterior não poderia mais alterar o status das mesmas, assim essa alteração só poderia ser feita diretamente no banco de dados **SQL**.
  Como apenas alguns funcionarios podem ter acesso direto ao banco e quem deveria alterar não tem o conhecimento para lidar com esse tipo de sistema, optei por fazer um programa de acesso direto a tabela que deve ser alterada filtrando o dado por uma chave de acesso do sistema e deixando para o usuario apenas a opção de visualizar os status da nota atual, fazer a alteração e visualizar o novo status da nota para conferencia. Podendo optar se repete o processo ou não.


  <br>
  
 
  O programa foi criado utilizando a linguagem python, com o acesso ao servidor e banco utilizando a biblioteca `pyodbc`, e a manipulação dos dados do mesmo utilizando a biblioteca `pandas`, já o executável foi criado via `pyinstaller`.

