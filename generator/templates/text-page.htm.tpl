{% extends "base.html.tpl" %}
{% block sidebar %}
{% include "back_button.htm.tpl" %}
{% endblock %}

{% block body %}
<div class="text-content">
    {{body}}
</div>
{% endblock %}

{%block foot%}
<p>
    Created: {{created.strftime('%a %d %b %Y, %I:%M%p') }}
</p>
<p>
    {%if modified != created%}Last edited: {{modified.strftime('%a %d %b %Y, %I:%M%p') }} {%endif%}
</p>
{%endblock%}