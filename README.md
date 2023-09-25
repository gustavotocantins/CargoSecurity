# CargoSecurity
Rede neural para analise de borda livre de embarcações


<img src="https://github.com/gustavotocantins/CargoSecurity/blob/main/treino/Leve%20(145).png">

## 🚀 Introdução

Desenvolvi com sucesso uma Rede Neural Convolucional (CNN) que tem a capacidade de classificar o estado de carga de embarcações em três categorias distintas: "Leve", "Carregado" e "Sobrecarregado". Essa classificação é realizada com base em imagens das embarcações que incluem o marcador de referência conhecido como "disco de plimsoll". O disco de plimsoll é uma marcação crítica em embarcações que ajuda a determinar a margem de segurança da borda livre, garantindo assim a segurança e a eficiência das operações de transporte marítimo.

Este sistema de classificação automatizada proporciona uma solução eficiente e precisa para avaliar o estado de carga das embarcações, reduzindo a dependência de avaliações manuais, que podem ser demoradas e sujeitas a erros humanos. Além disso, a capacidade da CNN de processar rapidamente grandes volumes de imagens contribui para uma análise mais eficaz do estado de carga em tempo real, o que é essencial para a gestão eficiente de operações de transporte marítimo.

### 📋 Pré-requisitos

- Python 3.8.0
- Tensorflow 2.12.0
- Numpy 1.23.5
- Matplotlib 3.7.1

### 🔧 Instalação
**Treinamento**

Caso você queira adicionar mais imagens no banco de dados, basta adicionar na pasta treinamento e depois treinar um modelo novo utilizando o arquivo chamado 'Rede Neural.ipynb'

**Modelo treinado**

Na pasta inicial do projeto, existe um arquivo chamado **cargosecurity.pkl** que é o modelo que teve como resultado 97.05% de precisão. Nesse sentido, basta utilizar a biblioteca 'pickle' para carregar o modelo e utilizar na correspondente.


## ⚙️ Funcionamento

Basta adicionar a foto de uma embarcação que possua o disco de plimsoll e ele vai classificar a embarcação de acordo com o seu estado de carga.

### 🔩 Resultados

<img src="https://github.com/gustavotocantins/CargoSecurity/blob/main/teste/Carregado%202.png">


## 🛠️ Construído com

Bibliotecas utilizadas

* [tensorflow](https://www.tensorflow.org/tutorials/keras/classification?hl=pt-br)
* [Matplotlib](https://matplotlib.org) 
* [numpy](https://numpy.org)


## ✒️ Autores

* **Gustavo Tocantins** - *Desenvolvedor Geral* - [Gustavo Tocantins](https://www.linkedin.com/in/gustavotocantins/)
* **Arthur Lima** - *Desenvolvedor - [Arthur Lima](https://www.linkedin.com/in/arthur-lima-6999a0178/)
