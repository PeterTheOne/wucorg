---
layout: post
title: O Que é Mineração de Bitcoin?
description: O Que é Mineração de Bitcoin?
author: Melvin Draupnir
author-url: /melvin-draupnir/
published: true
---

<center><iframe width="700" height="394" src="https://www.youtube.com/embed/GmOzih6I1zs" frameborder="0" allowfullscreen></iframe></center>

<h2>Antes de começarmos…</h2>

Antes de continuar a leitura, tenha em mente que a maioria dos usuários do Bitcoin não mineram! Mas se você quiser minerar, então essa unidade <a href="http://geni.us/3i0s">mineradora de Bitcoin</a> provavelmente oferece o melhor custo-benefício. A mineração bitcoin é bem competitiva, e a volatilidade no <a href="/en/bitcoin-price/">preço do Bitcoin</a> dificulta a obtenção de lucro sem também especular no preço. Minerar faz mais sentido se você estiver fazendo por diversão, para aprender ou para ajudar a manter o Bitcoin seguro, e não estiver interessado em lucrar. Se você tiver acesso a energia muito barata e a habilidade de gerenciar um negócio de grande escala, então você tem chance de fazer um lucro considerável com mineração Bitcoin.

Se você quiser ganhar bitcoins com base em uma quantidade fixa de poder de mineração, mas não quer operar o equipamento você mesmo, você pode comprar um contrato de mineração.

Outra ferramenta que muitos usuários costumam adquirir é o <a href="/bitcoin-debit-cards/">cartão de débito Bitcoin</a>, que é um cartão de débito pré-pago que pode receber fundos em bitcoins. 

<h2>O Que é Mineração de Bitcoin? </h2>

A mineração Bitcoin é como uma grande loteria onde você usa seu equipamento de mineração para competir com todos os outros mineradores da rede para ganhar bitcoins. Um equipamento de mineração mais poderoso consegue realizar mais tentativas por segundo para ganhar nessa loteria, enquanto a própria rede Bitcoin se auto-ajusta a cada duas semanas para manter a taxa de um acerto a cada 10 minutos. Em uma visão geral, a mineração de bitcoins é o processo que garante a integridade das transações gravadas no registro público (public ledger) do Bitcoin, a block chain. Conduzindo essa loteria onde o preço de admissão é a eletricidade consumida e o equipamento especializado, o custo para corromper a rede Bitcoin é proporcional ao poder computacional empregado pelos mineiros. 

<h2>Detalhes Técnicos </h2>

Durante a mineração, seu equipamento de mineração Bitcoin executa uma <a href="https://en.bitcoin.it/wiki/Proof_of_work">função hash criptográfica</a> (duas rodadas de SHA256) em algo chamado <a href="https://en.bitcoin.it/wiki/Block_hashing_algorithm">block header</a>, que é o cabeçalho de um bloco. Para cada hash que é tentado, o software de mineração irá usar um número diferente como o elemento aleatório do cabeçalho do bloco, esse número é chamado nonce. Dependendo do nonce e do resto do conteúdo do bloco, a função hash irá gerar um número parecido com esse: 93ef6f358fbb998c60802496863052290d4c63735b7fe5bdaac821de96a53a9a

Você pode olhar para o hash como um número bem longo. (Esse é um número em base hexadecimal, onde as letras A-F representam os valores de 10 a 15.) Para assegurar que os blocos sejam encontrados a cada 10 minutos, mais ou menos, existe algo chamado difficulty target, que define a dificuldade absoluta da geração do hash. Para criar um bloco válido, seu programa de mineração deve encontrar um hash que seja menor que esse valor. Por exemplo, se o difficulty target é

1000000000000000000000000000000000000000000000000000000000000000

qualquer número que comece com zero estaria abaixo do alvo, como por exemplo:

0787a6fd6e0782f7f8058fbef45f5c17fe89086ad4e78a1520d06505acb4522f

Mas, se diminuirmos o alvo para

0100000000000000000000000000000000000000000000000000000000000000

então agora nós precisamos de um número que comece com dois zeros para que ele seja válido:

00db27957bd0ba06a5af9e6c81226d74312a7028cf9a08fa125e49f15cae4979

Como o difficulty target é um número bem grande e difícil de lidar, os usuários costumam usar um número mais simples para expressar o alvo atual. Esse número é chamado de mining difficulty, ou dificuldade de mineração. Essa dificuldade é uma medida relativa que expressa a dificuldade atual de geração de um bloco comparada com a dificuldade na geração do primeiro bloco. Então, uma dificuldade de 70000 significa que para gerar um bloco você terá 70000 vezes mais trabalho do que <a href="https://en.bitcoin.it/wiki/Satoshi_Nakamoto">Satoshi Nakamoto</a> teve para gerar o primeiro bloco. Para ser honesto, naquela época, tanto o equipamento utilizado quanto o algoritmo implementado eram muito mais lentos e menos otimizados do que os atuais.

Para manter uma taxa de criação de cerca de 1 bloco a cada 10 minutos, a dificuldade é ajustada a cada 2016 blocos, usando uma formula compartilhada. A rede tenta manter a dificuldade em um nível tal que 2016 blocos levem cerca de 14 dias para serem processados usando o poder computacional atual da rede. Por isso, quando há um aumento do poder computacional empregado na rede, a dificuldade aumenta proporcionalmente.

<h2>Equipamento Para Mineração de Bitcoin </h2>

<strong>CPU</strong>

No início, minerar com uma CPU, o processador do computador, era a única maneira de minerar bitcoins, e o único software existente para mineração era o cliente criado por Satoshi. Em sua missão de aumentar a segurança da rede e ganhar mais bitcoins, os mineradores inovaram em várias frentes, e já há alguns anos minerar usando uma CPU se tornou um esforço relativamente fútil. Você pode minerar por décadas usando seu notebook sem ganhar uma única moeda.

<strong>GPU</strong>

Cerca de um ano e meio após o início da rede, foi descoberto que placas de vídeo de alto desempenho eram muito mais eficientes para minerar bitcoins, e o panorama mudou. A mineração agora passou a ser com o uso de GPU (Graphical Processing Unit), ou unidade de processamento gráfico. A principal característica de algumas dessas unidades é que elas são massivamente paralelas, ou seja, possuem vários núcleos de processamento trabalhando em paralelo, executando operações simultaneamente. Essa característica permitiu um aumento de 50 a 100 vezes no poder de mineração, com um consumo de energia muito menor por unidade de trabalho.

Qualquer GPU pode ser utilizada para minerar, mas a arquitetura da linha de GPUs da AMD se revelou muito superior à arquitetura da nVidia, para a mineração de bitcoins, e a ATI Radeon HD 5780 veio a ser a opção com melhor custo-benefício na época.

<strong>FPGA</strong>

Assim como ocorreu a transição da CPU para a GPU, o mundo bitcoin subiu mais ainda na escala de tecnologia e adotou as FPGAs. Com o sucesso no lançamento da FPGA ‘Single’, da Butterfly Labs, o panorama da mineração de bitcoins mudou novamente e deu lugar a equipamentos dedicados à mineração de bitcoins, montados especialmente para esse fim. 

Apesar de as FPGAs não oferecerem o mesmo aumento de 50-100 vezes na velocidade de mineração, como aconteceu na transição da CPU para a GPU, ainda assim sua vantagem era a maior eficiência energética e facilidade de uso. Uma placa de vídeo típica de 600 MH/s (atenção, não é MHz) consumia mais de 400W, enquanto um equipamento de mineração FPGA típico oferecia um hashrate de 826 MH/s com um consumo de apenas 80W.

Essa melhoria de cerca de 5x na eficiência energética permitiu que surgissem as primeiras fazendas de mineração em larga escala com lucro operacional. Assim teve início a indústria de mineração bitcoin.

<strong>ASIC</strong>

O mundo da mineração agora está solidamente na era ASIC (Application Specific Integrated Circuit). Um ASIC é um circuito integrado, ou chip, que executa uma tarefa específica, e apenas essa tarefa, nesse caso a mineração de bitcoins. Diferente das FPGAs, um ASIC não pode ser reprogramado para realizar outra tarefa. 

Um ASIC projetado para minerar bitcoins, só consegue minerar bitcoins, e sempre irá apenas minerar bitcoins. Essa falta de flexibilidade de um ASIC é compensada pelo fato de que ele oferece um aumento de 100 vezes em poder de hash, com uma redução ainda maior no consumo de energia quando comparado com todas as tecnologias anteriores.

Diferente de todas as gerações de equipamento anteriores ao ASIC, o ASIC pode ser o “fim da linha” quando se fala em avanços significativos em tecnologia de mineração. As CPUs foram substituídas pelas GPUs, que por sua vez foram substituídas pelas FPGAs, que finalmente foram substituídas pelos ASICs. Ainda não existe nenhuma tecnologia que virá a substituir os ASICs, agora ou em um futuro imediato, 

É claro que os produtos ASIC ainda podem sofrer melhorias e refinamentos que irão aumentar sua eficiência em pequenos incrementos, mas nada que irá oferecer um aumento de 50 a 100 vezes no poder de hashing ou que irá reduzir o consumo de energia em 7 vezes, como aconteceu nas transições anteriores. Isso torna o consumo de energia dos dispositivos ASIC o mais importante fator em qualquer produto que use a tecnologia, devido ao fato de a vida útil dos equipamentos de mineração com ASIC ser a maior de toda a história da mineração bitcoin.

É fácil conceber que um dispositivo ASIC comprado hoje ainda estará minerando daqui a dois anos, se o dispositivo oferecer uma eficiência energética boa o suficiente para que o custo da energia consumida não seja maior que ganho que ele permite. O lucro que você pode obter depende também da cotação da moeda, mas de maneira geral, quanto maior a eficiência energética do equipamento, mais lucrativo ele é. Se você quiser tentar a sorte com mineração de bitcoins, então esse  <a href="http://geni.us/3i0s">minerador Bitcoin</a>  é provavelmente a melhor oferta.

<h2>Software de Mineração de Bitcoin</h2>

Há duas maneiras básicas de minerar: por conta própria, ou como parte de um pool, ou adquirindo <a href="https://www.bitcoinmining.com/best-bitcoin-cloud-mining-contract-reviews/">contratos de mineração Bitcoin em nuvem</a>, tomando o cuidado de <a href="/avoid-bitcoin-cloud-mining-scams/">evitar scams de serviços de mineração Bitcoin em nuvem</a>. A grande maioria dos mineiros de bitcoin escolhe participar de um pool de mineração, pois isso equaliza melhor a sorte inerente ao processo de mineração de Bitcoin. Antes de fazer parte de um pool, configure uma <a href="/en/getting-started">carteira bitcoin</a> para que você tenha um local seguro para armazenar suas bitcoins. A seguir, você só precisa se juntar a um pool de mineração e configurar seu(s) cliente(s) de mineração para que se conecte(m) a esse pool. Com a mineração em pool, o lucro de cada bloco gerado por qualquer um dos membros desse pool é dividido por todos os membros, de acordo com o número de hashes que cada um contribuiu. 
  
Quanto de banda a mineração de Bitcoin consome? Se você estiver usando um <a href="https://www.bitcoinminer.com/">minerador bitcoin</a> para minerar em pool, então o consumo de banda é negligível, cerca de 10MB/dia. No entanto, o ideal é que você tenha uma conexão de boa qualidade, para que você receba todas as atualizações dos trabalhos o mais rápido possível.

Com esse método, todos os membros do pool recebem um montante mais frequente e estável (isso se chama reduzir a variância), mas o valor que você recebe pode ser reduzido se o pool cobrar algum tipo de taxa. Minerar por conta própria pode te retornar montantes maiores, mas infrequentes, enquanto que a mineração em pool te retorna montantes menores e frequentes, porém os dois equivalem ao mesmo montante a longo prazo, se você estiver em um pool sem cobrança de taxas.

<h2>Mineração de Bitcoin em Nuvem</h2>

Comprando contratos de mineração de Bitcoin em nuvem, os investidores podem ganhar bitcoins sem ter o trabalho de lidar com equipamento, software, eletricidade, conexão com a internet, e outras dificuldades relacionadas a essa atividade.

ATENÇÃO: Nós NÃO temos nenhuma garantia quanto aos serviços prestados pelos sites listados nesta seção. Recentemente tem surgido uma quantidade enorme de scams de mineração de bitcoins em nuvem.

<strong><a href="http://geni.us/hashflare">Review do Hashflare</a></strong>: O Hashflare oferece contratos de mineração SHA-256, bem como moedas SHA-256 mais rentáveis, com pagamento automático em BTC. O cliente precisa comprar no mínimo 10 GH/s.

<strong><a href="http://geni.us/advendorgm">Review da Genesis Mining</a></strong>: A Genesis Mining é a maior provedora de mineração em nuvem para Scrypt e Bitcoin. Ela oferece três planos de mineração em nuvem para Bitcoin com preços razoáveis. Ela também oferece contratos de mineração de Zcash.

<strong><a href="http://geni.us/hashing24">Review do Hashing 24</a></strong>: O Hashing24 está no mercado de mineração Bitcoin desde 2012. Eles têm instalações na Islândia e na Georgia, e usam os modernos chips ASIC da BitFury para obter máximo possível em desempenho e eficiência.

<h2>O Que é Mineração de Bitcoin?</h2>

<center><img src="/images/what-is-bitcoin-mining.png" alt="bitcoin mining saga" /></center>

Mineração de Bitcoin é o processo de adicionar registros de transações ao registro publico de transações realizadas da rede Bitcoin. Esse registro público de transações é chamado block chain, pois ele é organizado como uma cadeia de blocos. A block chain serve como garantia para o resto da rede de que as transações contidas ali foram de fato realizadas.

Os nós Bitcoin usam a block chain para distinguir transações Bitcoin legítimas das fraudulentas, como as tentativas de gastar novamente bitcoins que já foram gastas em outro lugar.

A mineração de Bitcoins foi intencionalmente projetada para ser custosa do ponto de vista computacional, de forma que o número de blocos encontrados por dia pelos mineiros seja estável. Cada bloco precisa conter uma “proof-of-work”, ou prova de trabalho, para ser considerado válido. Essa prova de trabalho é verificada por outros nós Bitcoin toda vez que eles recebem um bloco. O Bitcoin usa a função de prova de trabalho <a href="/what-is-hashcash/">hashcash</a>.

O propósito primário da mineração é permitir que os nós Bitcoin cheguem a um consenso seguro, à prova de fraudes, com relação à autenticidade das transações. Minerar também é o mecanismo usado para inserir novas Bitcoins no sistema: os mineiros são pagos através das taxas de transação, bem como um “subsídio” em emissões de novas moedas.

Isso serve tanto para disseminar novas moedas de uma forma descentralizada, como também para motivar as pessoas a proverem a segurança necessária ao sistema.

Esse processo é chamado de mineração de Bitcoin porque ele se assemelha ao processo de mineração de outros recursos naturais: requer esforço e lentamente disponibiliza novas moedas em uma taxa próxima daquelas em que outros recursos, como o ouro, são minerados do solo.

<h2>O Que é a Prova de Trabalho?</h2>

<center><img src="/images/what-is-proof-of-work.png" alt="bitcoin mining saga" /></center>

Uma prova de trabalho é um dado difícil (custoso, levou tempo) de ser produzido de forma a satisfazer certos requisitos. Verificar se esse dado satisfaz os requisitos impostos deve ser uma tarefa trivial.

Produzir uma prova de trabalho pode ser feito por meio de um processo aleatório com baixa probabilidade de acerto, para que seja necessário uma grande quantidade média de tentativas para que essa prova de trabalho seja gerada. O Bitcoin usa a prova de trabalho Hashcash.

<h2>O Que é a Dificuldade de Mineração de Bitcoin?</h2>

<center><img src="/images/what-is-bitcoin-mining-difficulty.png" alt="bitcoin mining saga" /></center>

<h2>O Problema da Dificuldade Computacional</h2>

Minerar um bloco Bitcoin é difícil porque o valor do hash SHA-256 do cabeçalho de um bloco precisa ser menor ou igual ao valor do alvo (target) para que o bloco seja aceito pela rede.

Esse problema pode ser simplificado para facilitar a explicação: O hash de um bloco precisa começar com um certo número de zeros. A probabilidade de calcular um hash que comece com muitos zeros é muito baixa, portanto são necessárias várias tentativas. A cada tentativa o nonce é incrementado, e então o novo hash é calculado. Veja Proof of Work para saber mais sobre o assunto.

<h2>A Métrica de Dificuldade da Rede Bitcoin</h2>

A dificuldade de mineração da rede Bitcoin é a medida relativa da dificuldade de encontrar um bloco comparada com o menor nível de dificuldade possível. Ela é recalculada a cada 2016 blocos para um valor tal que os últimos 2016 blocos gerados teriam sido gerados em exatamente duas semanas se todos estivessem minerando nessa dificuldade. Com isso, a taxa média de geração de blocos se mantém em cerca de um bloco a cada 10 minutos. 

À medida que novos mineiros se juntam à rede, a dificuldade aumenta para compensar o aumento do poder computacional empregado na rede, a fim de manter a taxa de criação de blocos constante. Qualquer bloco gerado por mineradores maliciosos que não atende ao requisito de dificuldade será rejeitado por todos na rede e, portanto, será inutilizado.

<h2>A Recompensa Pelo Bloco</h2>

Quando um bloco é descoberto, o seu descobridor pode se recompensar com um certo número de bitcoins, que é um valor consensual aceito por todos na rede. Atualmente essa recompensa é de 25 bitcoins; esse valor é reduzido pela metade a cada 210.000 blocos. Veja Controlled Currency Supply ou use uma <a href="http://www.bitcoinx.com/profit/">calculadora de mineração de bitcoin</a>.

Adicionalmente, o mineiro recebe também as taxas de transação pagas pelos usuários que enviaram as transações. Essas taxas são um incentivo para o mineiro incluir a transação em seu bloco. No futuro, à medida que a quantidade de bitcoins que cada mineiro pode criar ao gerar um bloco diminuir, essas taxas passarão a compor a maior parte da recompensa recebida pelo mineiro.

<h2>Agradecimentos</h2>

Ao Blitzboom e o pessoal da #bitcoin-dev pela ajuda na criação desse guia!
