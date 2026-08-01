# OKx: release management template

## Inhoudsopgave

1. [Inleiding](#1-inleiding)
2. [Releasepakket](#2-releasepakket)
3. [Eigenaarschap](#3-eigenaarschap)
4. [Versiebeheer](#4-versiebeheer)
5. [Communicatie](#5-communicatie)
6. [Releaseproces](#6-releaseproces)

---

## 1. Inleiding

*Beschrijf welk artifact dit document betreft en welke release artifacts het oplevert. Benoem de **aanleiding** (waarom bestaat dit artifact en dit releasepakket), het **doel** (welke vragen beantwoordt dit document) en de **scope** (wat valt er wel en niet onder). Sluit de scope af met de regel dat al het overige erbuiten valt.*

---

## 2. Releasepakket

*Beschrijf wat het releasepakket van dit artifact precies is: welke onderdelen samen als één releasebare eenheid worden gebouwd en gepubliceerd.*

---

## 3. Eigenaarschap

Benoem het **eigenaar-team** (het team dat merget in de betreffende repo, zie [Bijdragen](../../README.md#bijdragen)) en vul de RACI in met de daadwerkelijke teams en rollen (**R** = voert uit, **A** = eindverantwoordelijk, **C** = wordt geraadpleegd, **I** = wordt geïnformeerd):

| Activiteit | Eigenaar-team | Review-/consulterend team | Communicatie-rol |
|------------|:---:|:---:|:---:|
| Inhoud van het artifact | R/A | C | I |
| Release (versie bepalen, publiceren) | R/A | C | I |
| Vaststellen major/breaking wijziging | A | R | C |
| Communicatie naar belanghebbenden | C | C | R/A |

*Vervang "Eigenaar-team" en "Review-/consulterend team" door de daadwerkelijke teams.*

---

## 4. Versiebeheer

Dit artifact volgt het SemVer-schema en de generieke MAJOR/MINOR/PATCH-definities uit [algemene regels §3](Release-management-algemeen.md#3-versienummering). Beschrijf hier alleen wat **aanvullend of specifiek** is voor dit releasepakket:

---


## 5. Communicatie

Standaard geldt [algemene regels §5](Release-management-algemeen.md#5-communicatie-naar-belanghebbenden): PM is eigenaar van de communicatie, via een standaardroute. *Beschrijf hier alleen als dit voor dit artifact anders is (andere eigenaar, ander kanaal).*

---

## 6. Releaseproces

Standaard geldt het proces uit [algemene regels §6](Release-management-algemeen.md#6-releaseproces). *Beschrijf hier alleen artifact-specifieke afwijkingen of aanvullingen.*

---

