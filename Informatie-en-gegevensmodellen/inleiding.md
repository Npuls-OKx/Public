# Inleiding

Dit document legt vast wat onderwijsgegevens betekenen en in welke vorm ze over een koppeling gaan: de begrippen en hun definities, de objecttypen en hun samenhang, de entiteiten met hun velden, de JSON Schema's waartegen een implementatie kan valideren, de regels die zo'n schema niet kan uitdrukken, en per koppeling welk deel ervan meegaat.

**Aanleiding.** De modellen zijn eerder als bijlage bij de koppelvlakspecificatie uitgebracht. Ze hebben een eigen ritme: een veld erbij of een strakkere validatie raakt wel elke implementatie die tegen het schema valideert, maar niet de berichtstroom of het endpoint eromheen. Omgekeerd verandert een nieuwe koppelingspecificatie vaak niets aan de vorm van de gegevens. Als bijlage deelden beide noodgedwongen één versienummer, en zei een versiesprong van het ene niets over het andere.

**Context.** OKx modelleert in vier lagen, van betekenis naar techniek. De begrippen leggen vast wat een term betekent; het conceptueel informatiemodel ordent die begrippen en hun samenhang; het logisch gegevensmodel zet dat om in entiteiten, velden en relaties, onafhankelijk van de techniek; het technisch gegevensmodel legt vast hoe dat over de lijn gaat. Dit document draagt alle vier de lagen en verbindt ze: elk objecttype in het informatiemodel heeft een definitie in de begrippen, elke entiteit in het logisch model is terug te voeren op een objecttype, elke entiteit is terug te vinden als schema, en elk schema is terug te voeren op een entiteit. Laag 1 en 2 worden in de meta-repository gemodelleerd en gereviewd en komen hier als release-variant terecht.

| Laag | Wat de laag vastlegt | Waar |
|---|---|---|
| 1. Begrippen | Wat een term betekent | Dit document |
| 2. Conceptueel informatiemodel | Welke begrippen er zijn en hoe ze samenhangen | Dit document |
| 3. Logisch gegevensmodel | Entiteiten, velden en relaties, techniekonafhankelijk | Dit document |
| 4. Technisch gegevensmodel | De JSON Schema's waartegen een implementatie valideert | Dit document |

De [koppelvlakspecificatie](../Koppelvlakspecificaties/inleiding.md) beschrijft welke applicatiediensten een systeem implementeert en welk berichtverkeer daaroverheen gaat; zij verwijst naar dit pakket op een vastgelegde versie voor de vorm van wat er in die berichten zit. Deze modellen zijn **alfa en indicatief** ([U1](../Koppelvlakspecificaties/uitgangspunten.md#u1-indicatief-en-onderbouwend-niet-voorschrijvend)) en volgen de payloadvorm uit [U7](../Koppelvlakspecificaties/uitgangspunten.md#u7-payload-plat-met-verwijzingen-en-de-sleutelconventie): plat, met verwijzingen tussen objecten in plaats van nesting, zodat een consument alleen ophaalt wat hij nodig heeft.

**Doel.** Een bouwer moet hieruit kunnen afleiden wat een term betekent, welke objecten er zijn, hoe ze samenhangen, welke velden ze dragen, en wat er geldt bovenop wat het schema afdwingt. Geslaagd is het document wanneer twee partijen die er onafhankelijk tegenaan bouwen berichten uitwisselen die elkaar begrijpen.

**Scope.** De begrippen met hun definitie en de relatie met MORA en het Kernmodel Onderwijsinformatie, het conceptueel informatiemodel met de ontwerpkeuzes en de mapping op OEAPI v6, het logisch gegevensmodel met de regels daarbij, het technisch gegevensmodel met de voorbeeldpayloads en de mapping van Engelse veldnamen naar hun Nederlandse oorsprong, en de gebruiksprofielen per koppeling. Welke velden een koppeling gebruikt en waarom staat in de payload-specificatie van die koppeling, in de koppelvlakspecificatie; die is daarin leidend. HORA als derde referentiekader is nog niet onderzocht en staat als zodanig gemarkeerd. De interne structuur van een regelset, de endpoints waarover een payload gaat en de technische ontsluiting in OpenAPI vallen erbuiten, en al het overige eveneens.
