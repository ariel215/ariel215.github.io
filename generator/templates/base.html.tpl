<!DOCTYPE HTML>
<head>
    {% for sheet in stylesheets %}
    <link rel="stylesheet" type="text/css" href="{{ sheet }}"/>
    {% endfor %}
    <title> {{ name }} </title>
</head>
<body>
    <div class="page">
        <div class="sidebar">
            {% block sidebar %}
            {% endblock %}
        </div>
        {%block header -%}
        <div class="head">
            {{ header }}
        </div>
        {%endblock%}
        <div class="body">
            {% block body %}
            {% endblock %}
        </div>
    </div>
</body>