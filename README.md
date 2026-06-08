# AgroSat AI — Módulo de Cibersegurança

## Descrição do Projeto

O AgroSat AI é uma solução de agricultura inteligente por satélite que utiliza dados satelitais, sensores agrícolas, APIs externas e inteligência artificial para monitorar plantações, analisar riscos ambientais, prever produtividade e apoiar decisões no agronegócio.

Este repositório contém a implementação prática do Módulo de Cibersegurança desenvolvido para a Global Solution, com foco em backup automatizado de dados.

## Implementação Prática Escolhida

A implementação prática escolhida foi a criação de um script de backup automatizado em Python.

O objetivo do script é gerar cópias de segurança de um arquivo que simula o banco de dados do AgroSat AI. Essa prática contribui para a disponibilidade e recuperação dos dados em caso de falhas, exclusões acidentais, ataques ou perda de informações.

## Estrutura do Projeto

```text
AgroSat_AI_Ciberseguranca/
│
├── dados/
│   └── banco_agrosat_ai.txt
│
├── backups/
│   └── arquivos de backup gerados automaticamente
│
├── evidencias/
│   ├── evidencia_01_codigo_backup.png
│   ├── evidencia_02_terminal_backup.png
│   ├── evidencia_03_backup_gerado.png
│   └── evidencia_04_diagrama_arquitetura.png
│
├── backup_agrosat.py
└── README.md
```

## Como Executar

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal.
3. Execute o comando:

```bash
py backup_agrosat.py
```

Ou, dependendo da instalação do Python:

```bash
python backup_agrosat.py
```

## Resultado Esperado

Após a execução, o terminal deve exibir a mensagem:

```text
Backup realizado com sucesso!
```

Além disso, um novo arquivo será criado automaticamente dentro da pasta `backups`, contendo a data e o horário da execução.

## Relação com a Cibersegurança

O backup automatizado é um controle de segurança importante porque reduz o risco de perda de dados e melhora a capacidade de recuperação do sistema. No contexto do AgroSat AI, esse controle protege informações como usuários, mapas agrícolas, relatórios, histórico de análises, dados satelitais processados e resultados gerados pela inteligência artificial.

## Controles de Segurança Relacionados

Além do backup automatizado, o projeto também considera outros controles de segurança, como:

* Firewall e regras de segurança.
* Controle de acesso e autenticação.
* Criptografia de dados sensíveis.
* Monitoramento de logs.
* Backup automatizado.

## Evidências

As evidências da implementação estão disponíveis na pasta `evidencias`, contendo prints do código, execução no terminal, arquivos de backup gerados e diagrama da arquitetura segura.
