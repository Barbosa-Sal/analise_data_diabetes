# Aálise estatísticas de base de dados de diabetes

![imagem](imagens/diabetes.jpg).

## Contexto e Justificativa da Análise de Dados

O diabetes é uma doença crônica de alta prevalência e impacto global, caracterizada pela incapacidade do organismo em regular adequadamente os níveis de glicose no sangue. Essa disfunção metabólica pode desencadear diversas complicações a longo prazo, como doenças cardiovasculares, insuficiência renal, amputações e perda de visão, afetando significativamente a qualidade de vida dos indivíduos e reduzindo sua expectativa de vida. Além dos impactos clínicos, o diabetes representa uma sobrecarga crescente para os sistemas de saúde pública e gera custos expressivos relacionados a tratamentos contínuos, hospitalizações e perda de produtividade.

Diante desse cenário, torna-se essencial compreender os fatores de risco e os padrões comportamentais associados à ocorrência do diabetes, com o objetivo de subsidiar ações preventivas e estratégias de intervenção mais eficazes. A análise do conjuntos de dados populacionais permite identificar relações relevantes entre variáveis demográficas, hábitos de vida e condições de saúde autorreferidas, contribuindo para o aprimoramento das políticas públicas e para o direcionamento de recursos de forma mais eficiente.

Neste projeto, utilizou-se como base o **Sistema de Vigilância de Fatores de Risco Comportamentais (Behavioral Risk Factor Surveillance System – BRFSS)**, conduzido anualmente pelo **Centers for Disease Control and Prevention (CDC)** dos Estados Unidos. Trata-se de uma pesquisa nacional que coleta, por meio de entrevistas telefônicas, informações sobre comportamentos de risco, doenças crônicas e utilização de serviços preventivos. O banco de dados utilizado refere-se ao ano de 2015 e está disponível publicamente na plataforma Kaggle. Ele contempla milhares de registros de indivíduos de diferentes regiões e perfis sociodemográficos, oferecendo uma rica fonte para análise estatística e modelagem preditiva.

A partir desse conjunto de dados, a presente análise busca identificar os fatores associados ao diagnóstico de diabetes, avaliando variáveis como idade, IMC, nível de atividade física, consumo de tabaco e histórico de hipertensão, entre outros. Os resultados visam contribuir para a compreensão dos perfis de risco e para o desenvolvimento de estratégias de prevenção e promoção da saúde com foco na redução da incidência da doença.

## Organização do projeto

```
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto (MIT)
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
|
├── notebooks          <- upyter Notebooks.
│                         
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── estatistica.py  <- Funções criadas especificamente para este projeto.
|
├── referencias        <- Dicionários de dados.
|
├── imagens        <- Figuras de dominio publico para serem usados em relatórios.
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.

      ```bash
      conda env export > ambiente.yml

## Um pouco mais sobre a badse

[Clique aqui](referencias/01_dicionario_de_dados.md). para ver o dicionário de dados da base utilizada.


## Resumo dos principais resultados
