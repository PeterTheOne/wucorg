---
layout: post
title: Was ist Bitcoin-Mining?
description: Was ist Bitcoin-Mining?
author: Melvin Draupnir
author-url: /melvin-draupnir/
published: true
---

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/GmOzih6I1zs" frameborder="0" allowfullscreen></iframe></center>

<h2>Bevor wir beginnen...</h2>

Bevor Sie weiterlesen, machen Sie sich bitte bewusst, dass die meisten Bitcoin-Benutzer nicht schürfen! Wenn Sie aber schürfen, dürfte dieses<a href="http://geni.us/3i0s">Bitcoin-Schürfgerät</a> die beste Wahl sein.Beim kommerziellenMining (deutsch‚Schürfen‘) von Bitcoins herrscht starker Wettbewerb. Zudem macht es der schwankungsanfällige <a href=" /en/bitcoin-price/">Bitcoin-Preis</a>schwierig, finanzielle Gewinne zu erzielen, ohne auch auf den Preis zu spekulieren.Das Schürfen macht auch dann Sinn, wenn man sich nicht um Gewinne schert, es zum Spaß betreibt und lernen oder zur Sicherheit von Bitcoin beitragen will. Sofern große Mengen an billiger Elektrizität verfügbar sind und eine große kommerzielle Anlage verwaltet werden kann, wirft das Schürfen Gewinne ab.

Wer Bitcoins als Gegenleistung für eine festgelegte Rechenleistung bekommen möchte, die Hardware aber nicht selbst betreiben will, kann einen Schürfvertrag abschließen.
Ein weiteres Hilfsmittel, das gern gekauft wird, ist die <a href="/bitcoin-debit-cards/">Bitcoin-Debitkarte</a>, die man im Austausch gegen Bitcoins mit Geld aufladen kann. 

<h2>Was ist Bitcoin-Mining?</h2>

Das Bitcoin-Mining, das Schürfen von Bitcoins,ähneltstark einer riesigen Lotterie, bei der man mit seiner Schürf-Hardware mit allenanderen Leuten im Netzwerk konkurriert, um Bitcoins zu verdienen.Je schneller die Schürf-Hardware ist, desto mehr Versuche sind pro Sekunde möglich, diese Lotterie zu gewinnen.Unterdessen passt sich das Bitcoin-Netzwerk etwa alle zwei Wochen so an, dass die für dasErmitteln eines Gewinner-Blockhashs benötigte Zeit konstant bei zehn Minuten bleibt. Allgemein ausgedrückt: Das Schürfen von Bitcoins sorgt für die Sicherheit von Transaktionen, die in der öffentlichen Bitcoin-Datenbank, der Blockchain, verzeichnet werden.Der Preis für die Teilnahme an dieser Glückslotterie sind Elektrizität und eine spezielles Ausrüstung. Damit steigen die Kosten, um das Bitcoin-Netzwerk zu stören, parallel zu der gesamten Rechenleistung, die von allen Schürfernaufgewendet wird.

<h2>Technische Hintergründe</h2>

Beim Schürfen wendet die Hardware zweimal die <a href="https://en.bitcoin.it/wiki/Proof_of_work">kryptologische Hashfunktion</a> SHA256) auf den sogenannten <a href=" https://en.bitcoin.it/wiki/Block_hashing_algorithm">Blockheader</a> an. Die Schürf-Software verwendet bei jedem neuen Versuch, einen passenden Hash zu erzeugen, eine andere Zahl als zufälligen Bestandteil für den Blockheader. Diese Zahl wird Noncegenannt. Je nachdem, wie die Nonce lautet und was sich sonst noch in dem Block befindet, liefert die Hashfunktion einen Hash, der ungefähr so aussieht:

93ef6f358fbb998c60802496863052290d4c63735b7fe5bdaac821de96a53a9a

Man kann diesen Hash als eine extrem lange Zahl sehen, genauer gesagt eine Hexadezimalzahl, bei der die Buchstaben A–F den Zahlen 10–15 entsprechen. Um zu gewährleisten, dass etwa alle zehn Minuten ein Block gefunden wird, gibt es die sogenannte Ziel-Schwierigkeit. Die Schürf-Software muss, um einen gültigen Block zu erzeugen, einen Hash finden, der unter der Ziel-Schwierigkeit liegt. So läge bei einer Ziel-Schwierigkeit von

1000000000000000000000000000000000000000000000000000000000000000

jede Zahl, die kleiner als 0 ist, unterhalb der Ziel-Schwierigkeit, z. B.

0787a6fd6e0782f7f8058fbef45f5c17fe89086ad4e78a1520d06505acb4522f

Durch Herabsetzen der Ziel-Schwierigkeit auf

0100000000000000000000000000000000000000000000000000000000000000

sind zwei Nullen am Anfang nötig, damit der Hash darunter liegt:

00db27957bd0ba06a5af9e6c81226d74312a7028cf9a08fa125e49f15cae4979

Da das Ziel eine solch sperrige Zahl mit einer Unmenge von Stellen ist, verwenden die Schürfer meist eine einfachere Zahl, um das aktuelle Ziel auszudrücken.Diese Zahl ist die sogenannte Schürf- oder Mining-Schwierigkeit. Der Schwierigkeitsgrad drückt aus, um wie viel schwieriger das Erzeugen des aktuellen Blocks im Vergleich zum Erzeugen des ersten jemals erzeugten Blocks ist. Ein Schwierigkeitsgrad von 70.000 bedeutet demnach: Die für den aktuellen Block erforderliche Rechenleistung ist 70.000-mal höher als die Rechenleistung, die <a href="https://en.bitcoin.it/wiki/Satoshi_Nakamoto">Satoshi Nakamoto</a> brauchte, um den allerersten Block zu erzeugen. Der Fairness halber muss gesagt werden, dass die damalige Schürf-Software und die Algorithmen viel langsamer und weniger optimiert waren.

Damit kontinuierlich etwa alle zehn Minuten ein Block entsteht, wird der Schwierigkeitsgrad nach jeweils 2016 Blöcken mithilfe einer freigegebenen Formelangepasst. Das Netzwerk versucht den Schwierigkeitsgrad so zu verändern, dass es ungefähr 14 Tage dauert, um mit der aktuellen globalen Rechenleistung2016 Blöcke zu erzeugen. Das ist der Grund, warum mitzunehmender Netzwerk-Rechenleistung auch der Schwierigkeitsgrad steigt.

<h2>Bitcoin-Schürf-Hardware</h2>

<strong>CPU</strong>

Anfangs war das Schürfen per CPUund mithilfe des Original-Clients von Satoshi der einzige Weg, um Bitcoins zu erzeugen.Auf der Suche nach Möglichkeiten, das Netzwerk sicherer zu machen und mehr Bitcoins zu gewinnen, haben die Schürfer zahlreiche Innovationen entwickelt; mittlerweile ist das Schürfen per CPU seit Jahren relativ sinnlos. Mit dem Laptop schürft man möglicherweise jahrzehntelang, ohne einen einzigen Bitcoin zu verdienen.

<strong>GPU</strong>

Etwa anderthalb Jahre nach der Gründung des Netzwerks fand man heraus, dass sich mithilfe von High-End-Grafikkarten die Bitcoins viel effizienter schürfen ließen. Eine neue Situation war entstanden. Das CPU-basierte Schürfen wich dem Schürfen per GPU (Grafikprozessor, englisch graphics processing unit). Da einige Grafikprozessoren in der Lage waren, enorme Aufgabenmengen parallel auszuführen, ergab sicheine 50- bis 100-mal höhere Schürfleistung bei gleichzeitig weitausgeringerem Energieverbrauch pro Leistungseinheit.

Obwohl jeder moderne Grafikprozessor zum Schürfen verwendet werden kann, hat sich die Prozessorarchitekturvon AMD-Grafikkarten im Vergleich zur Architektur von nVidia-Grafikkarten als deutlich überlegen erwiesen. Die derzeit kosteneffizienteste Variante ist die ATI Radeon HD 5870.

<strong>FPGA</strong>

Wie schon beim Übergang vom CPU- zum GPU-basierten Schürfen stieg das Bitcoin-Schürfen dank Field Programmable Gate Array (FPGA) in der technologischen Nahrungskette weiter auf.Der erfolgreiche Start von Butterfly Labs FPGA Single machte den Weg frei für Hardware, die speziell für das Schürfen von Bitcoins ausgelegt ist.

Zwar brachten die FPGAs keine 50- bis 100-fache Erhöhung der Schürfgeschwindigkeit, wie es beim Übergang von CPU zu GPU der Fall gewesen war, doch dafür hatten FPGAs den Vorzug, energieeffizient und benutzerfreundlich zu sein. Während eine klassische Grafikkarte bei einer Leistung von 600 Mhash/s bis zu 400 Watt Strom verbrauchte, lieferte ein typisches FPGA-Schürfgerät eine Hashrate von 826 MHash/s – bei einem Verbrauch von 80 Watt.

Der fünfmal niedrigere Energieverbrauch machte es möglich, die ersten großen Bitcoin-Schürfparks, die operative Gewinne versprachen, zu bauen. Die Bitcoin-Schürfindustrie war geboren.

<strong>ASIC</strong>

Heute ist die Welt des Bitcoin-Schürfens längst im Zeitalter des Application Specific Integrated Circuit (ASIC, deutsch anwendungsspezifische integrierte Schaltung) angekommen. Ein ASIC ist ein Chip, der speziell für einen einzigen Zweck entwickelt wird.Anders als FPGAs lassen sich ASICsnicht für das Ausführen anderer Aufgaben umfunktionieren.

Ein ASIC, der für das Schürfen von Bitcoins entwickelt wurde, kann und wird nichts anderes tun als Bitcoins schürfen.Die fehlende Flexibilität des ASIC wird durch die Tatsache wettgemacht, dass er im Vergleich zu sämtlichen älteren Technologien 100-mal mehr Hashing-Leistung bietet und dabei auch noch weniger Strom verbraucht.

Anders als bei früheren Hardware-Entwicklungen könnte mit ASIC, was bahnbrechende Schürftechnologien betrifft, gewissermaßen das Ende der Fahnenstange erreicht sein. CPUs wurden abgelöst von GPUs, an deren Stelle FPGAs traten, die dannihrerseits durch ASICs verdrängt wurden.Es gibt weder jetzt noch in unmittelbarer Zukunft eine Technologie, die als Ersatz für ASICsgeeignet wäre.

Schrittweise Verbesserungen bei den ASICs-Produkten wird es zwargeben unddie Effizienz wird sich weiter erhöhen, doch die Zeiten, wo neue Technologien eine 50- bis 100-fache Steigerung der Hashing-Leistungbrachten, sind vorüber.So wird der Stromverbrauch von ASIC-Geräten zum wichtigsten aller Faktoren: Die zu erwartende Gebrauchsdauer eines beliebigen ASIC-Schürfgeräts istnämlich länger als die Geschichte des Bitcoin-Schürfens selbst.

Es darf angenommen werden, dass ein heute gekauftes ASIC-Gerät noch in zwei Jahren schürft, wenn das Gerät hinreichend energieeffizient ist und die Stromkosten nicht höher als die Ausbeute sind. Die Rentabilität des Schürfens hängt auch vom Wechselkurs ab, aber in jedem Fall gilt: Je energieeffizienter das Gerät ist, desto profitabler ist es. Für denjenigen, der sein Glück beim Bitcoin-Schürfen versuchen will, dürftedieses <a href="http://geni.us/3i0s">Bitcoin-Schürfgerät</a> die beste Wahl sein.

<h2>Bitcoin-Schürf-Software</h2>

Es gibt grundsätzlich zwei Bitcoin-Schürfmethoden: Allein oder als Mitglied eines Mining-Pools beziehungsweise über<a href=" https://www.bitcoinmining.com/best-bitcoin-cloud-mining-contract-reviews/">Cloud-Mining mit Schürfverträgen</a>. Vor <a href=" /avoid-bitcoin-cloud-mining-scams/">Bitcoin-Betrug beim Cloud-Mining</a> sollte man sich auf jeden Fall in Acht nehmen.Fast jeder, der Bitcoins schürft, entscheidet sich für einen Mining-Pool, um die Bedeutung des Zufalls während des Schürfvorgangs zu minimieren. Bevor man einem Pool beitritt, benötigt man eine <a href=" /en/getting-started">Bitcoin-Wallet</a>, eine digitale Geldbörse zum Lagern der Bitcoins. Anschließend tritt man einem Mining-Pool bei und muss das Schürfgerät (bzw. mehrere)mit dem Pool verbinden. Beim Pool-Mining werden alle aus den erzeugten Blöcken gezogenen Gewinne unter den Mitgliedern des Pools geteilt, der individuelle Anteil hängt davon ab, wie viele Hashs das Mitglied beigesteuert hat.

Wie viel Bandbreite benötigt man, um Bitcoins zu schürfen? Mit einem <a href="https://www.bitcoinminer.com/">Bitcoin-Schürfgerät</a> in einem Pool dürfte die Bandbreite mit 10 Megabyte pro Tag vernachlässigbar klein gering sein. Was man aber unbedingt braucht, ist eine besonders gute Konnektivität, damit man alle Updates zur Arbeitso schnell wie möglich erhält.

Wer als Mitglied eines Pools schürft, bekommt häufigere, gleichmäßige Auszahlungen (man spricht auch vom Reduzieren der Varianz), aber die Auszahlungen können wegen möglicher Gebühren, die der Pool erhebt, geringer ausfallen. Beim selbständigen Schürfen erhält man große, aber seltene Auszahlungen; beim Pool-Schürfen erhält man kleine, aber häufige Auszahlungen. Langfristig ergibt sich bei beiden Methoden die gleiche Summe, sofern man in einem gebührenfreien Pool schürft.

<h2>Bitcoin-Cloud-Mining</h2>

Durch das Abschließen von Cloud-Mining-Verträgen können Investoren Bitcoins verdienen, ohne sich mit Dingen wie Schürf-Hardware, Software, Elektrizität, Bandbreite und anderen Offline-Problemen befassen zu müssen.

Die folgende Liste ist NICHT dazu bestimmt, einzelne Dienste zu empfehlen. Sie dient lediglich dazu, Cloud-Mining-Anbieter zu vergleichen. In der Vergangenheit hat es eine enorme Zahl von Betrugsfällen im Zusammenhang mit Bitcoin und Cloud-Mining gegeben.

<strong><a href="http://geni.us/hashflare">Bewertung Hashflare</a></strong>: Hashflare bietet SHA-256-Schürfverträge an und es können die profitableren SHA-256-Coins geschürft werden, automatische Auszahlungen werden jedoch in Bitcoin vorgenommen. Kunden müssen mindestens 10 GHash/s kaufen.

<strong><a href="http://geni.us/advendorgm"> Bewertung Genesis Mining</a></strong>: Genesis Mining ist der größte Anbieter von Bitcoin- und Scrypt-Cloud-Mining. Genesis Mining bietet drei Tarife für Bitcoin-Cloud-Mining zu angemessenen Preisen an. Es sind auch Zcash-Schürfverträge erhältlich.

<strong><a href="http://geni.us/hashing24"> Bewertung Hashing 24</a></strong>: Hashing24 ist seit 2012 im Bitcoin-Schürfen aktiv.Der Anbieter betreibt Standorte in Island und Georgien. Er verwendet moderne ASIC-Chips von BitFury, welche die stärkste Leistung und größte Effizienz liefern, die möglich ist.

<h2>Was ist Bitcoin-Mining?</h2>

<center><img src="/images/what-is-bitcoin-mining.png" alt="bitcoin mining saga" /></center>

Bitcoin-Mining, also das Schürfen von Bitcoins, ist ein Prozess, bei dem in einer öffentlichen Transaktionsdatenbank sämtliche jemals durchgeführten Transaktionen verzeichnet werden. Diese Datenbank mit Transaktionen aus der Vergangenheitwird Blockchain genannt, weil sie eine Kette aus Blöcken darstellt.Die Blockchain dient den Mitgliedern des Netzwerks als Bestätigung, dass die Transaktionen stattgefunden haben.

Die Bitcoin-Knoten unterscheiden mithilfe der Blockchain legitime Bitcoin-Transaktionen von Versuchen, bereits ausgegebene Coins erneut auszugeben.

Das Bitcoin-Schürfen ist ganz bewusst so angelegt, dass es ressourcenintensiv und schwierig ist. So bleibt die Zahl der Blöcke, die pro Tag von den Schürfern gefunden werden, konstant. Die einzelnen Blöcke müssen einen sogenannten Proof of Work (deutsch etwa Arbeitsnachweis) enthalten, um als gültig anerkannt zu werden.Dieser Proof of Work wird von den anderen Bitcoin-Knoten jedes Mal überprüft, wenn sie einen Block erhalten. Bitcoin arbeitet mit der Proof-of-Work-Funktion <a href="/what-is-hashcash/">Hashcash</a>.

Das Hauptziel beim Schürfen ist, dass die Knoten ein sicheres, manipulationssicheres Maß an Übereinstimmung erreichen. Das Schürfen dient auch als ein Mechanismus, um Bitcoins ins System einzuführen: Schürfer bekommen alle Transaktionsgebühren bezahltund erhalten einen „Zuschuss” in Form von neu erzeugten Bitcoins.

Das dient zum einen dazu, neue Münzen auf dezentrale Weise zu verteilen; zum anderen sollen Leute dazu motiviert werden, zur Sicherheit des Systems beizutragen.

Das Bitcoin-Mining, das Schürfen von Bitcoins, heißt so, weil es dem Abbau anderer Rohstoffe ähnelt: Es erfordert Aufwand und es stellt neue Einheiten einer Währung in einem langsamen Tempo zur Verfügung, das der Geschwindigkeit ähnelt, mit der beispielsweise Gold aus dem Boden gewonnen wird.

<h2>Was ist der Proof of Work?</h2>

<center><img src="/images/what-is-proof-of-work.png" alt="bitcoin mining saga" /></center>

Ein <a href="/what-is-proof-of-work/">Proof of Work</a> (deutsch etwa Arbeitsnachweis) ist ein Datensatz, der schwierig (teuer, zeitaufwändig) zu produzieren war, weil bestimmte Anforderungen zu erfüllen waren. Es muss problemlos überprüfbar sein, ob die Daten den besagten Anforderungen genügen.

Das Erzeugen eines Proof of Work kann ein zufallsbasierter Vorgang mit geringer Profitabilität sein. Deshalb sind in der Regel viele Versuche erforderlich, bis ein gültiger Proof of Work generiert werden kann.Bitcoin arbeitet mit der Proof-of-Work-Funktion Hashcash.

<h2>Was hat es mit der Mining-Schwierigkeit auf sich?</h2>

<center><img src="/images/what-is-bitcoin-mining-difficulty.png" alt="bitcoin mining saga" /></center>

<h2>Das schwierige Rechenproblem</h2>

Es ist schwierig, mit Bitcoin einen Block zu erzeugen, weil der SHA-256-Hash am Anfang (Blockheader) eines Blocks kleiner oder gleich dem Ziel sein muss, damit der Block vom Netzwerk akzeptiert wird.

Vereinfacht ausgedrückt: Der Hash eines Blocks muss mit einer bestimmten Anzahl von Nullen beginnen. Da die Wahrscheinlichkeit, einen Hash zu berechnen, der mit vielen Nullen beginnt, sehr gering ist, werden viele Versuche benötigt. Um in jeder Runde einen neuen Hash zu erzeugen, wird eine Nonce inkrementiert. Weitere Informationen unter „Proof of Work”.

<h2>Der Schwierigkeitsgrad beim Bitcoin-Mining</h2>

Der <a href="/what-is-bitcoin-mining-difficulty/">Schwierigkeitsgrad beim Bitcoin-Mining</a> drückt aus, wie schwierig es ist, einen neuen Block zu finden, verglichen mit der leichtesten vorhandenen Möglichkeit. Das System berechnet die Schwierigkeit alle 2016 Blöcke neu. Der dabei ermittelte Wert entspricht der Schwierigkeit, mit der das gesamte Netzwerk exakt zwei Wochen lang hätte schürfen müssen, um die vorangegangenen 2016 Blöcke zu erzeugen. So entsteht im Durchschnitt alle zehn Minuten ein Block.

Je mehr Schürfer teilnehmen, desto mehr steigt die Geschwindigkeit, mit der Blöcke erzeugt werden. Dadurch steigt wiederum der Schwierigkeitsgrad, um die höhere Geschwindigkeit zu kompensieren, und die Blöcke werden wieder langsamer erzeugt. Jegliche von böswilligen Schürfern veröffentlichten Blöcke, die nicht der geforderten Ziel-Schwierigkeit entsprechen, werden von allen anderen Netzwerkmitgliedern einfach abgelehnt und sind damit wertlos.

<h2>Die Block-Belohnung</h2>

Wird ein Block gefunden, kann sich der Erzeuger selbst mit einer bestimmten Anzahl von Bitcoins belohnen, wobei das Einverständnis sämtlicher Netzwerkmitglieder erforderlich ist. Derzeit liegt diese Prämie bei 25 Bitcoins; der Wert halbiert sich alle 210.000 Blöcke. Siehe auch „Kontrollierte Geldmenge” oder verwenden Sie einen <a href="http://www.bitcoinx.com/profit/">Bitcoin-Mining-Rechner</a>.

Außerdem erhält der Schürfer Gebühren, die Nutzer für Transaktionen zahlen, als Belohnung. Das bietet ihm einen Anreiz, um die Transaktion in seinen Block einzubeziehen. In Zukunft, wenn die Zahl neuer Bitcoins, die ein Schürfer pro Block erzeugen darf, kleiner wird, werden die Gebühren einen weit größeren Anteil am Schürfeinkommen haben.

<h2>Vielen Dank an</h2>

Blitzboom und die Leute von #bitcoin-dev für ihre Hilfe beim Schreibens dieses Leitfadens!
