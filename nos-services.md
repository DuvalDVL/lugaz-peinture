---
layout: default
title: "Nos prestations"
meta_title: "Prestations de peinture, façade et plâtrerie en Haute-Savoie | Lugaz & Fils"
description: "Toutes les prestations de Lugaz & Fils : peinture intérieure, plâtrerie, sols, ravalement de façade, ITE, bois extérieur, entretien pour professionnels."
permalink: /nos-services.html
---
<section class="hero light plain">
  <div class="hero-t">
    <nav class="crumbs" aria-label="Fil d'Ariane"><ol><li><a href="{{ '/' | relative_url }}">Accueil</a></li><li aria-current="page">Nos prestations</li></ol></nav>
    <h1 class="sm">Peinture, façades, plâtrerie et sols en Haute-Savoie</h1>
    <p class="lead">Du rafraîchissement d'une pièce au ravalement complet d'un immeuble : l'ensemble de nos prestations, par une même entreprise.</p>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    {%- for f in site.data.families %}
    <div class="fam-block split">
      <div><h2><a href="{{ f.url | relative_url }}" style="color:inherit;text-decoration:none">{{ f.name }}</a></h2></div>
      <div class="idx">
        {%- for s in site.data.services %}{% if s.family == f.key %}
        <a class="row" href="{{ s.url | relative_url }}"><span class="nm">{{ s.name }}</span><span class="ds">{{ s.short }}</span></a>
        {%- endif %}{% endfor %}
      </div>
    </div>
    {%- endfor %}
  </div>
</section>
{% include cta-band.html title="Un projet en tête ?" %}
