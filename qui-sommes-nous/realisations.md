---
layout: default
title: "Nos réalisations"
meta_title: "Réalisations de peinture et façades en Haute-Savoie | Lugaz & Fils"
description: "Photos de chantiers réalisés par Lugaz & Fils : peinture intérieure, ravalement de façade, ITE, bois extérieur, sols en Haute-Savoie."
permalink: /qui-sommes-nous/realisations.html
---
<section class="ph-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><ol><li><a href="{{ '/' | relative_url }}">Accueil</a></li><li><a href="{{ '/qui-sommes-nous.html' | relative_url }}">Qui sommes-nous</a></li><li aria-current="page">Réalisations</li></ol></nav>
    <p class="eyebrow">Nos réalisations</p>
    <h1>Des chantiers réalisés en Haute-Savoie</h1>
    <p class="lead">Quelques exemples de chantiers récents : intérieurs, façades, bois extérieur et sols.</p>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="grid c3">
      {%- assign reals = "realisation-interieur-1|Peinture intérieure d'un séjour|realisation-facade-1|Ravalement de façade d'une maison|realisation-ite-1|Isolation par l'extérieur d'une maison|realisation-chalet-1|Dégrisage et lasure d'un chalet|realisation-sol-1|Pose de parquet|realisation-placo-1|Cloisons et plafonds en placo" | split: "|" -%}
      {%- for i in (0..5) %}{% assign k = i | times: 2 %}{% assign k2 = k | plus: 1 %}
      <figure class="card"><div class="pic" style="--ar:4/3">{% include img.html name=reals[k] alt=reals[k2] ratio="4/3" sizes="(min-width:980px) 360px, 100vw" %}</div><figcaption class="card-b"><h3>{{ reals[k2] }}</h3></figcaption></figure>
      {%- endfor %}
    </div>
    <p style="margin-top:28px">Retrouvez plus de chantiers sur notre compte <a href="{{ site.data.site.instagram }}" rel="noopener" target="_blank">Instagram @lugazetfils</a>.</p>
  </div>
</section>
{% include cta-band.html title="Votre projet pourrait être le prochain" %}
