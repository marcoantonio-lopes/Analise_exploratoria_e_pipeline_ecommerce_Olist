# Conclusões da análise de e-commerce

## 1. Atrasos e avaliações dos pedidos

### Pergunta

Pedidos entregues com atraso apresentam maior proporção
de avaliações ruins do que pedidos entregues no prazo?

Dentre os pedidos atrasados, entre quais faixas de atraso ocorre o maior aumento na proporção de avaliações ruins?

### Recorte utilizado

Foram considerados pedidos entregues, com avaliação
e informações disponíveis para calcular o atraso.

Cada linha representa um pedido.
Avaliações ruins correspondem às notas 1 e 2.
A definição de atraso segue a regra documentada no projeto.

### Resultado

Nos pedidos atrasados, a proporção de avaliações ruins
foi de 62,85%, contra 9,49% nos pedidos entregues no prazo.

A diferença foi de 53,36 pontos percentuais.

Foram analisados 6.492 pedidos atrasados e 89.438 pedidos
entregues no prazo.

Dentre os pedidos atrasados, foi observado que, até 3 dias de atraso, 32,31% apresentam avaliação ruim. Na faixa de 4 a 7 dias, essa taxa sobe para 67,99%, uma diferença de 35,68 pontos percentuais. Na faixa de 8 a 14 dias, a taxa chega a 80,48%, enquanto na faixa de 15 dias ou mais apresenta 78,57%.

### Interpretação

No recorte analisado, pedidos atrasados apresentaram
maior frequência de avaliações ruins.

No recorte dos pedidos atrasados, o maior aumento observado ocorre entre as faixas de até 3 dias e de 4 a 7 dias de atraso. Nas duas últimas faixas, as taxas de avaliações ruins permanecem elevadas, próximas de 80%, mas a proximidade dos valores não permite afirmar que se estabilizaram.

Isso indica uma associação entre atraso na entrega
e pior avaliação da experiência de compra.

### Ação sugerida

Investigar os segmentos que concentram maior quantidade
de pedidos atrasados e avaliações ruins, para orientar
a priorização de melhorias na entrega.

### Limitações

A comparação não demonstra que o atraso, isoladamente,
causou a avaliação ruim. Outros aspectos da experiência
de compra também podem estar relacionados às notas.

A comparação entre faixas não permite identificar um dia exato a partir do qual as avaliações pioram. As taxas também devem ser consideradas junto à quantidade de pedidos em cada faixa.

Os resultados se referem apenas ao recorte analisado.

## 2. Produtos e categorias

### Pergunta

Determinados produtos e categorias estão mais associados a avaliações ruins?

Características do produto, como peso, volume e preço, estão associadas a diferenças nas taxas de avaliações ruins?

### Recorte utilizado

Foram considerados pedidos entregues, com avaliação e com um único item. Para os rankings, foram incluídos produtos com pelo menos 10 pedidos e categorias com pelo menos 30 pedidos nesse recorte.

Cada linha representa um pedido associado a um produto.
Avaliações ruins correspondem às notas 1 e 2.
Nas análises de preço, volume e peso, foram utilizados os pedidos com informação disponível para cada característica.

### Resultado

Foi observado que existem 5 produtos com taxa de avaliações ruins acima de 60%, com alguns chegando a mais de 80%.

Dentre as categorias, 'fashion_roupa_masculina' e 'audio' apresentaram as maiores taxas de avaliações ruins, com 21,98% e 21,88%, respectivamente, sendo as únicas acima de 20% no ranking analisado.

Em relação a preço, volume e peso, foram criadas faixas a partir de quintis, com os limites arredondados. Por causa desse arredondamento, as faixas não necessariamente possuem a mesma quantidade de pedidos. A comparação realizada foi descritiva, sem aplicação de testes estatísticos.

Nas faixas de preço, as taxas de avaliações ruins variaram de 10,59% nos pedidos de até R$ 40 (20.497 pedidos) a 12,97% nos pedidos acima de R$ 160 (17.375 pedidos).

Nas faixas de peso, a menor taxa foi de 10,90% nos pedidos com produtos acima de 500 g até 1.000 g (15.181 pedidos), enquanto a maior foi de 12,76% nos pedidos com produtos acima de 2.500 g (17.054 pedidos).

Nas faixas de volume, a menor taxa foi de 10,59% nos pedidos com produtos acima de 4.000 cm³ até 9.000 cm³ (20.770 pedidos), enquanto a maior foi de 12,44% nos pedidos com produtos acima de 22.000 cm³ (17.378 pedidos).

### Interpretação

No recorte analisado, alguns produtos apresentam taxas elevadas de avaliações ruins e merecem investigação. Essas taxas devem ser consideradas junto à quantidade de pedidos e ao número de avaliações ruins, pois produtos com poucos pedidos podem apresentar grandes mudanças na taxa com poucas avaliações a mais ou a menos.

No ranking de categorias, as duas maiores taxas são próximas, mas isso não permite concluir que todas as categorias possuem resultados semelhantes.

Nas três características analisadas, a faixa de maior preço, peso ou volume apresentou a maior taxa de avaliações ruins. Entretanto, as taxas não aumentam de forma contínua entre todas as faixas. As diferenças entre a maior e a menor taxa foram de aproximadamente 2,38 pontos percentuais para preço, 1,86 para peso e 1,85 para volume. Esses resultados descrevem o recorte analisado e não demonstram que essas características causaram as avaliações ruins.

### Ação sugerida

Analisar os principais produtos do ranking, considerando a quantidade de pedidos, os comentários das avaliações e a ocorrência de atrasos, para investigar possíveis motivos das avaliações ruins.

### Limitações

Mesmo utilizando uma quantidade mínima de pedidos por produto e categoria, os grupos possuem quantidades diferentes de avaliações. Esse mínimo reduz a presença de grupos muito pequenos, mas não garante a mesma precisão para todas as taxas.

A avaliação representa a experiência do pedido, e não exclusivamente a qualidade do produto. Outros fatores, como entrega e atendimento, também podem estar relacionados às notas.

Os resultados representam apenas pedidos entregues, avaliados e com um único item.

## 3. Regiões

### Pergunta

Determinados estados ou regiões estão mais associados a avaliações ruins?

Estados e regiões com maior proporção de avaliações ruins apresentam maior proporção de pedidos sem vendedores locais?

### Recorte utilizado

Foram utilizados pedidos entregues e avaliados, com informação de atraso disponível, de clientes com estado e cidade preenchidos no cadastro. Os pedidos foram agrupados pelo estado e pela região do cliente.

Não foi utilizada uma quantidade mínima de pedidos, para manter todas as unidades geográficas na análise. Foi utilizada a participação no total de pedidos para contextualizar o volume de cada grupo.

### Resultado

Entre os estados analisados, AL, MA e SE apresentaram as maiores taxas de avaliações ruins, com 21,72%, 20,68% e 19,28%, respectivamente. AP, SP e PR apresentaram as menores taxas, com 5,97%, 10,94% e 11,11%, respectivamente.

Em relação a vendedores locais, SP apresentou a maior proporção de pedidos com pelo menos um vendedor do mesmo estado, com 73,13%, enquanto outros 14 estados apresentaram proporções entre 0% e 1%.

No ranking de regiões, as taxas de avaliações ruins variaram de 12,03% no Sul a 17,25% no Nordeste, que apresentaram a menor e a maior taxa, respectivamente.

### Interpretação

AL, MA e SE apresentaram as maiores taxas de avaliações ruins e, juntos, representam aproximadamente 1,5% dos pedidos analisados. Já o RJ apresentou uma taxa de avaliações ruins de 18,64% e concentrou 12,79% dos pedidos, sendo o segundo estado com maior participação.

Entre os 15 primeiros estados do ranking, as proporções de pedidos com vendedores locais foram inferiores a 2%, com exceção do RJ, que apresentou 7,81%.

No ranking de regiões, a diferença entre a maior e a menor taxa de avaliações ruins foi de 5,22 pontos percentuais. A comparação apresentada, por si só, não permite concluir que haja uma relação entre maiores taxas de avaliações ruins e menores proporções de pedidos com vendedores locais.

### Ação sugerida

O RJ merece uma análise mais aprofundada por apresentar uma taxa de avaliações ruins de 18,64% e concentrar 12,79% dos pedidos analisados. Essa combinação indica uma participação relevante no volume de avaliações ruins, mesmo sem apresentar a maior taxa entre os estados.
Também é necessário investigar os estados do Nordeste com taxas elevadas, considerando a quantidade de pedidos e de avaliações ruins em cada um.

### Limitações

A quantidade de pedidos varia muito entre os estados. Enquanto 15 estados possuem, individualmente, menos de 1% dos pedidos analisados, SP concentra 41,99%. Nos estados com poucos pedidos, pequenas mudanças na quantidade de avaliações ruins podem provocar variações maiores nas taxas.
Os resultados agrupados por estado e região não demonstram que pedidos com vendedores de fora recebem avaliações piores. Além disso, um pedido pode possuir vendedores locais e de fora ao mesmo tempo.

## 4. Vendedores

### Pergunta

Determinados vendedores estão mais associados a avaliações ruins e a pedidos atrasados?

Vendedores de determinados estados aparecem proporcionalmente mais entre os 100 vendedores com maiores taxas de avaliações ruins?

### Recorte utilizado

Foram utilizados pedidos entregues e avaliados, mantendo uma ocorrência de cada vendedor por pedido. Foram considerados vendedores com pelo menos 10 pedidos nesse recorte. Um pedido pode estar associado a mais de um vendedor.
A taxa de atraso considera apenas pedidos com informação de prazo disponível.

### Resultado

Foram analisados 90.180 pedidos entregues e avaliados, associados a 1.236 vendedores com pelo menos 10 pedidos no recorte. Cada pedido foi contado uma única vez, mesmo quando associado a mais de um vendedor. Nesse conjunto, 78,44% das avaliações foram boas, 8,38% neutras e 13,19% ruins. Entre os 90.173 pedidos com informação de prazo disponível, 6,76% foram entregues com atraso e 93,24% no prazo; sete pedidos não possuíam essa informação. Essas taxas servem como referência para comparar os resultados individuais dos vendedores.

São 17 vendedores com taxa de avaliações ruins igual ou superior a 40%, enquanto 10 vendedores apresentam taxa de atraso igual ou superior a 30%.

Dentre os 17 vendedores com maior taxa de avaliações ruins, 8 apresentam atraso em 20% ou mais de seus pedidos.

Dos 10 vendedores com atraso igual ou superior a 30%, nove apresentam pelo menos 30% de avaliações ruins.

Na PB, o único vendedor elegível está no top 100, resultando em uma taxa de 100%. PE e RN apresentam 33,33%, com um vendedor entre três elegíveis em cada estado, enquanto GO apresenta 20%, com três entre 15.

### Interpretação

Entre os 10 vendedores com taxa de atraso igual ou superior a 30%, nove também apresentam pelo menos 30% de avaliações ruins. Entretanto, entre os 17 vendedores com taxa de avaliações ruins igual ou superior a 40%, somente oito apresentam atrasos em pelo menos 20% dos pedidos.
Isso mostra que taxas elevadas de avaliações ruins também aparecem entre vendedores com taxas menores de atraso, indicando a necessidade de investigar outros aspectos dos pedidos. A comparação desses grupos, por si só, não demonstra uma correlação entre as taxas no conjunto de vendedores.

A distribuição de vendedores entre os estados é desigual. SP concentra 61,65% dos vendedores elegíveis, seguido pelo PR, com 11,25%. Os demais estados apresentam participações inferiores a 10%.

### Ação sugerida

Avaliar individualmente os vendedores com altas taxas de avaliações ruins e taxas menores de atraso, considerando os comentários das avaliações, os produtos vendidos e a quantidade de pedidos, para investigar outros possíveis motivos de insatisfação.

### Limitações

Alguns estados possuem poucos vendedores elegíveis. Na PB, por exemplo, o único vendedor elegível está no top 100, resultando em 100% nesse indicador. Esse resultado descreve um único vendedor e não permite generalizar o desempenho dos vendedores do estado.

Em pedidos com mais de um vendedor, a mesma avaliação e o mesmo indicador de atraso são associados aos vendedores envolvidos. Portanto, não é possível atribuir individualmente a responsabilidade pelo resultado do pedido.

## 5. Recompra

### Pergunta

Clientes com avaliações boas, neutras e ruins na primeira compra entregue apresentam diferenças na taxa de recompra observada?

### Recorte utilizado

Foi considerada a primeira compra entregue de cada cliente, com pelo menos 90 dias entre a entrega e o fim da base, para garantir um período mínimo de acompanhamento. Foram incluídos clientes com e sem avaliação nessa compra.
A recompra corresponde a um novo pedido posterior à compra de referência, com qualquer status e sem prazo máximo, desde que observado na base. Cada cliente é contado uma única vez.

### Resultado

A taxa geral de recompra no recorte analisado foi de 3,07%. Clientes com avaliação na compra de referência apresentaram taxa de 2,89%, enquanto clientes sem avaliação apresentaram taxa de 92,31%.

Entre os clientes cuja compra de referência recebeu avaliação ruim, 2,49% voltaram a comprar. Entre aqueles com avaliação neutra, 2,60% fizeram uma nova compra, enquanto entre os clientes com avaliação boa a taxa foi de 2,99%.

### Interpretação

Entre os clientes avaliados, a taxa de recompra foi maior nos grupos com notas melhores: 2,49% para avaliações ruins, 2,60% para neutras e 2,99% para boas. A diferença entre avaliações boas e ruins foi de 0,50 ponto percentual. Essa comparação é descritiva e não permite afirmar que a avaliação causou a diferença na recompra.

### Ação sugerida

Aprofundar a comparação entre os grupos de avaliação, considerando a quantidade de clientes e o tempo disponível para recompra. Uma análise estatística pode complementar essa comparação, avaliando a incerteza das diferenças observadas.

### Limitações

O acompanhamento mínimo de 90 dias evita incluir clientes com pouco tempo disponível, mas não iguala o período observado para todos. Clientes mais antigos podem ter mais tempo para recomprar. A ausência de uma nova compra na base não significa que o cliente nunca voltou a comprar, apenas que isso não foi observado no período.

O grupo sem avaliação possui 169 clientes, enquanto o recorte total contém 82.502. Sua taxa descreve um grupo pequeno e específico, exigindo cuidado na comparação e na generalização.
Como a recompra é contada após a data da compra de referência, ela pode ocorrer antes da entrega ou da avaliação. Por isso, os resultados não permitem interpretar toda recompra como uma resposta à experiência avaliada.


## 6. Comparação estatística da recompra

### Pergunta

A taxa de recompra observada difere entre clientes com avaliações boas e ruins na primeira compra entregue?

### Recorte utilizado

Foram utilizados os grupos preparados na análise de recompra, considerando uma observação por cliente e pelo menos 90 dias de acompanhamento após a primeira entrega.

A recompra considera um novo pedido posterior à compra de referência, com qualquer status, observado até o fim da base. Não está limitada a uma janela de 90 dias.

Foram comparados 64.233 clientes com avaliações boas e 11.128 com avaliações ruins. Clientes com avaliações neutras ou sem avaliação não participaram desta comparação.

### Método utilizado

Foi aplicado um teste Z bilateral para comparação de duas proporções, com nível de significância de 5%.

- Hipótese nula (H₀): as proporções de recompra dos grupos são iguais.
- Hipótese alternativa (H₁): as proporções de recompra dos grupos são diferentes.

As contagens esperadas atenderam ao critério adotado para a aproximação do teste. Também foi calculado um intervalo de confiança de 95% para a diferença entre as proporções pelo método de Newcombe.

### Resultado

Entre os clientes com avaliações boas, 1.920 recompraram, correspondendo a uma taxa de 2,99%. Entre os clientes com avaliações ruins, 277 recompraram, correspondendo a 2,49%.

A diferença entre os grupos foi de aproximadamente 0,50 ponto percentual, com maior taxa no grupo de avaliações boas.

O teste apresentou estatística Z de 2,8939 e p-valor de 0,003805. Como o p-valor foi inferior a 0,05, rejeitamos a hipótese de proporções iguais, sob os pressupostos do teste.

O intervalo de confiança de 95% para a diferença, calculada como Boa menos Ruim, foi de 0,17 a 0,80 ponto percentual.

### Interpretação

No recorte analisado, clientes com avaliações boas na primeira compra entregue apresentaram maior taxa de recompra observada que clientes com avaliações ruins. A diferença foi estatisticamente significativa sob os pressupostos adotados.

Esse resultado indica uma associação entre o grupo de avaliação e a recompra observada. Não demonstra que uma avaliação boa causa maior recompra ou que uma avaliação ruim impede o cliente de comprar novamente.

A significância estatística também não determina, sozinha, a importância prática da diferença para o negócio.

### Ação sugerida

Utilizar o resultado como informação complementar no acompanhamento da experiência dos clientes. A avaliação pode ajudar a identificar grupos para investigação, mas não deve ser usada isoladamente para prever recompra ou atribuir suas causas.

### Limitações

O acompanhamento mínimo de 90 dias não iguala o tempo disponível para todos os clientes. Clientes mais antigos podem ter mais oportunidades de recompra, e a comparação não ajusta essa diferença.

A recompra pode ocorrer antes da entrega ou da avaliação da compra de referência, pois é contada a partir da data da compra. Portanto, nem toda recompra observada pode ser interpretada como uma resposta à experiência avaliada.

O teste pressupõe independência entre clientes. Ter uma observação por cliente evita contagens repetidas, mas não garante esse pressuposto, pois clientes podem compartilhar fatores como vendedor e período de compra.

A análise é exploratória e utiliza dados observacionais. O teste e o intervalo de confiança não corrigem diferenças de composição entre os grupos nem garantem que o resultado se aplique a outros períodos ou populações.

## 7. Produtos e categorias: atraso e avaliação

### Pergunta

Entre os produtos e categorias com maiores taxas de avaliações ruins, a insatisfação também aparece nos pedidos entregues no prazo?

Quais produtos e categorias apresentam maiores taxas de atraso e como são avaliados em cada situação de entrega?

### Recorte utilizado

Foram utilizados pedidos entregues, avaliados e com um único item. Os rankings existentes selecionam produtos com pelo menos 10 pedidos e categorias com pelo menos 30 pedidos nesse recorte.

Foram comparadas duas seleções independentes: os 10 produtos e as 10 categorias com maiores taxas gerais de avaliações ruins e os 10 produtos e as 10 categorias com maiores taxas de atraso entre os elegíveis. Avaliações ruins correspondem às notas 1 e 2.

A separação por situação de entrega considera somente pedidos com prazo conhecido. A participação de atrasados usa o total de pedidos com prazo conhecido do próprio produto ou categoria; a taxa de avaliações ruins usa os pedidos da respectiva situação. Os mínimos de pedidos se aplicam ao grupo completo, e não separadamente a atrasados e no prazo.

### Resultado

Entre as categorias selecionadas pelas maiores taxas de avaliações ruins, todas as dez apresentaram proporções maiores de avaliações ruins nos pedidos atrasados do que nos pedidos no prazo.

Em 'fashion_roupa_masculina', apenas 4 dos 91 pedidos atrasaram (4,40%). Entretanto, 17 dos 87 pedidos no prazo receberam avaliações ruins (19,54%), contra 3 dos 4 atrasados (75,00%). Assim, a maior parte das avaliações ruins dessa categoria veio de pedidos entregues no prazo.

Em 'audio', 40 dos 329 pedidos atrasaram (12,16%). Entre os atrasados, 31 receberam avaliações ruins (77,50%); entre os 289 pedidos no prazo, foram 41 (14,19%). Em 'moveis_escritorio', foram 53 avaliações ruins entre 86 atrasados (61,63%) e 137 entre 924 pedidos no prazo (14,83%).

Entre os produtos, o identificador `cd46a885543f0e169a49f1eb25c04e43` apresentou 23 avaliações ruins em 27 pedidos (85,19%), todos entregues no prazo. Já `fd0065af7f09af4b82a0ca8f3eed1852` teve 9 pedidos atrasados em 10 (90,00%), todos os nove com avaliação ruim; seu único pedido no prazo recebeu nota neutra.

No ranking independente de atraso por categoria, 'moveis_colchao_e_estofado' ficou em primeiro lugar, com 5 atrasos em 37 pedidos (13,51%), seguida de 'audio', com 40 em 329 (12,16%), e 'casa_conforto', com 32 em 315 (10,16%). A categoria 'bebes', embora tivesse taxa menor de atraso (8,46%), reuniu 219 pedidos atrasados, dos quais 149 receberam avaliações ruins (68,04%).

### Interpretação

Os resultados mostram dois padrões que merecem investigações diferentes: grupos nos quais atrasos e avaliações ruins aparecem juntos e grupos com insatisfação elevada mesmo nas entregas no prazo.

O produto com 85,19% de avaliações ruins e todos os pedidos no prazo demonstra que atraso, conforme a definição utilizada, não está presente em todos os casos de insatisfação. Isso não identifica o motivo das notas nem permite atribuí-las exclusivamente à qualidade do produto.

Nas categorias analisadas, uma taxa maior de avaliações ruins entre atrasados pode coexistir com um número maior de avaliações ruins entre pedidos no prazo, pois o segundo grupo costuma ser mais numeroso. Taxa e volume devem ser considerados em conjunto na priorização.

### Ação sugerida

Investigar comentários e características dos pedidos de produtos com avaliações ruins mesmo no prazo. Para grupos como 'audio', analisar também os pedidos atrasados e os vendedores envolvidos. Considerar categorias com maior volume absoluto de atrasos e avaliações ruins, como 'bebes', além das primeiras posições por taxa.

### Limitações

Os rankings selecionam grupos com taxas extremas e não representam todos os produtos ou categorias. As duas seleções podem conter os mesmos grupos e não devem ser somadas como populações distintas. 'sem_categoria' é um grupo de dados ausentes, não uma categoria comercial identificada.

Os mínimos totais não garantem quantidade suficiente de pedidos em cada situação. Por exemplo, 'fashion_roupa_feminina' apresentou 100% de avaliações ruins entre atrasados, mas essa taxa corresponde a apenas um pedido. O produto com 90% de atraso tem somente 10 pedidos no total.

Não foram aplicados testes estatísticos ou ajustes por vendedor, período ou outras características. A avaliação descreve a experiência do pedido; as diferenças observadas não estabelecem causalidade nem identificam a responsabilidade pelo problema.

## 8. Regiões e estados: atraso e avaliação

### Pergunta

As diferenças nas avaliações entre estados e regiões persistem quando os pedidos são separados entre atrasados e entregues no prazo?

Qual a participação dos atrasos no total de pedidos de cada localização?

### Recorte utilizado

Foram considerados pedidos entregues, avaliados e com informação de prazo, agrupados pelo estado e pela região do cliente. Cada pedido aparece uma única vez em cada nível geográfico, sem exigir mínimo de pedidos por grupo.

A participação de cada situação usa como denominador o total de pedidos da própria localização nesse recorte. A taxa de avaliações ruins usa os pedidos da linha, e a referência geral é calculada pelas contagens de todos os pedidos da mesma situação, não pela média das taxas dos estados ou regiões.

### Resultado

Foram analisados 95.930 pedidos, sendo 6.492 atrasados e 89.438 no prazo. As referências gerais de avaliações ruins foram de 62,85% entre atrasados e 9,49% entre pedidos no prazo.

O Nordeste apresentou 1.147 atrasos entre 9.003 pedidos (12,74%), enquanto o Sul teve 806 entre 13.738 (5,87%). As taxas de avaliações ruins foram, respectivamente, 65,82% e 60,30% entre atrasados, e 10,16% e 9,02% entre pedidos no prazo.

Entre as cinco regiões, as taxas de avaliações ruins nos pedidos no prazo variaram de 9,02% no Sul a 10,58% no Norte. Entre atrasados, variaram de 60,30% no Sul a 66,88% no Norte. Todas as regiões apresentaram taxas maiores de avaliações ruins no grupo atrasado.

Em AL, 85 dos 396 pedidos atrasaram (21,46%). Entre eles, 58 receberam avaliações ruins (68,24%); entre os 311 pedidos no prazo, foram 28 (9,00%). Embora AL tivesse a maior taxa geral de avaliações ruins na análise anterior, sua taxa entre pedidos no prazo ficou abaixo da referência geral dessa situação (9,49%).

No RJ, 1.483 dos 12.272 pedidos atrasaram (12,08%). Entre os atrasados, 1.083 receberam avaliações ruins (73,03%); entre os 10.789 pedidos no prazo, foram 1.205 (11,17%). As duas taxas ficaram acima das respectivas referências gerais. SP teve taxa menor de atraso (4,49%), mas reuniu 1.809 pedidos atrasados, volume superior ao do RJ.

### Interpretação

A separação por situação de entrega muda a leitura do ranking geográfico. Em AL, a elevada taxa geral de avaliações ruins coexistiu com uma participação alta de atrasos, enquanto a taxa dos pedidos no prazo ficou abaixo da referência nacional desse grupo. Isso mostra a importância da composição dos pedidos na interpretação do resultado agregado, sem quantificar um efeito causal do atraso.

No RJ, a maior frequência de avaliações ruins também apareceu nas entregas no prazo, indicando que a investigação não deve se limitar aos atrasos. O contraste entre SP e RJ reforça a necessidade de considerar tanto taxas quanto quantidades absolutas.

### Ação sugerida

Investigar a distribuição dos atrasos em AL e no Nordeste, e aprofundar os casos do RJ separando pedidos atrasados e no prazo. Cruzar posteriormente esses grupos com vendedores, categorias e períodos, para identificar concentrações que possam orientar investigações operacionais.

### Limitações

Algumas situações têm poucos pedidos. RR apresentou 80,00% de avaliações ruins entre atrasados, correspondendo a 4 de apenas 5 pedidos. AP apresentou 0,00%, mas teve somente 2 pedidos atrasados. Essas posições extremas não sustentam generalizações sobre os estados.

Separar os pedidos por atraso não controla diferenças de categoria, vendedor, período ou outras características. Não foram realizados testes estatísticos nessa comparação. Estados e regiões são dois agrupamentos dos mesmos pedidos e não devem ser somados como bases independentes.

## 9. Recompra: atraso e avaliação da compra de referência

### Pergunta

Qual a proporção de atrasos entre clientes com avaliações boas, neutras e ruins na compra de referência?

A taxa de recompra observada difere entre clientes cuja compra de referência atrasou e aqueles que receberam no prazo, inclusive dentro de cada grupo de avaliação?

### Recorte utilizado

Foi mantida a regra da análise de recompra: primeira compra entregue observada de cada cliente, com pelo menos 90 dias entre a entrega e o fim da base. Um novo pedido estritamente posterior à compra de referência, com qualquer status e observado até o fim da base, conta como recompra. Não há janela máxima de 90 dias para recomprar.

Cada cliente é contado uma única vez. A avaliação e o atraso são da compra de referência. A proporção de atrasados considera clientes com prazo conhecido dentro de cada grupo de avaliação; a taxa de recompra usa todos os clientes da respectiva combinação. Neste resultado, os 82.502 clientes elegíveis tinham prazo conhecido.

### Resultado

Entre os clientes com avaliação ruim, 3.688 de 11.128 tiveram atraso na compra de referência (33,14%). Entre os clientes com avaliação boa, foram 1.393 de 64.233 (2,17%); entre os de avaliação neutra, 616 de 6.972 (8,84%). No grupo sem avaliação, foram 20 de 169 (11,83%).

Entre os 5.717 clientes com compra de referência atrasada, 143 recompraram (2,50%). Entre os 76.785 que receberam no prazo, 2.391 recompraram (3,11%).

No grupo de avaliação ruim, a taxa de recompra foi de 1,93% entre atrasados (71 de 3.688) e 2,77% entre pedidos no prazo (206 de 7.440). No grupo de avaliação boa, foi de 2,80% entre atrasados (39 de 1.393) e 2,99% entre pedidos no prazo (1.881 de 62.840). Entre avaliações neutras, ambas as taxas arredondaram para 2,60%, com 16 recompras entre 616 atrasados e 165 entre 6.356 clientes no prazo.

No grupo sem avaliação, as taxas foram de 85,00% entre atrasados (17 de 20) e 93,29% entre pedidos no prazo (139 de 149). Esses resultados descrevem um grupo pequeno e com comportamento distinto dos avaliados.

Das 143 recompras no grupo atrasado, 72 ocorreram antes da entrega da compra de referência. No grupo no prazo, foram 721 das 2.391 recompras. Entre os clientes sem avaliação, 152 das 156 recompras ocorreram antes da entrega de referência.

### Interpretação

O atraso foi mais frequente entre clientes que avaliaram mal a compra de referência. Esse resultado é uma associação entre atraso e avaliação: não significa que 33,14% dos pedidos atrasados foram mal avaliados, pois o denominador utilizado é o grupo de clientes com avaliação ruim.

A taxa de recompra observada foi menor no grupo atrasado, tanto no total quanto nos grupos de avaliação boa e ruim. A diferença foi mais pronunciada entre avaliações ruins; entre avaliações neutras, as taxas foram próximas. Essas comparações são descritivas e não receberam teste estatístico específico.

A ocorrência de recompras antes da entrega limita a interpretação: parte dos novos pedidos foi feita antes de o cliente conhecer o resultado final da entrega. Portanto, as taxas atuais não podem ser interpretadas integralmente como reação ao atraso ou à experiência avaliada.

### Ação sugerida

Como análise complementar futura, separar recompras anteriores e posteriores à entrega e considerar também a data da avaliação caso a pergunta seja sobre recompra após a experiência avaliada. Comparar grupos com períodos de acompanhamento mais semelhantes e investigar separadamente a ausência de avaliação, preservando a análise atual como referência.

### Limitações

O acompanhamento mínimo de 90 dias não iguala o tempo disponível para recomprar. Os grupos também podem diferir em características não controladas, como período, vendedor e tipo de produto. A ausência de nova compra significa somente que ela não foi observada na base.

O grupo sem avaliação tem apenas 169 clientes e concentra recompras anteriores à entrega. Sua inclusão influencia a taxa agregada e não deve ser interpretada como evidência de satisfação. Algumas combinações têm poucos eventos de recompra, tornando pequenas diferenças difíceis de avaliar sem análise de incerteza.

O teste estatístico da seção 6 compara avaliações boas e ruins no conjunto dos clientes avaliados. Seu resultado não se transfere automaticamente às comparações por atraso ou aos subgrupos desta seção.
