# PenduloAcoplado
Sistema de pendulo doble acoplado mediante un resorte a un pendulo simple, dicho proyecto contiene la solucion a la ecuacion diferencial del pendulo simple, por aparte la del pendulo doble y el sistema completo.


¿Alguna vez se han imaginado el mapeo de coordenadas de un sistema de p´endulos? Siendo esta la
inc´ognita la que se buscara solucionar en este proyecto,
se simulara mediante ODEINT/RK4 m´etodo num´erico
con la utilizaci´on de Python, adem´as de aprovechar este
mismo lenguaje para crear un mapeo del cambio de coordenadas generalizadas de un p´endulo doble, un p´endulo
simple y por ultimo la uni´on de ambos sistemas por un
resorte de constante de elasticidad k (N/m*m) los tres
p´endulos cuentan con una varilla r´ıgida sin elasticidad se
una longitud l, cuentan con la misma masa m, Mientras
que el primer p´endulo del p´endulo doble se encuentra
acoplado con un resorte de constante de elasticidad K al
p´endulo simple.
El cual, esperamos que su comportamiento sea ca´otico,
debido al subsistema existente del p´endulo doble, dicho
sistema se nombrara Sistema A, mientras que Sistema
B se tratara del p´endulo simple aislado. Para facilitar
imaginarse el comportamiento se analizara de manera
independiente el sistema A y el sistema B mediante la
teor´ıa del calculo variacional y las ecuaciones derivadas
del Lagrangiano, ya que estas facilitaran mucho el procedimiento a desarrollar.
