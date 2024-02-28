{% extends "base.html.tpl" %}
{% block sidebar %}
{% include "back_button.htm.tpl" %}
{% endblock %}

{% block body %}
<div class="text-content">
    {{body}}
</div>
<div class=times>
<p>
    Created: {{created}}
</p>
<p>
    {%if modified != created%}Last edited: {{modified}} {%endif%}
</p>
</div>
{% endblock %}