# homelab

Projet self-hosting personnel — un serveur réel, permanent, exposé à Internet, avec de vraies applications utiles. Contrairement à `sre-labs` (labs jetables, pannes simulées), ici rien ne se détruit à la fin d'une session : les problèmes émergent dans la durée, les enjeux de sécurité sont réels.

## Pourquoi ce projet

Suite à un entretien SRE chez Theodo Cloud (process conclu, non retenu — feedback : lacunes sur les fondamentaux Linux, en particulier gestion des permissions/utilisateurs système), ce projet vise à combler ce point précis en conditions réelles, tout en construisant des services personnellement utiles.

## Architecture

**Hébergement mixte** :
- **VPS (Contabo)** : services nécessitant une exposition publique stable — vitrine peintures, Mealie, Uptime Kuma, Vaultwarden
- **Matériel local** (tour / PC portable) : services gourmands en stockage, accessibles uniquement via VPN WireGuard — Nextcloud, Jellyfin, Pi-hole

Détail complet : voir [`ROADMAP.md`](./ROADMAP.md) et [`docs/architecture.md`](./docs/architecture.md).

## Domaine

`mafiabears.fr` (+ sous-domaines par service : `peintures.`, `recettes.`, etc.)

## Structure du dépôt

```
homelab/
├── docs/           # architecture, DNS, sécurité, journal d'incidents réels
├── infra/          # notes serveur (VPS Contabo + matériel local)
└── services/       # un dossier par service, avec son docker-compose.yml + NOTES.md
```

⚠️ Aucun secret n'est versionné ici — voir `.gitignore`. Les identifiants réels vivent dans des fichiers `.env` locaux au serveur, jamais commités.

## Statut

Voir [`ROADMAP.md`](./ROADMAP.md) pour l'avancement détaillé par phase.
