## 2026-09-17 — Déploiement Postgres sur l'API de contact : triple panne en cascade

**Impact** : formulaire de contact indisponible (502 Bad Gateway) pendant l'ajout du stockage
Postgres, sur plusieurs tentatives successives.

**Cause racine** : trois problèmes distincts, résolus l'un après l'autre :
1. `${DB_PASSWORD}` dans `docker-compose.yml` non résolu — cette syntaxe de substitution lit
   un fichier `.env` à la racine du service (`vitrine-peintures/.env`), différent du fichier
   `.env` référencé via `env_file:` (`api/.env`) qui n'est injecté qu'à l'intérieur du conteneur.
   Les deux avaient des rôles différents et non interchangeables.
2. Course de vitesse au démarrage : `contact-api` tentait sa connexion à Postgres avant que
   celui-ci soit réellement prêt à accepter des connexions (`depends_on` simple garantit
   l'ordre de lancement, pas la disponibilité réelle).
3. Nginx (`proxy`) gardait en mémoire l'ancienne IP de `contact-api`, recréé plusieurs fois
   entre-temps — nginx résout le nom d'un upstream une seule fois, au démarrage, jamais
   dynamiquement ensuite.

**Résolution** :
1. Création d'un second fichier `.env` à la racine du service, avec la même valeur `DB_PASSWORD`
   que dans `api/.env`.
2. Ajout d'un `healthcheck` (`pg_isready`) sur `db`, et `depends_on: db: condition: service_healthy`
   sur `contact-api`.
3. `docker compose up -d --force-recreate proxy` pour forcer une résolution DNS fraîche.

**Action corrective** : documenter clairement, dans le `README.md` du service, la distinction
entre les deux fichiers `.env` (racine du service vs `api/`) pour éviter de reproduire l'erreur
lors du prochain service ajouté (Mealie, Vaultwarden).

## 2026-09-17 — Site inaccessible en IPv6 depuis l'extérieur (iPhone 4G)

**Impact** : site inaccessible pour les visiteurs sur réseau mobile utilisant IPv6 par défaut.

**Cause racine** : le VPS Contabo répond correctement en IPv6 en local (confirmé via
`curl -6` depuis le serveur lui-même), mais le trafic IPv6 externe n'atteint jamais le
serveur — problème de routage réseau côté hébergeur, pas de configuration côté VPS/DNS
(confirmé via test-ipv6.com : DNS AAAA correct, connectivité IPv6 externe en échec).

**Résolution** : retrait temporaire de l'enregistrement AAAA chez IONOS, retour à l'IPv4
seul en attendant. Ticket support ouvert chez Contabo.

**Action corrective** : ne pas publier d'enregistrement AAAA avant d'avoir validé la
connectivité IPv6 externe (pas seulement locale) pour tout futur service.
