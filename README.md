# Vacinação

### Link da API: https://vacinacao-deploy.herokuapp.com/vaccinations
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