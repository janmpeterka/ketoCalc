{% extends "base.tpl" %}
{% block title %}
    Nová surovina
{% endblock %}

{% block style %}
    
{% endblock %}

{% block script %}
	
{% endblock %}

{% block content %}
    {% include('navbar.tpl') %}
        <div class="container">
            <form method="POST" action="/newingredient" class="form-group col-6" accept-charset="UTF-8">
                <label for="name">Název suroviny</label>
                <input type="text" name="name" class="form-control"  required placeholder="Nová surovina">
                <label for="protein">Množství bílkovin / 100 g</label>
                <input type="text" pattern="[0-9]+([\.][0-9]+)?" name="protein" class="form-control" step="0.01" required placeholder="0.0">
                <label for="fat">Množství tuku / 100 g</label>
                <input type="text" pattern="[0-9]+([\.][0-9]+)?" name="fat" class="form-control" step="0.01" required placeholder="0.0">
                <label for="sugar">Množství sacharidů / 100 g</label>
                <input type="text" pattern="[0-9]+([\.][0-9]+)?" name="sugar" class="form-control" step="0.01" required placeholder="0.0">
                <label for="sugar">Množství kalorií (kcal)/ 100 g</label>
                <input type="text" pattern="[0-9]+([\.][0-9]+)?" name="calorie" class="form-control" step="0.01" required placeholder="0.0">
                <input type="submit" class="btn btn-primary" value="Přidat surovinu" /><br>
            </form>
        </div>
{% endblock %}
