# <center><span style="color:red"><u> Grupo 2</u> </span> <center>
    
   <center><i>- Beatriz, Diego, Edwin, Luis -</i></center>

## <center> <u>Título: Open-Channel Flow Algorithm in Newton-Raphson Form </u>

<center>by: John N. Paine </center>


### <u>Objetivo</u>: Desenvolver um <u>algoritmo</u> para solucionar um problema de determinação do perfil d'água em um fluxo em regime permanente gradualmente variado baseado no<u> _Standard Step Method_</u>.

### <u> Justificativa</u>

- O escoamento **permanente gradualmente variado** vem sendo objeto de estudo por mais de <u>100 anos</u>.
- Conhecer o **perfil d'água** é extremamente importante pois <u>influencia diretamente as obras de engenharia</u>.
- Todavia, o problema é extremamente <u>complexo</u>, principalmente pelo ***tratamento matemático das equações*** que regem o movimento e também o **grande número de parâmetros hidráulicos** sujeitos a variações.
- Foram desenvolvidos diversos métodos, com destaque para os trabalho iniciais de **Bakhmeteff**.
- Há diversos métodos para determinação do perfil:
    1. métodos de integração gráfica;
    2. métodos de integração direta;
    3. métodos de soluções numéricas passo a passo (*step methods*):
        1. Direct step method;
        2. Standard step method;

> ### Direct step method
>
> - A distância é calculada a partir da altura;
> - Aplicável somente em canais prismáticos;

> ### Standard step method
>
> - A altura é calculada a partir da distância;
> - Aplicável em canais prismáticos e não prismáticos;
> - Processo de tentativas e erros
> - Envolve uma equação diferencial, é necessária uma condição de contorno.

<img src="canal.png" style="height:700px">

### <u>Equações</u>

> #### Energia disponível:
>
> $$H = i + y + \alpha \frac{V^2}{2g}$$

   
<br>

> #### Equação básica do standard step, com condições de contorno conhecidas em uma das seções:
>
> $$f(x) = \left( h + \frac{V^2}{2g}\right)_D- \left(h + \frac{V^2}{2g}\right)_U + \frac{\Delta x}{2} (S_{fU} + S_{fD})$$

<br>
   
> #### Gradiente de Energia
>
> $$S_f = \left( \frac{Qn}{AR^{2/3}} \right)^2$$

### <u>Constantes</u>

Algumas equações e passagens são chamadas de constantes **$(C_x)$** para simplificar as equações, sendo essas:

> $$C_1 = H$$
<br>
> $$C_2 = S_f$$
<br>
> $$C_3 = Qn$$
<br>
> $$C_4 = \frac {Z_L + Z_R}{2}$$
<br>
> $$C_5 = \left(1 + Z_L^2\right)^{1/2} + \left(1 + Z_R^2\right)^{1/2}$$

### <u>Equações Simplificadas para Newton-Raphson</u>

#### Função polinomial do gradiente de energia  em função de *y* como variável independente

> $$S_f(y)= C_3^2 \left(B + C_4y^2\right)^{-10/3}\left(B + yC_5\right)^{4/3}$$

<br>

#### Equação final do standard step method com as constantes definidas utilizada no algorítimo

> $$f(y) = \beta C_1 - \beta y - \beta i - \beta \frac {\left[ \frac{Q}{y \left(B + C_4y\right)}\right]^2}{2g} + \frac {\Delta x}{2} \left[S_f(y) + C_2 \right]$$

O termo **$\beta$** é <font color='blue'>positivo</font> se o calculo inicia com valores conhecidos na montante do canal ou <font color='red'>negativo</font> se são conhecidos os valores na jusante do canal.


