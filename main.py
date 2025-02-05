import requests
import json
import csv
import logging
import os
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(
    filename="bright_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Carrega variáveis do arquivo .env
load_dotenv()

class BrightSecResult:
    """Classe para gerenciar a obtenção e salvamento de scans e issues da API do Bright."""

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.limit = os.getenv("LIMIT")
        self.headers = {"Authorization": self.api_key, "accept": "application/json"}
        self.scans_url = "https://app.brightsec.com/api/v2/scans?limit={}".format(self.limit)

    def obter_scans_ids(self, url):
        """Faz uma requisição GET e retorna os dados JSON ou um erro."""
        logging.info(f"Fazendo requisição para {url}")
        resposta = requests.get(url, headers=self.headers)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            erro_msg = f"Erro {resposta.status_code}: {resposta.text}"
            logging.error(erro_msg)
            return {"erro": erro_msg}

    def obter_issues(self):
        """Obtém os issues de cada scan."""
        logging.info("Obtendo lista de scans...")
        scans_data = self.obter_scans_ids(self.scans_url)

        if "erro" in scans_data:
            print(scans_data["erro"])
            return {}

        issues_por_scan = {}
        for item in scans_data.get("items", []):
            scan_id = item["id"]
            logging.info(f"Obtendo issues para o scan ID: {scan_id}")

            issues_url = f"https://app.brightsec.com/api/v1/scans/{scan_id}/issues"
            issues_por_scan[scan_id] = self.obter_scans_ids(issues_url)

        return issues_por_scan

    def salvar_arquivo(self, nome_arquivo, dados, formato="json"):
        """Salva os dados em JSON ou CSV."""
        if formato == "json":
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        elif formato == "csv":
            with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(["scanId", "projectId", "id", "name", "severity", "labels", "assigneeIds", "status", "occurrences", "createdAt", "url", "method", "protocol"])

                for scan_id, issues in dados.items():
                    for issue in issues:
                        writer.writerow([
                            scan_id,  # Adicionando scanId
                            issue.get("projectId", ""),  # Adicionando projectId
                            issue.get("id", ""),
                            issue.get("name", ""),
                            issue.get("severity", ""),
                            ",".join(issue.get("labels", [])),
                            ",".join(issue.get("assigneeIds", [])),
                            issue.get("status", ""),
                            issue.get("occurrences", ""),
                            issue.get("createdAt", ""),
                            issue.get("url", ""),
                            issue.get("method", ""),
                            issue.get("protocol", "")
                        ])
        logging.info(f"Arquivo {nome_arquivo} salvo com sucesso.")

    def executar(self):
        """Executa o processo de obtenção e salvamento dos scans e issues."""
        logging.info("Iniciando processo de coleta de issues...")
        issues = self.obter_issues()
        if issues:
            self.salvar_arquivo("issues.json", issues, "json")
            self.salvar_arquivo("issues.csv", issues, "csv")
            print("Processo concluído. Arquivos gerados: issues.json e issues.csv")
        else:
            print("Nenhum dado foi salvo.")

# Executar o script
if __name__ == "__main__":
    retrieve = BrightSecResult()
    retrieve.executar()