{% extends 'base.html.tpl' %}
{% block header %}
<div class='head'><h1> Ariel Davis </h1></div>
{% endblock %}

{% block body %}
<div class="flexbox">
{% for page in pages -%}
<a href={{ page.path }}>
    <div class="flexitem">
    {{ page.name }}
    </div>
</a>
{% endfor %}
{%endblock%}