import mailbox
import os

def mbox_to_eml(mbox_path, output_dir):
    # Abre o arquivo MBOX
    mbox = mailbox.mbox(mbox_path)
    
    # Cria o diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Itera sobre as mensagens no arquivo MBOX
    for i, message in enumerate(mbox):
        # Verifica e ajusta o cabeçalho 'From'
        from_header = message['From']
        if "<" in from_header and ">" in from_header:
            # Supondo que o formato seja Nome <email@dominio.com>
            name, email = from_header.split("<")
            name = name.strip()
            email = email.strip(">")
            corrected_from = f"{name} <{email}>"
            message.replace_header('From', corrected_from)
        elif "@" not in from_header:
            # Caso não seja um email válido, define um padrão
            message.replace_header('From', 'default name <email@exemplo.com>')
        
        # Gera o nome do arquivo EML
        eml_filename = f"email_{i+1}.eml"
        eml_path = os.path.join(output_dir, eml_filename)
        
        # Converte a mensagem para o formato EML e salva em arquivo com codificação UTF-8
        with open(eml_path, 'w', encoding='utf-8') as eml_file:
            eml_file.write(message.as_string())

if __name__ == "__main__":
    # Caminho do arquivo MBOX
    mbox_path = r"C:\your\path\to\exemple.mbox"

    # Diretório para salvar os arquivos EML
    output_dir = r"C:\path\to\folder\inside\this\project\save"
    
    # Chama a função para converter os arquivos
    mbox_to_eml(mbox_path, output_dir)