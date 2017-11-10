---
layout: post
title: ¿Qué es la minería de bitcoins?
description: ¿Qué es la minería de bitcoins?
author: Melvin Draupnir
author-url: /melvin-draupnir/
published: true
---

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/GmOzih6I1zs" frameborder="0" allowfullscreen></iframe></center>

<h2>Antes de que comencemos...</h2>

Antes de que avancemos, es necesario comprender que ¡la mayoría de los usuarios de bitcoin no minan! Pero si esto es lo que deseas hacer <a href="http://geni.us/3i0s">Bitcoin Miner</a> probablemente es tu mejor opción. La minería de Bitcoin por lucro es muy competitiva y la volatilidad en el <a href="/en/bitcoin-price/">precio del Bitcoin</a> dificulta materializar ganancias monetarias sin especular con su precio al mismo tiempo. La minería tiene sentido si planeas hacerlo por diversión, para aprender o para apoyar la seguridad de la red Bitcoin y no te interesa si obtienes una ganancia. Si cuentas con acceso a electricidad barata en grandes cantidades y la habilidad de mantener instalaciones grandes y un negocio, puedes minar por lucro. 

Si deseas obtener bitcoins tomando en cuenta un valor fijo de poder de extracción, pero no quieres encargarte del hardware por tu cuenta, puedes adquirir un contrato minero. 

Otra herramienta que a muchas personas les gusta adquirir es una <a href="/bitcoin-debit-cards/">tarjeta de débito Bitcoin</a> lo que les permite añadir fondos a una tarjeta de débito usando bitcoins. 

<h2>¿Qué es la minería de bitcoin?</h2>

El minado de bitcoin se asemeja mucho a una enorme lotería donde se compite con el hardware de minado junto a todos los participantes de la red para extraer bitcoins.  Hardware de minado de bitcoins más rápido permite realizar más intentos por segundo para ganar esta lotería mientras la red Bitcoin se auto regula aproximadamente cada dos semanas para mantener la tasa a la que se consigue un bloque ganador en cada diez minutos. En el panorama general, el minado Bitcoin asegura las transacciones registradas en el historial público de Bitcoin, la cadena de bloques.  Al llevar a cabo una lotería aleatoria en la que la electricidad y el equipo especializado son el precio de admisión, el costo de alterar la red Bitcoin aumenta proporcionalmente con el poder computacional empleado por todos los participantes de la extracción.

<h2>Antecedentes técnicos</h2>

Durante la extracción, el software de minado de Bitcoin ejecuta una <a href="https://en.bitcoin.it/wiki/Proof_of_work">función criptográfica de hashing</a> (dos rondas de SHA256) en lo que se llama la <a href="https://en.bitcoin.it/wiki/Block_hashing_algorithm">cabecera del bloque</a>. Por cada nuevo hash que se intenta, el software de minería usará un número diferente como el elemento aleatorio de la cabecera del bloque, este número es llamado el nonce. Dependiendo del nonce y de qué más se encuentre en el bloque, la función de hashing retornará un hash que se verá algo así:

93ef6f358fbb998c60802496863052290d4c63735b7fe5bdaac821de96a53a9a

Puedes entender este hash como un número muy largo. (Es un número hexadecimal, lo que significa que las letras A-F son los dígitos 10-15). Para asegurar que los bloques sean hallados aproximadamente cada diez minutos, existe algo llamado objetivo de dificultad. Para crear un bloque válido tu minero debe encontrar un hash por debajo del objetivo de dificultad. De manera que si por ejemplo el objetivo de dificultad es 

1000000000000000000000000000000000000000000000000000000000000000

cualquier número que comience con un cero estaría por debajo del objetivo de dificultad, por ejemplo:

0787a6fd6e0782f7f8058fbef45f5c17fe89086ad4e78a1520d06505acb4522f

si reducimos el objetivo a 

0100000000000000000000000000000000000000000000000000000000000000

ahora necesitaremos dos ceros al inicio para estar por debajo: 

00db27957bd0ba06a5af9e6c81226d74312a7028cf9a08fa125e49f15cae4979

Debido a que el objetivo es un número engorroso con muchos dígitos, por lo general la gente usa un número más sencillo para expresar el objetivo actual. Este número es llamado la dificultad minera. La dificultad minera expresa qué tan difícil de generar es el bloque actual en comparación al primer bloque generado. Es decir que una dificultad de 70000 significa que para generar el bloque actual fue necesario realizar un esfuerzo 70000 mayor al de <a href="https://en.bitcoin.it/wiki/Satoshi_Nakamoto">Satoshi Nakamoto</a> al generar el primer bloque, Siendo justos, en esos tiempos el hardware de minería y los algoritmos eran mucho más lentos y menos optimizados.

Para que los bloques sigan apareciendo alrededor de cada diez minutos, la dificultad es ajustada usando una fórmula compartida cada 2016 bloques. La red intenta cambiarla de manera tal que tomando en cuenta el poder de procesamiento global actual, cada 2016 bloques tarden aproximadamente 14 días. Es por eso que cuando la potencia de la red aumenta, la dificultad también aumenta.

<h2>Hardware de minado de bitcoins</h2>

<strong>CPU</strong>

En un principio, la única forma de minar era con un CPU y esto se hacía usando el cliente original Satoshi. En la búsqueda de mayor seguridad en la red y de ganar más bitcoins, los mineros han innovado en diversos frentes y durante ya algunos años, el minar usando un CPU resulta inútil. Puedes minar durante décadas usando tu laptop sin obtener una sola moneda.

<strong>GPU</strong>

Alrededor de un año y medio después del comienzo de la red, se descubrió que las tarjetas gráficas de alta gama eran mucho más eficientes a la hora de minar bitcoins lo que cambió el panorama por completo. El minado de bitcoins con CPU dio paso al minado con GPU (Unidad de Procesamiento Gráfico). La naturaleza masivamente paralela de algunos GPU permitió aumentos de 50x a 100x en la capacidad de extracción de bitcoins al tiempo que se necesitaría mucha menos energía eléctrica por unidad de trabajo.

Aunque cualquier GPU moderno puede ser usado para minar, la línea de arquitectura GPU de AMD resultó ser bastamente superior a la arquitectura nVidia al momento de minar bitcoins, siendo la ATI Radeon HD 5870 la opción con mejor relación precio valor de la época.

<strong>FPGA</strong>

Al igual que con la transición de CPU a GPU, el mundo de la minería de bitcoins progresó en la cadena alimentaria al Field Programmable Gate Array. Con el exitoso lanzamiento del FPGA 'Single' de Butterfly Labs, el panorama del hardware en la minería de bitcoins abrió el camino a hardware especialmente dedicado al minado de bitcoins.

Aunque los FPGA no disfrutaron de un aumento de 50x - 100x en la velocidad de extracción como fue el caso en la transición del CPU al GPU, proporcionaron el beneficio añadido de la eficiencia energética y facilidad de uso. Una tarjeta gráfica típica de 600 MH/s consumía más de 400w de energía, mientras que una tarjeta FPGA típica proveía un hashrate de 826 MH/s con tan sólo 80w de electricidad.

La mejora de 5x permitió la construcción de las primeras granjas de minería rentables.  Esto dio lugar al nacimiento de la industria de la minería de bitcoins.

<strong>ASIC</strong>

El mundo de la minería de bitcoins se encuentra firmemente en la era del Circuito Integrado para Aplicaciones Específicas (ASIC). Un chip ASIC está diseñado específicamente para hacer una sola cosa. A diferencia de los FPGA, un ASIC no puede ser reutilizado para realizar otras tareas.

Un ASIC diseñado para minar bitcoins sólo puede minar bitcoins y minar bitcoins es lo único que hará mientras exista.  La inflexibilidad del ASIC es compensada por el hecho de que ofrece un aumento en la capacidad de hashing de 100x junto a un consumo eléctrico reducido en comparación a tecnologías anteriores.

A diferencia de todas las generaciones que precedieron ASIC, ASIC podría ser "el final de la línea" en lo que se refiere a tecnologías disruptivas en el mundo de la minería. Los CPU fueron reemplazados por los GPU, quienes a su vez fueron reemplazados por ASIC. No existe nada actualmente o en el futuro cercano capaz de reemplazar los ASIC.

Un refinamiento escalonado y aumento de la eficiencia de los productos ASIC tomará lugar, pero nada ofrecerá el aumento de 50x a 100x en la capacidad de hashing o una reducción de 7x en el consumo de energía como sucedió con lo ofrecido por las tecnologías anteriores. Esto hace que el consumo de energía en un dispositivo ASIC sea el factor más importante en cualquier producto ASIC, ya que el tiempo de vida útil estimado de un dispositivo minero ASIC es más que el tiempo entero que la minería de bitcoins lleva existiendo.

Es completamente posible que un dispositivo ASIC comprado hoy continúe minando dentro de dos años si el dispositivo es lo suficientemente eficiente en su consumo de energía y el costo de la electricidad no exceda al de su producción. La rentabilidad de la minería también está determinada por el tipo de cambio, pero bajo cualquier circunstancia mientras menor consumo de energía tenga el dispositivo de minería, más rentable será. Si quieres probar tu suerte con el minado de bitcoins entonces este <a href="http://geni.us/3i0s">minero Bitcoin</a> probablemente sea tu mejor opción.

<h2>Software para minar bitcoins</h2>

Existen dos maneras básicas de minar: Por tu cuenta o como parte de un grupo denominado de Bitcoin (pool) o con <a href="https://www.bitcoinmining.com/best-bitcoin-cloud-mining-contract-reviews/">contratos de minado en la nube</a> y siempre asegúrate de <a href="/avoid-bitcoin-cloud-mining-scams/">evitar estafas de minado Bitcoin en la nube</a>. Casi todos los mineros eligen minar como parte de un pool debido a que suaviza los efectos del azar inherente en el proceso de extracción de bitcoins. Antes de que te unas a un pool, asegúrate de que posees una <a href="/en/getting-started">cartera de bitcoins</a> de manera que tengas un lugar donde almacenar tus bitcoins. A continuación deberás unirte a un pool de minado y configurar tu minero(s) para que se conecten a ese pool. Minando en un pool, la ganancia generada por cualquier bloque generado por un miembro del pool es dividida entre los miembros del pool de acuerdo a la cantidad de hashes con la que contribuyeron.

¿Cuánto ancho de banda requiere la minería Bitcoin? Si estás usando un <a href="https://www.bitcoinminer.com/">minero bitcoin</a> para minar como parte de un pool entonces el número es insignificante con unos 10 MB/día.  Sin embargo, lo que sí es necesario es conectividad excelente de manera que puedas recibir las actualizaciones de la red lo más rápido posible.

Esto le proporciona a los miembros del pool pagos más frecuentes y constantes (a esto se le llama reducir la varianza), pero tu pago(s) puede ser reducido por las tarifas que pudiese cargar el pool.  El minar por tu cuenta te proporcionará pagos mayores de menor frecuencia y el minar en un pool te dará pagos pequeños pero constantes, pero ambos generarán lo mismo a fin de cuentas, si estás usando un pool de tarifas cero a largo plazo.

<h2>Minado de bitcoins en la nube</h2>

Al adquirir contratos de minado Bitcoin en la nube, los inversores pueden ganar Bitcoins sin necesidad de complicarse con el hardware de minado, software, la electricidad, ancho de nada u otros problemas offline.

El estar listado en esta sección NO significa un apoyo a estos servicios y debe servir únicamente como una comprobación entre mineros de Bitcoin en la nube. Han ocurrido una cantidad enorme de fraudes referentes a mineros de bitcoins en la nube.

<strong><a href="http://geni.us/hashflare">Hashflare Reseña</a></strong>: Hashflare ofrece contratos de minado SHA-256 y las muy rentables monedas SHA-256 pueden ser minadas al tiempo que los pagos automáticos siguen siendo en BTC. Los usuarios deben comprar al menos 10 GH/s.

<strong><a href="http://geni.us/advendorgm">Genesis Mining Reseña</a></strong>: Genesis Mining es el proveedor de minado de bitcoins en la nube y de scrypt más grande. Genesis Mining ofrece tres planes de minado Bitcoin a precios razonables. También hay disponibilidad de contratos de minado Zcash.

<strong><a href="http://geni.us/hashing24">Hashing 24 Reseña</a></strong>: Hashing24 ha formado parte de la minería Bitcoin desde 2012. Cuentas con instalaciones en Islandia y Georgia. Usan modernos chips ASIC de BitFury proporcionando el mejor desempeño y eficiencia posibles.

<h2>¿Qué es la minería de bitcoins?</h2>

<center><img src="/images/what-is-bitcoin-mining.png" alt="bitcoin mining saga" /></center>

El minado de bitcoins es el proceso de añadir registros de transacciones a la lista colectiva de las transacciones pasadas de Bitcoin. Esta lista de transacciones pasadas es llamada la cadena de bloques ya que es como una cadena formada por los bloques. La cadena de bloques sirve para confirmar al resto de la red que las transacciones tomaron lugar.

Los nodos Bitcoin usan la cadena de bloques para distinguir transacciones Bitcoin legítimas de intentos de reusar monedas que ya han sido gastadas en otra operación.

El minado de bitcoins está diseñado intencionalmente para ser difícil demandante en recursos de manera que el número de bloques encontrado por los mineros diariamente permaneciera estable.  Los bloques individuales deben contener una prueba de trabajo para ser considerados válidos. Esta prueba de trabajo es verificada por otros nodos de Bitcoin cada vez que reciben un bloque. Bitcoin usa la función de prueba de trabajo <a href="/what-is-hashcash/">hashcash</a>.

El propósito primario de la extracción es permitir a los nodos Bitcoin alcanzar un consenso seguro a prueba de falsificaciones.  El minado también es el mecanismo usado para introducir Bitcoins al sistema: Los mineros son pagados honorarios por las transacciones así como un "subsidio" por las monedas nuevas creadas.

Esto cumple el propósito de diseminar las nuevas monedas de una manera descentralizada, así como motivar a las personas a proveer seguridad para el sistema.

La minería o extracción de bitcoins es llamada así porque se asemeja al minado de otros productos: requiere un esfuerzo y lentamente pone a disposición una nueva moneda a una tasa que se asemeja a la tasa a la que otras mercancías como el oro son extraídos de la tierra. 

<h2>¿Qué es la prueba de trabajo?</h2>

<center><img src="/images/what-is-proof-of-work.png" alt="bitcoin mining saga" /></center>

La <a href="/what-is-proof-of-work/">prueba de trabajo</a> es una pieza de data difícil de producir (que consume muchos recursos, tiempo) de tal manera que logra satisfacer ciertos requerimientos. El comprobar si la data satisface los requerimientos debe ser trivial.

Producir una prueba de trabajo puede ser un proceso aleatorio con bajas probabilidades, de manera que es necesario un proceso de prueba y error extensivo antes de que se genere una prueba de trabajo válida. Bitcoin usa el Hashcash como prueba de trabajo.

<h2>¿Qué es la dificultad en el minado de bitcoins?</h2>

<center><img src="/images/what-is-bitcoin-mining-difficulty.png" alt="bitcoin mining saga" /></center>

<h2>Un problema computacionalmente difícil</h2>

El minado de bitcoins es difícil debido a que el hash SHA-256 de la cabecera de un bloque debe ser igual o inferior al objetivo para que el bloque sea aceptado por la red.

Este problema puede ser simplificado para su explicación: El hash de un bloque debe comenzar con un cierto número de ceros. La probabilidad de calcular un hash que comience con muchos ceros es muy baja, por lo tanto es necesario realizar muchos intentos. Para poder generar un nuevo hash en cada ronda, es necesario que se incremente un nonce. Para más información revisa Prueba de Trabajo.

<h2>La métrica de la dificultad en la red Bitcoin</h2>

La <a href="/what-is-bitcoin-mining-difficulty/">dificultad en la minería de bitcoins</a> es la medida de qué tan difícil es hallar un nuevo bloque en comparación al caso más sencillo posible. Es recalculada cada 2016 bloques de manera tal que los 2016 bloques anteriores habrían sido generados en un lapso de dos semanas, si todo el mundo hubiese minado con este nivel de dificultad. Esto resultará, en promedio, en un bloque cada diez minutos.

A medida que se unen más mineros, el ritmo de creación de los bloques aumentará.  A medida que la tasa de generación de los bloques aumenta, la dificultad aumenta para compensar lo cual disminuye nuevamente la tasa de creación de los bloques. Cualquier bloque liberado por mineros maliciosos que no cumpla con el objetivo de dificultad requerido sencillamente será rechazado por todos en la red y por lo tanto carecerá de valor.

<h2>Recompensa por bloque</h2>

Cuando un bloque es descubierto, quien lo descubre puede otorgarse un cierto número de bitcoins, el cual fue previamente acordado por todos los participantes de la red. Actualmente esta recompensa es de 25 bitcoins; este valor se reducirá a la mitad cada 210.000 bloques. Revisa Suministro Controlado de la Moneda o usa una <a href="http://www.bitcoinx.com/profit/">calculadora de minado de bitcoins</a>.

Adicionalmente, al minero se le otorgan honorarios pagados por los usuarios que realizan las transacciones. Este honorario es un incentivo para el minero para que incluya la transacción en su bloque. En el futuro, a medida que el número de nuevos mineros a los que se les permite crear en cada bloque se reduce, los honorarios pasarán a ser un porcentaje mucho más importante del ingreso minero. 

<h2>¡Gracias a</h2>

Blitzboom y a los chicos de #bitcoin-dev por su ayuda al momento de escribir esta guía!
