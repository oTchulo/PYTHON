# ✈️ Sistema de Controle de Passageiros de Aeroporto

Este sistema foi desenvolvido em **Python** como um **trabalho universitário**, utilizando os conhecimentos adquiridos durante as aulas. O desenvolvimento levou aproximadamente **2 semanas**, com melhorias e testes até a versão atual.

---

## 📋 Descrição

O objetivo deste projeto é gerenciar os **dados de passageiros de um aeroporto** por meio de uma interface em linha de comando, simples e intuitiva.  
Ele oferece as seguintes funcionalidades:

- ✅ Cadastro de passageiros com validação de CPF, datas e horários.
- ✅ Consulta dos dados de um passageiro por CPF.
- ✅ Remoção de passageiros do sistema.
- ✅ Relatório completo de passageiros em formato de tabela (usando a biblioteca [`tabulate`](https://pypi.org/project/tabulate/)).
- ✅ Relatório financeiro com soma total e individual dos valores pagos.
- ✅ Relatório dos destinos mais frequentes entre os passageiros.

Os dados são armazenados em um arquivo `.txt` para garantir a persistência entre as execuções.  
A interface limpa o terminal a cada operação para melhorar a navegação e a experiência do usuário.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- Python 3
- [tabulate](https://pypi.org/project/tabulate/) — para exibir os relatórios em tabelas organizadas.
- Bibliotecas padrão:
  - `os` — para manipular o terminal e o sistema de arquivos.
  - `datetime` — para validação e manipulação de datas e horários.
  - `collections.Counter` — para análise estatística dos destinos.

---

## 🚀 Como Executar

1️⃣ Clone ou baixe este repositório em sua máquina.  
2️⃣ Certifique-se de ter o Python 3 instalado.  
3️⃣ Instale a biblioteca `tabulate` caso ainda não a tenha:  

```bash
pip install tabulate
