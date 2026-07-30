# OKx Public

De **publieke bron** van de releaseartefacten van **OKx** (Onderwijskoppelingen): de specificaties waarmee instellingen en leveranciers gestandaardiseerde koppelvlakken voor onderwijslogistiek kunnen bouwen.

OKx werkt aan uniforme koppelvlakken zodat systemen in de onderwijsketen beter samenwerken. De scope start bij het MBO en breidt later uit naar het HO. OKx is onderdeel van [Npuls, pilaar Leren Zonder Drempels](https://npuls.nl/project-onderwijskoppelingen).

## Wat staat waar

| Map | Container | Inhoud |
| --- | --- | --- |
| [`Koppelvlakspecificaties/`](Koppelvlakspecificaties/) | Source Material | Het releasepakket **koppelvlakspecificatie**: uitgangspunten en de koppelingspecificaties per informatiestroom (OC naar P&R, LMS en SIS) met hun payload-specificaties |
| [`Referentiemateriaal/`](Referentiemateriaal/) | Reference Material | De kaderscenario's per leerroute, de architectuurbesluiten (ADR's) en de ontwerpprincipes waarop de specificaties steunen; onderbouwing, geen onderdeel van een releasepakket |
| [`Werkwijze/`](Werkwijze/) | Documentation | Hoe we werken: de sjablonen waarmee een specificatie wordt opgezet |
| [`scripts/`](scripts/) | CI/CD | Gereedschap, waaronder de generator en validator voor de schema- en instantiebomen in de payload-specificaties |

De kolom *Container* verwijst naar het repo-setupmodel, dat deze repository beschrijft als **Public source**: de bron van de releaseartefacten, naast een private projectrepository en de gepubliceerde releasepakketten.

## Waar te beginnen

Nieuw hier? Begin bij [`Koppelvlakspecificaties/README.md`](Koppelvlakspecificaties/README.md). Dat document geeft het ketenoverzicht, de afkortingenlegenda en de leesvolgorde.

## Verhouding met de meta-repository

De kaderstelling ontstaat in [`Npuls-OKx/meta`](https://github.com/Npuls-OKx/meta), de knowledge base waar referentiekader, scenario's, het ArchiMate-model en het OEAPI consumer-profiel worden ontwikkeld. Wat daar tot een releasebaar artefact rijpt, komt hierheen. Achtergronddocumenten die niet meeverhuizen worden vanuit deze repository **gepind** aangehaald op een meta-commit, zodat een gepubliceerde specificatie niet met de bron meebeweegt.

## Bijdragen

Iedereen mag issues en pull requests indienen; alleen het verantwoordelijke OKx-team merget. Werk gaat via een feature branch naar `dev`; van `dev` naar een release branch, waar een releasepakket een versielabel krijgt.
