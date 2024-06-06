# Conversor de MBOX para EML

Este projeto inclui um script Python que converte e-mails armazenados em um arquivo MBOX para o formato EML individual. Cada e-mail do arquivo MBOX será salvo como um arquivo .eml separado no diretório especificado.

## Como usar

Para utilizar este script, você precisa ter Python instalado em sua máquina. O script foi testado com Python 3.8, mas deve funcionar com outras versões que suportam as bibliotecas utilizadas.

### Instalação

1. **Instalar Python:**
   - **Windows:** Baixe o instalador do Python em [python.org](https://www.python.org/downloads/) e siga as instruções de instalação. Certifique-se de marcar a opção 'Add Python to PATH' no início da instalação.
   - **MacOS:** Você pode instalar Python usando o Homebrew com o comando `brew install python`.
   - **Linux:** Python geralmente já está instalado, mas você pode instalá-lo via gerenciador de pacotes com `sudo apt-get install python3` para Ubuntu, por exemplo.

### Configuração

Edite as variáveis `mbox_path` e `output_dir` no script para apontar para o caminho do seu arquivo MBOX e para o diretório onde você deseja salvar os arquivos EML, respectivamente.

### Execução

Para rodar o script, simplesmente navegue até o diretório do script em seu terminal e execute:

```bash
python conversor.py