---
layout: default
title: "Nous contacter"
meta_title: "Contact et devis gratuit | Lugaz & Fils, peintre à Copponex"
description: "Demandez un devis gratuit à Lugaz & Fils, artisan peintre à Copponex : 06 03 03 05 36, formulaire en ligne. Annecy, Genevois, Savoie, canton de Genève."
permalink: /nous-contacter.html
---
<section class="hero light plain">
  <div class="hero-t">
    <nav class="crumbs" aria-label="Fil d'Ariane"><ol><li><a href="{{ '/' | relative_url }}">Accueil</a></li><li aria-current="page">Contact</li></ol></nav>
    <h1 class="sm">Demandez votre devis gratuit</h1>
    <p class="lead">Décrivez votre projet : nous revenons vers vous rapidement.</p>
  </div>
</section>
<section class="sec quote-sec">
  <div class="wrap layout">
    <div>
      <h2>Nos coordonnées</h2>
      <p><strong>{{ site.data.site.name }}</strong><br>{{ site.data.site.street }}<br>{{ site.data.site.zip }} {{ site.data.site.city }}</p>
      <p>Téléphone : <a href="tel:{{ site.data.site.phone_e164 }}"><strong>{{ site.data.site.phone }}</strong></a><br>Autre ligne : <a href="tel:{{ site.data.site.phone2_e164 }}">{{ site.data.site.phone2 }}</a></p>
      <p>E-mail : <a href="mailto:{{ site.data.site.email }}">{{ site.data.site.email }}</a></p>
      <p>{{ site.data.site.hours_label }}.</p>
      <p>Zone d'intervention : {{ site.data.site.areas | join: ", " }}.</p>
    </div>
    {% include contact-form.html %}
  </div>
</section>
