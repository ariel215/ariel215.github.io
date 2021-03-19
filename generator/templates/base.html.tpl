<!DOCTYPE HTML>
<head>
    {% for sheet in stylesheets %}
    <link rel="stylesheet" type="text/css" href="{{ sheet }}"/>
    {% endfor %}
</head>
<body>
    <div class="page">
        <div class="sidebar">
            {% block sidebar %}
            {% endblock %}
        </div>
        <div class="head">
            {{ header }}
        </div>
        <div class="body">
            {% block body %}
            {% endblock %}
        </div>
    </div>
</body>