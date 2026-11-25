import os
NAV=[("index","Accueil"),("parcours","Parcours"),("realisations","Réalisations"),("stages","Stages"),("veille","Veille"),("tableau-synthese","Synthèse E5"),("contact","Contact")]
NOM="Prénom Nom"
def ph(t): return f'<span class="ph">[{t}]</span>'
def page(slug,title,body,active=None):
    nav="".join(f'<a href="{s}.html"{" aria-current=page" if s==(active or slug) else ""}>{l}</a>' for s,l in NAV)
    html=f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {NOM}</title><meta name="description" content="Portfolio BTS SIO option SISR de {NOM}"><link rel="stylesheet" href="style.css"></head>
<body><header><a class="brand" href="index.html">{NOM}</a><nav>{nav}</nav></header>
<main>{body}</main>
<footer><p>Portfolio BTS SIO SISR — session {ph("année")}. Les données sensibles (IP, mots de passe, noms) sont anonymisées.</p><p><a href="#top">Haut de page</a></p></footer></body></html>'''
    open(slug+".html","w",encoding="utf-8").write(html)

# Accueil
topo='''<svg viewBox="0 0 320 200" role="img" aria-label="Schéma réseau : Internet, pare-feu, DMZ et LAN"><g fill="none" stroke="currentColor" stroke-width="2"><path d="M60 100h60M200 60l-40 30M200 140l-40-30M200 60h60M200 140h60"/><circle cx="40" cy="100" r="20"/><rect x="120" y="80" width="40" height="40" rx="6"/><rect x="200" y="40" width="60" height="40" rx="6"/><rect x="200" y="120" width="60" height="40" rx="6"/></g><g fill="currentColor" font-size="11" text-anchor="middle"><text x="40" y="104">WAN</text><text x="140" y="104">FW</text><text x="230" y="64">DMZ</text><text x="230" y="144">LAN</text></g></svg>'''
page("index","Accueil",f'''<section class="hero"><div><h1>{NOM}, étudiant en BTS SIO option SISR</h1>
<p class="lead">Je conçois, installe et sécurise des infrastructures : systèmes, réseaux, services et supervision. Ce portfolio rassemble mes réalisations professionnelles, mes stages et ma veille technologique pour l'épreuve E5.</p>
<p><a class="btn" href="realisations.html">Voir mes réalisations</a> <a class="btn alt" href="tableau-synthese.html">Tableau de synthèse E5</a></p></div>
<div class="art">{topo}</div></section>
<section><h2>Présentation</h2><p>{ph("2 à 3 phrases : qui vous êtes, votre parcours, ce qui vous motive dans l'infrastructure et la cybersécurité.")}</p>
<ul class="facts"><li><strong>Formation</strong> BTS SIO option SISR, {ph("établissement")}</li><li><strong>Année</strong> {ph("2e année, 2026–2027")}</li><li><strong>Domaines</strong> {ph("Linux, réseaux, virtualisation, supervision")}</li></ul></section>
<section><h2>Parcourir le portfolio</h2><div class="cards">
<a class="card" href="parcours.html"><h3>Parcours</h3><p>Formation, compétences et CV.</p></a>
<a class="card" href="realisations.html"><h3>Réalisations</h3><p>Une fiche détaillée par projet, avec preuves.</p></a>
<a class="card" href="stages.html"><h3>Stages</h3><p>Missions réalisées en entreprise.</p></a>
<a class="card" href="veille.html"><h3>Veille technologique</h3><p>Sujet suivi, sources et synthèses.</p></a>
<a class="card" href="tableau-synthese.html"><h3>Synthèse E5</h3><p>Réalisations reliées au référentiel.</p></a></div></section>''')

# Parcours
page("parcours","Parcours",f'''<h1>Parcours</h1><p><a class="btn" href="cv.pdf">Télécharger mon CV (PDF)</a></p>
<section><h2>Formation</h2><ol class="timeline">
<li><time>{ph("2026–2027")}</time><h3>BTS SIO option SISR, 2e année</h3><p>{ph("Établissement, ville")}</p></li>
<li><time>{ph("2025–2026")}</time><h3>BTS SIO option SISR, 1re année</h3><p>{ph("Établissement, ville")}</p></li>
<li><time>{ph("2024–2025")}</time><h3>Baccalauréat {ph("série / mention")}</h3><p>{ph("Établissement, ville")}</p></li></ol></section>
<section><h2>Compétences techniques</h2><div class="cards">
<div class="card"><h3>Systèmes et services</h3><p>{ph("Linux, Windows Server, Nginx/Apache, DHCP, DNS")}</p></div>
<div class="card"><h3>Réseaux</h3><p>{ph("Cisco Packet Tracer, Wireshark, iptables, VLAN")}</p></div>
<div class="card"><h3>Virtualisation</h3><p>{ph("VirtualBox, Proxmox, LXC")}</p></div>
<div class="card"><h3>Supervision et sauvegarde</h3><p>{ph("Munin, Rsync")}</p></div></div>
<p class="note">Ne listez que ce que vous pouvez expliquer et démontrer à l'oral.</p></section>
<section><h2>Langues et centres d'intérêt</h2><p>{ph("Français, anglais, ... — sport, musique, ...")}</p></section>''')

# Réalisations
R=[("realisation-1","Mise en place d'un service web","Nginx/Apache, vhosts, DNS","B2"),
   ("realisation-2","Supervision d'une infrastructure virtualisée","Proxmox/LXC, Munin","B2"),
   ("realisation-3","Services réseau DHCP et DNS","Packet Tracer, Wireshark","B2")]
cards="".join(f'<a class="card" href="{s}.html"><h3>{t}</h3><p>{o}</p></a>' for s,t,o,_ in R)
page("realisations","Réalisations",f'''<h1>Réalisations professionnelles</h1><p class="lead">Chaque fiche présente le contexte, les besoins, la solution, les tests et les preuves.</p><div class="cards">{cards}</div>
<p class="note">Pour ajouter une réalisation : copiez <code>realisation-3.html</code>, renommez-la, puis ajoutez-la ici et dans le tableau de synthèse.</p>''',"realisations")
for i,(s,t,o,_) in enumerate(R,1):
    page(s,t,f'''<p><a href="realisations.html">← Toutes les réalisations</a></p><h1>{t}</h1>
<dl class="meta"><dt>Période</dt><dd>{ph("dates")}</dd><dt>Cadre</dt><dd>{ph("TP / projet de groupe / stage")}</dd><dt>Technologies</dt><dd>{o}</dd></dl>
<section><h2>Contexte</h2><p>{ph("Organisation fictive ou réelle, situation de départ, pourquoi ce projet.")}</p></section>
<section><h2>Besoins</h2><ul><li>{ph("besoin 1")}</li><li>{ph("besoin 2")}</li></ul></section>
<section><h2>Solution mise en place</h2><p>{ph("Architecture choisie et justification des choix techniques.")}</p></section>
<section><h2>Étapes de réalisation</h2><ol><li>{ph("installation")}</li><li>{ph("configuration")}</li><li>{ph("sécurisation")}</li></ol></section>
<section><h2>Tests de validation</h2><p>{ph("Ce que vous avez testé, résultat attendu, résultat obtenu.")}</p></section>
<section><h2>Compétences du référentiel</h2><ul><li>{ph("ex. B2 — Administrer et superviser une infrastructure réseau")}</li></ul></section>
<section><h2>Preuves</h2><div class="proofs"><figure><div class="shot">Schéma réseau</div><figcaption>{ph("légende")}</figcaption></figure><figure><div class="shot">Capture de configuration</div><figcaption>{ph("légende")}</figcaption></figure></div>
<p class="note">Remplacez chaque bloc par <code>&lt;img src="images/mon-fichier.png" alt="description"&gt;</code>. Anonymisez les captures.</p>
<p><a class="btn alt" href="docs/documentation-{i}.pdf">Documentation technique (PDF)</a></p></section>''',"realisations")

# Stages
def stage(n):return f'''<article class="entry"><h2>Stage {n} — {ph("entreprise")}</h2><dl class="meta"><dt>Période</dt><dd>{ph("dates, durée")}</dd><dt>Lieu</dt><dd>{ph("ville")}</dd><dt>Tuteur</dt><dd>{ph("nom, fonction")}</dd></dl>
<h3>Missions</h3><ul><li>{ph("mission 1")}</li><li>{ph("mission 2")}</li></ul><h3>Environnement technique</h3><p>{ph("outils, systèmes, réseau")}</p><h3>Bilan</h3><p>{ph("ce que vous avez appris, difficultés, résultats")}</p></article>'''
page("stages","Stages",f'<h1>Stages</h1>{stage(1)}{stage(2)}')

# Veille
page("veille","Veille technologique",f'''<h1>Veille technologique</h1>
<section><h2>Sujet suivi</h2><p>{ph("ex. Vulnérabilités critiques sur les services exposés (Nginx, OpenSSH...)")}</p><p>Pourquoi ce sujet : {ph("lien avec votre option et vos réalisations")}</p></section>
<section><h2>Sources et outils</h2><ul><li>{ph("ANSSI / CERT-FR")}</li><li>{ph("source 2")}</li><li>Agrégateur : {ph("Feedly, Inoreader...")}</li></ul><p>Fréquence : {ph("1 fois par semaine")}</p></section>
<section><h2>Synthèses</h2><table><thead><tr><th>Date</th><th>Article</th><th>Résumé et analyse</th></tr></thead><tbody>
<tr><td>{ph("jj/mm/aaaa")}</td><td>{ph("titre + lien")}</td><td>{ph("3 à 5 lignes avec votre avis")}</td></tr>
<tr><td>{ph("jj/mm/aaaa")}</td><td>{ph("titre + lien")}</td><td>{ph("résumé")}</td></tr></tbody></table></section>''')

# Synthèse
rows="".join(f'<tr><th scope="row"><a href="{s}.html">{t}</a></th><td>{ph("période")}</td><td class="c">✓</td><td class="c">{ph("✓")}</td><td class="c">{ph("✓")}</td></tr>' for s,t,o,_ in R)
page("tableau-synthese","Tableau de synthèse E5",f'''<h1>Tableau de synthèse E5</h1><p class="lead">Chaque réalisation est reliée aux blocs de compétences du référentiel.</p>
<div class="scroll"><table><thead><tr><th>Réalisation</th><th>Période</th><th>B1 Support</th><th>B2 Administration</th><th>B3 Cybersécurité</th></tr></thead><tbody>{rows}</tbody></table></div>
<p><a class="btn" href="docs/tableau-synthese.pdf">Télécharger le tableau (PDF)</a></p><p class="note">Vérifiez avec votre professeur le format officiel attendu pour votre session.</p>''')

# Contact
page("contact","Contact",f'''<h1>Contact</h1><p class="lead">Pour toute question sur mes réalisations ou mon parcours.</p>
<ul class="facts"><li><strong>E-mail</strong> <a href="mailto:adresse@exemple.fr">{ph("adresse@exemple.fr")}</a></li><li><strong>GitHub</strong> <a href="https://github.com/">{ph("github.com/pseudo")}</a></li><li><strong>LinkedIn</strong> {ph("lien")}</li></ul>''')
