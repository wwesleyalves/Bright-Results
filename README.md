# BrightSec Results

## 📌 Sobre
Este script coleta informações sobre **scans** e **issues** da API da BrightSec e os salva em arquivos **JSON** e **CSV**.

## 🛠️ Instalação

### 1️⃣ Clonar o repositório
```sh
git clone https://github.com/wwesleyalves/Bright-Results.git
cd Bright-Results
```

### 2️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 3️⃣ Criar um arquivo **.env** e adicionar sua API Key:
Crie o arquivo `.env` na raiz do projeto e adicione:
```sh
API_KEY=Sua-Api-Key-Aqui
LIMIT=Numero limite de scans
```

---

## 🚀 Como Usar
Execute o script com:
```sh
python main.py
```

O script irá:
✅ **Coletar os scans da API**  
✅ **Obter os issues correspondentes**  
✅ **Salvar os resultados em `issues.json` e `issues.csv`**  
✅ **Gerar logs detalhados em `bright_results.log`**

---

## 📁 Estrutura dos Arquivos
```
Brightsec-Results/
│── main.py          # Script principal
│── .env                # Configurações (API Key) e limites de numero de scans
│── bright_results.log         # Logs das execuções
│── issues.json         # Arquivo JSON gerado
│── issues.csv          # Arquivo CSV gerado
│── README.md           # Documentação
│── requirements.txt    # Dependências do projeto
```

---

## 🔧 Logs
O script gera um log detalhado em `bright_results.log`, incluindo:
- Erros de requisição
- Processamento dos dados
- Status dos arquivos gerados

---

## 📝 Requisitos
- Python 3.8+
- Bibliotecas: `requests`, `python-dotenv`

Instale as dependências com:
```sh
pip install -r requirements.txt
```
