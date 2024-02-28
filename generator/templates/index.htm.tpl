{% extends 'base.html.tpl' %}

{% block title %}
<div class='head'><h1> Ariel Davis </h1></div>
{% endblock %}

{% block sidebar %}
{% for page in pages -%}{% if page.header.category == "info" %}
    <div class="sidebar-entry flexbox">

<a href={{ page.path }}>
    {{ page.name }}
</a>
    </div>

{% endif %}{% endfor %}
{%endblock%}

{% block body%}
<h2> Posts </h2>
<hr>
{% for page in pages-%}
{% if page.header.category == "post" %}
<a href={{ page.path }}>
    <div class="post-link">
    {{ page.name }}
    </div>
</a>
{%endif%}{%- endfor%}
{% endblock %}
