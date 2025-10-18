# Mercado Libre ETL - Samsung Galaxy Analysis

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Descrição do Projeto

Este projeto implementa um processo ETL (Extract, Transform, Load) automatizado que utiliza as APIs públicas do Mercado Libre para extrair e analisar dados de produtos Samsung Galaxy no mercado argentino. O objetivo é fornecer insights valiosos sobre vendedores, preços, garantias e métodos de envio.

## 🎯 Objetivo

Desenvolver uma automatização ETL em Python que acesse as APIs públicas do Mercado Libre para responder questões estratégicas sobre produtos para o mercado latino americano.

## 🔍 Problemática

Um best seller do Mercado Libre na Argentina necessita de dados específicos sobre publicações de produtos "Samsung Galaxy" para otimizar sua estratégia comercial.

## ❓ Perguntas de Negócio

O projeto visa responder as seguintes questões analíticas:

1. **Vendedores com Múltiplas Publicações**: Há algum vendedor com múltiplas publicações? Se sim, quantas?
2. **Média de Vendas por Vendedor**: Qual é o promédio de vendas por seller?
3. **Preço Médio em Dólares**: Qual é o preço promédio dos produtos em USD?
4. **Percentual de Garantia**: Que porcentagem dos artículos oferece garantia?
5. **Métodos de Envio**: Quais são os métodos de shipping disponíveis?

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal do projeto
- **Requests**: Para consumo das APIs REST
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Operações numéricas
- **Matplotlib/Seaborn**: Visualização de dados
- **Jupyter Notebook**: Análise exploratória
- **Streamlit**: Framework para aplicações web
## 📡 APIs do Mercado Libre

O projeto utiliza os seguintes endpoints da [API oficial do Mercado Libre](https://developers.mercadolibre.com/):

| Endpoint | Descrição |
|----------|-----------|
| `/currencies` | Informações sobre moedas disponíveis |
| `/currency_conversions` | Conversões entre moedas |
| `/search` | Busca de produtos no marketplace |
| `/items` | Detalhes específicos de produtos |

## 🏗️ Arquitetura ETL

### Extract (Extração)
- Coleta de dados via APIs do Mercado Libre
- Busca por produtos Samsung Galaxy na Argentina
- Extração de informações de vendedores, preços e características

### Transform (Transformação)
- Limpeza e normalização dos dados
- Conversão de preços para USD
- Cálculo de métricas agregadas
- Tratamento de dados ausentes

### Load (Carregamento)
- Armazenamento em formato estruturado (CSV/JSON)
- Geração de relatórios analíticos
- Criação de visualizações

## 📁 Estrutura do Projeto

```
Mercado_Libre_ETL/
│
├── src/
│   ├── extract/
│   │   └── api_client.py
│   ├── transform/
│   │   └── data_processor.py
│   └── load/
│       └── data_exporter.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── config/
│   └── settings.py
│
├── tests/
│   └── test_etl.py
│
├── requirements.txt
├── main.py
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos
```bash
python >=3.11
uv
```

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Mercado_Libre_ETL.git
cd Mercado_Libre_ETL

# Crie um ambiente virtual com UV
venv build  

```

## 📊 Resultados Esperados

O projeto gerará:

- **Relatório de Vendedores**: Lista de sellers com múltiplas publicações
- **Análise de Preços**: Estatísticas de preços em USD
- **Relatório de Garantias**: Percentual de produtos com garantia
- **Análise de Shipping**: Métodos de envio mais utilizados
- **Dashboard Visual**: Gráficos e visualizações dos insights

## 📈 Métricas e KPIs

- Total de produtos analisados
- Número de vendedores únicos
- Preço médio, mediano e desvio padrão
- Taxa de produtos com garantia
- Distribuição de métodos de envio

## 🔧 Configuração

Edite o arquivo `config/settings.py` para personalizar:

```python
# Parâmetros de busca
SEARCH_QUERY = "Samsung Galaxy"
COUNTRY = "AR"  # Argentina
CURRENCY = "ARS"
LIMIT = 1000

# APIs endpoints
BASE_URL = "https://api.mercadolibre.com"
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 License

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

- **Autor**: Thiago Yuki
- **Email**: thiagoyuki@resolvedortech.online
- **LinkedIn**: [Seu LinkedIn](https://www.linkedin.com/in/thiagoyuki/)

---

*Deus é bom e fiel*
