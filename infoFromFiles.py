def read_medicos(file_path):
    medicos_dict = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("Doctors:"):
            # A linha seguinte contém os detalhes dos médicos
            medicos_info = lines[i+1].strip().split(', ')
            
            # Itera sobre as informações de cada médico
            for info in medicos_info:
                nome, experiencia, hora, custo, tempo = info.split(', ')
                
                # Cria uma chave única para cada médico (usando nome, experiência e um identificador único)
                chave = f"{nome}_{experiencia}_{i}"
                
                # Adiciona as informações ao dicionário
                medicos_dict[chave] = {
                    'Nome': nome,
                    'Experiência': experiencia,
                    'Hora': hora,
                    'Custo': custo,
                    'Tempo': tempo
                }

    return medicos_dict

def read_mothers(file_path):
    mothers_dict = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("Mothers:"):
            # A linha seguinte contém os detalhes das mães
            maes_info = lines[i+1].strip().split(', ')
            
            # Itera sobre as informações de cada mãe
            for info in maes_info:
                nome, idade, Urgencia, Risco = info.split(', ')
                
                # Cria uma chave única para cada mãe (usando nome e idade)
                chave = f"{nome}_{idade}"
                
                # Adiciona as informações ao dicionário
                mothers_dict[chave] = {
                    'Nome': nome,
                    'Idade': idade,
                    'Urgencia': Urgencia,
                    'Risco': Risco
                }

    return mothers_dict


