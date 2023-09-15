#Tipo de dado dict(Dicionário)

henrique = {
    'sobrenome' : 'Queiroz',
    'ultimo_nome' : 'Junior',
    'telefone': 92991973627 ,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

print(henrique['telefone'])
print(henrique['ultimo_nome'])
print(henrique['enderecos'])
print(henrique['sobrenome'])
print(henrique,type(henrique))