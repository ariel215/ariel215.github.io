{% extends 'base.html.tpl' %}
{% block 'header' %}
Ariel Davis
{% endblock %}

{% block body %}
<div class="flexbox">
{% for item in pages -%}
<a href={{ page.path }}>
    <div class="flexitem">
    {{ page.name }}
    </div>
</a>
{% endfor %}