# Hadoop-simulation-urban-modbility 
 
[SUMO - Simulation of Urban MObility](https://github.com/eclipse/sumo), é um "pacote" de simulação de tráfego multimodal 
contínuo, microscópico e de código aberto, projetado para lidar com grandes redes. 
 
Nesse repositório tem como objetivo de demonstrar a utilização do Hadoop, Sumo e Python, calculando a emissão de gases 
de acordo com o tipo de veículo das regiões próximas aos redores da Universidade Federal do Mato Grosso do Sul - UFMS. O 
script mapper.python está mapeando o conjunto de dados necessários para realizar os cálculos que a demonstração propõe, 
que são: 
 
- `timestep_time(seconds)`: O intervalo de tempo descrito pelos valores neste elemento timestep 
- `vehicle_CO(mg/s)`: CO emitido pelo veículo  
- `vehicle_CO2(mg/s)`: A quantidade de CO2 emitida pelo veículo 
- `vehicle_HC(mg/s)`: A quantidade de HC emitida pelo veículo 
- `vehicle_NOx(mg/s)`: A quantidade de NOX emitida pelo veículo 
- `vehicle_PMx(mg/s)`: A quantidade de PMX emitida pelo veículo 
- `vehicle_electricity(Wh/s)`: A quantidade de eletricidade usada pelo veículo 
- `vehicle_fuel(ml/s)`:A quantidade de combustível usado pelo veículo na etapa 
- `vehicle_noise(dB)`: O ruído emitido pelo veículo 
- `vehicle_speed(m/s)`: A velocidade do veículo 
- `vehicle_type`: Tipo do veiculo 
 
O script reducer.py está sumarizando os dados coletados pelo mapper, calculando a média de cada tipo de dado, rasteando 
o menor e maior valor. Após a execução é mostrado esses dados no formato csv. Segue o exemplo: 
 
```text 
bus_bus;167622.0;32566.35999999993;20386665.33;6567.39000000001;158607.36000000028;3471.6200000000067;0.0;8694.239999999987;101174.91000000012;12901.470000000012;122.44119795471147;23.788429510591623;14891.64742878013;4.797216946676413;115.8563623082544;2.535880204528858;0.0;6.350796201607003;73.90424397370352;9.424010226442668 
moto_motorcycle;59589.0;91276.11000000006;2703455.630000003;419.6699999999999;580.49;145.48000000000002;0.0;1162.2300000000007;49304.77000000004;7820.490000000001;27.793376865671643;42.572812500000026;1260.9401259328372;0.1957416044776119;0.2707509328358209;0.0678544776119403;0.0;0.5420848880597018;22.996627798507483;3.647616604477612 
truck_truck;252478.0;52028.68999999997;38087008.54999999;0.0;322402.09;6259.910000000003;0.0;16147.299999999974;174677.71999999988;22867.380000000005;56.04395116537181;11.549098779134289;8454.385915649276;0.0;71.56539178690345;1.3895471698113213;0.0;3.584306326304101;38.774188679245256;5.076000000000001 
veh_passenger;316881.0;128269.60999999996;8380966.5999999875;779.6100000000005;3399.259999999995;145.52000000000044;0.0;3603.0200000000073;195831.6000000004;32806.709999999985;41.661977386273996;16.864266368656317;1101.888850907177;0.10249934262424408;0.4469182224559552;0.01913226400210366;0.0;0.4737075992637401;25.746989219037655;4.313267157507229 
``` 
 
As colunas do CSV corresponde a seguinte ordem: `vehicle_name`,`vehicle_CO`,`vehicle_CO2`,`vehicle_HC`,`vehicle_NOx`,`vehicle_PMx`,`vehicle_electricity`,`vehicle_fuel`,`vehicle_noise`,`vehicle_speed`,`vehicle_CO_max`,`vehicle_CO2_max`,`vehicle_HC_max`,`vehicle_NOx_max`,`vehicle_PMx_max`,`vehicle_electricity_max`,`vehicle_fuel_max`,`vehicle_noise_max`,`vehicle_speed_max`,`vehicle_CO_min`,`vehicle_CO2_min`,`vehicle_HC_min`,`vehicle_NOx_min`,`vehicle_PMx_min`,`vehicle_electricity_min`,`vehicle_fuel_min`,`vehicle_noise_min`,`vehicle_speed_min`,`vehicle_CO_mean`,`vehicle_CO2_mean`,`vehicle_HC_mean`,`vehicle_NOx_mean`,`vehicle_PMx_mean`,`vehicle_electricity_mean`,`vehicle_fuel_mean`,`vehicle_noise_mean`,`vehicle_speed_mean`. Segue a leitura desses dados na forma de tabela: 
 
|'vehicle_name' |vehicle_CO' |'vehicle_CO2' |'vehicle_HC' |'vehicle_NOx' |'vehicle_PMx' |'vehicle_electricity'|'vehicle_fuel' |'vehicle_noise' |'vehicle_speed' |'vehicle_CO_max'|'vehicle_CO2_max'|'vehicle_HC_max'|'vehicle_NOx_max'|'vehicle_PMx_max'|'vehicle_electricity_max'|'vehicle_fuel_max'|'vehicle_noise_max'|'vehicle_speed_max'|'vehicle_CO_min'|'vehicle_CO2_min'|'vehicle_HC_min'|'vehicle_NOx_min'|'vehicle_PMx_min'|'vehicle_electricity_min'|'vehicle_fuel_min'|'vehicle_noise_min'|'vehicle_speed_min'|'vehicle_CO_mean' |'vehicle_CO2_mean'|'vehicle_HC_mean' |'vehicle_NOx_mean'|'vehicle_PMx_mean' |'vehicle_electricity_mean'|'vehicle_fuel_mean'|'vehicle_noise_mean'|'vehicle_speed_mean'| 
|---------------|------------------|------------------|-----------------|------------------|------------------|---------------------|------------------|------------------|------------------|----------------|-----------------|----------------|-----------------|-----------------|-------------------------|------------------|-------------------|-------------------|----------------|-----------------|----------------|-----------------|-----------------|-------------------------|------------------|-------------------|-------------------|------------------|------------------|-------------------|------------------|-------------------|--------------------------|-------------------|--------------------|--------------------| 
|bus_bus |32566.35999999993 |20386665.33 |6567.39000000001 |158607.36000000028|3471.6200000000067|0.0 |8694.239999999987 |71936.27000000008 |8835.360000000002 |56.2 |42235.28 |9.62 |310.93 |6.07 |0.0 |18.01 |80.82 |13.89 |20.17 |5286.11 |4.85 |60.75 |2.01 |0.0 |2.25 |67.11 |0.0 |34.38897571277712 |21527.629704329458|6.9349419218585115 |167.4840126715948 |3.6659134107708624 |0.0 |9.18082365364307 |75.9622703273496 |9.32984160506864 | 
|moto_motorcycle|91276.11000000006 |2703455.630000003 |419.6699999999999|580.49 |145.48000000000002|0.0 |1162.2300000000007|28153.27000000001 |4363.500000000001 |1048.06 |42235.28 |9.62 |310.93 |6.07 |0.0 |18.01 |87.54 |16.15 |1.36 |1228.61 |0.08 |0.31 |0.03 |0.0 |0.53 |55.94 |0.0 |67.1641721854305 |1989.2977409860214|0.30880794701986747|0.4271449595290655|0.10704930095658574|0.0 |0.8552097130242831 |20.716166298749087 |3.210816777041943 | 
|truck_truck |52028.68999999997 |38087008.54999999 |0.0 |322402.09 |6259.910000000003 |0.0 |16147.299999999974|118232.40000000013|14955.420000000015|1048.06 |51198.19 |9.62 |410.36 |7.13 |0.0 |21.71 |87.54 |16.15 |1.36 |1228.61 |0.0 |0.31 |0.03 |0.0 |0.53 |55.94 |0.0 |17.879274914089336|13088.319089347075|0.0 |110.79109621993128|2.1511718213058426 |0.0 |5.548900343642603 |40.629690721649524 |5.139319587628871 | 
|veh_passenger |128269.60999999996|8244417.179999988 |777.7000000000014|3356.899999999995 |144.5900000000004 |0.0 |3544.3100000000068|111174.84000000005|17916.409999999978|1048.06 |51198.19 |9.62 |410.36 |7.13 |0.0 |21.71 |87.54 |16.27 |0.07 |1228.61 |0.0 |0.31 |0.01 |0.0 |0.53 |55.94 |0.0 |27.902895366543387|1793.4342353708914|0.1691755492712642 |0.7302371111594508|0.03145312160104425|0.0 |0.771005003262999 |24.18421579290843 |3.8974135305634063 | 
 
 
## Executar o ambiente 
 
O ambiente pode ser executadfo utilizando o [laboratorio na Google Cloud](https://github.com/DiegoBulhoes/lab-hadoop) ou 
localmente com o [Docker](https://www.docker.com/). Segue o exemplo de um container já 
configurado `https://github.com/DiegoBulhoes/Docker-hadoop` 
 
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
$HADOOP_HOME/bin/hdfs dfs -cat emission.csv 
```  
 
- Para realizar o job de mapper e reducer execute a seguinte comando: 
 
```shell  
$HADOOP_HOME/bin/mapred streaming -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/hadoop/emission.csv -output /user/hadoop/output  
```  
 
- Para realizar o download da saída do Mapreduce 
 
```shell  
$HADOOP_HOME/bin/hdfs dfs -get /user/hadoop/output  
```
 
### Referencias: 
 
- [Hadoop with Python](https://www.oreilly.com/library/view/hadoop-with-python/9781492048435/) 
- [Simulation of Urban MObility](https://www.eclipse.org/sumo/) 
 