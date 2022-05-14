# Vacinação

# Rubrica - Vacinação

|Critérios | Pts |
|---|---|
|Utilizar SQLAlchemy, Dataclass, Blueprint, Migrations e Padrão Flask Factory corretamente.|1.5 pts|
|POST /vaccinations 201 - Ao fazer requisição nessa rota passando os dados corretos deve retornar o status code 201 (CREATED) e fazer a inserção dos dados normalizados no banco de dados.|1.25 pts|
|POST /vaccination 400 - Ao fazer requisição nessa rota passando uma `string` com mais de 11 characters para a chave 'cpf', deve retornar o status code 400 (BAD REQUEST) com uma mensagem de erro que faça sentido.|1.25 pts|
|POST /vaccination 400 - Ao fazer a requisição nessa rota com o valor de qualquer uma das chaves sendo diferente de `string`, deve retornar o status code 400 (BAD REQUEST) com uma mensagem de erro que faça sentido.|1.25 pts|
|POST /vaccination 400 - Ao fazer a requisição nessa rota faltando qualquer uma das chaves (cpf, name, health_unit_name e vaccine_name), deve retornar o status code 400 (BAD REQUEST) com uma mensagem de erro que faça sentido.|1.25 pts|
|POST /vaccination 409 - Ao fazer a requisição nessa rota passando um CPF que já exista no banco de dados, deve retornar o status code 409 (CONFLICT) com uma mensagem de erro que faça sentido.|1.25 pts|
|POST /vaccinations 201 - Ao fazer requisição nessa rota passando uma chave a mais, deve retornar o status code 201 (CREATED) e fazer a criação corretamente ignorando a chave passada.|1.25 pts|
|GET /vaccinations 200 - Deve retornar todas as vacinas registradas no banco de dados, status code 200 (OK)|1.0 pts|
||Total de pontos: 10.0

### Link da API: https://vacinacao-deploy.herokuapp.com/
#

### Para capturar os dados (GET) deve se usar a seguinte url: https://vacinacao-deploy.herokuapp.com/vaccinations
#

### Para inserir algum dado (POST) deve se usar a seguinte url: https://vacinacao-deploy.herokuapp.com/vaccinations

```
{
	"cpf": "11111111112",
	"name": "Joao",
	"first_shot_date": "28/09/2011",
	"vaccine_name": "Pfizer",
	"health_unit_name": "Hospital"
}
```

### Ao inserir estes dados, será retornado o Status Code 201, e seus respectivos dados criados: 

```
{
	"cpf": "11111111112",
	"first_shot_date": "Fri, 22 Apr 2022 01:19:01 GMT",
	"health_unit_name": "Hospital",
	"name": "Joao",
	"second_shot_date": "Thu, 21 Jul 2022 01:19:01 GMT",
	"vaccine_name": "Pfizer"
}
``` 

### Caso esquecer algum dado como o exemplo abaixo:

```
{
	"cpf": "11111111113",
	"first_shot_date": "28/09/2011",
	"vaccine_name": "Pfizer",
	"health_unit_name": "Hospital"
}
```

### Será retornado o Status Code 400, e a seguinte mensagem:

```
{
	"error": "Missing fields",
	"missing_keys": [
		"name"
	]
}
```
