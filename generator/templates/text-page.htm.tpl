{% extends "base.html.tpl" %}
{% block sidebar %}
{% include "back_button.htm.tpl" %}
{% endblock %}

{% block body %}
<div class="text-content">
    {{body}}
</div>
{% endblock %}