# Roadmap — homelab

## Phase 0 — Hébergement 🔶 en cours
- [x] Nom de domaine acheté (`mafiabears.fr`, chez IONOS)
- [x] VPS créé (Contabo — Hetzner indisponible au moment de la commande)
- [x] Accès SSH fonctionnel à l'IP du VPS
- [x] Enregistrement DNS A configuré (domaine → IP du VPS)
- [ ] Stratégie de sauvegarde à définir (pas d'option backup Contabo prise à la commande)

## Phase 1 — Fondamentaux Linux 🔶 en cours
- [x] Utilisateur non-root créé, `sudo` configuré
- [ ] Exercice dédié : reproduire et résoudre un bug de permissions UID/GID (comme rencontré en entretien)
- [ ] Notes dans `docs/linux-fondamentaux.md`

## Phase 2 — Réseau exposé 🔶 en cours
- [x] Reverse proxy (Nginx) installé sur le VPS
- [x] HTTPS via Let's Encrypt
- [ ] Premier service exposé pour valider toute la chaîne (Uptime Kuma)

## Phase 3 — Sécurité 🔶 en cours
- [x] Durcissement SSH (clé uniquement, pas de mot de passe) — en attente d'ajout des clés des autres machines
- [ ] Fail2ban
- [ ] VPN WireGuard pour l'accès au matériel local

## Phase 4 — Applications 🔶 en cours
- [x] Vitrine peintures (site statique + API contact FastAPI) — **en cours de démarrage**
- [ ] Mealie (gestion de recettes)
- [ ] Vaultwarden
- [ ] Pi-hole (matériel local)

## Phase 5 — Observabilité et sauvegardes ⬜ à venir
- [ ] Monitoring continu (Prometheus/Grafana ou Uptime Kuma étendu)
- [ ] Sauvegardes automatisées (à définir, pas d'option Contabo prise)

## Phase 6 — CI/CD ⬜ à venir

## Phase 7 — Documentation 🔶 en cours
- [x] Structure du dépôt posée
- [x] `docs/incidents.md` alimenté au fil de l'eau
