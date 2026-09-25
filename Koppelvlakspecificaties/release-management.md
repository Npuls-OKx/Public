# Release management van de koppelvlakspecificatie

## 1. Inleiding

**Aanleiding.** De [algemene releaseregels](../Algemeen/release-management/Release-management-algemeen.md) definiëren een major als een niet-backward-compatibele wijziging waarna afnemers wordt geadviseerd te migreren. Die definitie gaat uit van een artifact waaraan een afnemer zich houdt. Dat is de koppelvlakspecificatie niet. Zij beschrijft hoe partijen kúnnen koppelen, niet of ze moeten koppelen, en welke koppeling een partij aangaat bepaalt die partij zelf. Het generieke schema toepassen alsof dit pakket een contract is, dwingt migraties af die niemand nodig heeft; wat dat kost is doorgerekend in het versiescenario.

**Context.** Het pakket bevat een lijst van koppelingen die systemen aan elkaar knoopt, en per koppeling de berichtstromen waarmee dat kan. Een berichtstroom is samengesteld uit bouwblokken die los daarvan zijn vastgelegd: applicatiediensten met hun endpoints en payloads, en interactiepatronen. Die bouwblokken zijn wat een implementatie deelt met andere implementaties.

**Doel.** Vastleggen wat versiebeheer voor dit pakket betekent: waar een partij zich aan houdt, wat een versienummer wel en niet zegt, en langs welke weg de inhoud wijzigt. Het beantwoordt daarmee de vraag wanneer een release een major, een minor of een patch is, en wat een afnemer bij elk van die drie moet doen.

**Scope.** Het releasepakket koppelvlakspecificatie. De [informatie- en gegevensmodellen](../Informatie-en-gegevensmodellen/README.md) vormen een eigen pakket met een eigen versie en leggen hun versiebeheer zelf vast; dit document legt alleen de verhouding met dat pakket vast. De OpenAPI-specificatie valt erbuiten, net als de vraag welke partij met welke andere partij koppelt. Al het overige valt buiten dit document.

---

## 2. Releasepakket

Het pakket bestaat uit de inleiding en de uitgangspunten, de requirementsboom, de applicatiecomponenten met hun koppelvlak, de koppelingspecificaties met de berichtstromen, de applicatiediensten met hun endpoints, de interactiepatronen en de auth-standaard. Wat er in welke volgorde in het gebouwde document komt, en op welke versie van de informatie- en gegevensmodellen het bouwt, staat in [`release.json`](release.json).

---

## 3. Eigenaarschap

| Activiteit | Eigenaar-team | Review-/consulterend team | Communicatie-rol |
|------------|:---:|:---:|:---:|
| Inhoud van het artifact | R/A | C | I |
| Release (versie bepalen, publiceren) | R/A | C | I |
| Vaststellen dat een bouwblok in plaats wijzigt | A | R | C |
| Vaststellen dat een berichtstroom vervalt | A | R | C |
| Communicatie naar belanghebbenden | C | C | R/A |

Het eigenaar-team is het OKx-team dat in dit repository merget. De twee rijen die in het [template](../Algemeen/release-management/Release-management-template.md#3-eigenaarschap) samen één regel vormen zijn hier gesplitst, omdat dit de twee besluiten zijn die in [§4](#4-versiebeheer) een uitzondering vormen op de hoofdregel. Welke teams de kolommen invullen is nog niet belegd.

---

## 4. Versiebeheer

Dit pakket volgt het SemVer-schema en de definities uit [algemene regels §3](../Algemeen/release-management/Release-management-algemeen.md#3-versienummering). Wat hieronder staat is wat daar specifiek voor dit pakket bij komt.

### 4.1 Waaraan een partij zich houdt

Een partij houdt zich niet aan een versie van dit document. Zij implementeert **bouwblokken**: applicatiediensten, hun endpoints, de payloads daarvan en de interactiepatronen. Dat is wat haar implementatie deelt met andere implementaties, en dat is waar de term OKx-conform op slaat.

Het versienummer van het pakket is daarmee een **vindmiddel en geen contract**. Het zegt welke uitgave van de documentatie een partij heeft gevolgd en of er een nieuwere is, zodat zij kan terugzoeken waar zij vandaan komt. Niemand voldoet aan `v2.0.0`; men implementeert bouwblokken die in `v2.0.0` beschreven staan.

### 4.2 Berichtstromen zijn een aanbod

Een koppelingspecificatie groepeert twee of meer systemen en beschrijft de berichtstromen waarmee die kunnen koppelen. Een partij implementeert de stromen die zij nodig heeft en is nooit verplicht er een te implementeren. Wil zij koppelen met een partij die een bepaalde stroom vereist, dan implementeert zij die stroom — maar dat is een afspraak tussen die twee, geen eis uit dit pakket.

Omdat een berichtstroom is samengesteld uit bouwblokken die zelfstandig zijn vastgelegd, kan een partij ook een eigen stroom samenstellen uit diezelfde bouwblokken. De lijst met stromen is daarmee een voorstel en geen voorschrift ([U1](uitgangspunten.md#u1-indicatief-en-onderbouwend-niet-voorschrijvend)). Wat dit pakket wegneemt is de vraag hoe de interfaces heten en welke vorm ze hebben, niet de vraag wie met wie koppelt.

### 4.3 Toevoegen is de hoofdregel

Een uitgave **voegt toe en wijzigt niet**. Nieuwe berichtstromen, nieuwe applicatiediensten, nieuwe endpoints en nieuwe optionele velden komen erbij; wat er is blijft zoals het is. Een bestaande implementatie blijft daarmee werken zonder dat iemand iets doet.

Moet een berichtstroom anders, dan komt er een **nieuwe stroom naast**: naast `x` verschijnt `x2`, en daarnaast te zijner tijd `x3`. De oude blijft staan zolang er partijen op draaien. Wie de nieuwe wil gebruiken stapt over wanneer het hem uitkomt; wie dat niet wil doet niets.

Dit is de reden dat brekende wijzigingen in dit pakket zeldzaam horen te zijn. Ze bestaan alleen in de twee uitzonderingen hieronder.

### 4.4 Twee uitzonderingen

**Een bouwblok wijzigt in plaats.** Soms is het beter een berichtstroom, een applicatiedienst of een endpoint te wijzigen dan er een naast te zetten: als elke partij erbij wint en een tweede variant het geheel alleen maar troebeler maakt. Dat is een besluit, geen constatering, en het hoort bij de rijen in [§3](#3-eigenaarschap) die daarvoor zijn aangewezen. Dit is de enige plek waar een wijziging bestaande implementaties breekt.

**Een berichtstroom vervalt.** Een stroom waarop niemand meer draait kan worden uitgefaseerd. Ook dat is een besluit, en het vraagt om een aankondiging vooraf, omdat de uitgever niet kan zien wie er nog op draait.

### 4.5 Wanneer welke bump

| Bump | Wanneer | Wat een afnemer moet doen |
|---|---|---|
| **PATCH** | Tekstcorrectie, verduidelijking, hersteld voorbeeld: het contract wijzigt niet | Niets |
| **MINOR** | Er komt iets bij: een berichtstroom, een applicatiedienst, een endpoint, een optioneel veld, een enum-waarde, of een variant `x2` naast `x` | Niets, tenzij hij de nieuwe mogelijkheid wil gebruiken |
| **MAJOR** | Een van de twee uitzonderingen uit [§4.4](#44-twee-uitzonderingen) | Nagaan of het gewijzigde of vervallen bouwblok in zijn implementatie zit, en zo ja: overstappen binnen de aangekondigde termijn |

Een major is daarmee zeldzaam en de norm is een minor. Dat is geen versoepeling van de algemene regels maar een gevolg van de manier waarop de inhoud wijzigt.

### 4.6 Verhouding tot de informatie- en gegevensmodellen

Dit pakket bouwt op een vastgelegde versie van de informatie- en gegevensmodellen, gepind in `release.json`. De twee versienummers zijn onafhankelijk: een nieuwe uitgave van de gegevensmodellen dwingt geen uitgave van dit pakket af, en omgekeerd. Wat een uitgave van dit pakket wel doet, is vastleggen op welke versie van de gegevensmodellen de beschreven bouwblokken staan.

### 4.7 Nog te beslissen

Twee dingen volgen uit dit model maar zijn nog niet geregeld.

**Een berichtstroom heeft geen stabiele aanduiding.** Hij wordt nu geïdentificeerd door zijn kop in het document. Dat werkt niet zodra `x2` naast `x` komt, en het werkt ook niet voor een partij die in haar eigen documentatie wil verwijzen naar de stromen die zij ondersteunt. Een aanduiding die niet meebeweegt met de formulering van de kop is daarvoor nodig.

**De versiekolom bij een berichtstroom.** Elke stroom draagt nu een kolom `Versie`, vandaag overal `1.0`. Als een stroom nooit in plaats wijzigt, heeft dat nummer geen betekenis meer: een wijziging levert immers `x2` op en niet `x` versie `1.1`. Die kolom kan vervallen, of gaan aangeven in welke uitgave van het pakket de stroom is toegevoegd.

---

## 5. Communicatie

Standaard geldt [algemene regels §5](../Algemeen/release-management/Release-management-algemeen.md#5-communicatie-naar-belanghebbenden). Aanvullend geldt voor dit pakket dat de release notes **benoemen welke berichtstromen, applicatiediensten en endpoints erbij zijn gekomen**, zodat een afnemer kan zien of er iets bij zit dat hij wil gebruiken. Bij een van de twee uitzonderingen uit [§4.4](#44-twee-uitzonderingen) noemen de release notes bovendien welk bouwblok wijzigt of vervalt, en binnen welke termijn.

---

## 6. Releaseproces

Standaard geldt het proces uit [algemene regels §6](../Algemeen/release-management/Release-management-algemeen.md#6-releaseproces). Eén aanvulling: omdat een uitgave in de regel toevoegt en niet wijzigt, landt vrijwel alles op zowel release branch N als N-1. De tweede branch komt pas in beeld bij een van de twee uitzonderingen, en is de rest van de tijd een kopie van de eerste.
