---
layout: default
title: "Nos réalisations"
meta_title: "Réalisations de peinture et façades en Haute-Savoie | Lugaz & Fils"
description: "Photos de chantiers réalisés par Lugaz & Fils : peinture intérieure, ravalement de façade, ITE, bois extérieur, sols en Haute-Savoie."
permalink: /qui-sommes-nous/realisations.html
---
<section class="hero light plain">
  <div class="hero-t">
    <nav class="crumbs" aria-label="Fil d'Ariane"><ol><li><a href="{{ '/' | relative_url }}">Accueil</a></li><li><a href="{{ '/qui-sommes-nous.html' | relative_url }}">Qui sommes-nous</a></li><li aria-current="page">Réalisations</li></ol></nav>
    <h1 class="sm">Réalisations</h1>
    <p class="lead">Intérieurs, façades, bois extérieur et sols : des chantiers menés en Haute-Savoie.</p>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="gal">
      {%- for r in site.data.realisations %}
      <figure><div class="pic" style="--ar:4/3">{% include img.html name=r.name alt=r.alt ratio="4/3" sizes="(min-width:980px) 560px, 100vw" %}</div><figcaption>{{ r.alt }}</figcaption></figure>
      {%- endfor %}
    </div>
    <p style="margin-top:34px">Plus de chantiers sur <a href="{{ site.data.site.instagram }}" rel="noopener" target="_blank">Instagram @lugazetfils</a>.</p>
  </div>
</section>
{% include cta-band.html title="Votre projet" %}
