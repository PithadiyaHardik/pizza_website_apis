1)http://127.0.0.1:8000/store_pizza=>		This api endpoint is used to add the new pizza in database.It is used with template.
2)http://127.0.0.1:8000/show_all=>		This api endpoint is used to get all the types of the pizzas from the database.
3)http://127.0.0.1:8000/update_pizza/<int:id>=> This api endpoint is used to edit the existing pizza in database if pizza is not present it gives 404.
4)http://127.0.0.1:8000/delete_pizza/<int:id>=> This api endpoint is used to remove the pizza from the database.
5)http://127.0.0.1:8000/add_order=>		This api ise used by clients to place the order if the user add the detail of the pizza which is not present in databse the it will return json response as pizza not avilable else it will return Thank you in json response.
