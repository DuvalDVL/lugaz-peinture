---
layout: default
title: "Nos prestations"
meta_title: "Prestations de peinture, façade et plâtrerie en Haute-Savoie | Lugaz & Fils"
description: "Toutes les prestations de Lugaz & Fils : peinture intérieure, plâtrerie, sols, ravalement de façade, ITE, bois extérieur, entretien pour professionnels."
permalink: /nos-services.html
---
<section class="ph-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><ol><li><a href="{{ '/' | relative_url }}">Accueil</a></li><li aria-current="page">Nos prestations</li></ol></nav>
    <p class="eyebrow">Nos prestations</p>
    <h1>Peinture, façades, plâtrerie et sols en Haute-Savoie</h1>
    <p class="lead">Trois univers d'intervention, une même équipe : du rafraîchissement d'une pièce au ravalement complet d'un immeuble.</p>
  </div>
</section>
{%- for f in site.data.families %}
<section class="sec{% if forloop.index == 2 %} alt{% endif %}">
  <div class="wrap">
    <div class="sec-h"><h2><a href="{{ f.url | relative_url }}" style="color:inherit;text-decoration:none">{{ f.name }}</a></h2></div>
    <div class="grid c3">
      {%- for s in site.data.services %}{% if s.family == f.key %}
      <article class="card"><div class="card-b"><h3><a href="{{ s.url | relative_url }}">{{ s.name }}</a></h3><p>{{ s.short }}</p><span class="more">Découvrir →</span></div></article>
      {%- endif %}{% endfor %}
    </div>
  </div>
</section>
{%- endfor %}
{% include cta-band.html title="Un projet en tête ?" %}
