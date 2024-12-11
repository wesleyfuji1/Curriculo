from fpdf import FPDF
import re

# Função para limpar o texto antes de adicionar ao PDF
def limpar_texto(texto):
    # Substitui caracteres problemáticos por alternativas
    texto = texto.replace('–', '-')
    # Remove caracteres que não podem ser representados em Latin-1
    texto = texto.encode('latin-1', 'ignore').decode('latin-1')
    return texto

# Criando o PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()

# Título
pdf.set_font('Arial', 'BU', 18)
pdf.cell(200, 8, limpar_texto('Wesley de Paiva Silva'), ln=True, align='C')

# Dados pessoais
pdf.ln(8)
pdf.set_font('Arial', '', 12)
pdf.set_x(10)
pdf.cell(19, 4, 'Telefone: +55 (44) 99134-9231', ln=False, align='L')
pdf.link(pdf.get_x(), pdf.get_y(),40, 4, 'https://wa.me/5544991349231')

# Links de E-mail e Linkedin
pdf.set_font('Arial', '', 12)
pdf.set_text_color(0, 0, 255)

pdf.ln(8)
pdf.set_x(10)
pdf.cell(1, 4, 'LinkedIn |', ln=False, align='L')
pdf.link(pdf.get_x(), pdf.get_y(),16, 4, 'https://www.linkedin.com/in/wesley-de-paiva-silva-945627142')

pdf.set_x(30)
pdf.cell(1, 4, 'E-mail', ln=False)
pdf.link(pdf.get_x(), pdf.get_y(), 13, 4, 'mailto:wesley_fuji@hotmail.com')

# Continuação dos dados
pdf.ln(8)
pdf.set_text_color(0, 0, 0)
pdf.cell(200, 4, limpar_texto('Localização: Umuarama, PR'), ln=True)

# Resumo profissional
pdf.ln(8)
pdf.set_font('Arial', 'BI', 14)
pdf.cell(200, 8, limpar_texto('Resumo Profissional'), ln=True)
pdf.ln(1)
pdf.set_font('Arial', '', 12)
summary_text = "Profissional com mais de 2 anos de experiência em vendas internas e atendimento ao cliente, com foco em Customer Experience (CX) e relacionamento digital. "\
               "Reconhecido como 2º melhor vendedor do Brasil no programa Best Quality Sales Honda 2023 pela excelência no relacionamento com clientes e parceiros.\n"\
               "Atualmente em transição para a área de Tecnologia da Informação, cursando Análise e Desenvolvimento de Sistemas. Possuo conhecimentos em Python, SQL e análise de dados, "\
               "com habilidades em gestão de projetos, suporte técnico em TI e otimização de processos."
pdf.multi_cell(0, 7, limpar_texto(summary_text))

# Experiência Profissional
pdf.ln(8)
pdf.set_font('Arial', 'BI', 14)
pdf.cell(200, 8, limpar_texto('Experiência Profissional'), ln=True)

# Fuji-Moto Honda
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Fuji-Moto Honda - Vendedor Interno e F&I'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Abril de 2022 – Atual | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
fuji_moto_text = "Atendimento ao cliente presencial e remoto, garantindo experiências positivas e fidelização, com foco em Customer Experience (CX).\n"\
                 "Relacionamento com parceiros financeiros para viabilizar financiamentos de forma ágil e eficaz.\n"\
                 "Reconhecimento como 2º melhor vendedor do Brasil no programa Best Quality Sales Honda 2023."
pdf.multi_cell(0, 7, limpar_texto(fuji_moto_text))

# Ultrafarma
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Ultrafarma - Atendimento ao Cliente'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Outubro de 2021 – Março de 2022 | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
ultrafarma_text = "Atendimento via WhatsApp e presencial, proporcionando uma experiência de compra personalizada e consistente.\n"\
                  "Responsável por atingir consistentemente os melhores resultados de vendas."
pdf.multi_cell(0, 7, limpar_texto(ultrafarma_text))

# Farmácias Pague Menos
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Farmácias Pague Menos - Atendimento ao Cliente'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Abril de 2021 – Outubro de 2021 | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
pague_menos_text = "Atendimento no balcão e operação de caixa, garantindo um relacionamento direto e eficaz com os clientes."
pdf.multi_cell(0, 7, limpar_texto(pague_menos_text))

# Fuji-Moto Honda (Vendedor de Varejo)
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Fuji-Moto Honda - Vendedor de Varejo'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Dezembro de 2019 – Abril de 2021 | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
vendedor_text = "Vendas internas e externas de motocicletas e consórcios, abrangendo mais de 20 cidades.\n"\
                "Manutenção e suporte técnico em TI, incluindo configuração e resolução de problemas em impressoras, computadores e notebooks."
pdf.multi_cell(0, 7, limpar_texto(vendedor_text))

# Hospital do Câncer Uopeccan
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Hospital do Câncer Uopeccan - Assistente de Farmácia'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Dezembro de 2018 – Dezembro de 2019 | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
hospital_text = "Controle de validade e separação de medicamentos e materiais para diferentes setores do hospital, garantindo organização e qualidade nos processos."
pdf.multi_cell(0, 7, limpar_texto(hospital_text))

# Fuji-Moto Honda (Auxiliar Administrativo)
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Fuji-Moto Honda - Auxiliar Administrativo'), ln=True)
pdf.set_font('Arial', 'I', 12)
pdf.cell(200, 7, limpar_texto('Maio de 2013 – Novembro de 2018 | Umuarama, PR'), ln=True)
pdf.set_font('Arial', '', 12)
auxiliar_text = "Vendas de motocicletas e seguros, além de suporte técnico avançado em TI e organização financeira (contas a pagar/receber)."
pdf.multi_cell(0, 7, limpar_texto(auxiliar_text))

# Formação Acadêmica
pdf.ln(8)
pdf.set_font('Arial', 'BI', 14)
pdf.cell(200, 8, limpar_texto('Formação Acadêmica'), ln=True)

# UniFatecie
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('Centro Universitário UniFatecie'), ln=True)
pdf.set_font('Arial', '', 12)
pdf.cell(200, 8, limpar_texto('- Tecnologia em Análise e Desenvolvimento de Sistemas'), ln=True)
pdf.cell(200, 8, limpar_texto('   Novembro de 2024 – Atual'), ln=True)

# UNINGÁ
pdf.ln(2)
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 8, limpar_texto('UNINGÁ – Centro Universitário Ingá'), ln=True)
pdf.set_font('Arial', '', 12)
pdf.cell(200, 8, limpar_texto('- Bacharelado em Farmácia'), ln=True)
pdf.cell(200, 8, limpar_texto('   Janeiro de 2018 (Trancada)'), ln=True)

# Competências Técnicas
pdf.ln(8)
pdf.set_font('Arial', 'BI', 14)
pdf.cell(200, 8, limpar_texto('Competências Técnicas'), ln=True)

pdf.ln(2)
pdf.set_font('Arial', '', 12)
competencias_text = "- Linguagens de Programação: Python, SQL, Java, C#, HTML, CSS, JavaScript;\n"\
                    "- Ferramentas: Excel Avançado, Power BI, Git/GitHub;\n"\
                    "- Habilidades: Gestão de projetos, análise de dados, manutenção e suporte técnico em TI, atenção aos detalhes, comunicação interpessoal."
pdf.multi_cell(0, 8, limpar_texto(competencias_text))

# Certificações
pdf.ln(8)
pdf.set_font('Arial', 'BI', 14)
pdf.cell(200, 8, limpar_texto('Certificações'), ln=True)

pdf.ln(2)
pdf.set_font('Arial', '', 12)
certificacoes_text = "- Best Quality Sales Honda 2023 – 2º Melhor Vendedor do Brasil.\n"\
                     "- Introdução à Programação Orientada a Objetos (POO).\n"\
                     "- Desenvolvimento Orientado a Objetos Utilizando a Linguagem Python.\n"\
                     "- Linguagem de Programação Python – Básico.\n"\
                     "- Hardware e Software – Montagem e Manutenção."
pdf.multi_cell(0, 8, limpar_texto(certificacoes_text))

# Salvando o arquivo
file_path = 'Curriculo_Wesley_de_Paiva_Silva.pdf'
pdf.output(file_path)

# Retornar o caminho do arquivo
file_path