# Sistema Jurídico - Testes ⚖️

![img_inicio](img.png)
> Trabalho Final da disciplina de Engenharia de Software - SOFT

> **Universidade do Estado de Santa Catarina (UDESC) - CCT** 

## 📄 Sobre o Projeto


Este projeto consiste no desenvolvimento do núcleo de um sistema para gestão de **Processos Judiciais** no contexto brasileiro. O objetivo é organizar informações e criar um fluxo intuitivo para o andamento processual, permitindo o rastreamento completo desde a abertura da ação até a decisão final do juiz.

O sistema foca no gerenciamento de trâmites, documentos, audiências e no controle das partes envolvidas (Advogados, Juízes e Partes).

![img_diagrama](diagrama%20de%20classes.png)

---

## 🚀 Funcionalidades Principais

Conforme definido nos Requisitos Funcionais do projeto:

* **Gestão de Pessoas:** Cadastro de Advogados, Juízes e Partes (Autores/Réus).
* **Controle de Processo:** Abertura de processos com numeração única e vínculo com Varas.
* **Movimentação (Trâmites):** Histórico de ações temporais vinculadas ao processo.
* **Gestão de Documentos:** Geração e anexo de documentos via trâmites.
* **Julgamento:** Registro de decisões judiciais e encerramento de processos.

---

## 🏗️ Arquitetura e Padrões de Projeto

O projeto segue a Programação Orientada a Objetos (POO) e implementa padrões de projeto (Design Patterns) definidos no Diagrama de Classes UML:

### 1. Padrão Observer 

* **Objetivo:** Notificar as partes interessadas (Advogados) automaticamente sempre que houver uma nova movimentação (Trâmite) no processo.
* **Implementação:** A classe `Processo` atua como *Subject* e a classe `Advogado` atua como *Observer*.

### 2. Padrão Factory Method 

* **Objetivo:** Desacoplar a lógica de criação de documentos da lógica de negócios do trâmite.
* **Implementação:** O método `gerar_documento` na classe `Tramite` é responsável por instanciar os objetos `Documento` corretamente.

---

## 📂 Estrutura do Repositório

* `sistemaJuridico.py`: Código fonte contendo as classes de domínio e implementação dos padrões (Fase 1).
* `test_sistema_juridico.py`: Suíte de Testes Unitários cobrindo fluxos críticos (Fase 2).
* `README.md`: Documentação do projeto.

---

## 🛠️ Como Executar

### Pré-requisitos

* Python 3.x instalado.
* Biblioteca padrão do Python (não requer instalação de pacotes externos).

### Executando os Testes Unitários (Fase 2)

Para validar a integridade do sistema e os padrões de projeto, execute a suíte de testes elaborada com o framework `unittest`:

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python -m unittest test_sistema_juridico.py -v
```


### Cobertura dos Testes

Os testes focam nos métodos mais críticos do sistema, conforme exigido na descrição do trabalho:

1. **Fluxo de Notificação (Observer):** Garante que advogados recebam alertas de novos trâmites.
2. **Ciclo de Vida do Processo:** Valida se um Juiz consegue julgar e encerrar um processo corretamente.
3. **Criação de Documentos (Factory):** Valida a integridade da geração de anexos.
4. **Regras de Negócio:** Impede encerramento de processos já finalizados.

---

## 👥 Autores

* **Adriano Silva**
* **Herton Silveira**

---

*Bacharelado em Ciência da Computação - 2025*
