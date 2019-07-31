{% extends "base.html.j2" %}
{% block title %}
    Vytvoření nového hesla
{% endblock %}

{% block script %}
    <script type="text/javascript" src="{{ url_for('static', filename='toggle_visibility.js') }}"></script>
{% endblock %}

{% block content %}
    <div class="container">
        <div class="col-10">
           <form action="/new_password" method="post" class="form-group form-control" accept-charset="UTF-8">

                {{ form.csrf_token }}
                {% from "_form_element.html.j2" import render_field %}

                {{ form.password.label }}
                <div class="form-group">
                    {{ render_field(form.password, class="form-control", label=False)}}
                    <span class="fa fa-fw fa-eye field-icon" onmouseover="turnOnVisibility()", onmouseout="turnOffVisibility()"></span>
                </div>

                {{ render_field(form.recaptcha) }}
                {{ form.submit(class_='btn btn-primary')}}
            </form>
        </div>
    </div>
{% endblock %}

