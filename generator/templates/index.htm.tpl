{% extends 'base.html.tpl' %}

{% block title %}
<div class='head'><h1> Ariel Davis </h1></div>
{% endblock %}

{% block sidebar %}
<div class="sidebar">
{% for page in pages -%}{% if page.header.category == "info" %}
<a href={{ page.path }}>
    <div class="sidebar sidebar-entry">
    {{ page.name }}
    </div>
</a>
{% endif %}{% endfor %}
</div>
{%endblock%}

{% block body%}
{% for page in pages -%}{% if page.header.category == "post" %}
<a href={{ page.path }}>
    <div class="post-link">
    {{ page.name }}
    </div>
</a>
{%endif%}{%endfor%}
{% endblock %}
