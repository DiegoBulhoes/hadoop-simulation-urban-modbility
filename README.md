# Hadoop-simulation-urban-modbility

## Teste do ambiente do Hadoop

Exemplo baseado do livro [Hadoop with Python](https://www.oreilly.com/library/view/hadoop-with-python/9781492048435/)

A lista de palavras foi criada utilizando a seguinte ferramenta [Mockaroo](https://www.mockaroo.com/), nessa lista
contém uma lista de modelos de carros.

- Crie um hdfs

```shell 
$HADOOP_HOME/bin/hdfs namenode -format 
``` 

- Start todos os serviços

```shell 
/opt/hadoop/sbin/start-all.sh 
``` 

- Criar um diretório no HDFS para armazenar alguns arquivos

```shell 
$HADOOP_HOME/bin/hdfs dfs -mkdir /user 
``` 

```shell 
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/hadoop 
``` 

- Realizar o upload da lista de modelos de carros

```shell 
$HADOOP_HOME/bin/hdfs dfs -put /home/hadoop/input /user/hadoop 
``` 

Para exibir a lista basta executar o seguinte comando:

```shell 
$HADOOP_HOME/bin/hdfs dfs -cat input 
``` 

- Para realizar o job de mapper e reducer execute a seguinte comando:

```shell 
$HADOOP_HOME/bin/mapred streaming -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/hadoop/input -output /user/hadoop/output 
``` 

- Para realizar o download da saída do Mapreduce

```shell 
$HADOOP_HOME/bin/hdfs dfs -get /user/hadoop/output 
``` 
 
